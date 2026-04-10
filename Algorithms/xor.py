def build_prefix_xor(arr):
    prefix = [0] * (len(arr) + 1)

    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i - 1] ^ arr[i - 1]

    return prefix

def range_xor(prefix, a, b):
    return prefix[b] ^ prefix[a - 1]

def range_xor_bruteforce(arr, a, b):
    xor_sum = 0

    for i in range(a - 1, b):
        xor_sum = xor_sum ^ arr[i]

    return xor_sum

if __name__ == "__main__":
    arr = [3, 2, 4, 5, 1, 1, 5, 3]

    queries = [
        (2, 4),
        (5, 6),
        (1, 8),
        (3, 3)
    ]

    prefix = build_prefix_xor(arr)

    print("Fast (prefix XOR):")
    for a, b in queries:
        print(range_xor(prefix, a, b))

    print("\nBrute force:")
    for a, b in queries:
        print(range_xor_bruteforce(arr, a, b))