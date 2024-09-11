'''
40:Given a Huffman Tree and a Huffman encoded string, decode the string to get the original message.
Test Case 1:
Input:
n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
encoded_string = '1101100111110'
Output:"abacd"
Test Case 2:
Input:
n = 6
characters = ['f', 'e', 'd', 'c', 'b', 'a']
frequencies = [5, 9, 12, 13, 16, 45]
encoded_string = '110011011100101111001011'
Output:"fcbade"
 Container Loading

'''
import heapq
from collections import defaultdict, namedtuple

# Define a node structure for the Huffman Tree
Node = namedtuple('Node', ['char', 'freq', 'left', 'right'])

def build_huffman_tree(characters, frequencies):
    heap = [Node(char, freq, None, None) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_code_map(node, prefix='', code_map={}):
    if node.char is not None:
        code_map[node.char] = prefix
    else:
        build_code_map(node.left, prefix + '0', code_map)
        build_code_map(node.right, prefix + '1', code_map)
    return code_map

def decode_huffman(encoded_string, huffman_tree):
    current_node = huffman_tree
    decoded_message = []
    
    for bit in encoded_string:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_message.append(current_node.char)
            current_node = huffman_tree
            
    return ''.join(decoded_message)

# Example usage
n = 4
characters = ['a', 'b', 'c', 'd']
frequencies = [5, 9, 12, 13]
encoded_string = '1101100111110'

huffman_tree = build_huffman_tree(characters, frequencies)
decoded_message = decode_huffman(encoded_string, huffman_tree)
print(decoded_message)  # Output: abacd
