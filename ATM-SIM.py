                                                                                                                                                 
from abc import ABC , abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def transaction(self):
        pass

class Account:
    transaction_history=[]
    def __init__(self,name,acc_no,bal,pw):
        self.__balance=bal
        self.__pass=pw
        self.name=name
        self._acc_no=acc_no
        print("USER ACCOUNT CREATED !")
    def show_details(self):
        return self.name , self._acc_no 
    def show_balance(self):
        return self.__balance
    def modify_balance(self,new_bal):
        self.__balance=new_bal
        return self.__balance
    def  pass_varification(self,p):
       return  True if  int(p)==int(self.__pass) else False
class ATM(BankAccount,Account):
    bank_name=" NARASIMHA BANKING & FINANCE LIMITED , INDIA"
    def deposit_money(self,amt):
        self.transaction()
        psw=int(input("enter your four digit pin"))
        if self.pass_varification(psw):
            n_bal=self.show_balance()+amt
            self.transaction_history.append(f" DEPOSITED AMOUNT {amt}")
            self.modify_balance(n_bal)
            print(f"TRANSACTION COMPLETED SUCESSFULLY ! @ {self.name}")

        else :
            print("invalid pin")
    def with_draw(self,amt):
        self.transaction()
        if validate_money(amt):
            if amt>10000:
                p=int(input("ENTER YOUR PASSWORD : "))
                if self.pass_varification(p):
                    if self.valid_amt(amt):
                        n_bal=self.show_balance()-amt
                        self.modify_balance(n_bal)
                        self.transaction_history.append(f" WITHDRAWN AMOUNT {amt}")
                        print(f"TRANSACTION COMPLETED SUCESSFULLY ! @ {self.name}")
                    else:
                        print("INSUFFICENT FUNDS ! ")
                else:
                    print("INVALID PASSWORD !") 
            else:
                print("WITHDRAW LIMIT ONLY 20000 Rs ") 
        else:
            print("ENTER A VALID AMOUNT ! ")
    def valid_amt(self,duddu):
        if (self.show_balance()-duddu)>0:
            return True
        else:
            return False

    def transaction(self):
        print("transaction intialized ! ")
    def show_bank_name(cls):
        print("+===================================================================+")
        print(f"|                 {cls.bank_name}                   |")
        print("+===================================================================+")
def validate_money(money):
    if money> 0:
        return True
    else:
        return False

u_name=input(":: enter user name ::")
u_acc_no=int(input(":: ENTER THE USER ACCOUNT NUMBER ::"))
px=input("enter four digit pin ")
pw=0
if len(px)==4:
    pw=px
else:
    print("INVALID PIN ! ")
    print("YOU ARE EXITTING NOW ")
    print("THE PIN MUST BE IN ONLY FOUR DIGIT NUMBER ")
    exit()
u_bal=int(input(":: enter your balance amount in current account ::"))

user=ATM(u_name,u_acc_no,u_bal,pw)
user.show_bank_name()

while True:
    print("+      +   -----------------------   +      +")
    print("|-------   MENU FOR ACCOUNT HOLDER   -------|")
    print("+      +   -----------------------   +      +")
    print("[ 1 ] SHOW BALANCE")
    print("[ 2 ] DEPOSIT MONEY")
    print("[ 3 ] WITHDRAW AMOUNT")
    print("[ 4 ] TRANSACTION HISTORY AND COUNT ")
    print("[ 5 ] ACCOUNT DETAILS")
    print("[ 6 ] EXIT")
    choice=int(input("ENTER YOUR CHOICE : "))
    if choice==1:
        print(user.show_balance())
    elif choice==2:
        amount=int(input("ENTER AMOUNT TO DEPOSIT : "))
        if validate_money(amount):
            user.deposit_money(amount)
    elif choice ==3:
        amount=int(input("ENTER THE AMOUNT TO WITHDRAWN "))
        user.with_draw(amount)
    elif choice== 4:
        th=user.transaction_history
        print("+----------------------------+")
        print("|    TRANSACTION HISTORY     |")
        print("+----------------------------+")
        print(f"total transaction count{len(th)}")
        for i in th:
            print(i)
    elif choice==6: 
        c=input("ARE YOU SURE TO EXIT[Y/N] :").upper()
        if c=="Y":
            break
        elif c=="N" :
            pass
        else:
            print("INVALID CHOICE  !:")
    elif choice ==5:
        l=[]
        l=user.show_details()
        print("ACCOUNT HOLDER ID :",l[0])
        print("ACCOUNT NUMBER ",l[1] )
    else:
        print(" INVALID OPTION ! ")

