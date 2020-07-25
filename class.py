class BankAccount:
    bank = "Cooperative bank"


    def _init_(self,first_name,last_name):
        self.first_name =first_name = first_name
        self.last_name =last_name = last_name
        self.balance = 0
        self.phone_number = phone_number
        self.bank = bank
        self.deposit = []
        self.withdrawals =[]
        self.loan = 0


    def account_name(self):
        name = "{} account for {} {}".format(self.bank,self.first_name,self.last_name)
        return  name


    def deposit(self,amount):
        try:
            amount = 1000
        except TypeError:
            print("please enter amount in figures") 
            return 
        if amount <=0:
           print("you cannot deposit zero or negative") 
        else:     
            self .balance += amount
            self.deposit.append(amount)
            time = datetime.now()
            formarted_time = time.strftime("%A,%B,%e,%Y,%I:%M %P")
            print("you have deposited {} to {} on {}".format(amount,self.account_name),formarted_time)        

    def withdraw(self, amount):
        try:
            amount = 1000
        except TypeError:
            print("please enter amount  in figures")
            return
        if amount <=0:
            print("you cannot withdraw zero or negative")
        elif amount >self.balance:
            print("you don't have enough balance")
        else:
            self.balance +=amount
            self.withdrawls.append(amount)
            time = datetime.now()
            formarted_time = time.strftime("%A,%B,%e,%Y,%I:%M %P")

            print("you have withrawn {} from {} on {}".format(amount,self.account_name),formated_time)        
    
    def get_balance(self):
        return "The balance for {} is {} on {}".format(self.account_name(),self.balance)



    def show_deposit_statment(self):
        for deposit in self.deposit:
            print(deposit)
        else:
             self.balance +=(amount)
             time = datetime.now()
             formarted_time = time.strftime("%A,%B,%e,%Y,%I:%M %P")
             print("you have deposited {} on {}".format(amount,formarted_time))

    def show_withdrawals_statment(self):
        for withdrawals in self.withdrawals:
            print(withdrawal)
        else:
             self.balance +=(amount)
             self.withdrawals.append(amount)
             time = datetime.now()
             formarted_time = time.strftime("%A,%B,%e,%Y,%I:%M %P")
             print("you have withdraw {} on {}".format(amount,formarted_time))


    def request_loan(self,amount):
         try:
            amount = 1000
         except TypeError:
            print("please enter amount  in figures")
            return
         if amount <=0:
            print("you cannot request a loan of that amount")
         else:
            self.balance +=amount
            self.loan.append(amount)
            time = datetime.now()
            formarted_time = time.strftime("%A,%B,%e,%Y,%I:%M %P")
            print("you have been given a loan of {} on {}".format(amount,formarted_time))


