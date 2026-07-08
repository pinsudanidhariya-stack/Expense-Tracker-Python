# prject 1
#Expence tracker Project

expensesList=[]     # LIst of expenses in from on dictionary

print("Welcome to Expense tracker :")

while True:
    print("=====MENU====")
    print("1.Add expense")
    print("2.View All expense")
    print("3.View total Spending")
    print("4.Exit")

    choice=int(input("Please Enter Your Choice :  "))

#Add expense
    if(choice==1):
        date=input("Enter Date : ")
        category=input("Enter the category(Food,travel,sloon,Books) : ")
        description=input("Catgry all details : ")
        amount=float(input("Enter the amount : "))
        
        
        expens={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expensesList.append(expens)
        print("\n Expenses Added succesfully ! ")


#2 View All expense
    elif(choice==2):
        if(len(expensesList)==0):
            print("No expenses add. Add Expenses")
        else:
            print("==== Your expenses ====")
            count= 1
            for eachexpense in expensesList:
                print(f"Expense Num {count} -> {eachexpense['date']}, {eachexpense['category']}, {eachexpense['description']}, {eachexpense['amount']}")
                count=count+1


# 3 View total Spending

    elif(choice==3):
        total=0
        for eachexpense in expensesList:
            total=total + eachexpense["amount"]
        print("\n Total expense = ",total)


# 4 Exit

    elif(choice==4):
        print("Thank Your For Use ")
        break

    else:
        print("INVALID CHOICE! ")
