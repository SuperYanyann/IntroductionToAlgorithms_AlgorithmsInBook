'''
 * Copyright 2018/9/27 Yan Wang.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * Author: dieqi317@gmail.com
 *
 '''
# the function is use to merge two sorted list: arr[begin:middle] and arr[middle+1:end]
# to one list which is sorted
def merge(arr,begin,middle,end):
    temp_arr_1 = arr[begin:middle+1]
    temp_arr_2 = arr[middle+1:end+1]
    len_1 = len(temp_arr_1) - 1
    len_2 = len(temp_arr_2) - 1

    # use the method in exercise 2.3-2 , put the remaining elements into the new list
    # by judging whether getting the end of the list
    # you can also use infinity as the end of the array
    vernier_1 = 0
    vernier_2 = 0
    i = begin
    while vernier_1 <= len_1 and vernier_2 <= len_2:
        if temp_arr_1[vernier_1] < temp_arr_2[vernier_2]:
            arr[i] = temp_arr_1[vernier_1]
            vernier_1 += 1
            i += 1
        else:
            arr[i] = temp_arr_2[vernier_2]
            vernier_2 += 1
            i += 1


    while (vernier_1 <= len_1):
            arr[i] = temp_arr_1[vernier_1]
            vernier_1 += 1
            i += 1
    while (vernier_2 <= len_2):
            arr[i] = temp_arr_2[vernier_2]
            vernier_2 += 1
            i += 1

def merge_sort(arr,begin,end):
    if begin < end:
        middle = (begin + end)/2
        merge_sort(arr,begin,middle)
        merge_sort(arr,middle+1,end)
        merge(arr,begin,middle,end)

# for testing
if __name__ == '__main__':
    test_arr = [10,1,5,27,100,32,6,15,101,23,55,578,66,9]
    len_arr = len(test_arr)
    merge_sort(test_arr,0,len_arr-1)
    print test_arr
