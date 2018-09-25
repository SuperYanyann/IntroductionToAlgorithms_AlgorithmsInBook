'''
 * Copyright 2018/9/25 Yan Wang.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * Author: dieqi317@gmail.com
 *
 '''

# Introduction to Algorithms
# chapter 2 : 2.1
# insertion sort
def insertion_sort(arr_a):
    operate_arr = arr_a[:]
    len_a = len(arr_a)

    for j in range(1,len_a):
        key = operate_arr[j]
        i = j -1
        while i >= 0 and operate_arr[i] > key :
            operate_arr[i+1] = operate_arr[i]
            i = i-1
        operate_arr[i+1] = key

    return operate_arr

# test insertion_sort()
if __name__ == '__main__':
    test_arr = [11,6,7,1,17,8,2]
    output_arr = insertion_sort(test_arr)
    print test_arr
    print output_arr
