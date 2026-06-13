d = dict()
n = int(input("Enter entries: ")) 

for i in range(n):
    name = input("Enter name : ")
    marks = int(input("Enter marks out of 100 : "))
    d[name] = marks

print(d)

# Calculating average marks :

total = sum(d.values())
avg = float(total/n)
print("Average marks is : ", avg)

# Calculating max and min marks :

max_marks = max(d.values())
min_marks = min(d.values())
print(f"Maximum marks: {max_marks}, Minimum marks: {min_marks}")

# Students scoring above average :

print("Students scoring above average : ")
for name, marks in d.items():
    if marks > avg:
        print(name)

# Assigning grades : 
grade_A = 90
grade_B = 80
grade_C = 70
grade_D = 60
for name, marks in d.items():
    if marks >= grade_A:
        print("Students with grade A : ", name)
    elif marks in range(grade_B, grade_A):
        print("Students with grade B: ", name)
    elif marks in range(grade_C, grade_B):
        print("Students with grade C : ", name)
    elif marks in range(grade_D, grade_C):
        print("Students with grade D : ", name)
