def is_prime(n):
    if n<2:
        return False
    return all(n%i != 0 for i in range(2, int(n**0.5)+1))

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

num_list= list(map(int, input().split()))
prime_numbers = filter_prime(num_list)

print(prime_numbers)