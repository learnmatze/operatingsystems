class PageTable:
    def __init__(self, num_pages, page_size):
        self.num_pages = num_pages
        self.page_size = page_size
        self.pages = [None] * num_pages

    def load_page(self, page_num, data):
        if page_num < 0 or page_num >= self.num_pages:
            return False
        if len(data) != self.page_size:
            return False
        self.pages[page_num] = data
        return True

    def access_memory(self, logical_address):
        page_num, offset = divmod(logical_address, self.page_size)
        if page_num < 0 or page_num >= self.num_pages or self.pages[page_num] is None:
            return None
        physical_address = (page_num * self.page_size) + offset
        return self.pages[page_num][offset], physical_address

def main():
    num_pages = 4
    page_size = 4096  # 4 KB
    page_table = PageTable(num_pages, page_size)

    # Laden von Seiten in den Speicher
    for i in range(num_pages):
        data = bytearray([i] * page_size)
        page_table.load_page(i, data)

    # Zugriff auf logische Adressen
    logical_addresses = [8192, 16384, 12288, 4096]
    for address in logical_addresses:
        data, physical_address = page_table.access_memory(address)
        if data is not None:
            print(f"Logische Adresse {address} => Physische Adresse {physical_address}, Wert: {data}")
        else:
            print(f"Seite nicht im Speicher: Logische Adresse {address}")

if __name__ == "__main__":
    main()