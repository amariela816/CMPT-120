
def printHello():
    print("Hello")
    
def printName(x):
    print(x)
    
def addition(x, y):
    #add x and y together and return them
    return(x+y)

def smaller(i, j):
    #if i is smaller than j, return i
    #if j is smaller than i, return j
    #if they're even, return 0
    if i<j:
        return(i)
    elif j<i:
        return(j)
    else:
        return(0)
def main():
    
    #call the printHello function here
    printHello()
    #call printName and give it the parameter of your name
    printName("Athiná")
    var1= 10
    var2= 20
    #What do we put in here to make it work?
    print(addition(10,20))
    
    num1 = int(input("Enter number 1"))
    num2 = int(input("Enter number 2"))
    #what go here?
    print(smaller(num1, num2))






main()


number1 = random.randint(10000, 19999)
number2 = random.randint(10000, 19999)
number3 = random.randint(10000, 19999)

grade1 = random.uniform(1.0, 4.0)
grade2 = random.uniform(1.0, 4.0)
grade3 = random.uniform(1.0, 4.0)

rank1 = random.choices(years)
rank2 = random.choices(years)
rank3 = random.choices(years)

# create three students and check if they get free lunch and if they qualify for honors
kid1 = student("Athiná", 19831, rank1, "Computer Science", grade1)
print(kid1.idNum, rank1, grade1, kid1.honors(), kid1.lotto(), winner)

kid2 = student("Catalina", number2, rank2, "Fashion Design", grade2)
print(number2, rank2, grade2, kid2.honors(), kid2.lotto(), winner)

kid3 = student("Emi", number3, rank3, "spanish education", grade3)
print(number3, rank3, grade3, kid3.honors(), kid3.lotto(), winner)



    kid2 = student("Catalina", number2, rank2, "Fashion Design", grade)
    print(number, rank, grade, kid2.honors(), kid2.lotto(), winner)

    kid3 = student("Emi", number, rank, "spanish education", grade)
    print(number, rank, grade, kid3.honors(), kid3.lotto(), winner)

gpa = random.randint(99, 401) / 100