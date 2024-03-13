"""
Link:https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are the multiples of 3 or 5,we get 3,5,6,9. The sum of these multiples is 23. 
Find the sum of all the multiples of 3 or 5 below 1000


"""

def find_sum_for_multiples_of_three_or_five(max):
    return sum(e for e in range(1, max) if e%3==0 or e%5==0)
    #return sum(e for e in range(3, n) if e % 3 == 0 or e % 5 == 0)


if __name__ == "__main__":
    max=1000
    sum=find_sum_for_multiples_of_three_or_five(max)
    print(f"Sum Of Multiple Of 3 or 5 , below {max} is {sum}")
