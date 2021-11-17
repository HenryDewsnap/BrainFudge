#include <functional>
#include <iostream>
#include <vector>
#include <map>

class interpreter {
    //Brain Fuck Functions.
    private:
        void imp() { memory_pointer += 1; if (memory_pointer >= 256) { memory_pointer = 0; } }; //Incriment Mem Pointer
        void dmp() { memory_pointer -= 1; if (memory_pointer < 0) { memory_pointer =  255; } }; //Decrement Mem Pointer
        
        void ivs() { memory.at(memory_pointer) += 1; }; //Increase Value Stored
        void dvs() { memory.at(memory_pointer) -= 1; }; //Decrease Value Stored

        void slp() { loopLayer+=1; loopStarts.push_back(instruction_pointer); }; //Start A Loop (Executes until the mem pointers addressed value == 0)
        void elp() { if (memory.at(memory_pointer) == 0) { loopLayer -= 1; loopStarts.pop_back(); } else { instruction_pointer = loopStarts.back(); } }; //End A Loop / return backto start.

        void gtc() { std::string inpStr; std::vector<char> inpStrVec; std::cin >> inpStr; for (char c: inpStr) { inpStrVec.push_back(c); } memory.at( memory_pointer ) = (int)inpStrVec.at(0); }; //Get character (reads one character from the console/cli)
        void ptc() { std::cout << (char)memory.at(memory_pointer) << std::endl; }; //Put character (prints one character to the console/cli)

    //Interpreter Variables.
    private:
        int memory_pointer = 0;
        int instruction_pointer = 0;
        std::vector<int> memory;
        std::string program_data;

        std::vector<int> loopStarts; //This takes the loop depth and returns their initial functions address allowing for nested recursion.
        int loopLayer = 0;

    public:
        bool logging = true;
        void interpret();
};

void interpreter::interpret() {
    while (true) {
        if (logging) {
            std::cout << "Instruction Pointer: " << instruction_pointer << std::endl;
            std::cout << "Memory Pointer: " << memory_pointer << std::endl;
            std::cout << "Current Address Value: " << memory.at(memory_pointer) << std::endl;
        }

        char currentInst = program_data[instruction_pointer];

        //Im aware i should use a switch/case statement but they dont appear to like me very much...
        if (currentInst == (char)">") {
            imp();
        }
        if (currentInst == (char)"<") {
            dmp();
        }
        if (currentInst == (char)"+") {
            ivs();
        }
        if (currentInst == (char)"-") {
            dvs();
        }
        if (currentInst == (char)"[") {
            slp();
        }
        if (currentInst == (char)"]") {
            elp();
        }
        if (currentInst == (char)",") {
            gtc();
        }
        if (currentInst == (char)".") {
            ptc();
        }

        instruction_pointer += 1;
    }
}


