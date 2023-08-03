# #  Написать на одном из языков программирования программу вычисления суммы 
# #  элементов квадратной матрицы четвертого порядка, лежащих ниже побочной диагонали

# Определить размер матрицы
string = int(4)
column = int(4)

# Задали матрицу
matrix = []  
print("Матрица 4х4:")  
from random import randint

# Ввод значений матрицы
for i in range(string):
   a =[]  
   for j in range(column):  
      a.append(randint(1,9))  
   matrix.append(a)  

# Вывод матрицы
for i in range(string):  
   for j in range(column):  
      print(matrix[i][j], end = " ")  
   print()

#Вывод суммы
import math
sum1=0
for i in range(string):
   for j in range(column):
      if i+j > 3:
       sum1 += matrix[i][j]
print ("Сумма элементов ниже побочной диагонали =",sum1) 


