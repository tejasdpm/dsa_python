#step 1 Recursive case - the flow
# s1 : divide the number by 2
# s2 : get the integer quotient for the next iteration
# s3 : get the remainder for the binary digit
# s4 : repeat the steps until the quotient is equal to 0
# 10 to binary 10/2 = q=5, r=0, 5/2 = q=2,r=1, 2/2 = q=1 r=0, 1/2 q=0, r=1,  (calculate from back i.e. 1010)
# f(n) = n mod 2 + 10 * f(n/2)
# step 2 : base case - the stopping criterion n = 0
# step 3 : unintentional case - the constraint    n must be positive integers

def decimalToBinary(n):
    assert int(n) == n, 'the parameter must be an integer only'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))



print(decimalToBinary(10))