class LMC:
    def __init__(self):
        self.memory = [0] * 100
        self.pc = 0
        self.acc = 0
        self.running = True

    def load_program(self, program):
        """
        Load a program into memory.

        :param program: A list of integers representing LMC instructions.
        """
        if len(program) <= len(self.memory):
            for i in range(len(program)):
                self.memory[i] = program[i]

    def fetch(self):
        """
        Fetch the next instruction from memory and increment the program counter.
        """
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def execute(self, opcode, operand):
        """
        Execute an LMC instruction based on its opcode and operand.
        """
        if opcode == 1:  # LDA (Load)
            print(f"Loading Value {self.memory[operand]}")
            self.acc = self.memory[operand]
        elif opcode == 2: # STA (Store)
            print(f"Storing Value {self.memory[operand]}")
            self.memory[operand] = self.acc
        elif opcode == 3:  # ADD (Add)
            print(f"Adding {self.memory[operand]} to {self.acc} = {self.acc + self.memory[operand]}")
            self.acc += self.memory[operand]
        elif opcode == 4:  # SUB (Subtract)
            print(f"Subtracting {self.memory[operand]} from {self.acc} = {self.acc - self.memory[operand]}")
            self.acc -= self.memory[operand]
        elif opcode == 5:  # INP (Input)
            value = int(input("Enter a number:"))
            print(f"Input {value}")
            self.memory[operand] = value
        elif opcode == 6:  # OUT (Output)
            print(f"Outputing {self.acc}")            
        elif opcode == 0:  # HLT (Halt)
            print(f"Halting programm")
            self.running = False

    def run(self):
        self.running = True
        """
        Run the LMC program until HLT instruction is encountered.
        """
        while self.running:
            instruction = self.fetch()
            # print(instruction)
            opcode = instruction // 100
            operand = instruction % 100
            self.execute(opcode, operand)

    def assemble(self, program):
        """
        Assemble LMC assembly code into numeric instructions.
        """
        opcode_map = {            
            "LDA": 1,  # Load to Accumulator
            "STA": 2,  # Store Accumulator
            "ADD": 3,  # Add to Accumulator
            "SUB": 4,  # Subtract from Accumulator            
            "INP": 5,  # Input
            "OUT": 6,  # Output
            "HLT": 0,  # Halt
            "DAT": 8,  #
        }

        assembled_program = []

        for line in program:
            parts = line.split()
            if parts[0] in opcode_map:
                opcode = opcode_map[parts[0]]
                if len(parts) > 1:
                    operand = int(parts[1])
                else:
                    operand = 0
                assembled_program.append(opcode * 100 + operand)
            else:
                # print(f"Unknown instruction: {line}")
                opcode = parts[0]                
                operand = int(parts[0])                
                assembled_program.append(operand)

        return assembled_program

if __name__ == "__main__":    
    # programm in opcode
    # lmc = LMC()
    # programOne = [
    #     0,   1,   2,   3,   4,   5
    #     104, 305, 600, 000, 10, 20
    #     # This program adds two numbers and outputs the result.      
    # ]    
    # lmc.load_program(programOne)
    # lmc.run()
   
    # programm in opcode
    # lmc = LMC()
    # programTwo = [
    # #   0,   1,   2,   3,   4,   5
    #     104, 405, 600, 000, 20, 5
    #     # This program subtracts two numbers and outputs the result.      
    # ]
    # lmc.load_program(programTwo)
    # lmc.run()
   
    #programm in assembler
    lmc = LMC()
    assembly_program = [
        "LDA 4",        
        "ADD 5",
        "OUT",
        "HLT",
        "10",
        "20"      
    ]
    program = lmc.assemble(assembly_program)
    lmc.load_program(program)
    lmc.run()