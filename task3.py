
# Задайте список из n чисел последовательности (1+1/𝑛)𝑛 выведите на экран их сумму.
# Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37} сумма 6,62


def sequence_and_summ(n,x={},sum=0):
    for i in range(1,n+1):
        x[i]=round((1 + (1/i))**i ,2)
    print(x)
    for i in x.values():
        sum+=i
    print(sum)

pos = sequence_and_summ(n:=int(input("Введите число: ")))
