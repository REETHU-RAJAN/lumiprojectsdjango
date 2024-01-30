"""1.Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
 between 1500 and 2700 (both included)."""
for i in range(1499,2701):
   if i % 7==0 and i % 5==0:
     print(i,end=" ")

"""output:
 1505 1540 1575 1610 1645 1680 1715 1750 1785 1820 1855 1890 1925 1960 1995 2030
 2065 2100 2135 2170 2205 2240 2275 2310 2345 2380 2415 2450 2485 2520 2555 2590 2625 2660 2695"""   

"""2.Write a Python program to convert temperatures to and from Celsius and Fahrenheit?"""

def cel_to_faren():
   celsius=float(input("enter the temp in celsius: "))
   farenheit=(celsius*9/5)+32
   return farenheit

def faren_to_cel():
    farenheit=float(input("enter the temp in farenheit:"))
    celsius=(farenheit-32)*5/9
    return celsius
print("farenheit: ",cel_to_faren())
print("celsius: ",faren_to_cel())
""" output:enter the temp in celsius: 37
farenheit:  98.6
enter the temp in farenheit:98.6
celsius:  37.0"""



"""3.Write a Python program to check the validity of passwords input by users.
{length of password should be between 6 to 16,atleast one small letter,
One capital letter,one digit,and one special character} """
password=input("Enter a password:")
low=0
up=0
dig=0
spec=0
if len(password)>=6 and len(password)<=16 :
   
   for i in password:
        if i.islower()==True:
           low=low+1
        elif i.isupper()==True :
           up=up+1
        elif i.isdigit()==True :
           dig=dig+1
        
        elif i in '!@#$%^&*_':
           spec=spec+1
if low>=1 and up>=1 and dig>=1 and spec>=1:            
    print("valied password")
else:
    print("invalid password")
    """ output:Enter a password:rrrERRR344#
valied password"""

""" 4.Write a Python program to check if a triangle is equilateral, isosceles or scalene. 
and show its area and perimeter."""
a=int(input("enter a side of triangle:"))
b=int(input("enter a side of triangle:"))
c=int(input("enter a side of triangle:"))
if a==b==c:
   print("Equilateral Triangle")
   
elif a==b or b==c or a==c:
   print("Isoceles Triangle")
   
else:
   print("Scalene Triangle")

base=int(input("enter base length"))
height=int(input("enter height "))
area=(1/2)*base*height
print("area of  triangle:",area)
perimeter=a+b+c
print("perimeter of trinagle:",perimeter)

"""output: enter a side of triangle:4
enter a side of triangle:5
enter a side of triangle:6
Scalene Triangle
enter base length6
enter height 6
area of  triangle: 18.0
perimeter of trinagle: 15
"""




""" 5.Ask the user if it is raining and convert their answer to lower case so it doesn’t
matter what case they type it in. If they answer “yes”, ask if it is windy. If they answer
 “yes” to this second question, display the answer “It is too windy for an umbrella”, 
 otherwise display the message “Take an umbrella”. If they did not answer yes to the first
   question, display the answer “Enjoy your day”.""" 
user=input("if it is raining: ")
lower=user.lower()
print(lower)
if lower=="yes":
    user=input("if it is windy:")
    user.lower()
    if user.lower()=="yes":
        print("it is too windy for an umbrella")
    else:
        print("take an umbrerlla")
else:
    print("enjoy your day")
"""output: if it is raining: yes
yes
if it is windy:yes
it is too windy for an umbrella

"""



""" 6.Display the following message:{1:square 2:Triangle entrer a number} . If the user
   enters 1, then it should ask them for the length of oneof its sides and display the area.
   If they select 2, it should ask for the base and height of the triangle and display the 
   area. If they type in anything else, it should give them a suitable error message. """
def square():
    length=int(input("enter the length of one side: "))
    area=length*length
    print("Area of Square: ",area)
def triangle():
    base=int(input(" enter the base of triangle: "))
    height=int(input(" enter the height of triangle: "))
    area=(1/2)*base*height
    print("Area of Triangle: ",area)

while True:
    choice=input("enter the choice: 1)square  2)Triangle 3)quit")
    if choice=="1":
        square()
    elif choice=="2":
        triangle()
    else:
        print("plz, enter a valid choice")
        break

"""output:enter the choice: 1)square  2)Triangle1
enter the length of one side: 5
Area of Square:  25
enter the choice: 1)square  2)Triangle2
 enter the base of triangle: 4
 enter the height of triangle: 5
Area of Triangle:  10.0
enter the choice: 1)square  2)Triangle3
plz, enter a valid choice"""      



""" 7.Write a Program to print duplicates from a list of integers"""
list=[1,4,5,4,4,3,3,7]
dupli=[]
unique=[]
for i in list:
    if i not in unique:
        unique.append(i)
    elif i not in dupli:
        dupli.append(i)
print("duplicates in list are: ",dupli)
"""output:duplicates in list are:  [4, 3]"""




""" 8.Ask the user’s age. If they are 18 or over, display the message “You can vote”, 
if they are aged 17, display the message “You can learn to drive”, if they are 16, 
display the message“You can buy a lottery ticket”,if they are under 16, display the 
message “You can go for treat”."""
age=int(input("Enter your age"))
if age>=18:
   print("you can vote")
elif age==17:
   print("you can learn to drive")
elif age==16:
   print("You can buy a lottery ticket")
else :
   print("You can go for treat")
"""output: Enter your age18
you can vote"""

""" 9.Ask how many people the user wants to invite to a party. If they enter a number below
 10, ask for the names and after each name display “[name] has been invited”. If they enter
   a number which is 10 or higher,display the message “Too many people”."""
No_Of_People_To_Invite=int(input("enter how many people user wants to invite: "))
if No_Of_People_To_Invite<10:
    for i in range(1,No_Of_People_To_Invite+1):
        name=input("enter the name: ")
        print(f"{name} has been invited")
elif No_Of_People_To_Invite>=10:
    print("too many people")
""" output:enter how many people user wants to invite: 5
enter the name: reethu
reethu has been invited
enter the name: gg
gg has been invited
enter the name: hh
hh has been invited
enter the name: thhh
thhh has been invited
enter the name: ghjh
ghjh has been invited"""    


""" 10.Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”,
if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter 
anything else, display “Error message”."""
num =int(input("enter a number (1,2,3)"))
if num==1:
    print("Thank you")

elif num==2:
    print("Well done")
elif num==3:
   print("Correct")
else:
   print("Error message")

   """output:enter a number (1,2,3)3
Correct"""





