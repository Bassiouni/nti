def fill_arr():
    arr = input("->> ").split(" ")
    if len(arr) != 5:
        raise Exception("Not of size 5")

    for idx, _ in enumerate(arr):
        arr[idx] = int(arr[idx])

    arr.sort()
    print(arr)
    arr.sort(reverse=True)
    print(arr)


print("fill_arr")
fill_arr()


print("=" * 50)
