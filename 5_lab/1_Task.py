data = 'Иванов Иван, 20, Математика; Петров Петр, 21, Физика; Сидоров Сидор, 22, Химия'
students = data.split(';')
for student in students:
    name, age, fac = student.split(',')
    print(f'''Имя: {name}
Возраст: {age}
Факультет: {fac}''')