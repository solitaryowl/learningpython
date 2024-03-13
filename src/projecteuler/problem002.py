"""
Link:https://projecteuler.net/minimal=2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,the first 5 terms will be: 1,2,3,5,8

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""


def fibonacci_even_sum_upto_max(max):
    sum=0
    n1=1
    n2=2
    while n2 < max:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        sum = sum + n3
    return sum


if __name__ == "__main__":
    max = 4000000
    sum = (fibonacci_even_sum_upto_max(max))
    print(f"Sum of even numbered fibonacci sequence smaller than {max} is: {sum}")