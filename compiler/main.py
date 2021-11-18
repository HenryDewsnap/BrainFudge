def add(compObject, args):
    compObject.brainFuDGE += "+"*int(args[0])


def sub(compObject, args):
    compObject.brainFuDGE += "-"*int(args[0])


def setMemAddr(compObject, args):
    while compObject.memoryPointer != int(args[0]):
        if compObject.memoryPointer > int(args[0]):
            compObject.brainFuDGE += "<"
            compObject.memoryPointer -= 1
        else:
            compObject.brainFuDGE += ">"
            compObject.memoryPointer += 1


def incMemAddr(compObject, args):
    compObject.brainFuDGE += ">"
    compObject.memoryPointer += 1


def decMemAddr(compObject, args):
    compObject.brainFuDGE += "<"
    compObject.memoryPointer -= 1


def zeroMemValue(compObject, args):
    compObject.brainFuDGE += "[-]"


def forLoop(compObject, args): ##Args: 0: set value for I, 1: pre-compiled BF code, 2: Steps (ints supported only).
    zeroMemValue(compObject, args)
    add(compObject, args)
    ##Find a way to pre-compile args[1] when you wake up idiot.

    compObject.brainFuDGE += "[" + args[1] + "-"*int(args[2]) + "]"











def parseFunctions(func):
    funcChars = list(func.replace(" ", ""))
    funcName = ""
    args = []

    funcPtr = 0
    while funcChars[funcPtr] != "(": #Iterates through the function to determine the functions name.
        funcName += funcChars[funcPtr]
        funcPtr += 1

    findingArgs = True
    while (findingArgs):
        currentArg = ""
        funcPtr += 1
        while funcChars[funcPtr] != ",":
            if funcChars[funcPtr] == ")":
                findingArgs = False
                break
            currentArg += funcChars[funcPtr]
            funcPtr += 1
        args.append(currentArg)
        
    for argPtr in range(len(args)):
        try:
            args[argPtr] = args[argPtr].replace("'", "")
            
        except:
            args[argPtr] = args[argPtr].replace('"', "")

    return {"name":funcName, "args":args}




class compiler:
    def __init__(self, codeData): ##Code is an array of functions (defined as strings.)
        self.memoryPointer = 0 #The compiler needs to keep track of the memory pointer so it knows how many of certain operations to perform.
        self.code = codeData
        self.parsedCode = []
        self.brainFuDGE = ""

    def parseCode(self):
        for line in self.code:
            try:
                self.parsedCode.append(parseFunctions(line))
            except:
                print(f"Exception whilst parsing: {line}")

    def CompileCode(self):
        for parsedCodeLine in self.parsedCode:
            try:
                globals()[parsedCodeLine["name"]](self, parsedCodeLine["args"])
                
            except:
                print(f"Error Compiling function:   {parsedCodeLine['name']}   WITH   args:   {parsedCodeLine['args']}")
                return "COMPILATION FAILED"
            
        return "COMPILATION SUCCESSFUL"

compilerObj = compiler(["sub(10)", "setMemAddr(10)"])
compilerObj.parseCode()
compilerObj.CompileCode()
print(compilerObj.brainFuDGE)
