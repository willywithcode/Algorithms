# The main merge sort function
def Merge_Sort(arr,left, right):
    # The base case: return if the sub-array has only one element
    if (left >= right):
        return
    # Calculate the middle index
    mid = left + (right-left)//2
    # Recursively sort the first half of the sub-array
    Merge_Sort(arr,left,mid)
    # Recursively sort the second half of the sub-array
    Merge_Sort(arr,mid+1,right)
    # Merge the two sorted sub-arrays
    Merge_SubArr(arr,left,mid,right,arr[left:mid+1],arr[mid+1:right+1])

# The helper function to merge the two sub-arrays
def Merge_SubArr(arr,left,mid,right,FirstArr,SendArr):
    # Initialize pointers for the two sub-arrays
    a = b = 0
    # Merge the two sub-arrays into the original array
    for i in range(left,right+1):
        # If the current element of the second sub-array is smaller
        # or the first sub-array is exhausted, add the current element of the second sub-array
        if b < len(SendArr) and (a >= len(FirstArr) or SendArr[b] < FirstArr[a]):
            arr[i] = SendArr[b]
            b +=1
        # Otherwise, add the current element of the first sub-array
        else:
            arr[i] = FirstArr[a]
            a += 1

# Example usage
arr = [1,4,2,6,5,10]
Merge_Sort(arr,0,len(arr)-1)
print(arr)
