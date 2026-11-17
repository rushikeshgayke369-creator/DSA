
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    result = []

    for i in range(n - m + 1):
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            result.append(i)

    print("Matching indices:", result)


text = input("Enter text: ")
pattern = input("Enter pattern: ")

naive_search(text, pattern)
