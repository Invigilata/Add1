grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Создаем словарь для хранения средних баллов
average_grades = {}

# Итерируем по индексам студентов и их оценок
for i in range(len(students)):
    student_name = list(students)[i]
    student_grades = grades[i]

    # Рассчитываем средний балл каждого ученика
    avg_grade = sum(student_grades) / len(student_grades)

    # Добавляем в словарь имя ученика и его средний балл
    average_grades[student_name] = avg_grade

print(average_grades)
