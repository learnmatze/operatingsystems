class Memory:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def read(self, address):
        if 0 <= address < self.size:
            return self.data[address]
        else:
            return None

    def write(self, address, value):
        if 0 <= address < self.size:
            self.data[address] = value
            return True
        else:
            return False

class Swapper:
    def __init__(self, memory, secondary_storage):
        self.memory = memory
        self.secondary_storage = secondary_storage

    def swap_to_secondary_storage(self, address):
        if 0 <= address < self.memory.size:
            data = self.memory.data[address]
            if data is not None:
                self.memory.data[address] = None
                self.secondary_storage.store(address, data)
                return True
        return False

    def swap_to_memory(self, address):
        if 0 <= address < self.memory.size:
            data = self.secondary_storage.load(address)
            if data is not None:
                self.memory.data[address] = data
                return True
        return False

class SecondaryStorage:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def store(self, address, data):
        if 0 <= address < self.size:
            self.data[address] = data

    def load(self, address):
        if 0 <= address < self.size:
            return self.data[address]
        else:
            return None

def main():
    memory = Memory(4096)
    secondary_storage = SecondaryStorage(8192)
    swapper = Swapper(memory, secondary_storage)
    # Daten in den Speicher schreiben
    memory.write(100, "Daten im Speicher")
    memory.write(200, "Anderne Daten im Speicher")
    # Daten von Speicher in sekundären Speicher verschieben
    swapper.swap_to_secondary_storage(100)
    data = memory.read(100)
    if data == None:
        # Daten von sekundärem Speicher in den Speicher zurückverschieben
        swapper.swap_to_memory(100)
    second_data = memory.read(200)
    if second_data == None:
        # Daten von sekundärem Speicher in den Speicher zurückverschieben
        swapper.swap_to_memory(200)
    # Lesen der Daten
    data = memory.read(100)
    print("Gelesene Daten:", data)
    second_data = memory.read(200)
    print("Gelesene Andere Daten:", second_data)
    

if __name__ == "__main__":
    main()