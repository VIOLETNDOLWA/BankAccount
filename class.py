class BankAccount:
    bank = "Cooperative bank"


    def _init_(self,first_name,last_name):
        self.first_name =first_name
        self.last_name =last_name
        self.balance = 0

    def account_name(self):
         name = "{}.account for {} {}".format(self.bank,self.first_name,self.last_name_
         return name


    def withdraw(self,amount):
         self .balance += amount


         print("you have withdraw {} to your accoun".format(amount))  
    def get_balance(self) 
      return "This balance for {} is {}".format(self.account_name(),self.balance)

    def deposi(self.amount):
        self.balance +=amount

        print("you have deposited {} to your account".format(amount))
        if amount > 0:
           print("you have deposited {}from your account".format(amount))
        else :
            print("money isn't sufficient)
acc1 =BankAccount("Leila","marvelous")
acc2 =BankAccount("charles","precious")

acc3 =BankAccount("Favour","Pendo")
acc4 =BankAccount("Darius","handsome")

acc1.deposit(9000)
acc2.deposit(4000)
acc1.deposit(1000)
acc2.deposit(700)

acc3.withdraw(14000)
acc4.withdraw(1000)
acc3.withdraw(750)
acc.withdraw(700)

print(acc1.get_balance())
print(acc2.get_balance())

print(acc1.account_name())
print(acc2.account_name())

# write a method to return the withdrawl transaction
     def lend_loan(self,loan):
         if loan <=0:
             print("invalid request")
             else:
                 self.loan_balance +=loan
                 print("{} you have borrowed {}".format(self.account_name,loan))

    def deposit_statment(self,amount):
        self.deposit(self.amount)
        return self.deposit_statment_summary.append(amount)


acc1 =BankAccount("Favour","Blessing"'+2547890269,"KCB")
print(acc1.phone_number)
acc1.deposit(150000)
acc1.withdraw(12000)
acc1.withdraw(10000)
acc1.deposit(7000)
acc1.deposit(5000)
acc1.lend_loan(20000)
acc1.pay_loan(8000)
print(acc1.loan_balance)
print(acc1.deposit_summary)

    