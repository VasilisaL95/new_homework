grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))
res1 = sum(grades[0]) / len(grades[0])
res2 = sum(grades[1]) / len(grades[1])
res3 = sum(grades[2]) / len(grades[2])
res4 = sum(grades[3]) / len(grades[3])
res5 = sum(grades[4]) / len(grades[4])

grade_point_average_list = [res1, res2, res3, res4, res5]

grade_point_average = dict(zip(students_list,grade_point_average_list))
print(grade_point_average)
