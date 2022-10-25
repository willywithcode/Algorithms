print("Nhap so hang thu nhat:")
__integer__1 = str(input())
print("Nhap so hang thu hai:")
__integer__2 = str(input())
def add(__number__1,__number__2):
    max_len = max(len(__number__1),len(__number__2))
    __number__1 = __number__1.zfill(max_len)
    __number__2 = __number__2.zfill(max_len)
    sum = ""
    count = max_len -1
    temp = 0
    while count != -1:
        sum1 = int(__number__1[count] ) + int(__number__2[count]) + temp
        temp = sum1 // 10
        sum = str(sum1)[-1] + sum
        count -= 1
    if temp == 1:
        return str(temp) + sum
    return sum



def mini__multiply(__number__1,__number__2):
    temp = 0
    multi = ""
    count = len(__number__1) -1
    while count != -1: 
        multi__temp = int(__number__1[count]) * int(__number__2) + temp
        multi = str(multi__temp)[-1] + multi
        temp = multi__temp // 10
        count -= 1
    if temp != 0: 
        return str(temp) + multi
    return multi

def multiply(__number__1,__number__2):
    sum = ""
    for n in range(len(__number__2)):
        sum = add(mini__multiply(__number__1,__number__2[-n-1])+'0'*n,sum)
    return sum
print("Tich hai so tren la : \n",multiply(__integer__1,__integer__2))