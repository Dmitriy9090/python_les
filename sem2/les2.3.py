## Задача на нахождение сколько дней длилась самая длинная оттепель
date = [int(i) for i in input('введите числа через пробел: ').split()]
n = len(date)
max_count = 0
count = 0
for i in date:
    if i > 0:
        count += 1
    else:
        if max_count < count:
            max_count = count
        count = 0
print(max_count)
