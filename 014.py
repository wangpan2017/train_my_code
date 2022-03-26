import os

def three_sum(num_list):
    '''
    a+b+c = 0, a<b<c
    sort num_list

    '''
    num_list.sort()

    n = len(num_list)
    assert len(num_list)>2, 'length error.'

    res_list = []
    k = 0
    while k<n-2:

        i = k+1
        j = n-1

        while i<j:
            ch = [num_list[k], num_list[i], num_list[j]]
            sum_ch = sum(ch)
            if sum_ch==0:
                res_list.append(ch)
                i+=1
                j-=1
            elif sum_ch>0:
                j-=1
            else:
                i+=1
        
        if k<n-3 and num_list[k]==num_list[k+1]:
            k+=2
        else:
            k+=1
            
    return res_list

if __name__ == '__main__':
    a = [2,4,5,-3,0, -9, -2, -1, -6, -7, -8, 6,7, 8]
    print(three_sum(a))


    