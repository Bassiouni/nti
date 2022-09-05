def gen_arr(length: int, start: int) -> list[int]:
    rt = []

    x = 0
    while x != length:
        rt.append(start + x)
        x += 1

    return rt


print("gen_arr", gen_arr(5, 3))

print("=" * 50)
