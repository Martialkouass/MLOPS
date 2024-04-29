# function to check if a number is prime or not
import math
def is_prime(n):
    if n < 2:
        return False
    elif isinstance(n, float):
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(nums):
    return sum([n for n in nums if is_prime(n)])

def main():
    # Take input as a list of numbers separated by spaces
    nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    
    # Check if each number is prime and sum the prime numbers
    primes = [num for num in nums if is_prime(num)]
    print("Prime numbers in the list:", primes)
    print("Sum of prime numbers in the list:", sum_of_primes(nums))

if __name__ == "__main__":
    main()