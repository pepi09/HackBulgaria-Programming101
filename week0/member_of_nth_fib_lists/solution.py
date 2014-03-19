def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        return nth_fib_lists(listB,listA+listB,n-1) 

def member_of_nth_fib_lists(listA,listB,needle):
    i = 1
    temp_list = listA
    while len(temp_list) < len(needle):
        temp_list = nth_fib_lists(listA,listB,i)
        i+=1
    if temp_list == needle:
        return True
    else:
        return False