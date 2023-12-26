'''
#Task 1
def eligibility(credit_score,annual_income):
    if credit_score > 700 and annual_income > 50000:
        return "You are eligible for loan"
    else:
        return "You are not eligible for loan"

credit_score=int(input('Enter your credit score:'))
annual_income=int(input('Enter your annual income:'))
print(eligibility(credit_score,annual_income))



#task2
def atm(current_balance,transaction):
    if transaction == 1:
        print(current_balance)

    elif transaction == 2:
        amount=int(input('Amount you want to withdraw:'))
        if amount > current_balance:
            return 'Insufficient balance'
        elif amount%100 != 0:
            return 'amount should be in 100s only'

        else:
            current_balance -= amount
            return 'transaction success \n current balance:%d'%(current_balance)
    elif transaction == 3:
        amount=int(input('Amount you want to deposit:'))
        current_balance +=amount
        return 'transaction success \n current balance:%d'%(current_balance)

current_balance = int(input("enter your current balance:"))
transaction=int(input('What you want to do \n 1 : Check balance \n 2 : Withdraw \n 3 : Deposit \n enter :' ))
print(atm(current_balance,transaction))


#task 3
def future(balance,intrest,years):
    future_balance=balance*(1+intrest/100)**years
    print(future_balance)

while True:
    balance=int(input('Enter your initial balance:'))
    intrest=float(input('Enter your intrset rate:'))
    years=int(input('Enter your number of years:'))
    print(future(balance,intrest,years))
    ask=input('do you want to check for next customer:')
    if ask in ['NO','No','nO','no']:
        print('Process ended')
        break


#task-4
bank={1:100,2:200,3:300,4:400}

def bank_details(account):
    for i in bank.keys():
        if account == i:
            return bank.get(i)
    else:
        return 'Enter Correct account number'

account=int(input('Enter Bank account number:'))
print(bank_details(account))



#task5
def password(password):
    if len(password) > 7 and password.islower() == False and any(map(str.isdigit,password)) == True:
        print('Valid password')
    else:
        print('not a valid password')

inp_pass=str(input('Enter password:'))
print(password(inp_pass))




# task6
balance = 100
output = []
while True:
    transaction = str(input('What you want to do:'))
    if transaction == 'exit':
        break
    elif transaction == 'deposit':
        deposit = int(input('Enter amount you want to deposit:'))
        balance += deposit
        history = ('amount deposited:', str(deposit))
        output.append(history)
    elif transaction == 'withdraw':
        withdraw = int(input('enter amount you want to withdraw:'))
        if withdraw > balance:
            print('insufficient balance')
        else:
            balance -= withdraw
            history = ('amount withdraw:', str(withdraw))
            output.append(history)
print(output)
'''