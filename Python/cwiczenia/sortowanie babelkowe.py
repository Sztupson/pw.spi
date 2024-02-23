# Napisz pseudokod alorytmu, a nastepnie przekształć go w kod Pythona, który sortuje lisę liczb metodą bąbelkową:
# - wejscie: tablica (array)
# - wyjscie: tablica

# # # # tab = [5,4,3,1,2]


# # # # def BubbleSort(tab):
# # # #     for i in range(len(tab)):
# # # #         if tab[i]>tab[i+1]:
# # # #             pass 
# # # #         else:
# # # #             tab[i+1], tab[i] = tab[i] , tab[i+1]
# # # #     return(tab)


# # # # BubbleSort(tab)
# # # # print(tab)

array = [5,6,8,6,4,8,2,1]

@staticmethod
def sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)
sort(array)
