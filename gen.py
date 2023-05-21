import random
import os


def bin_get():
  
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

  visa = '4' or [] 

  master = str(random.randint(51,55))

  
  discover = '6011' or []

  
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



def bin_gen():
  
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

  visa = '4' or [] 

  master_in = '51', '52', '53', '54', '55' or []

  discover = '6011' or []
  
  gen = True
  while gen:
      ask = input('Which bin do you want to generate ?\n')
      quantity = int(input("How many bins do you want to generate ?\n"))   
      length = int(input("What is the length of the bin you want (Bin length = 6 ,PAYMENT_GATE_ASK length = 16  )?\n"))
    
      if ask.startswith(visa):
        visa = ask
    
      elif ask.startswith(tuple(master_in)):
        master_in = ask

      elif ask.startswith(tuple(discover)):
        discover = ask
        
    
      if ask == visa:
          for num in range (0, quantity):
              prefix = visa   
              for num in range (1,length ):
                  num = str(random.choice(numbers))
                  prefix += num 
              print(prefix)

      elif ask == master_in:
        for num in range (0, quantity):
            prefix = master_in
            for num in range (2, length):
                num = str(random.choice(numbers))
                prefix += num
            print(prefix)
      
      elif ask == discover:
        for num in range (0, quantity):
            prefix = discover
            for num in range (4, length):
                num = str(random.choice(numbers))
                prefix += num
            print(prefix)
          
      
      c = input("Do you want to gen again 'yes' or 'no'?\n")
      if c == "yes":
        gen = True
        os.system('cls' if os.name=='nt' else 'clear')
      else:
        gen = False

  
  
  return ask , quantity, length,c


if __name__ == "__main__":
  
  op_1 = input("Do you want to get a bin ? then Press 1\n")
  
  if op_1 == "1":
    ask,quantity,length,c =  bin_get()
    
  op_2 = input("Do you want to generate a bin ? then press 2\n")
  
  if op_2 == "2":
    ask,quantity,length,c =  bin_gen()
      
  else:
    print("Thank you for using our bin generator")
    
    os.system('cls' if os.name=='nt' else 'clear')
    exit()





























