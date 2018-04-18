#Atm in py
print("You will have 3 chances to use this")
print("If still have any problem using this,then for call to bank for further information")
card = int(input("Enter your card number:"))
if card>10000 and card<99999:
    print("Valid")
    print("Good morning")
    print("0 for Use this")
    print("1 for Terminate this")    
    choice = int(input("Enter your choice:"))    
    if choice == 0:
        cvv = int(input("Enter your cvv number:"))
        if cvv>100 and cvv<999:
            print("Welcome to bank")
            pin = int(input("Enter your pin:"))
            Balance = pin*1000/100
            print("Your Balance is:{}".format(Balance))
            if pin>1000 and pin<9999:
                print("Your current Balance")
                print("Now choose your option")
                print("Here are following option")
                print("1 for Withdrawal")
                print("2 for Saving")
                print("3 for Current")
                print("4 for Exit")
                print("5 for Re-use")
                option = int(input("Enter your choice:"))
                if option == 1:
                    print("You choose Withdrawal")
                    amount = int(input("Enter your amount:"))
                    Withdrawal = Balance-amount
                    print("Your amount is :",Withdrawal)
                    print("Take your receipt")
                if option == 2:
                    print("You choose Saving")
                    amount = int(input("Enter your amount:"))
                    Saving = Balance+10000-amount
                    print("Your saving amount is",Saving)
                    print("Take your receipt")
                if option == 3:
                    print("You choose Current")
                    amount = int(input("Enter your amount:"))
                    Current = Balance-1000-amount
                    print("Your current amount is",Current)
                    print("Take your receipt")
                if option == 4:
                    print("You want to exit\nThanks for using this\n Have a nice day")
                if option == 5:
                    print("Now choose your option")
                    print("Here are following option")
                    print("1 for Withdrawal")
                    print("2 for Saving")
                    print("3 for Current")
                    print("4 for Exit")
                    print("5 for Re-use")
            else:
                print("Not valid")
        elif cvv<100 :
            print("Can't fetch data")
        elif cvv>999:
            print("Can't fetch data")
        else:
            print("Call to Bank for help")
        print("\n")    
        print("Now this is your 2 chance")    
        print("0 for Use this")
        print("1 for Terminate this")
        choice = int(input("Enter your choice:"))
        if choice == 0:
            cvv = int(input("Enter your cvv number:"))
            if cvv>100 and cvv<999:
                print("Welcome to bank")
                pin = int(input("Enter your pin:"))
                Balance = pin*1000/100
                print("Your Balance is:{}".format(Balance))
                if pin>1000 and pin<9999:
                    print("Your current Balance")
                    print("Now choose your option")
                    print("Here are following option")
                    print("1 for Withdrawal")
                    print("2 for Saving")
                    print("3 for Current")
                    print("4 for Exit")
                    print("5 for Re-use")
                    option = int(input("Enter your choice:"))
                    if option == 1:
                        print("You choose Withdrawal")
                        amount = int(input("Enter your amount:"))
                        Withdrawal = Balance-amount
                        print("Your amount is :",Withdrawal)
                        print("Take your receipt")
                    if option == 2:
                        print("You choose Saving")
                        amount = int(input("Enter your amount:"))
                        Saving = Balance+10000-amount
                        print("Your saving amount is",Saving)
                        print("Take your receipt")
                    if option == 3:
                        print("You choose Current")
                        amount = int(input("Enter your amount:"))
                        Current = Balance-1000-amount
                        print("Your current amount is",Current)
                        print("Take your receipt")
                    if option == 4:
                        print("You want to exit\nThanks for using this\n Have a nice day")
                    if option == 5:
                        print("Now choose your option")
                        print("Here are following option")
                        print("1 for Withdrawal")
                        print("2 for Saving")
                        print("3 for Current")
                        print("4 for Exit")
                        print("5 for Re-use")
                else:
                    print("Not valid") 
            elif cvv<100 :
                print("Can't fetch data")
            elif cvv>999:
                print("Can't fetch data")
            else:
                print("Call to Bank for help")
                print("\n")        
                print("Now this is your 3 and last chance")        
                print("0 for Use this")
                print("1 for Terminate this")
                choice = int(input("Enter your choice:"))
            if choice == 0:
                cvv = int(input("Enter your cvv number:"))
                if cvv>100 and cvv<999:
                    print("Welcome to bank")
                    pin = int(input("Enter your pin:"))
                    Balance = pin*1000/100
                    print("Your Balance is:{}".format(Balance))
                    if pin>1000 and pin<9999:
                        print("Your current Balance")
                        print("Now choose your option")
                        print("Here are following option")
                        print("1 for Withdrawal")
                        print("2 for Saving")
                        print("3 for Current")
                        print("4 for Exit")
                        print("5 for Re-use")
                        option = int(input("Enter your choice:"))
                        if option == 1:
                            print("You choose Withdrawal")
                            amount = int(input("Enter your amount:"))
                            Withdrawal = Balance-amount
                            print("Your amount is :",Withdrawal)
                            print("Take your receipt")
                        if option == 2:
                            print("You choose Saving")
                            amount = int(input("Enter your amount:"))
                            Saving = Balance+10000-amount
                            print("Your saving amount is",Saving)
                            print("Take your receipt")
                        if option == 3:
                            print("You choose Current")
                            amount = int(input("Enter your amount:"))
                            Current = Balance-1000-amount
                            print("Your current amount is",Current)
                            print("Take your receipt")
                        if option == 4:
                            print("You want to exit\nThanks for using this\n Have a nice day")
                        if option == 5:
                            print("Now choose your option")
                            print("Here are following option")
                            print("1 for Withdrawal")
                            print("2 for Saving")
                            print("3 for Current")
                            print("4 for Exit")
                            print("5 for Re-use")
                    else:
                        print("Not valid")
                elif cvv<100 :
                    print("Can't fetch data")
                elif cvv>999:
                    print("Can't fetch data")
                else:
                    print("Call to Bank for help")
        if choice == 1:
            print("Have good day,If you have any enquiry so please call +91^##$&*%%##")
else:
    print("Access Denied")

    
    
    
    
    
    
