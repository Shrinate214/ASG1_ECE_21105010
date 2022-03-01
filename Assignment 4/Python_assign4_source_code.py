#program 1
count = 0                                                                       # variable defined to count total number of steps
def towerofhanoi(n, initial_rod, destination_rod, mid_rod):
    global count
    if n == 0:                                                                  #Base case
        return
    count += 1
    towerofhanoi(n-1, initial_rod, mid_rod, destination_rod)                    #Recursion call
    print("Move disk",n,"from rod",initial_rod,"to rod",destination_rod)
    towerofhanoi(n-1, mid_rod, destination_rod, initial_rod)

N =3                                                                            # 3 discs are given in the problem, so N(number of discs) is set at 3 
print("Let A be the initial rod where the discs are currently present")
print("Let B is the extra or mid rod")
print("And C be the final rod where the discs are supposed to reach")
print("Steps Required to solve the Tower of Hanoi problem for %d discs :" %(N))
towerofhanoi(N, 'A', 'C', 'B')                                                  
print("Number of steps will be: %d" % (count))
#program 2
i=j=0
def facto(n):                                                                   #function for calculating factorial
  if n==0:
   return 1                                                                     # 0!=1
  else:
   s=1                                                                          # variable s defined to calculate the factorial
   for i in range(1,n+1):                                                       
     s=s*i
   return s                                                                     #returns factorial of a number 
n= int(input("Enter number of rows to be printed in the pascal triangle problem:"))
if n>=0:
  print("The Pascal's Triangle using iteration is:")                            #ITERATION METHOD
  for i in range(n):                                                            #for number of iterations or rows to print        
    for j in range(1,n-i):                                                      # for spacing
        print(" ",end="")                                                       # spaces are printed
    for k in range(i+1):                                                        #using combination method
        print(facto(i)//(facto(k)*facto(i-k)), end=" ")                         #nCr = n!/((n-r)!*r!)
    print()                                                                     # for new line
else:
  print(" ERROR!! number of rows must be positive. Try again")     
print("The Pascal's Triangle using recusion is:")
def pascaltriangle(num):
    if num == 0:
        return [[0]]
    elif num == 1:                                                              #Base case
        return [[1]]
    else:
        result = pascaltriangle(num-1)                                          #Recursion calling 
        current_row = [1]                                                       #The first element of each row is 1
        previous_row = result[-1]                                               #Taking the last row from the data of all rows
        for i in range(len(previous_row)-1):                                    #Loop for adding the values of top 2 numbers for computing current number's value
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]                                                      #The last element of each row is 1
        result.append(current_row)                                              #Adding row to the data of all rows
    return result
for i in pascaltriangle(n):
    print((n-len(i))*" ",end="")                                                                        
    for j in i:
        if j != 0:
            print(j, end =" ")
    print()                                                                     # for spacing after a line to go into the next line        

#program 3
N1=int(input("Enter the first integer:"))                                                                #taking input of first integer
N2=int(input("Enter the second integer:"))                                                               #taking input of second integer
Remainder=Quotient=0
A=max(N1,N2)                                                                                             #A is the dividend
B=min(N1,N2)                                                                                             #B is the divisor
if (B!=0):
  Remainder=A%B
  Quotient=A//B
  print("Remainder is:", Remainder)
  print("Quotient is:",Quotient)
else:
  print("Division by 0 is not possible") 
  Remainder=A
  Quotient=0
print("Checking whether the function (divmod()) is callable or not:")                                    #Q3)a)
Z = callable(divmod)
if Z == True:
    print("It returns true which means it is callable")
else:
    print("it returns false which means it is not callable")
Result_of_division=(Remainder,Quotient)  
print("Checking whether all the values are zero or not:")                                                #Q3)b)
if all(x != 0 for x in Result_of_division):
    print("All values in result(quotient and remainder) are non-zero")
else:
    print("All values in result(quotient and remainder) are not non-zero(which means one of them is 0)") 
