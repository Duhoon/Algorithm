def insertion_sort(arr) :
    for i in range(1, len(arr)) :
        current_num = arr[i]
        current_idx = i
        for j in range(i-1, -1, -1) :
            compare_num = arr[j]
            if compare_num > current_num : 
                arr[current_idx] = compare_num
                current_idx -= 1
                if j == 0: 
                    arr[j] = current_num
            else : 
                arr[current_idx] = current_num
                break


temp = [5, 7, 1, 3, 6]
insertion_sort(temp)
print(temp)

temp = [8, 8, 8, 4, 1, 9, 9, 9, 9]
insertion_sort(temp)
print(temp)