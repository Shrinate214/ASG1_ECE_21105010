#program 1
print("the solution of program 1 is:")
def freq(a,b, c):                                                               #function defined to find frequency
  for a in b:                                                                     
    if a in c:                                                                    
         c[a] += 1                                                              #if a is present in c frequency is updated
    else:
         c[a] = 1                                                               #if not present, frequency is set at 1 
  print(str(c)) 
frequency_char={}                                                               #for storing frequency for characters in 1 worded string
STRING=str(input("Enter a string :")).lower()                                   #to input a string and convert all characters in lower case                                                                     #for characters
if (STRING.find(" ")==-1):                                                      #condition to check if string is one worded or has multiple words 
 print("Count of all characters in the 1 word string is:") 
 print(frequency_char)                         
 freq(i,STRING,frequency_char)                                                  #for printing frequency for characters in 1 worded string             
list1=STRING.split()
word=""
print ("Count of all words in STRING is:")                                        
frequencywords={}                                                               #for storing frequency of words in string 
freq(word, list1, frequencywords)                                               #for printing frequency of words in string

#program 2
print("the solution of program 2 is:")
month=int(input("Enter a number for month between 1 and 12:"))                  #to input month  
date=int(input("Enter a number for date between 1 and 31 :"))                   #to input date
year=int(input("Enter an year between 1800 to 2025:"))                          #to input year 
print("Next date in format Date/Month/Year is:")                                
if((1<=month<=12) and (1<=date<=31)and (1800<=year<=2025)):                     #given condition    
  if(month in [1,3,5,7,8,10]):                                                  #31 days in months of January, March, May, July, August, October, December
    if(date in range(31)):                                                      #for dates from 1 to 30
      date=date+1                                                               #updating statement for date
      print(date,month,year)                                                    #printing date/month/year
    else:                                                                       #for date==31   
      month=month+1                                                             #updating statement for month 
      date=1                                                                    #date reset to 1  
      print(date,month,year)                                                    #printing date/month/year
  elif(month==12):                                                              #for month of december
    if date in range (31):                                                      #for dates from 1 to 30 
       date=date+1                                                              #updating statement for date
       print(date,month,year)                                                   #printing date/month/year
    else:                                                                       #for date==31 
      date=1                                                                    #date reset to 1
      month=1                                                                   #month reset to 1
      year=year+1                                                               #updating statement for year
      print(date,month,year)                                                    #printing date/month/year
  elif(month==2 and (year%4==0)):                                               #for month of february in a leap year
    if date in range(29):                                                       #for dates from 1 to 28
      date=date+1                                                               #updating statement for date
      print(date,month,year)                                                    #printing date/month/year
    elif (date==29):                                                            #for date==29
      month=month+1                                                             #updating statement for month
      date=1                                                                    #date reset to 1
      print(date,month,year)                                                    #printing date/month/year
    else:                                                                       #if dates entered are 30 or 31   
      print("Date or Month Out of Range. Try Again")
  elif (month==2 and (year%4!=0)):                                              #for month of february in a non leap year
     if date in range(28):                                                      #for dates from 1 to 27
       date=date+1                                                              #updating statement for date
       print(date,month,year)                                                   #printing date/month/year  
     elif (date==28):                                                           #if dates entered are 30 or 31 
      month=month+1                                                             #updating statement for month
      date=1                                                                    #date reset to 1
      print(date,month,year)                                                    #printing date/month/year
     else:                                                                      #if dates entered are29, 30 or 31
       print("Date or Month Out of Range. Try Again")  
  elif month in ([4,6,9,11]):                                                   #30 days in April,June, September, November
    if(date in range(30)):                                                      #for dates from 1 to 29
      date=date+1                                                               #updating statement for date
      print(date,month,year)                                                    #printing date/month/year
    elif (date==30):                                                            #for date==30
      month=month+1                                                             #updating statement for month
      date=1                                                                    #date reset to 1
      print(date,month,year)                                                    #printing date/month/year
    else:
      print("Date or Month Out of Range. Try Again")                            #if date entered is 31 
  else:
    print("Date or Month Out of Range. Try Again")
else:
  print("Date or Month Out of Range. Try Again")                                #if the month or year or month condition is not held by user entered data

#program3
print("the solution of program 3 is:")  
N=int(input("Enter number of elements in list:"))                               #to take input of number of terms in list
i=1                                         
LIST=[]
while(i<=N):                                                                    #loop run from 1 to N
  INPUT=int(input("Enter a number:"))                                           #to take input of a number 
  SQ= INPUT*INPUT                                                               #to store square of number that is given as input in INPUT  
  t=(INPUT,SQ)                                                                  #to create a tuple 
  LIST.append(t)                                                                #tuple added in list
  i+=1                                                                          #updating statement
