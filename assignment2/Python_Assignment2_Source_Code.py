#program 1
string='Python is a case sensitive language'
print("the string is:",string)
print("length of string is:",len(string))
print("reversed string is:",string[: :-1])
sliced_string=string[10:27]
print("the substring found on slicing is:",sliced_string)
replaced_string=string.replace('a case sensitive','object oriented')
print("The string found on replacing substring is:",replaced_string)
index_position= string.find('a')
print("the index of substring 'a' is:", index_position)
new_string=string.replace(" ", "")
print("string found on removing all whitespaces is:",new_string)

#program 2

Name='Akshat Shrinate'
SID=21105010
Department_name='ECE'
CGPA=9.9
print("Hey, %s Here!\n"
      "My SID is %d\n"
       "I am from %s Department and My CGPA is %f" % (Name,SID,Department_name,CGPA))


#program 3

#     128 64 32 16 8 4 2 1
#a=   0   0   1  1 1 0 0 0 
#b=   0   0   0  0 1 0 1 0  
#a&b= 0   0   0  0 1 0 0 0 
#a|b= 0   0   1  1 1 0 1 0
#a^b= 0   0   1  1 0 0 1 0
#a<<2 1   1   1  0 0 0 0 0
#a>>2 0   0   0  0 1 1 1 0
#b<<2 0   0   1  0 1 0 0 0
#b>>4 0   0   0  0 0 0 0 0

a=56
b=10
print("Using & (bitwise AND) operator:", (a&b))
print("Using |(bitwise OR) operator:", (a|b))
print("Using ^ (bitwise XOR) operator:",(a^b))
print("using left side shift operator(<<) for a by 2bits:",(a<<2))
print("using left side shift operator(<<) for b by 2bits:",(b<<2)) 
print("using right side shift operator(>>) for a by 2bits:",(a>>2)) 
print("using right side shift operator(>>) for b by 4bits:",(b>>4))


#program 4

A=int(input("enter the first number:"))
B=int(input("enter the second number:"))
C=int(input("enter the first number:"))
if (A>B and A>C):
  print("Greatest number is:",A)
elif (B>A and B>C):
  print("Gretest number is:",B)
else:
  print("Greatest number is:",C)

#program 5


String=str(input("enter the string:"))
Word_to_find='name'
if (Word_to_find in String):
  print(" 'name' is Present")

else:
  print(" 'name' is Not Present ")

# proram 6

Length1=float(input("enter the length of first side:"))
Length1=int(Length1)
Length2=float(input("enter the length of second side:"))
Length2=int(Length2)
Length3=float(input("enter the length of third side:")) 
Length3=int(Length3)
if (Length1> (Length2+Length3)):
  print("No, triangle is not possible")
elif (Length2>(Length1+Length3)):
  print("No, triangle is not possible")
elif (Length3> (Length2+Length1)):
  print("No, Triangle is not possible")
else :
  print("Triangle is possible") 
  
  












