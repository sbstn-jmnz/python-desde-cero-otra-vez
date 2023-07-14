# Escribir un programa que imprima una lista de los estudiantes con promedio superior a 6

averages = {
  "Seba": 5,
  "Gaby": 6.5,
  "Fran": 7,
  "Jose": 6.4,
  "Coni": 6.2,
  "Gonza": 4.8
}

approved_students = []

for student in averages.keys(): # => ["Seba","Gaby","Fran",...]
  if averages[student] > 6:
    approved_students.append(student)

print(approved_students)