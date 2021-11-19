import os

colours = {
    "default":"\033[0;37;40m",
    "red":"\033[1;31;40m",
    "yellow":"\033[1;33;40m",
    "green":"\033[1;32;40m"
}

functions = {
    "add":{"args":1,},                #Adds a certain ammount to the current cell.
    "sub":{"args":1},                #Subs a certain ammount from the current cell.
    "zero":{"args":0},               #Sets the current cell to 0.

    "incMemCell":{"args":0},
    "decMemCell":{"args":0},
    "setMemCell":{"args":1},         #Updates the memory cell to a spesific location.

    "startLoop":{"args":2},          #First arg is the ammount of iterations and the second is the address of the incrimentor.
    "endLoop":{"args":0} #Checks the pointer of the current loop layer to see whether it should continue or recur back to the start of the loop.

}

def compilerLog(msg, colour="default", logType="default"):
    if logType == "default":
        preFix = "[Brain Fudge Compiler]: "
    else:
        preFix = f"[Compiler log type: {colours[colour]}{logType.upper()}{colours['default']}]: "
    print(f"{preFix}{colours[colour]}{msg}{colours['default']}")



class compile:
    def __init__(self):
        self.source_code = []
        self.memory_values = []
        self.memory_address = 0

        self.parsed_code = []
        self.variables_and_locations = {}


    ##Takes the code and seperates it into its key values.
    def parseCode(self):
        for function in self.source_code: ##Each line represents a new function with new arguments (because I don't know how to make an actual good programming language B) ).
            try:
                function = function.replace(" ", "")

                functionInfo = {"name":"", "args":[]}

                functionPtr = 0
                functionChars = list(function)
                while functionChars[functionPtr] != "(":
                    functionInfo["name"] += functionChars[functionPtr]
                    functionPtr += 1

                midArg = False
                currentArg = ""
                argCount = functions[functionInfo["name"]]["args"]
                foundArgs = 0
                functionPtr += 1
                while foundArgs < argCount and functionChars[functionPtr] != ")":
                    if functionChars[functionPtr] != ",":
                        currentArg += functionChars[functionPtr]
                        midArg = True
                    
                    else:
                        functionInfo["args"].append(currentArg)
                        currentArg = ""
                        foundArgs += 1
                    
                    if foundArgs >= argCount:
                        midArg = False

                    functionPtr += 1

                if midArg == True:
                    functionInfo["args"].append(currentArg)
                
                self.parsed_code.append(functionInfo)

            except:
                compilerLog(f"failed to parse line {function}", "red", "error")    
                exit()
        
        compilerLog("successfully parsed code", "green", "success")
            


    #Opens the file where the program is stored
    def loadProgram(self):
        compilerLog(f"{os.getcwd()}", "green", "output")
        compilerLog(f"{os.listdir()}", "green", "current dir")

        try:
            self.source_code = open(input("File Path: "), "r").readlines()
            compilerLog("file read successfully.", "green", "success")

        except:
            compilerLog("file not found / unable to read.", "red", "error")



compilerObj = compile()
compilerObj.loadProgram()
compilerObj.parseCode()
print(compilerObj.parsed_code)
