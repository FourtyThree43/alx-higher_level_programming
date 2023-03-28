arr = "Imagine how good your life would be if you had a 26yo nursing \
assintant by your side, now replace S with N"
arr1 = arr.replace('S', 'N')
print(arr1)


def replace_char(arr, old_char, new_char):
    arr = arr.copy()
    for i in range(len(arr)):
        arr[i] = arr[i].replace(old_char, new_char)
    return arr


input_str = arr
input_list = input_str.split()
output_list = replace_char(input_list, 'S', 'N')
output_str = ' '.join(output_list)

print(output_str)