print("The list created is :")                        
print(LIST)                                                                     #list is printed 

#program 4
print("the solution of program 4 is:")
Grade=int(input("Enter a grade between 4 and 10:"))                             #to take input of grade 
if(Grade>=4 and Grade<=10):                                                     #given condition
  if (Grade==10):                                                   
    print("Your Grade is 'A+' and Performance is Outstanding ")
  elif (Grade==9):
    print("Your Grade is 'A' and Performance is Excellent")
  elif (Grade==8):
    print("Your Grade is 'B+' and Performance is Very Good ")        
  elif (Grade==7):
    print("Your Grade is 'B' and Performance is Good")
  elif (Grade==6):
    print("Your Grade is 'C+' and Performance is Average") 
  elif (Grade==5):
    print("Your Grade is 'C' and Performance is Below Average") 
  else:
    print("Your Grade is 'D' and Performance is Poor")  
else:
 print("Grade out of range.Try again")

#program 5
print("the solution of program 5 is:") 
Input="ABCDEFGHIJK"
i=1                                                     #variable to run outermost loop for rows
j=0                                                     #variable to print alphabets and spaces
while(i<=6):
  for j in range(i):                                    #loop for spaces 
    print(" ",end="") 
  for j in range (len(Input)-(j*2)):                    #loop for printing characters from string 'Input'              
    print(Input[j],end="")                       
  print()                                               #used to change lines 
  i+=1                                                  #updating statement

#program 6
print("the solution of program 6 is:")  
name=""                                                 #global variable
SID=0                                                   #global variable
z_dict1=dict()                                          #directory created whose keys are SID’s and values are student’s name
while(1):                                               #infinite loop
 Ask_User=str(input("enter Y or N:"))                   
 if (Ask_User=='Y'):                                    #data gets entered in directory if user enters Y   
  name=str(input("enter name:"))                               
  SID=int(input("enter SID:"))
  z_dict1[str(SID)]=name                                   
 elif(Ask_User=='N'):                                                  
  break                                                 #loop breaks if N is entered  
 else:
  print("try again")
print("The Dictionary created is:",z_dict1) 
print("sorting using values:")                         
print(sorted(z_dict1.items(), key =
             lambda kv:(kv[1], kv[0])))                 #to print result of sorting using values 
print ("sorting using keys:")
for i in sorted (z_dict1) :
    print ((i, z_dict1[i]), end =" ")                   #to print result of sorting using keys
print()
D=int(input("enter SID to search:"))
if (str(D)) in z_dict1:
  print(z_dict1[str(D)])                                #to print name of student whose SID is searched for
else:
  print("Wrong SID. Try again") 


#program 7
                                                            #fibonacci terms are 0,1,1,2,3,5,8,11...
print("the solution of program 7 is:")  
a=0                                                         #first term
b=1                                                         #second term
c=int(input("enter the number of terms to be printed:"))    #to take input of number of terms to be printed 
print("the fibonacci series is as follows:")
Sum=(a+b)                                                   #variable to store sum of all terms of fibonacci series till 'c' number of terms
print(a,end=", ")                                              
print(b,end=", ")
for i in range(0,c-2):                                      #to run loop for printing fibonacci terms other than the first two
 d=a+b                                                      
 print(d,end=", ")
 a=b
 b=d
 Sum+=(d)                                                   #to update sum of terms on every iteration     
print()                                                      
print("average=",(Sum/c))

#program 8
print("the solution of program 8 is:")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
print("Set1:",Set1)
print("Set2:",Set2)
print("Set3:",Set3)
Set4=Set1^Set2                                                                                                  # (^) used to find (Union of sets - interesection part in sets)                                                                
print("Set of all elements that are in Set1 and Set2 but not both:",Set4)
Set5=Set1^Set2^Set3                                                                                             # (^) used to find (Union of sets - interesection part in sets)  
print("Set of all elements that are in only one of the three sets Set1,Set2 and Set3:",Set5)
Set6={1,2,3,4,5,6,7,8,9,10}
print("Set of all integers in the range 1 to 10 that are not in Set1:",Set6-Set1)                               # (-) operator used to find difference of sets 
print("Set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3:",Set6-(Set1|Set2|Set3))     # (|) operator used to create union of sets 
