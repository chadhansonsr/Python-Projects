import sys


class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.direction = ''


def char_freq(data):
    chars = dict()
    for x in data:
        if chars.get(x) is None:
            chars[x] = 1
        else:
            chars[x] += 1
    return chars


codes = dict()


def huffman_codes(node, value=''):
    newValue = value + str(node.direction)
    if (node.left):
        huffman_codes(node.left, newValue)
    if (node.right):
        huffman_codes(node.right, newValue)
    if (not node.left and not node.right):
        codes[node.char] = newValue

    return codes


def huffman_encoding(data):
    char_with_freq = char_freq(data)
    chars = char_with_freq.keys()

    nodes = []

    for char in chars:
        nodes.append(Node(char_with_freq.get(char), char))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        right = nodes[0]
        left = nodes[1]

        left.direction = 0
        right.direction = 1

        newNode = Node(left.freq+right.freq, left.char+right.char, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    huffman_encoding = huffman_codes(nodes[0])
    encodedOutput = encoded_output(data, huffman_encoding)
    return encodedOutput, nodes[0]


def encoded_output(data, coding):
    encodedOutput = []
    for _ in data:
        encodedOutput.append(coding[_])

    string = ''.join([str(x) for x in encodedOutput])
    return string


def huffman_decoding(data, tree):
    head = tree
    decodedOutput = []
    for _ in data:
        if _ == '1':
            tree = tree.right
        elif _ == '0':
            tree = tree.left
        try:
            if tree.left.char is None and tree.right.char is None:
                pass
        except AttributeError:
            decodedOutput.append(tree.char)
            tree = head

    string = ''.join([str(x) for x in decodedOutput])
    return string


if __name__ == "__main__":

    a_great_sentance = "The bird is the word"

    print("\n\nThe size of the data is: {}".format(sys.getsizeof(a_great_sentance)))  # noqa size is 69
    print("The content of the data is: {}".format(a_great_sentance))

    encoded_data, tree = huffman_encoding(a_great_sentance)

    if encoded_data:
        encoded_data_int = int(encoded_data, base=2)
        print("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data_int)))  # noqa
        print("The content of the encoded data is: {}".format(encoded_data))
    else:
        print("The data cannot be encoded as entered. Please try a different entry.")  # noqa

    decoded_data = huffman_decoding(encoded_data, tree)

    if decoded_data:
        decoded_data_int = int(encoded_data, base=2)
        print("The size of the decoded data is: {}".format(sys.getsizeof(huffman_decoding(encoded_data, tree))))  # noqa
        print("The content of the decoded data is: {}".format(decoded_data))  # noqa size is 36
    else:
        print("There is no encoded data to show. ")

    test_case_1 = "AAAAA"

    print("\n\nThe size of the data is: {}".format(sys.getsizeof(test_case_1)))  # noqa size is 69
    print("The content of the data is: {}".format(test_case_1))

    encoded_data, tree = huffman_encoding(test_case_1)

    if encoded_data:
        encoded_data_int = int(encoded_data, base=2)
        print("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data_int)))  # noqa
        print("The content of the encoded data is: {}".format(encoded_data))
    else:
        print("The data cannot be encoded as entered. Please try another entry.")  # noqa

    decoded_data = huffman_decoding(encoded_data, tree)

    if decoded_data:
        decoded_data_int = int(encoded_data, base=2)
        print("The size of the decoded data is: {}".format(sys.getsizeof(huffman_decoding(encoded_data, tree))))  # noqa
        print("The content of the decoded data is: {}".format(decoded_data))
    else:
        print("There is no encoded data to show. ")  # noqa error will be displayed since data cannot be encoded

    test_case_2 = "GO BLUE!!!"

    print("\n\nThe size of the data is: {}".format(sys.getsizeof(test_case_2)))  # noqa size is 74
    print("The content of the data is: {}".format(test_case_2))

    encoded_data, tree = huffman_encoding(test_case_2)

    if encoded_data:
        encoded_data_int = int(encoded_data, base=2)
        print("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data_int)))  # noqa
        print("The content of the encoded data is: {}".format(encoded_data))
    else:
        print("The data cannot be encoded as entered. Please try another entry.")  # noqa

    decoded_data = huffman_decoding(encoded_data, tree)

    if decoded_data:
        decoded_data_int = int(encoded_data, base=2)
        print("The size of the decoded data is: {}".format(sys.getsizeof(huffman_decoding(encoded_data, tree))))  # noqa
        print("The content of the decoded data is: {}".format(decoded_data))  # noqa size is 75
    else:
        print("There is no encoded data to show. ")

    test_case_3 = ("ABC" * 99)

    print("\n\nThe size of the data is: {}".format(sys.getsizeof(test_case_3)))  # noqa size is 74
    print("The content of the data is: {}".format(test_case_3))

    encoded_data, tree = huffman_encoding(test_case_3)

    if encoded_data:
        encoded_data_int = int(encoded_data, base=2)
        print("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data_int)))  # noqa
        print("The content of the encoded data is: {}".format(encoded_data))
    else:
        print("The data cannot be encoded as entered. Please try another entry.")  # noqa

    decoded_data = huffman_decoding(encoded_data, tree)

    if decoded_data:
        decoded_data_int = int(encoded_data, base=2)
        print("The size of the decoded data is: {}".format(sys.getsizeof(huffman_decoding(encoded_data, tree))))  # noqa
        print("The content of the decoded data is: {}".format(decoded_data))  # noqa size is 75
    else:
        print("There is no encoded data to show. ")
