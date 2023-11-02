class MemorySegment:
    def __init__(self, base, limit, name):
        self.base = base
        self.limit = limit
        self.name = name
        self.data = bytearray(limit)

    def read(self, logical_address):
        if self.base <= logical_address < self.base + self.limit:
            offset = logical_address - self.base
            return self.data[offset]
        else:
            return None

    def write(self, logical_address, value):
        if self.base <= logical_address < self.base + self.limit:
            offset = logical_address - self.base
            self.data[offset] = value
            return True
        else:
            return False

class MemoryManager:
    def __init__(self):
        self.segments = []

    def create_segment(self, base, limit, name):
        for segment in self.segments:
            if (base < segment.base + segment.limit and
                    base + limit > segment.base):
                return False  # Überlappung verhindern
        segment = MemorySegment(base, limit, name)
        self.segments.append(segment)
        return True

    def access_memory(self, logical_address):
        for segment in self.segments:
            value = segment.read(logical_address)
            if value is not None:
                return value, segment.name
        return None, "Nicht gefunden"

def main():
    memory_manager = MemoryManager()

    # Erstellen von Speichersegmenten
    memory_manager.create_segment(0, 4096, "Code")
    memory_manager.create_segment(4096, 4096, "Daten")
    memory_manager.create_segment(8192, 2048, "Stack")

    # Zugriff auf logische Adressen
    logical_addresses = [2048, 6144, 9000, 12000]
    for address in logical_addresses:
        data, segment_name = memory_manager.access_memory(address)
        if data is not None:
            print(f"Logische Adresse {address} => Segment {segment_name}, Wert: {data}")
        else:
            print(f"Logische Adresse {address} nicht zugeordnet")

if __name__ == "__main__":
    main()