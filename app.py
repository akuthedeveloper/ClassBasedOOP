# This is an online plat for peer to peer money transfer across different platform using public API
Class m-bongo-cash():
    def deposit_to_m-bongocash()
        pass
# class based Object oriented structure
Class m-bongo-cash():
    def_init_(self):
        self.initial_amount=0
        # function to deposit money to m-bongo-cash using any mobile company
    def deposit_to_mbongocash(self, deposit):
        if amount(deposit)== int and deposit!=""
        if deposit >=0
        self.balance += deposit
        return self.balance
    else:
        return 'Invalid Amount'
    else:
        raise ValueError()
        # withdraw money from the m-bongo platform
        def withdraw(self,amount):
    if type(amount) == int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:
          if (self.balance -amount) > 1000:
            self.balance-=amount
            return self.balance
          else:
            return 'Insufficient funds in Account'
        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid Amount'
    else:
      raise ValueError()
# The user is suppossed to create a savings account
class SavingsAccount(m-bongo-cash):
  def __init__(self):
    self.balance = 0

# deposit to your savings account. Inheritance plays a role since the class inherits the deposit
# from m-bongo cash
  def deposit_to_mbongocash(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid deposit amount'

    else:
      raise ValueError()

  def withdraw_from_mbongocash(self,amount):
    if type(amount) ==  int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:

          self.balance-=amount
          return self.balance

        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid withdraw amount'
      else:
        raise ValueError()
