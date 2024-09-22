s:int = 0
n = int(input("Введите 8-разрядное число: "))
for i in range(8):
    s += n % 10
    n //= 10
print (f"Сумма всех цифр равна {s}")