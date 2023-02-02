# This code implements multiplication of two integers
# entered by the user.

# Take user input for the first integer
print("Nhap so hang thu nhat:")
__integer__1 = str(input())

# Take user input for the second integer
print("Nhap so hang thu hai:")
__integer__2 = str(input())

# Function to add two integers
def add(__number__1,__number__2):
    # Find the length of the larger integer
    max_len = max(len(__number__1),len(__number__2))
    # Fill the smaller integer with leading zeros to match the length of the larger integer
    __number__1 = __number__1.zfill(max_len)
    __number__2 = __number__2.zfill(max_len)
    # Initialize the sum string and the carry variable
    sum = ""
    temp = 0
    # Loop through the digits of both integers starting from the rightmost digit
    count = max_len -1
    while count != -1:
        # Add the current digits and the carry
        sum1 = int(__number__1[count] ) + int(__number__2[count]) + temp
        # Update the carry
        temp = sum1 // 10
        # Append the rightmost digit of the sum to the sum string
        sum = str(sum1)[-1] + sum
        count -= 1
    # If there is a carry, append it to the sum string
    if temp == 1:
        return str(temp) + sum
    # Return the sum string
    return sum


# Function to multiply a single-digit integer with another integer
def mini__multiply(__number__1,__number__2):
    # Initialize the carry variable
    temp = 0
    # Initialize the product string
    multi = ""
    # Loop through the digits of the second integer starting from the rightmost digit
    count = len(__number__1) -1
    while count != -1: 
        # Multiply the current digit with the single-digit integer and add the carry
        multi__temp = int(__number__1[count]) * int(__number__2) + temp
        # Update the product string with the rightmost digit of the product
        multi = str(multi__temp)[-1] + multi
        # Update the carry
        temp = multi__temp // 10
        count -= 1
    # If there is a carry, append it to the product string
    if temp != 0: 
        return str(temp) + multi
    # Return the product string
    return multi

# Function to multiply two integers
def multiply(__number__1,__number__2):
    # Initialize the sum string
    sum = ""
    # Loop through the digits of the second integer starting from the rightmost digit
    for n in range(len(__number__2)):
        # Add the product of the current digit of the second integer with the first integer
        # to the sum string after shifting it to the right by n places
        sum = add(mini__multiply(__number__1,__number__2[-n-1])+'0'*n,sum)
    # Return the final product
    return sum

# Print the product of tow integers

print("Tich hai so tren la : \n",multiply(__integer__1,__integer__2))