print("On Adding (4,5,6) to the result of division and filtering out values greater than 4:")            #Q3(c)
Y = Result_of_division + (4,5,6)
print ("The new list formed is:",Y)
output = sorted(list((x for x in Y if x>4)))
print("Values greater than 4 are:",output)   
print("Converting the output from list 1into a set datatype:")                                           #Q3(d)
SET1 = set(output)
print("The output of previous part in set datatype would be:", SET1)

print("Making the output set of previous part immutable:")                                               #Q3(e)
Set1_frozen = frozenset(SET1)
print("The immutable set would be:", Set1_frozen) 
print("Evaluating the maximum value from the set and finding out its hash value:")                       #Q3(f)
Set_max = max(Set1_frozen)
print("The maximum value from the set is:", Set_max)
print("The hash value of set on considering it to be an integer is:", hash(Set_max))
print("The hash value of set on considering it as a string is:", hash(str(Set_max)))    
#program 4
class Student:                                                                                                  #Creating class Student
    def __init__(self,name,rllno):                                                                              #defining function __init__
        self.name = name
        self.rllno = rllno
        print("Object has been Created")
    def __del__(self):                                                                                          # defining function __del__
        print("Object has been destroyed")
name = input("Enter name of student:")                                                                          #taking Input of name of student 
roll_no = int(input("Enter roll number/SID of student:"))                                                       # taking input of roll number of student
student1 = Student(name,roll_no)                                                                                #Creating object
print("The name of the student is %s and his/her/their roll number is %d" % (student1.name,student1.rllno))     #Printing the assigned values
del student1

#program 5
class Employee:                                                                                         #Creating class Employee
    def __init__(self,name,salary):                                                                     
        self.name = name
        self.salary = salary
    def print_data(self):                                                                              
        print("%s has a salary of %d rupees" % (self.name,self.salary))
employee1 = Employee("Mehak",40000)                                                                     #Creating instances for storing names
employee2 = Employee("Ashok",50000)                                                                     # and salaries of various employees
employee3 = Employee("Viren",60000)
print("The current database is as follows:")                                                            #Printing the initial values
for i in [employee1,employee2,employee3]:
    i.print_data()
print("(i) Salary of %s has been updated from %d to " % (employee1.name,employee1.salary), end = "")    #Updating salary of Mehak to 70000
employee1.salary = 70000
print(employee1.salary)
print("(ii) The record of %s has been deleted" % (employee3.name))
del employee3
print("The final database is:")                                                                         #Printing the final values
for i in [employee1,employee2]:
    i.print_data()

#program 6
def list_letters(word):                                                                  #Function defined to convert a word into a list of letters
    list_out = []
    for i in word:
        list_out.append(i)
    return list_out
def countZ(word):                                                                        #to count number of letters
  count2=0
  for i in range(0, len(word)):  
    if(word[i] != ' '):  
        count2 = count2 + 1;  
  return count2      
George_word = str(input("Enter George's word:")).lower().split()
Barbie_word = str(input("Enter Barbie's guessed word:")).lower().split()
if (len(George_word) == 1):
  if(len(Barbie_word) == 1):
   George_word=George_word[0]
   Barbie_word=Barbie_word[0]
   letters_in_George_word=list_letters(George_word)
   letters_in_Barbie_word=list_letters(Barbie_word)
   if (countZ(George_word)==countZ(Barbie_word)):                                                              #checking if  count of letters is not sames
     if (sorted(letters_in_George_word)!=sorted(letters_in_Barbie_word)):                                      #checking if ame letters are present in the words
       print("ERROR! Letters of both the words are not same. Friendship is fake.")
     elif (George_word == Barbie_word):
       print("ERROR! Same word spoken. Utter a different word.")
     else:
       statement_shopkeeper = str(input("Is the word meaningful?( Enter YES or NO):"))
       if (statement_shopkeeper == 'YES'):
         print("Congratulations!, you passed the test!!")
       elif (statement_shopkeeper == 'NO'):
         print("Word is not meaningful, friendship is fake!!")
       else:
         print("Invalid input, try again")
   else:
     print("Words are not the same.Friendship is fake!!")      
  else:
     print("Speak only 1 word.Try again.")
else:
  print("Test should be limited to one word. Try again")     
    
