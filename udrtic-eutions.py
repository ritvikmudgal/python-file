import math
A=int(input("Enter A-")) 
B=int(input("Enter B-")) 
C=int(input("Enter C-")) 
D=(B*B)-(4*A*C) 
if D>0:
    E=(-B+(math.sqrt(D)))/(2*A )
    F=(-B-(math.sqrt(D)))/(2*A)
    print("First root = ",E) 
    print() 
    print("Second root = ",F) 
if D==0: 
    E=(-B+(math.sqrt(D)))/2*A 
    print("Same roots exist")
    print("root = ",E) 
if D<0: 
    print("No Real roots")

