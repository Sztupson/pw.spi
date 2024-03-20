

array = [9,6,4,2,1,5,3,8,7,0,-1,44,13,89,1020]

# class SortingMethods:
#     def __init__(self, array):
#         self.array = array

    # @staticmethod
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array  

# array = SortingMethods
# array = array.bubble_sort
bubble_sort(array)
print(array)