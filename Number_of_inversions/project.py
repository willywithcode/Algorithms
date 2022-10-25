sum_count = 0
def count_and_sort(list):
    if len(list) <= 1:
        return list
    else:
        len_list = len(list)
        pivot = len_list//2  
        return count_split_and_sort(count_and_sort(list[:pivot]),count_and_sort(list[pivot:]))

def count_split_and_sort(first_list,second_list):
    global sum_count
    sorted = []
    i = 0
    j = 0
    len_first = len(first_list)
    len_second = len(second_list)
    while i < len_first and j < len_second:
        if first_list[i] > second_list[j]:
            sorted.append(second_list[j])
            sum_count += len_first - i
            j += 1
        else:
            sorted.append(first_list[i])
            i += 1
    while i < len_first:
        sorted.append(first_list[i])
        i += 1
    
    while j < len_second:
        sorted.append(second_list[j])
        j += 1
    return sorted

graph = []
# with open('Integer__Array.txt') as f:
#     data = f.readlines()
#     for line in data:
#         graph.append(line)
arr = [1,2,3,4,5,6,7,8,9,0]
print(count_and_sort(arr))
count_and_sort(arr)
print(sum_count)
