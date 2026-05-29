#atm machine

class Atm:

  #constructor(special func superpower=)
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()

  def menu(self):
   user_input=input("""
           hi how can I help you?
          1. press 1 to create pin
          2. press 2 to change pin
          3. press 3 to check balance 
          4. press 4 to withdraw
          5. anything else to exit
                    :)
          
          """)
   
   if user_input=='1':
     #create pin
     self.create_pin()

   elif user_input=='2':
     #create pin
     self.change_pin()
   elif user_input=='3':
     #check balance
     self.check_balance()
   elif user_input=='4':
     #withdraw
     self.withdraw()
   else:
     exit()

  def create_pin(self):
    user_pin=input('enter pin : ')
    self.pin=user_pin

    user_balance=int(input ('enter balance : '))
    self.balance = user_balance

    print('pin created sucessfully  :)')
    self.menu()

  def change_pin(self):
    old_pin = input('enter old pin : ')

    if old_pin== self.pin:
      new_pin = input('enter new pin : ')
      self.pin = new_pin
      print('pin change sucessfull')
     
    else:
      print('invalid pin go to my boss')
    self.menu()
  
  def check_balance(self):

    user_pin = input ('enter your pin : ')
    if user_pin== self.pin:
      print('uour balance is ', self.balance)

    else:
      print('who the f are u')
    self.menu
  
  def withdraw(self):

    user_pin = input(' enter your pin : ')
    if user_pin== self.pin:
      print('your balance is : ', self.balance)

      amt = int(input('enter amt : '))
      if  amt <= self.balance:
        self.balance=self.balance - amt
        print('withraw sucessfull , current balance = ',self.balance)
       
      else:
        print('bhikari sale ')
     

    else:
      print('sale chor')
    
    self.menu()
  
  
   
  
object = Atm()
print(type(object))  

