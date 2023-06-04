# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def Chek(number):
    for i in range(2,number):
        if number%i<=0:   
         print("\033[31m\0")
         return(f"Output: No") 
        print("\033[32m\0") 
    return(f"Output: Yes") 
print("\033[33m\0") 
number=int(input("Input: "))
res=Chek(number)
print(res)   
