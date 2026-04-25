
#Sum of differneces between two lists
def sum_of_differences(lst):
    if len(lst) < 2:
        return 0
    else:
        lst.sort()
        sum = 0
        for i in range(len(lst)-1):
            sum += lst[i+1] - lst[i]
        return sum
    
print(sum_of_differences([1, 2, 10]))
