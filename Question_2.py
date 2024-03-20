n = int(input())
for i in range(n):
    one = []
    two = []
    three = []

    solution = 0
    c = int(input()) # / 4
    
    for l in range(c):
        case = input().split()
        
        if case[0] == '1':
            one.append(int(case[1]))
        elif case[0] == '2':
            two.append(int(case[1]))
        elif case[0] == '3':
            three.append(int(case[1]))
            
    if max(one) > min(two):
        solution = 0
    else:
        numbers_one_two = [num for num in three if num >= max(one) and num <= min(two)]
        operation = min(two) - (len(numbers_one_two) + (max(one) - 1))
                
        solution = operation
    
    print(solution)