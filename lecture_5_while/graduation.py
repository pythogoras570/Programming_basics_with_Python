
# input
student_name = input()
fails = 0
average = 0
student_class = 1
grade = 0
# logic

while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails >= 2:
            print(f'{student_name} has been excluded at {student_class} grade')
            break
        continue
    student_class += 1
    average += grade
    if student_class > 12:
        print(f'{student_name} graduated. Average grade: {average / 12:.2f}')
        break
