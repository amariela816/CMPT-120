def main():
  
  #set this to any double
  doubleValue= 4.5
  #set this to any int
  intValue = 9

  #print out addition, subtraction, multiplication, and division of these two values
  print("Addition:", doubleValue + intValue)
  print("Subtraction:", doubleValue - intValue)
  print("Multiplication:", doubleValue * intValue)
  print("Division:", doubleValue / intValue)
  
  
  #populate this list
  myFriends = ["Emi","Erin","Ellie","Bella"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])

  #populate this list with five numbers
  fiveNumbers = [3,5,6,4,24]
  
  #do each of the four equations with different numbers each time.
  print("Addition:", fiveNumbers[0] + fiveNumbers[1])
  print("Subtraction:", fiveNumbers[3] - fiveNumbers[2])
  print("Multiplication:", fiveNumbers[2] * fiveNumbers[4])
  print("Division:", fiveNumbers[3] / fiveNumbers[4])
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[1] = 6
  fiveNumbers[3] = 7

  #print out the list
  print( fiveNumbers)


main()
