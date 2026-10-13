def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Test edge cases
test_numbers = [-5, 0, 1, 2, 3, 4, 9, 17, 25]
for n in test_numbers:
    print(f"{n}: {'Prime' if is_prime(n) else 'Not prime'}")
# Generate prime numbers within a range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
if start > end:
    print("Invalid range!")
else:
    print(f"Prime numbers between {start} and {end}:")

    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()
