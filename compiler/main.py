

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

    def parseCode(self):
        for line in self.code:
            try:
                self.parsedCode.append(parseFunctions(line))
            except:
                print(f"Exception whilst parsing: {line}")

    def CompileCode(self):
        for parsedCodeLine in self.parsedCode:
            try:
                globals()[parsedCodeLine["name"]](parsedCodeLine["args"])
                
            except:
                print(f"Error Compiling function:   {parsedCodeLine['name']}   WITH   args:   {parsedCodeLine['args']}")

compilerObj = compiler(["print('Hello')", "wait(10)", "print('Ah')"])
compilerObj.parseCode()
compilerObj.CompileCode()
