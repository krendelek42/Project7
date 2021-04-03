'''Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.'''

strok = int(input()) # количество строк
stolb = int(input()) # количество столбцов
t = []

for i in range(strok):
    a = []
    for j in range(stolb):
        n = int(input())
        a.append(n)
    t.append(a)
print('Исходная матрица:')
for i in t:
    for j in i:
        print(j, end=' ')
    print()
print()
print('Конечная матрица:')
for i in range(strok):
    for j in range(stolb):
        a = i + 1
        b = j + 1
        if a > strok-1:
            a = 0
        if b > stolb-1:
            b = 0
        print(t[i - 1][j] + t[a][j] + t[i][j - 1] + t[i][b], end=' ')
    print()