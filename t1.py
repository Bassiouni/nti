def count_vowels(string: str) -> int:
    v: str = "aeiou"
    rt: int = 0

    for e in string:
        if e in v:
            rt += 1

    return rt


print("count_vowels", count_vowels("hello there people"))

print("=" * 50)
