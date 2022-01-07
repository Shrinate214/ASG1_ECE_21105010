#question 1
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
Average=(a+b+c)/3
print("the average is:",Average)

#question 2

Total_income= int(input("Enter the total income:"))
Standard_income=10000
Rate_of_tax=20
Dependent_deduction=3000
Number_of_dependents=int(input("enter the number of dependents:"))
Taxable_income=Total_income-Standard_income-(Dependent_deduction*Number_of_dependents)
Tax=(Taxable_income*Rate_of_tax)/100
print("Total tax:",Tax)

#question 3

SID=21105010
Name="Akshat Shrinate"
Gender='M'
Course_Name="ECE"
CGPA=9.7
Student_details=[SID, Name, Gender, Course_Name, CGPA]
print("The details are in the order[SID, Name, Gender, Course Name, CGPA]")
print("The Student details are:",Student_details)

#question 4

M1=int(input("enter the marks in student 1:"))
M2=int(input("enter the marks in student 2:"))
M3=int(input("enter the marks in student 3:"))
M4=int(input("enter the marks in student 4:"))
M5=int(input("enter the marks in student 5:"))
Marks=[M1,M2,M3,M4,M5]
print("the marks of 5 students are:",Marks)
Marks.sort()
print("Sorted marks of 5 students are:",Marks)

#Question 5
#a)

colour= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour.pop(3)
print("New list of colours:",colour)

#b)

colour=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour[3:5]=["Purple"]
print("New list of colours:",colour)

#assignment Over 










