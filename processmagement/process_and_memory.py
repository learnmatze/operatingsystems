class Memory:
    def __init__(self, size):
        self.size = size
        self.memory = [0] * size

    def read(self, address):
        if 0 <= address < self.size:
            return self.memory[address]
        else:
            return None

    def write(self, address, data):
        if 0 <= address < self.size:
            self.memory[address] = data

class Process:
    def __init__(self, pid):
        self.pid = pid

    def execute(self, memory, instructions):
        for address, data in instructions:
            memory.write(address, data)

if __name__ == "__main__":
    instructions = { "load": 1, "store": 2, "add": 3, "sub": 4, "mul": 5}
    memory_size = 50
    memory = Memory(memory_size)
    process1 = Process(1)    
    instructions1 = [(0, 1), (1, 1), (2, 3), (3, 1), (4, 4), (5, 2)]
    process1.execute(memory, instructions1)
    process2 = Process(2)
    instructions2 = [(10, 1), (11, 1), (12, 3), (13, 2)]
    process2.execute(memory, instructions2)
    # Display memory contents
    for i in range(memory_size):
        data = memory.read(i)
        if data is not None:
            key = [key for key, value in instructions.items() if value == data]
            if key != []:
                print(f"Address {i}: {data} ({key[0]})")
            else:
                print(f"Address {i}: {data}")