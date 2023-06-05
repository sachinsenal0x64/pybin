import random
import os


def bin_get():
  
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

  visa = '4'
  master = str(random.randint(51,55))
  discover = '6011' 

  
  gen = True
  while gen:
      ask = input('Which network bin you want to get such as "visa" or "master" or "discover" ?\n')
      quantity = int(input("How many bins do you want to generate ?\n"))   
      length = int(input("What is the length of the bin you want (default = 6)?\n"))
    
    
      if ask.lower() == "visa" or ask.startswith(visa)  :
          for num in range (0, quantity):
              prefix = visa     
              for num in range (1,length ):
                  num = str(random.choice(numbers))
                  prefix += num 
              print(prefix)

      elif ask.lower() == "master" or ask.startswith(tuple(master)):
          for num in range (0, quantity):
              prefix = master
              for num in range (2, length):
                  num = str(random.choice(numbers))
                  prefix += num
              print(prefix)
      
      elif ask.lower() == "discover" or ask.startswith(tuple(discover)):
            for num in range (0, quantity):
              prefix = discover
              for num in range (4, length):
                  num = str(random.choice(numbers))
                  prefix += num
              print(prefix)
        
      
      
      c = input("Do you want to get again 'yes' or 'no'?\n")
      if c == "yes":
        gen = True
        os.system('cls' if os.name=='nt' else 'clear')
      else:
        gen = False

  
  
  return ask , quantity, length,c



if __name__ == "__main__":
  
  op_1 = input("Need More ? then Press 1\n")
  
  if op_1 == "1":
    ask,quantity,length,c =  bin_get()
      
  else:
    print("Thank you for using our bin generator")
    
    os.system('cls' if os.name=='nt' else 'clear')
    exit()





























