def return_recursion_result(n):

    sum_even = 0
    sum_odd = 0

    def recursive_function(n):
        if n == 0 or n == 1: # in case a number is odd => n-2...1
            return 0

        return n + recursive_function(n-2)

    if n % 2 == 0:
        sum_even = recursive_function(n)
        sum_odd = 1 + recursive_function(n-1)
    else:
        sum_odd = 1 + recursive_function(n) # in case an odd number occurs, the function stops at 1 => add 1 here
        sum_even = recursive_function(n-1)

    return sum_odd+sum_even, sum_even, sum_odd # tuple