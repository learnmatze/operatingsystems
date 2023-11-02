import os
import struct

# Constants
SECTOR_SIZE = 512  # Standard sector size for FAT file systems
CLUSTER_SIZE = 4096  # Cluster size in bytes

# Initialize the FAT table
FAT_TABLE = [0] * (CLUSTER_SIZE // 4)  # Each entry is a 32-bit value (4 bytes)
NUM_CLUSTERS = 10  # Number of clusters in the file system
FAT_TABLE[0] = 0xFFFFFFF8  # Reserved cluster
FAT_TABLE[1] = 0xFFFFFFFF  # End of cluster chain
for i in range(2, NUM_CLUSTERS):
    FAT_TABLE[i] = i + 1  # Link clusters in a chain

# Simple directory structure
ROOT_DIR = {
    "file1.txt": {"cluster": 2, "size": 512},
    "file2.txt": {"cluster": 4, "size": 768},
}

def read_cluster(cluster_number):
    # Simulate reading a cluster from storage
    data = bytearray(CLUSTER_SIZE)
    for i in range(CLUSTER_SIZE):
        data[i] = i % 256  # Filling with some sample data
    return data

def get_cluster_offset(cluster_number):
    # Calculate the offset of a cluster in bytes
    return cluster_number * CLUSTER_SIZE

def read_file(filename):
    if filename in ROOT_DIR:
        file_info = ROOT_DIR[filename]
        cluster_number = file_info["cluster"]
        data = bytearray(file_info["size"])
        offset = 0
        while cluster_number < 0xFFFFFFF7:
            cluster_data = read_cluster(cluster_number)
            data[offset : offset + CLUSTER_SIZE] = cluster_data
            offset += CLUSTER_SIZE
            cluster_number = FAT_TABLE[cluster_number]
        return data
    return None

def main():
    # Example: Read a file
    filename = "file1.txt"
    data = read_file(filename)
    if data:
        print(f"Reading '{filename}' ({len(data)} bytes):")
        print(data)
    else:
        print(f"'{filename}' not found.")

if __name__ == "__main__":
    main()