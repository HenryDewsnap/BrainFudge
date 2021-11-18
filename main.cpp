#include <functional>
#include <iostream>
#include <vector>
#include <math.h>
#include <map>

/*BrainFuDGE Commands:
> = incriment memory pointer
< = decrement memory pointer
+ = incriment value stored at memory pointer
- = decriment value stored at memory pointer
[ = start loop (with current mem address != 0 as its condition)
] = checks loop conditions, returns if false, continues if true
, = gets single character from CLI
. = writes single char to CLI
*/

class interpreter {
    //Brain FuDGE Functions.
    private:
        void imp() { memory_pointer += 1; if (memory_pointer >= 256) { memory_pointer = 0; } }; //Incriment Mem Pointer
        void dmp() { memory_pointer -= 1; if (memory_pointer < 0) { memory_pointer =  255; } }; //Decrement Mem Pointer
        
        void ivs() { memory.at(memory_pointer) += 1; }; //Increase Value Stored
        void dvs() { memory.at(memory_pointer) -= 1; }; //Decrease Value Stored

        void slp() { 
            loopLayer+=1; 
            loopStarts.push_back(instruction_pointer); 
            conditionAddr.push_back(memory_pointer);
            }; //Start A Loop (Executes until the mem pointers addressed value == 0)

        void elp() { 
            if (memory.at(conditionAddr.at(loopLayer-1)) == 0) { 
                loopLayer -= 1; 
                loopStarts.pop_back(); 
                conditionAddr.pop_back(); 
            }
            else { 
                instruction_pointer = loopStarts.back(); 
                }
            }; //End A Loop / return backto start.

        void gtc() { std::cin >> memory.at(memory_pointer); }; //Get character (reads one character from the console/cli)
        void ptc() { std::cout << (char)memory.at(memory_pointer) << std::endl; }; //Put character (prints one character to the console/cli)

    //Interpreter Variables.
    private:
        int memory_pointer = 0;
        int instruction_pointer = 0;
        std::vector<int> memory;
        std::string program_data;

        std::vector<int> loopStarts; //This takes the loop depth and returns their initial functions address allowing for nested recursion.
        std::vector<int> conditionAddr;
        int loopLayer = 0;

        void interpreterLogging();

    public:
        bool logging = false;
        void interpret();
        void loadProgram(std::string program);

        interpreter() {
            memory.resize(256, 0);
        }
};

void interpreter::interpret() {
    while (instruction_pointer <= program_data.size()) {
        std::string currentInst(1, program_data[instruction_pointer]);
        
        //Im aware i should use a switch/case statement but they dont appear to like me very much...
        if (currentInst == ">") { imp(); }
        if (currentInst == "<") { dmp(); } 
        if (currentInst == "+") { ivs(); } 
        if (currentInst == "-") { dvs(); } 
        if (currentInst == "[") { slp(); } 
        if (currentInst == "]") { elp(); } 
        if (currentInst == ",") { gtc(); } 
        if (currentInst == ".") { ptc(); }
        
        instruction_pointer += 1;

        interpreterLogging();
    }
}

void interpreter::loadProgram(std::string program) {
    program_data = program;
    std::cout << "[BrainFuDGE]: Program Loaded" << std::endl;
}

void interpreter::interpreterLogging() {
    if (logging == true) {
        std::cout << std::endl;
        std::cout << "CURRENT INSTRUCTION: " << instruction_pointer << std::endl;
        std::cout << "  Memory Pointer: " << memory_pointer << std::endl;
        std::cout << "  Memory Value At Pointer: " << memory.at(memory_pointer) << std::endl;
        std::cout << "  Loop Depth: " << loopLayer << std::endl;
        std::cout << std::endl;
    }
}



int main() {
    interpreter brainFuDGETest;
    brainFuDGETest.logging = false;

    std::string program;
    std::cout << "Enter Your Program: " << std::endl;
    std::cin >> program;

    brainFuDGETest.loadProgram(program);

    brainFuDGETest.interpret();

    std::cin; //So the console doesnt close after executing lol.
}
/* Example Program
"+++++[>+++++[.-]<-]"

mem[0] = 5
while mem[0] != 0 {
    mem[1] += 1
    mem[0] -= 1
}
print(mem[1])

This program has no purpose, it is just here for demonstrational purposes and to demonstrate the interpreteres ability to nest loops.
*/
