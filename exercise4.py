X = 1
A = 3
B = 5
C = 8
D = 7

print(not(X>3)) # False
print((X<1) and not(B>D)) # False
print(not(D<0) and (C>5)) # True
print(not(X>3) or (C<7)) # True
print((A>B) or (C>B)) # True
print((X>=2)) # False
print((X<1) and (B>=D)) # False