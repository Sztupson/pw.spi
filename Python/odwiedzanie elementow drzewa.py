tree = [9,2,15,1,4,11,]

def get_left_child(index):
    return 2 * index + 1
def get_right_child(index):
    return 2 * index + 2
def get_parent(index):
    return (index - 1) // 2