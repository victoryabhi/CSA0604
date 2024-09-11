'''
Optimal Tree Problem: Huffman Trees and Codes
39:Given a set of characters and their corresponding frequencies, construct the Huffman Tree and generate the Huffman Codes for each character.
Test Case 1:
Input:n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
Output:[('a', '110'), ('b', '10'), ('c', '0'), ('d', '111')]
Test Case 2:
Input:
n = 6
characters = ['f', 'e', 'd', 'c', 'b', 'a']
frequencies = [5, 9, 12, 13, 16, 45]
Output:[ ('a', '0'), ('b', '101'), ('c', '100'), ('d', '111'), ('e', '1101'), ('f', '1100')]


'''
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(characters, frequencies):
    heap = [Node(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}
    generate_codes(root, "", codes)
    return sorted(codes.items(), key=lambda x: x[1])

def generate_codes(node, current_code, codes):
    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)

# Test Case 1
characters1 = ['a', 'b', 'c', 'd']
frequencies1 = [5, 9, 12, 13]
print(huffman_coding(characters1, frequencies1))

# Test Case 2
characters2 = ['f', 'e', 'd', 'c', 'b', 'a']
frequencies2 = [5, 9, 12, 13, 16, 45]
print(huffman_coding(characters2, frequencies2))
