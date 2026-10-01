import MySQLdb
import random
class sbi:
    def __init__(self):
        self.con=MySQLdb.connect(user="root",
                  password="abhi4561",
                  host="localhost")
        sql="create database if not exists sbi_bank"
        self.cursor=self.con.cursor()
        self.cursor.execute(sql)
        self.cursor.execute("use sbi_bank")
        table='''create table if not exists bank(Name varchar(30),Age int,Gender char(6),Phone Bigint,Account_Number bigint,Type varchar(30),Balance bigint,IFSC_Code varchar(20) default "SBI012345")'''
        self.cursor.execute(table)
    def create(self):
        print("-------Creating Account------")
        name=input("Enter Your Name: ")
        Age=int(input("Enter Your Age: "))
        gender=input("Enter Your Gender: ")
        phone=int(input("Enter Your Mobile Number: "))
        acc=random.randint(1000000000,9999999999)
        print('''1.Zero Account/2.Savings Account''')
        x=int(input("Please select option: "))
        while True:
            if x==1:
                bal=int(input("Please Deposit ₹500 in Your Account"))
                if bal>=500:
                    type="Zero Account"
                    balance=bal
                    break
                else:
                    print("Please Enter the valid Amount ₹500")
            else:
                b=int(input("Please Deposit ₹1000 in Your Account"))
                if b>=1000:
                    type="Savings Account"
                    balance=b
                    break
                else:
                    print("Please Enter the valid amount ₹1000")
        insert_data = '''
        insert into bank
        (Name, Age, Gender, Phone, Account_Number, Type, Balance)
        values (%s, %s, %s, %s, %s, %s, %s)
        '''

        values = (
            name,
            Age,
            gender,
            phone,
            acc,
            type,
            balance
        )
        print("----Account Created----")
        print("Account Number: ",acc)
        self.cursor.execute(insert_data, values)
        self.con.commit()
    def deposit(self):
        print('----welcome to deposit----')
        acc_name=input("enter your name: ")
        acc_num = int(input('enter Account number:'))
        
        bank_ac='''select Account_Number from bank where Name=%s and Account_number=%s  '''
        self.cursor.execute(bank_ac,(acc_name,acc_num))
        data=self.cursor.fetchone()
        if data:
            
            Amount = int(input('Enter Deposit Amount:'))
            update_amount='''update  bank set Balance=Balance+%s where Account_Number=%s'''
            self.cursor.execute(update_amount,(Amount,acc_num))
            self.con.commit()
            print("---Amount Deposited---")
        else:
            print('---INvalid Account number---')
        
    def withdraw(self):
        print('-----withdraw method----')

        acc_name = input("enter your name: ")
        acc_num = int(input('enter Account number: '))

        sql = '''
        select Balance
        from bank
        where Name=%s and Account_Number=%s
        '''

        self.cursor.execute(sql, (acc_name, acc_num))

        data = self.cursor.fetchone()

        if data:

            balance = data[0]

            print("Available Balance:", balance)

            Amount = int(input('Enter withdrawal Amount: '))

            if Amount > balance:
                print("---Insufficient Funds---")

            else:

                update_amount = '''
                update bank
                set Balance=Balance-%s
                where Account_Number=%s
                '''

                self.cursor.execute(
                    update_amount,
                    (Amount, acc_num)
                )

                self.con.commit()

                print("---Amount Withdrawal Success---")

        else:
            print('---Invalid Account number or Name---')
    def Details(self):
        print('-----Details-----')
        print()                              
        self.cursor.execute("select * from bank")
        data=self.cursor.fetchall()
        for row in data:
            print(row)
obj = sbi()

while True:
    print('--------------------------')
    print('''
          1) Create Account
          2) deposit
          3) withdraw
          4) Details
          5)Exit''')
    print('--------------------------')
    
    k = int(input('Select one option:'))
    if k==1:
        obj.create()
    elif k==2:
        obj.deposit()
    elif k==3:
        obj.withdraw()
    elif k==4:
        obj.Details()
    elif k==5:
        break