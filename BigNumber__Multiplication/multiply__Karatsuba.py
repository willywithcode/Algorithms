
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



def subtract(__number__1,__number__2):
    max_len = max(len(__number__1),len(__number__2))
    __number__1 = __number__1.zfill(max_len)
    __number__2 = __number__2.zfill(max_len)
    sub = ""
    temp = 0
    for n in range(max_len):
        mini__sub = int(__number__1[-n-1]) - int(__number__2[-n-1]) - temp
        if mini__sub >= 0: 
            sub = str(mini__sub) + sub
            temp = 0
        else:
            sub = str(mini__sub + 10) + sub
            temp = 1
    return sub

def multiply(__number__1,__number__2):
    if len(__number__2) == 1 or len(__number__1) == 1:
        return mini__multiply(__number__1,__number__2)
    else:
        len__int = len(__number__1)
        pivot = len__int //2
        mul__1 = multiply(__number__1[:pivot],__number__2[:pivot])
        mul__2 = multiply(__number__1[pivot:],__number__2[pivot:])
        sum__1 = add(__number__1[:pivot],__number__1[pivot:])
        sum__2 = add(__number__2[:pivot],__number__2[pivot:])
        mul_3 = multiply(sum__1,sum__2)
        sub__1 = subtract(mul_3,mul__1)
        sub__2 = subtract(sub__1,mul__2)
        sum = add(mul__1 +'0'*(len__int - pivot)*2,mul__2)
        sum = add(sum,sub__2 + '0'*(len__int - pivot))
        return sum
print("Tich hai so tren la : \n",multiply(__integer__1,__integer__2))





