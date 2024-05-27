#snacks
IceCandyPA_price = 15
IceCandyCnC_price = 15
IceCandyMG_price = 15
Milkbars_price = 15
CreamO_price = 10

IceCandyPA_stock = 25
IceCandyCnC_stock = 25
IceCandyMG_stock = 25
Milkbars_stock = 25
CreamO_stock = 25

#drinks
Coke_price = 15
Icedtea_price = 15
Sprite_price = 15
Zesto_price = 12
Royal_price = 15

Coke_stock = 25
Icedtea_stock = 25
Sprite_stock = 25
Zesto_stock = 25
Royal_stock = 25


#sudan
Chopsouy_price = 25
Manok_price = 35
SaladCucumber_price = 28 
ChickenLiver_price = 23 
Maranay_price = 20

Chopsouy_stock = 25
Manok_stock = 25
SaladCucumber_stock = 25 
ChickenLiver_stock = 25
Maranay_stock = 25

#rice
rice_price = 15
brice_price = 25

rice_stock = 25
brice_stock = 25


price = 0
orders = []
loop = 1
i = 0
orders.append([i],)

while loop == 1:
    
    
    
    
    print("""options:
            1 - view menu/reserve
            2 - view reserved 
            3 - exit""")
    
    try:
          choice1 = int(input("Insert choice here: "))
          
    except ValueError:
          print("that's not a number.")
          continue
    
    if choice1 > 3:
          print("That's not part of the choices")
          continue

    
    
    if choice1 == 1:
          
          print(orders)
          
            
          choice1_loop = 1
          
          while choice1_loop == 1:
            
            
            print("""options:
            1 - snacks
            2 - drinks
            3 - viand(sudan)
            4 - rice
            5 - return
            
            current price = {}
            6 - remove order (scrapped)
            7 - reserve""".format(price))
          
            try:
                  choice1_1 = int(input("Input choice here: "))
                
            except ValueError:
                  print("That's not a number")
                  continue
                  
            if choice1_1 == 1:
                choice1_a = 1
                if choice1_a == 1:
                    print("""                        1 - Ice Candy (Peanut Avocado) - {0} | {1} stock
                        2 - Ice Candy (Cookies n Cream) - {2} | {3} stock
                        3 - Ice Candy (Mango Graham) - {4} | {5} stock
                        4 - Milkbars - {6} | {7} stock 
                        5 - Cream-O - {8} | {9} stock
                        6 - return""".format(IceCandyPA_price, IceCandyPA_stock, IceCandyCnC_price, IceCandyCnC_stock, IceCandyMG_price,
                                             IceCandyMG_stock, Milkbars_price, Milkbars_stock, CreamO_price, CreamO_stock))
                    try:
                        choice1_b = int(input("Input choice here: "))
                    except ValueError:
                        print("That's not a number")
                        continue
                    if choice1_b >=7:
                        print("That's not a choice")
                        continue    
                        
                    if choice1_b == 1:
                        price = IceCandyPA_price + price
                        IceCandyPA_stock -= 1
                        orders[i].append("Ice Candy (Peanut Avocado)")
                        choice1_a = 0
                        continue
                    
                    if choice1_b == 2:
                        price = IceCandyCnC_price + price
                        IceCandyCnC_stock -= 1
                        orders[i].append("Ice Candy (Cookies n Cream)")
                        choice1_a = 0
                        continue     
                     
                    if choice1_a == 3:
                        price = IceCandyMG_price + price
                        IceCandyMG_stock -= 1
                        orders[i].append("Ice Candy (Mango Graham)")
                        choice1_a = 0
                        continue
                    
                    if choice1_a == 4:
                        price = brice_price + price
                        brice_stock -= 1
                        orders[i].append("Milkbars")
                        choice1_a = 0
                        continue   
                        
                    if choice1_a == 5:
                        price = rice_price + price
                        rice_stock -= 1
                        orders[i].append("Cream-O")
                        choice1_a = 0
                        continue
                    
                    if choice1_a == 6:
                        choice1_a = 0
                        continue   
            
            if choice1_1 == 2:
                choice2_a = 1
                if choice2_a == 1:
                    print("""                        1 - Coke - {0} | {1} stock
                        2 - Iced tea - {2} | {3} stock
                        3 - Sprite - {4} | {5} stock
                        4 - Juice Zesto - {6} | {7} stock 
                        5 - Royal - {8} | {9} stock
                        6 - return""".format(Coke_price, Coke_stock, Icedtea_price, Icedtea_stock, Sprite_price, Sprite_stock,
                                             Zesto_price, Zesto_stock, Royal_price, Royal_stock))
                    try:
                        choice2_b = int(input("Input choice here: "))
                    except ValueError:
                        print("That's not a number")
                        continue
                    if choice2_b >=7:
                        print("That's not a choice")
                        continue    
                        
                    if choice2_b == 1:
                        price = price + Coke_price
                        Coke_stock -= 1
                        orders[i].append("Coke")
                        choice2_a = 0
                        continue
                    
                    if choice2_b == 2:
                        price = price + Icedtea_price
                        Icedtea_stock -= 1
                        orders[i].append("Iced tea")
                        choice2_a = 0
                        continue     
                     
                    if choice2_b == 3:
                        price = price + Sprite_price
                        Sprite_stock -= 1
                        orders[i].append("Sprite")
                        choice2_a = 0
                        continue
                    
                    if choice2_b == 4:
                        price = price + Zesto_price
                        Zesto_stock -= 1
                        orders[i].append("Juice Zesto")
                        choice2_a = 0
                        continue   
                        
                    if choice2_b == 5:
                        price = price + Royal_price
                        Royal_stock -= 1
                        orders[i].append("Royal")
                        choice2_a = 0
                        continue
                    
                    if choice2_b == 6:
                        choice2_a = 0
                        continue
            
            if choice1_1 == 3:
                choice3_a = 1
                if choice3_a == 1:
                    print("""                        1 - Chopsouy - {0} | {1} stock
                        2 - Manok - {2} | {3} stock
                        3 - SaladCucumber - {4} | {5} stock
                        4 - ChickenLiver - {6} | {7} stock 
                        5 - Maranay - {8} | {9} stock
                        6 - return""".format(Chopsouy_price,Chopsouy_stock,Manok_price,Manok_stock,SaladCucumber_price,SaladCucumber_stock,ChickenLiver_price,
                                             ChickenLiver_stock,Maranay_price,Maranay_stock))
                    try:
                        choice3_b = int(input("Input choice here: "))
                    except ValueError:
                        print("That's not a number")
                        continue
                    if choice3_b >=7:
                        print("That's not a choice")
                        continue    
                        
                    if choice3_b == 1:
                        price = price + Chopsouy_price
                        Chopsouy_stock -= 1
                        orders[i].append("Chopsouy")
                        choice3_a = 0
                        continue
                    
                    if choice3_b == 2:
                        price = price + Manok_price
                        Manok_stock -= 1
                        orders[i].append("Manok")
                        choice3_a = 0
                        continue     
                     
                    if choice3_b == 3:
                        price = SaladCucumber_price + price
                        SaladCucumber_stock -= 1
                        orders[i].append("SaladCucumber")
                        choice3_a = 0
                        continue
                    
                    if choice3_b == 4:
                        price = price + ChickenLiver_price
                        ChickenLiver_stock -= 1
                        orders[i].append("ChickenLiver")
                        choice3_a = 0
                        continue   
                        
                    if choice3_b == 5:
                        price = price + Maranay_price
                        Maranay_stock -= 1
                        orders[i].append("Maranay")
                        choice3_b = 0
                        continue
                    
                    if choice3_b == 6:
                        choice3_a = 0
                        continue
                        
            if choice1_1 == 4:
                choice4 = 1
                  
                if choice4 == 1:
                    print("""                        1 - Regular rice - {0} | {1} stock
                        2 - Brown rice - {2} | {3} stock
                        3 - return""".format(rice_price, rice_stock, brice_price, brice_stock))
                        
                    try:
                        choice2_1 = int(input("Input choice here: "))
                    except ValueError:
                        print("That's not a number")
                        continue
                    
                    if choice2_1 >=4:
                        print("That's not a choice")
                        continue
                    
                    if choice2_1 == 1:
                        price = rice_price + price
                        rice_stock -= 1
                        orders[i].append("rice")
                        choice2 = 0
                        continue
                    
                    if choice2_1 == 2:
                        price = brice_price + price
                        brice_stock -= 1
                        orders[i].append(" Brown rice")
                        choice2 = 0
                        continue
                    
                    if choice2_1 == 3:
                        choice4 = 0
                        continue
                        
                        
                  
            if choice1_1 == 5:
                    price = 0
                    choice1_loop = 0
                    print(orders)
                    orders[i].clear()
                    continue
          
            if choice1_1 == 6:
                    print("scrapped")
                    continue
          
            if choice1_1 == 7:
                
                if price == 0:
                    print("you didn't buy anything.")
                    choice1_1 = 0
                    continue
                
                print(orders[i])
                print("It will all cost {} pesos".format(price))
                try:
                    reserve_flag = int(input("nice, nice. Are you sure you ordered everything? (1 - yes, 2 - no): "))
                except ValueError:
                    print("Bruh that's not a number")
                
                
                if reserve_flag == 1:
                  
                    try:   
                        time = int(input("Insert military time you will be getting your reservation: "))
                    except ValueError:
                        print("That's not a number")
                        
                    orders[i].append(time)
                    orders[i].append(input("Please insert your name here: "))    
                    
                    price = 0
                    choice1_loop = 0
                    
                    ++i
                    
                    i = i+1
                    orders.append([i],)
                    
                    continue
                    
                if reserve_flag >= 3:
                    print("Bruh.") 
                    continue
                
                else:
                    print("that's not a number bruh.")
                    continue
            
            
          
            if choice1_1 > 7:
                  print("That's not part of the choices")
                  continue
    
                  
    if choice1 == 2:
        
        for l in range(len(orders)):
            print(orders[l-1])

    if choice1 == 3:
        
        loop = 0
        break