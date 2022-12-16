#  Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, 
#  другие методы из библиотеки random - можно).
          

list = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(list) // 2):
        current = list[i]
        list[i] = list[-i-1]
        list[-i - 1] = current
print(list)
