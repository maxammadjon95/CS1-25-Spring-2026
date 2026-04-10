def count_distinct_bruteforce(s):
    substrings = set()

    for i in range(len(s)):
        current = ""
        for j in range(i, len(s)):
            current += s[j]
            substrings.add(current)

    return len(substrings)


def count_distinct_efficient(s):
    n = len(s)

    suffixes = [s[i:] for i in range(n)]

    suffixes.sort()

    def lcp(a, b):
        length = 0
        while length < min(len(a), len(b)) and a[length] == b[length]:
            length += 1
        return length

    total = n * (n + 1) // 2

    overlap = 0
    for i in range(1, n):
        overlap += lcp(suffixes[i], suffixes[i - 1])

    return total - overlap

if __name__ == "__main__":
    s = "abaa"

    print("String:", s)

    print("\nBrute force result:")
    print(count_distinct_bruteforce(s))

    print("\nEfficient result:")
    print(count_distinct_efficient(s))