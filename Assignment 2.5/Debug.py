
def main():

    #that's not right... how can we make sure it also includes equals 5?
    temp = 5
    if temp >= 5:
        print("temp is greater than or equal to 5")
        
    
    #enter your name here
    name = "Athina"
    ##in this if/elif/else, add 4 mispellings of your name for if/elif comparisons, and then have your last elif be elif name = "your properly spelled name"
    if name == "Athena":
        print("That's not right!")
    elif name == "Atheno ":
        print("That's not right!")
    elif name == "Athiena":
        print("That's not right!")
    else:
        print("That's not right!")
    #etc etc, the else can be whatever you want
    
    
    #we're gonna check if a user input number is even
    #pick any number
    even = int(input("Enter a number to find out if its even or odd"))

    #what do we replace the question marks with?
    if even % 2 == 0:
        #what would be appropriate in these print statements?
        print(even, "is even")
    else:
        print(even, "is odd")
  
  
    #i'm trying to do math with the numbers 2 and 4, but it's getting 3 and 5... why?
    numbers = [1,2,3,4,5]
    print(numbers[1])
    print(numbers[3])
    print(numbers[3] / numbers[1])
    print(numbers[3] * numbers[1])
    
    #again, why is it getting 7 and 20, I wanted 3 and 29!
    numbers2 = [465,3,30,7,29,20,82,13,5]
    print(numbers2[1])
    print(numbers2[4])
    
    #Here's a fun one: This is a list of everyone's name. Find where yours is and print the index of your name
    students = students = ["Tobi","Brad","Tiff","Oscar","Tommy","Kyra","Matt C","Morgan","Haley","Matt F","Sydney","Pedro","Nathan","Bryce","Chris","Iram","Pat","Maddie","Daniel","Tomas","Gabriella","Ben","Lucian","Dean","Jack","Natalie","Athina"]
    print(students[26])
main()
    
    

    
