def fizzbuzz(n: int):
    msg = ''

    if n % 3 == 0:
        msg += "Fizz"

    if n % 5 == 0:
        msg += "Buzz"

    print(msg if msg else n)


for i in range(1, 21):
    fizzbuzz(i)

print("=" * 50)
