# how to find the power of number using recursion ?
# step 1 : recursive case - the flow x^n = x * x^n-1
# step 2 : base case - the stopping criterion n = 0 , n = 1
# step 3 : unintentional case - the constraint power(-1, 2) , power(3.2,2) , power(2,1.2), power(2,-1)


def power(base, exp):
    assert exp>=0 and int(exp) == exp, 'The exponent must be positive integer only!'
    if exp == 0:
        return 1
    if exp == 1:
        return base

    return base * power(base, exp-1)

