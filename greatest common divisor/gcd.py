# gcd of two numbers
# step 1 : recursive case - the flow
# gcd is the largest positive integer that divides the number without a remainder
# gcd(48/18)
# step 1 : 48/18 = 2 remainder 12
# step 2 : 18/12 = 1 remainder 6
# step 3 : 12/6 = 2 remainder 0
# gcd(a,0) = a
# gcd(a,b) = gcd(b,a mod b)

# step 2 : base case - the stopping criterion b = 0
# step 3 : unintentional case - the constraint    positive integers, convert negative numbers to positive

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'the numbers must be integers only !'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
print(gcd(48,18))