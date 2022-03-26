import os

'''
aabc
    
'''
def remove_deplicate_num(num_list):
    n = len(num_list)
    if n<=1: return n, num_list

    i=0
    j=1
    while j<n:
        if num_list[i]==num_list[j]:
            j+=1
            continue
        i+=1
        num_list[i] = num_list[j]
        j+=1
    return i+1, num_list[:i+1]


def remove(A):
    length = len(A)
    # trivial
    if length==0 or length==1:
        return length
    # closed pointer, open pointer
    i = 0
    j = 1
    while j<length:
        # find the next non-duplicate:
        if A[i]==A[j]:
            j += 1
            continue  # go to the next iteration
        A[i+1] = A[j]
        i += 1
        j += 1
    return i+1, A[:i+1]

M= [l for l in 'aaabcccddfeggg']
print(remove(M))