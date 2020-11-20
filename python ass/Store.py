print("\tWelcome to Pystore")
     #samsung
name = input("Enter your name please: ")
purchase = input(f"{name}, What would you like to purchase please\n(1)Phone\n(2)cars\n(3)wrist-watches\n ")
if  purchase.lower() == "phone" or purchase == "1":
    brand = input(f"{name}, Which type of brand would you like to purchase?: ")
    if brand.lower() == "samsung":
        print(f"\t{name},These are the lists of Samsung Smartphones we sell in Pystore.\n(1)Samsung J5\n(2)Samsung J6\n(3)Samsung J7\n(4)Samsung S10\n(5)Samsung S20")
        choose = input(f"{name}, Choose your perfered phone to purchase: ")
        if choose == "1" or choose.lower() == "samsung j5" or choose.lower() == "samsungj5" :
            price = 55000
            quantity = int(input(f"{name}, How many Samsung J5 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() ==  "samusng j6" or choose.lower() == "samsungj6":
            price = 89000
            quantity = int(input(f"{name}, How many Samsung J6 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "samsung j7" or choose.lower() == "samsungj7":
            price = 150000
            quantity = int(input(f",{name}, How many Samsung J7 would you like to purchase: "))
            bill = f"{name},Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "samsung s10" or choose.lower() == "samsungs10":
            price1 = 472527
            quantity = int(input(f"{name}, How many Samsung S10 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "samsung s20" or choose.lower() == "samsungs20":
            price1 = 500000
            quantity = int(input(f"{name}, How many Samsung S20 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number or input!!!")
      #tecno
    elif brand.lower() == "Tecno":
        print(f"\t{name}, These are the lists of Tecno Smartphones we sell in Pystore\n(1)Techo Camon 12 PRO\n(2)Tecno Spark 4\n(3)Tecno Camon 15\n(4)Tecno Spark 5\n(5)Tecno Pouvoir 4")
        choose = input(f"{name}, Choose your perfered phone to purchase: ")
        if choose == "1" or choose.lower() == "tecno camon 12 pro" or choose.lower() == "tecnocamon12pro":
            price = 58500
            quantity = input(f"{name}, How many Tecno Camon 12 PRO would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() == "tecno spark 4" or choose.lower() == "tecnospark4":
            price = 43500
            quantity = input(f"{name},How many Tecno Spark 4 would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "tecno camon 15" or choose.lower() == "tecnocamon15":
            price = 63413
            quantity = input(f"{name}, How many Tecno Camon 15 would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "tecno spark 5" or choose.lower() == "tecnospark5":
            price1 = 47500
            quantity = input(f"{name}, How many Tecno Spark 5 would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "tecno pouvoir 4" or choose.lower() == "tecnopouvoir4":
            price1 = 50000
            quantity = input(f"{name}, How many Tecno Pouvoir 4 would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number")
            #iphone
    elif brand.lower() == "iphone":
        print(f"\t{name}, These are the lists of iphone Smartphones we sell in Pystore\n(1)iphone 11 PRO\n(2)iphone xsmax\n(3)iphone x\n(4)iphone 8+\n(5)iphone 7+")
        choose = input(f"{name}, Choose your perfered phone to purchase: ")
        if choose == "1" or choose.lower() == "iphone 11 pro" or choose.lower() == "iphone11pro":
            price = 520000
            quantity = input(f"{name}, How many iphone 11 PRO would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() == "iphone xsmax" or choose.lower() == "iphonexsmax":
            price = 330000
            quantity = input(f"{name},How many iphone xsmax would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "iphone x" or choose.lower() == "iphonex":
            price = 240000
            quantity = input(f"{name}, How many iphone x would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "iphone 8+" or choose.lower() == "iphone8+":
            price1 = 220000
            quantity = input(f"{name}, How many iphone 8+ would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "iphone 7+" or choose.lower() == "iphone7+":
            price1 = 180000
            quantity = input(f"{name}, How many iphone 7+ would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number")
            #WE ALSO SELL CARS... THESE ARE THE PRICE LIST 
if  purchase.lower() == "cars" or purchase == "2":
    brand = input(f"{name}, Which type of brand would you like to purchase?: ")
    if brand.lower() == "mercedes":
        print(f"\t{name},These are the lists of mercedes cars we sell in Pystore.\n(1)Mercedes benz\n(2)Mercedes acura\n(3)Mercedes c class\n(4)mercedes E300\n(5)Mercedes pilot")
        choose = input(f"{name}, Choose your perfered car to purchase: ")
        if choose == "1" or choose.lower() == "Mercedes benz" or choose.lower() == "Mercedesbenz":
            price = 40000000
            quantity = int(input(f"{name}, How many Mercedes benz would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() ==  "Mercedes acura" or choose.lower() == "Mercedesacura":
            price = 2000000
            quantity = int(input(f"{name}, How many Mercedes acura would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "Mercedes c class" or choose.lower() == "MercedeCclass":
            price = 15000000
            quantity = int(input(f",{name}, How many Mercedes c class would you like to purchase: "))
            bill = f"{name},Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "mercedes E300" or choose.lower() == "mercedesE300":
            price1 = 14000000
            quantity = int(input(f"{name}, How many mercedes E300 would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "Mercedes pilot" or choose.lower() == "Mercedespilot":
            price1 = 500000
            quantity = int(input(f"{name}, How many Mercedes pilot would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number or input!!!")
            #toyota
    elif brand.lower() == "Toyota":
        print(f"\t{name}, These are the lists of Tecno Smartphones we sell in Pystore\n(1)Toyota Corolla\n(2)Toyota hilux\n(3)Toyota camry\n(4)Toyota tundra\n(5)Toyota highlander")
        choose = input(f"{name}, Choose your perfered phone to purchase: ")
        if choose == "1" or choose.lower() == "Toyota Corolla" or choose.lower() == "ToyotaCorolla":
            price = 1000000
            quantity = input(f"{name}, How many Toyota Corolla would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() == "Toyota hilux" or choose.lower() == "Toyotahilux":
            price = 43000000
            quantity = input(f"{name},How many Toyota hilux would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "Toyota camry" or choose.lower() == "Toyotacamry":
            price = 6000000
            quantity = input(f"{name}, How many Toyota camry would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "Toyota tundra" or choose.lower() == "Toyotatundra":
            price1 = 47000000
            quantity = input(f"{name}, How many Toyota tundra would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "Toyota highlander" or choose.lower() == "Toyotahighlander":
            price1 = 5000000
            quantity = input(f"{name}, How many Toyota highlander would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number")
        #FORD
    elif brand.lower() == "Ford":
        print(f"\t{name}, These are the lists of Tecno Smartphones we sell in Pystore\n(1)Ford GT\n(2)Ford Galaxy\n(3)Ford x-mas\n(4)Ford puma\n(5)Ford edge")
        choose = input(f"{name}, Choose your perfered phone to purchase: ")
        if choose == "1" or choose.lower() == "Ford GT" or choose.lower() == "FordGT":
            price = 1000000
            quantity = input(f"{name}, How many Ford GT would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() == "Ford Galaxy" or choose.lower() == "FordGalaxy":
            price = 43000000
            quantity = input(f"{name},How many Ford Galaxy would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "Ford x-mas" or choose.lower() == "Fordx-mas":
            price = 6000000
            quantity = input(f"{name}, How many Ford x-mas would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "Ford puma" or choose.lower() == "Fordpuma":
            price1 = 47000000
            quantity = input(f"{name}, How many Ford puma would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "Ford edge" or choose.lower() == "Fordedge":
            price1 = 5000000
            quantity = input(f"{name}, How many Ford edge would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number")
        #WE ALSO SELL WRIST-WATCHES... THESE ARE THE PRICE LIST
if  purchase.lower() == "wrist-watches" or purchase == "3":
    brand = input(f"{name}, Which type of brand would you like to purchase?: ")
    if brand.lower() == "Rolex":
        print(f"\t{name},These are the lists of Rolex watches we sell in Pystore.\n(1)Vintage rolex\n(2)cellini rolex\n(3)Milgauss rolex\n(4)Air-king rolex\n(5)Submariner rolex")
        choose = input(f"{name}, Choose your perfered car to purchase: ")
        if choose == "1" or choose.lower() == "Vintage rolex" or choose.lower() == "Vintagerolex":
            price = 40000
            quantity = int(input(f"{name}, How many Vintage rolex would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() ==  "cellini rolex" or choose.lower() == "cellinirolex":
            price = 20000
            quantity = int(input(f"{name}, How many cellini rolex would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "Milgauss rolex" or choose.lower() == "Milgaussrolex":
            price = 15000
            quantity = int(input(f",{name}, How many Milgauss rolex would you like to purchase: "))
            bill = f"{name},Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "Air-king rolex" or choose.lower() == "Air-kingrolex":
            price1 = 140000
            quantity = int(input(f"{name}, How many Air-king rolex would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "Submariner rolex" or choose.lower() == "Submarinerrolex":
            price1 = 50000
            quantity = int(input(f"{name}, How many Submariner rolex would you like to purchase: "))
            bill = f"{name}, Your bill is N{price * quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number or input!!!")

    elif brand.lower() == "Ford":
        print(f"\t{name}, These are the lists of Tecno Smartphones we sell in Pystore\n(1)Ford GT\n(2)Ford Galaxy\n(3)Ford x-mas\n(4)Ford puma\n(5)Ford edge")
        choose = input(f"{name}, Choose your perfered phone to purchase: ")
        if choose == "1" or choose.lower() == "Ford GT" or choose.lower() == "FordGT":
            price = 1000000
            quantity = input(f"{name}, How many Ford GT would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "2" or choose.lower() == "Ford Galaxy" or choose.lower() == "FordGalaxy":
            price = 43000000
            quantity = input(f"{name},How many Ford Galaxy would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "3" or choose.lower() == "Ford x-mas" or choose.lower() == "Fordx-mas":
            price = 6000000
            quantity = input(f"{name}, How many Ford x-mas would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "4" or choose.lower() == "Ford puma" or choose.lower() == "Fordpuma":
            price1 = 47000000
            quantity = input(f"{name}, How many Ford puma would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        elif choose == "5" or choose.lower() == "Ford edge" or choose.lower() == "Fordedge":
            price1 = 5000000
            quantity = input(f"{name}, How many Ford edge would you like to purchase: ")
            bill = f"{name}, Your bill is N{price * Quantity} for the phone(s)."
            print(f"{bill}\n\tThank you for using Pystore.")
        else:
            print("\tInalid input!!!\nEnter a valid number or input!!!")