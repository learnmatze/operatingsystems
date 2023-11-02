class MemoryBlock:
    def __init__(self, start, size, is_allocated=False):
        self.start = start
        self.size = size
        self.is_allocated = is_allocated
        self.next_block = None

class MemoryManager:
    def __init__(self, total_memory_size):
        self.total_memory_size = total_memory_size
        self.memory = MemoryBlock(0, total_memory_size)
   
    def allocate_memory(self, size):
        current_block = self.memory
        while current_block:
            if not current_block.is_allocated and current_block.size >= size:
                if current_block.size > size:
                    # Split the block if it's larger than needed
                    new_block = MemoryBlock(current_block.start + size, current_block.size - size)
                    new_block.next_block = current_block.next_block
                    current_block.next_block = new_block
                current_block.size = size
                current_block.is_allocated = True
                return current_block.start
            current_block = current_block.next_block
        return None

    def deallocate_memory(self, start):
        current_block = self.memory
        while current_block:
            if current_block.start == start:
                current_block.is_allocated = False
                # Merge adjacent free blocks
                while current_block.next_block and not current_block.next_block.is_allocated:
                    current_block.size += current_block.next_block.size
                    current_block.next_block = current_block.next_block.next_block
                return
            current_block = current_block.next_block

    def print_memory_status(self):
        current_block = self.memory
        while current_block:
            status = "Allocated" if current_block.is_allocated else "Free"
            print(f"Start: {current_block.start}, Size: {current_block.size}, Status: {status}")
            current_block = current_block.next_block

# Beispielverwendung
memory_manager = MemoryManager(1024)  # Gesamtspeichergröße: 1024 Einheiten

# Allokation von Speicherblöcken
block1 = memory_manager.allocate_memory(256)
block2 = memory_manager.allocate_memory(128)
block3 = memory_manager.allocate_memory(512)

# Druck der aktuellen Speicherbelegung
memory_manager.print_memory_status()

# Deallokation von Speicherblöcken
memory_manager.deallocate_memory(block1)
memory_manager.deallocate_memory(block2)

# Druck der aktualisierten Speicherbelegung nach Deallokation
memory_manager.print_memory_status()