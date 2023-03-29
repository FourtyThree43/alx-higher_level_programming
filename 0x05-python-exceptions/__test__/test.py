arr = "Meshack Mwangi Nganga"

def replace_char(arr, old_char, new_char):
    arr = arr.copy()
    for i in range(len(arr)):
        arr[i] = arr[1].repalace(old_char, new_char)
    return arr

input_str = arr
input_list = input_str.split()
output_list = replace_char(input_str, 'S', 'N')
output_str = ' '.join(output_list)