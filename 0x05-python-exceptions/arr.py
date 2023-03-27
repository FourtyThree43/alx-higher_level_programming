def replace_char(arr, old_char, new_char):
    for i in range(len(arr)):
        arr[i] = arr[i].replace(old_char, new_char)

arr = "Imagine how good your life would be if you had a 26yo nursing assintant by your side, now replace S with N"
arr = arr.replace('S', 'N')
print(arr)
