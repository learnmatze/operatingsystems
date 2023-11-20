class MemoryBlock:
    def __init__(self, start, size, is_allocated=False):
        self.start = start
        self.size = size
        self.is_allocated = is_allocated
        self.next_block = None

class MemoryManager:

    def __init__(self, total_memory_size, fit_algorithm="first_fit"):
        self.total_memory_size = total_memory_size
        self.memory = MemoryBlock(0, total_memory_size)
        self.fit_algorithm = fit_algorithm

    def allocate_memory(self, size):
        if self.fit_algorithm == "first_fit":
            return self.first_fit(size)
        elif self.fit_algorithm == "best_fit":
            return self.best_fit(size)
        elif self.fit_algorithm == "worst_fit":
            return self.worst_fit(size)
        else:
            print("Invalid fit algorithm specified.")
            return None

    def first_fit(self, size):
        current_block = self.memory
        while current_block:
            if not current_block.is_allocated and current_block.size >= size:
                if current_block.size > size:
                    new_block = MemoryBlock(current_block.start + size, current_block.size - size)
                    new_block.next_block = current_block.next_block
                    current_block.next_block = new_block
                current_block.size = size
                current_block.is_allocated = True
                return current_block.start
            current_block = current_block.next_block
        return None

    def best_fit(self, size):
        best_fit_block = None
        current_block = self.memory

        while current_block:
            if not current_block.is_allocated and current_block.size >= size:
                if best_fit_block is None or current_block.size < best_fit_block.size:
                    best_fit_block = current_block

            current_block = current_block.next_block

        if best_fit_block:
            if best_fit_block.size > size:
                new_block = MemoryBlock(best_fit_block.start + size, best_fit_block.size - size)
                new_block.next_block = best_fit_block.next_block
                best_fit_block.next_block = new_block

            best_fit_block.size = size
            best_fit_block.is_allocated = True
            return best_fit_block.start

        return None

    def worst_fit(self, size):
        # Implement worst fit logic here
        # ...
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
memory_manager = MemoryManager(1024, fit_algorithm="first_fit")

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
