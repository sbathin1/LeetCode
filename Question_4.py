def commonElements (A, B, C, n1, n2, n3):
    A=set(A)
    B=set(B)
    C=set(C)
    x=[]
    for i in A:
        if i in B and i in C:
            x.append(i)
    x.sort()
    print(x)
        
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}

commonElements(A, B, C, n1, n2, n3)