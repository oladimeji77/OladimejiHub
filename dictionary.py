#you cant use index, rather use the keys or put the dictionary in a List
salary = {'deji':400, 'enitan':500, 'bolu':350}
salaries = {'ayo':[20,30,40], 'dele':[25,35,45]}
print(salary)
print(salary['enitan'])
salary['kenny'] = 800
print(salary['kenny'])
salary['enitan'] = salary['enitan'] + 100
print(salary)
salary['deji'] = 1000
print(salary)
print(salaries)
print(salaries['ayo'])
print(salaries['dele'][1])

student_attendance ={"deji": 90, 'tobi':55, 'nuru': 80}
#To print the keys ie names
for student in student_attendance:
    print(student)
#to print the grades ie values
for grade in student_attendance:
    print(student_attendance[grade])
#to grab key and values ie names and grades
for student in student_attendance:
    print(f"{student} : {student_attendance[student]}")
#Another way to print key and value using dictionary unpacking items(), tuple unpacking
for student, grades in student_attendance.items():
    print(student, " : " , grades)

#Test, calculate average score of students  values(), len and sum method
total_attendance_values = student_attendance.values()
average_score = sum(total_attendance_values) / len(student_attendance)
print(average_score)
