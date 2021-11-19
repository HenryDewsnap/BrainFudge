import os

colours = {
    "default":"\033[0;37;40m",
    "red":"\033[1;31;40m",
    "yellow":"\033[1;33;40m",
    "green":"\033[1;32;40m"
}

functions = {
    "add":{"args":1,},               #Adds a certain ammount to the current cell.
    "sub":{"args":1},                #Subs a certain ammount from the current cell.
    "zero":{"args":0},               #Sets the current cell to 0.

    "incMemCell":{"args":0},         #Updates the memory address by +1
    "decMemCell":{"args":0},         #Updates the memory address by -1
    "setMemCell":{"args":1},         #Updates the memory cell to a spesific location.

    "startLoop":{"args":2},          #First arg is the ammount of iterations and the second is the address of the incrimentor.
    "endLoop":{"args":0}             #Checks the pointer of the current loop layer to see whether it should continue or recur back to the start of the loop.

}

def compilerLog(msg, colour="default", logType="default"):
    if logType == "default":
        preFix = "[Brain Fudge Compiler]: "
    else:
        preFix = f"[Compiler log type: {colours[colour]}{logType.upper()}{colours['default']}]: "
    print(f"{preFix}{colours[colour]}{msg}{colours['default']}")


##Functions:
def add(compilerObj, args):
    compilerObj.brain_fudge_code += "+" * int(args[0])

def sub(compilerObj, args):
    compilerObj.brain_fudge_code += "-" * int(args[0])

def zero(compilerObj, args=[]):
    compilerObj.brain_fudge_code += "[-]"

def incMemCell(compilerObj, args=[]):
    compilerObj.brain_fudge_code += ">"
    compilerObj.memory_address += 1

def decMemCell(compilerObj, args=[]):
    compilerObj.brain_fudge_code += "<"
    compilerObj.memory_address -= 1

def setMemCell(compilerObj, args):
    diffarence = compilerObj.memory_address - int(args[0])

    while diffarence != 0:
        if diffarence > 0:
            decMemCell(compilerObj)
            diffarence -= 1

        if diffarence < 0:
            incMemCell(compilerObj)
            diffarence += 1
    
    compilerObj.memory_address = int(args[0])


def startLoop(compilerObj, args):
    pass

def endLoop(compilerObj, args):
    pass


class compile:
    def __init__(self):
        self.source_code = []
        self.memory_values = []
        self.memory_address = 0

        self.parsed_code = []
        self.variables_and_locations = {}

        self.brain_fudge_code = ""


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
    
    def compileToBrainFudge(self):
        for parsed_function in self.parsed_code:
            try:
                self.globals()[parsed_function["name"]](self, parsed_function["args"])
                compilerLog(f"compiled function {parsed_function}", "green", "success")
            except:
                compilerLog(f"failed to compile function {parsed_function}", "red", "error")
                exit()

        compilerLog("Compilation completed", "green", "completed")


    #Opens the file where the program is stored
    def loadProgram(self):
        compilerLog(f"{os.getcwd()}", "green", "output")
        compilerLog(f"{os.listdir()}", "green", "current dir")

        try:
            source_code = open(input("File Path: "), "r").readlines()
            compilerLog("file read successfully.", "green", "success")

        except:
            compilerLog("file not found / unable to read.", "red", "error")



compilerObj = compile()
compilerObj.loadProgram()
print(compilerObj.source_code)
compilerObj.parseCode()
compilerObj.compileToBrainFudge()
