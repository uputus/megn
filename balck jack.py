import random
shop = {"phone": 1000}
inventory = {}
in_shop = False
balance = 1000
print("Balance: "+str(balance))
print("You are playing blackjack!\nFor Rules type >rules\nTo play type >play.\nTo shop >shop")
while balance > 0:
    action = input(">").lower()

    if action == "rules":
        print("""
    In blackjack you draw cards until 21, or you go bust!
    You must get a better number than your opponent!
    If both go over 21 no one wins!
        """)
    elif action == "play":
        out = False
        opp_chance = random.randint(1,5)
        if opp_chance == 1:
            opp_number = random.randint(16,23)
        elif opp_chance == 2:
            opp_number = random.randint(14, 21)
        elif opp_chance == 3:
            opp_number = random.randint(18, 25)
        elif opp_chance == 4:
            opp_number = random.randint(15,22)
        elif opp_chance == 5:
            opp_number = random.randint(17,24)
        number = 0
        bet = int(input("Your bet? >"))
        while out == False:
            deed = input("Would you like to Draw or Stay? You have: "+str(number)+" >").lower()
            if deed == "draw":
                draw = random.randint(1,10)
                number += draw
                print("You drew "+str(draw)+"!")
                print("You have: "+str(number))
            elif deed == "stay":
                out = True
            if out == True:
                print("Your opponent drew "+str(opp_number))
                print("You drew " + str(number))
                if number > opp_number and number <= 21 or number <= opp_number and opp_number > 21 and number <= 21:
                    balance += bet
                    print("You win! "+"Your balance is now "+str(balance)+"\n >play to play again")
                elif number < opp_number and opp_number <= 21 or number > opp_number and opp_number <= 21 and number > 21:
                    balance -= bet
                    print("You lose! "+"Your balance is now "+str(balance)+"\n >play to play again")
                elif number == opp_number or number > 21 and opp_number > 21:
                    print("Both lose! no money lost!\n >play to play again")
                else:
                    print("Both lose! no money lost!\n >play to play again")

    elif action == "shop":
        in_shop =True
        for i in shop:
            print(i,str(shop[i])+"$")

        while in_shop == True:
            shop_L = input(">").lower()
            for i in shop:
                if shop_L == i:
                    inventory[i] = shop[i]
            if shop_L == "leave":
                in_shop =False




    elif action == "inventory":
        print(inventory)

