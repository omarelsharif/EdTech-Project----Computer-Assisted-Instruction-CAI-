'''This project validates input and output,
varies congratulatory statements to reduce student fatigue,
uses a menu driven process, varies difficulty, and provides a final score.'''




def randomnums(difficulty):

  
  import random

  if difficulty == 1: 
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
  else: 
  
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

  return [num1,num2]


def positiveresponse():
  import random 
  positiveresponses =  ["Very good!",  "Excellent", "Nice work!","Keep up the good work!"]

  x = random.randint(0,3)
 
  return positiveresponses[x] 


def negativeresponse():
  import random
  negativeresponses =  ["No. Please try again.", "Wrong Try once more.",  "Don't give up!", "No. Keep trying."]
  x = random.randint(0,3)
  return negativeresponses[x] 
  

def menu(): 
  print("1 = addition")
  print("2 = subtraction")
  print("3 = multiplication")
  print("4 = division")
  print ("5 = random operation")
  studychoice = int(input("Enter the operation (1 to 5): "))
  
  
  import random
  if studychoice ==5:
    studychoice = random.randint(1,4)
  return (studychoice)


def difficultyselection(): 
  difficulty = int(input("Enter difficulty level (1 or 2): "))
  return difficulty



def addition(difficulty): 
  nums = randomnums(difficulty)
  print("How much is "+ str(nums[0])+ " + " + str(nums[1]) + "? ") 
  useranswer = int(input("Enter your answer (-1 to exit): "))

  
  answer  = nums[0] + nums[1
                           ]
  if useranswer == -1:

    return("stop") 
  elif useranswer != answer:
   

    return False 
  else:
    
    return True

  

def subtraction(difficulty): 
  nums = randomnums(difficulty)
  if nums[0] >= nums[1]:
    print("How much is "+ str(nums[0])+ " - " + str(nums[1]) + "? ") 
    useranswer = int(input("Enter your answer (-1 to exit): "))

    answer  = nums[0] - nums[1]
  elif nums[1] >= nums[0]: 
    print("How much is "+ str(nums[1])+ " - " + str(nums[0]) + "? ")
    useranswer = int(input("Enter your answer (-1 to exit): "))
    
    answer  = nums[1] - nums[0]

  if useranswer == -1:

    return("stop")
  
  elif useranswer != answer:
    return False 
  else: 
    return True   

def multiplication(difficulty): 
  nums = randomnums(difficulty)
  print("How much is "+ str(nums[0])+ " * " + str(nums[1]) + "? ") 
  useranswer = int(input("Enter your answer (-1 to exit): "))

  answer  = nums[0] * nums[1]
  if useranswer == -1:

    return("stop") 

  
  elif useranswer != answer:
    return False 
  else: 
    return True 

def division(difficulty): 
  nums = randomnums(difficulty)
  if nums[1] == 0:
    nums[1] = 1
  
  print("How much is "+ str(nums[0])+ " // " + str(nums[1]) + "? ") 
  useranswer = int(input("Enter your answer (-1 to exit): "))

  answer  = nums[0] // nums[1]

  if useranswer == -1:

    return("stop") 

  
  elif useranswer != answer:
    return False 
  else: 
    return True



def stop(corrects, wrongs):
  print("Number of correct answers: ", corrects)
  print("Number of wrong answers: ", wrongs)
  print("Thanks for playing!")


def main(difficultyy): 
  difficulty = difficultyy 

  #studychoice = menu()
  studychoice =  0
  wrongs = 0 
  corrects  = 0
  answer = -2
  
  while answer!= "stop":
    #print("Answer: ", answer)
    studychoice = menu() 

    
    print(" ")
    if studychoice == 1:

      answer = addition(difficulty) 
      
      if answer == False:
        wrongs +=1
        print(negativeresponse())
        print(" ")
      elif answer == True: 
        print(positiveresponse())
        print(" ")
        corrects +=1
  
    if studychoice == 2:
      answer = subtraction(difficulty)
      if answer == False:
        print(negativeresponse())
        print(" ")
        wrongs += 1
      elif answer == True: 
        print(positiveresponse())
        print(" ")
        corrects +=1
      
    if studychoice == 3:
      
      answer = multiplication(difficulty) 
      if answer == False:

          print(negativeresponse())
          print(" ")

          wrongs += 1
      elif answer == True: 

          print(positiveresponse())
          print(" ")

          corrects += 1
      
    if studychoice == 4:

      answer = division(difficulty)

      if answer == False:

          print(negativeresponse())
          print(" ")

          wrongs += 1
      elif answer == True: 

          print(positiveresponse())
          print(" ")
          corrects += 1

  if answer == "stop": 
    stop(corrects, wrongs)
    #return studychoice
    

difficultyy = difficultyselection()



main(difficultyy)







