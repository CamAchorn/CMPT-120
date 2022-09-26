def main():
  
  #set this to any double
  doubleValue = 2.5
  
  #set this to any int
  intValue = 4
  
  #print out addition, subtraction, multiplication, and division of these two values
  print (intValue * doubleValue)
  print(intValue + doubleValue)
  print(intValue - doubleValue)
  print(intValue / doubleValue)
  
  #populate this list
  myFriends = ["Courtney", "Mary", "Wandy", "Syd"]
  
  #print out your friends at index 2 and index 3
  print (myFriends[2])
  print (myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [0,1,2,3,4,5]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[1] + fiveNumbers[2])
  print(fiveNumbers[3] - fiveNumbers[5])
  print(fiveNumbers[4] / fiveNumbers[2])
  print(fiveNumbers[0] * fiveNumbers[5])

  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[1] = 10

  #print out the list
  print(fiveNumbers)
  
main()
