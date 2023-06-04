
name= input("enter name of student:")
print("Enter marks of five subjects:")

print("Subject 1")
subject_1=float(input())
print("Subject 2")
subject_2=float(input())
print ("Subject 3")
subject_3=float(input())
print("Subject 4")
subject_4=float(input())
print("Subject 5")
subject_5=float(input())

total, average, percentage, grade = None, None, None, None

total=subject_1+ subject_2 +subject_3+ subject_4 + subject_5
average= total/ 5.0
percentage= (total/500.00)* 100

if average>= 90:
    grade = 'A'
elif average >=80 and average <90:
    grade = 'B'
elif average >=70 and average < 80:
    grade ='C'
elif average >=60 and average <70:
    grade= 'D'
else:
    grade ='E'

print("The total marks are:   \t", total, "/500.00")
print("The average marks are: \t", average)
print("Percentage is:          \t", percentage, "%")
print ("Grade is:      \t", grade)