def bubble_sort(my_list:list[int])->list[int]:
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp

    return my_list

def selection_sort(my_list:list[int])->list[int]:
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


def insertion_sort(my_list:list[int])->list[int]:
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


#merge sort

def merge(array1:list[int], array2:list[int])->list[int]:
    combined:list[int]=[]
    i=0
    j=0
    while i<len(array1) and j<len(array2):
        if array1[i]<array2[j]:
            combined.append(array1[i])
        else:
            combined.append(array2[j])
            j+=1

        while i < len(array1):
            combined.append(array1[i])

        while j<len(array2):
            combined.append(array2[j])
            j+=1

        return combined

print(merge(a,b))

def merge_sort(my_list:list[int])->list[int]:
    if len(my_list)==1:
        return my_list
    
    mid_index = int(len(my_list)/2)
    left:list[int]= merge_sort(my_list[:mid_index])
    right:list[int]=merge_sort(my_list[mid_index:])

    return merge(left, right)