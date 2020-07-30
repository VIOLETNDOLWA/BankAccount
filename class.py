class Account:
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
            amount + 1000
        except TypeError:
            print("please enter amount in figures") 
            return 
        if amount <=0:
           print("you cannot deposit zero or negative") 
        else:     
            self .balance += amount
            self.deposit.append(amount)
            time =  deposit("amount")
            formarted_time = self.get_formated_time(time)
            amount =deposit["amount"]
            statment ="you have deposit {} on {}".format(amount,formarted_time)
            print(deposit)        

    def withdraw(self, amount):
        try:
            amount + 1000
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
            formarted_time = self.get_formated_time(time)
            amount =deposit["amount"]
            statment ="you have withdrwa{} on {}".format(amount,formarted_time)
            print(withdraw)             
    
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
            amount + 1000
         except TypeError:
            print("please enter amount  in figures")
            return
        if amount <=0:
            print("you cannot request a loan of that amount")
        else:
             self.loan = amount
             print("you have been given a loan of  {}".format(amount))

    def repay_loan(self,amount):
         try:
            amount + 1000
         except TypeError:
            print("please enter amount  in figures")
            return

        if amount <=0:
            print("you cannot pay with that amount")
        elif self.amount =0:
            print("you do not have a loan of that amount")
        elif amount > self.loan
            print("your loan is {},please enter amount that is less or equal".format(self.loan))

            
         else:
             self.loan -= amount
             time =time.now() 
             repayment ={
                 "time":time,
                 "amount":amount
             }  
             self.loan_repayment.append(repayment)
             print("you have repaid your loan with {}.your loan balance is {}",format(self.loan))
     def loan_repayment _statment(self):
         for repayment in self.loan_repayment:
             time = repayment["time"]
             amount = repayment ["amount"]
             formarted_time =self.get_formated_time(time)
             statment ="you repaid {} on {}".format(amount,formatted_time)
             print(statment)



class BankAccount(Account):
    def _init_(self,first_name,last_name,phone_number,bank):
        self.bank = bank
        self.bill = []
        self.receive = []
        self.send =[]
        super()._init_(first_name,last_name,phone_number)

    def pay_bill(self,amount):
         if amount >self.balance
           print("you don't have enough balance.your balance is {}".format(self.balance)) 
        else:
            self.balance -=amount
            time =datetime.now()
            bill ={
                "time":time,
                "bill":amount
            }
            self.bill.append(bill)
            print("you paid {} on {}".format(amount,formatted_time))

    def received_money(self,amount):
        if amount > self.balance
           print("you don't have enough balance.your balance is {}".format(self.balance)) 
        else:
            self.balance -=amount
            time =datetime.now()
            bill ={
                "time":time,
                "receive":amount
            }
            self.receive.append(receive)
            print("you have receive {} on {}".format(amount,formatted_time))
    def send_money(self,amount):
         if amount > self.balance
           print("you don't have enough balance.your balance is {}".format(self.balance)) 
        else:
            self.balance -=amount
            time =datetime.now()
            bill ={
                "time":time,
                "receive":amount
            }
            self.send.append(send)
            print("you have send {} on {}".format(amount,formatted_time))



        
        




 class MobileMoneyAccount(Account):
     def _init_ (self,first_name,last_name,phone_number,services_provider):
         self.services_provider = services_provider
         self.airtime = [] 
         self.bill = []
         self.receive = []
         self.send = []
          super()._init_(first_name,last_name,phone_number) 

     def buy_airtime(self,amount):
         try:
             amount + 1
          except TypeError:
               print("please enter the amount in figures")
               return
            if  amount >self.balance
                 print("you don't have enough balance. your balance is {}".format(self.balance))
             else:
                 self.balance -= amount
                 time = datetime.now()  
                 airtime = {
                     "time":time,
                     "airtime":amount
                 } 
                 self.airtime.append(airtime) 
                 print("you have bought airtime worth {} on {}".format(amount,self.get_formatted_time(time(time))))  

     def pay_bill(self,amount):
         if amount >self.balance
           print("you don't have enough balance.your balance is {}".format(self.balance)) 
        else:
            self.balance -=amount
            time =datetime.now()
            bill ={
                "time":time,
                "bill":amount
            }
            self.bill.append(bill)
            print("you paid {} on {}".format(amount,formatted_time))

     def  received_money(self,amount):
        if amount > self.balance
           print("you don't have enough balance.your balance is {}".format(self.balance)) 
        else:
            self.balance -=amount
            time =datetime.now()
            bill ={
                "time":time,
                "receive":amount
            }
            self.receiv_money.append(receive)
            print("you have receive {} on {}".format(amount,formatted_time))


    def send_money(self,amount):
         if amount > self.balance
           print("you don't have enough balance.your balance is {}".format(self.balance)) 
        else:
            self.balance -=amount
            time =datetime.now()
            bill ={
                "time":time,
                "receive":amount
            }
            self.send_money.append(send)
            print("you have send {} on {}".format(amount,formatted_time))



        
