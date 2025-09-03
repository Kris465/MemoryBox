def create_list():
    array = []
    for i in range(1,6):
        value = int(input("Input you number: "))
        array.append(value)
    return array

def find_max(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max

res = create_list()
print(res)
max = find_max(res)
print(f"Maximum value is {max}")
