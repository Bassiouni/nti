def longest_substr(string: str):
    l = [string[0]]
    li = 0

    idx = 1
    while len(string) != idx:
        if l[li][-1] < string[idx]:
            l[li] += string[idx]
        else:
            li += 1
            l.append(string[idx])
        idx += 1

    return max(l, key=len)


print(longest_substr("abdulrahman"))
