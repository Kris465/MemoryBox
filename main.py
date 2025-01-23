def create_node(value):
    return {'value': value, 'left': None, 'right': None}

def insert(root, value):
    if root is None:
        return create_node(value)
    if value < root['value']:
        root['left'] = insert(root['left'], value)
    else:
        root['right'] = insert(root['right'], value)
    return root

def in_order_traversal(node, sorted_values):
    if node is not None:
        in_order_traversal(node['left'], sorted_values)
        sorted_values.append(node['value'])
        in_order_traversal(node['right'], sorted_values)


arr = [38, 27, 43, 3, 9, 82, 10]


root = None
for value in arr:
    root = insert(root, value)


sorted_arr = []
in_order_traversal(root, sorted_arr)
print("Отсортированный массив:", sorted_arr)
