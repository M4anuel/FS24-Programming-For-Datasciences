def find_divisors(number: int) -> list[int]:
    divisors: list[int] = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)

    return divisors
def find_common_divisors(number1: int, number2: int) -> list[int]:
    return list(set(find_divisors(number1)) & set(find_divisors(number2)))

print(find_divisors(20))
print(find_common_divisors(20,30))