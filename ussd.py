user = input("Dial your code: ")
if user == "*777#":
    print("please wait...")
else:
    print("invalid ussd code")


code1 = ["1. Register NIN", "2. Data", "3. E-Top Up", "4. Berekete ++"]
[print(x) for x in code1]
#
#
com = int(input("kindly select any option above: "))
# data section
if com == 2:
    code3 = ["1.Buy Data Plan", "2.Gift Data Plan", "3.Share Data Plan", "4.Check Data balance",
             "5.Manage Data Plan", "6.Blackberry", "7.GLOTV Data Plan", "8.Back", "9. Exist"]
    [print(x) for x in code3]
    cat = int(input("Select an option above: "))
    if cat == 1:
      code4 = ["1. Proceed (Auto-Renew)", "2. Proceed (One-Off)", "0. Back"]
      [print(x) for x in code4]

    wolf = int(input("Please select: "))
    if wolf == 1:
        code5 = ["1. Mini Plans", "2. Monthly Plan", "3. Mega Plans", "4. Super Mega Plans", "5. Special Data Offer", "6. Social Bundles", "7. Night and Weekend plans", "8. Back", "0. Exit"]
        [print(x) for x in code5]

        dot = int(input("Select please: "))
        if dot == 1:
            code6 = ["1.N100=150MB 1 Day incl 35mb nite", "2.N200=350MB 2 Days incl 110Mb", "3.N500=1.8GB 14 Days incl 1GB nite", "4.N50=50MB 1 Day incl 5Mb nite", "5.More plans", "6.Back"]
            [print(x) for x in code6]

            jab = int(input("Select please any option from above: "))
            if jab == 1:
                print("SORRY!Insufficient credit balance for the plan you want to buy.Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *321#")
            if jab == 2:
                print(
                    "SORRY!Insufficient credit balance for the plan you want to buy.Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *321#")
            if jab == 3:
                print(
                    "SORRY!Insufficient credit balance for the plan you want to buy.Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *321#")
            if jab == 4:
                print(
                    "SORRY!Insufficient credit balance for the plan you want to buy.Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *321#")
            if jab == 5:
                code7 = ["1.N1000=3.9GB 30Days inc2 1GB nite", "2.N1500=7.5GB 30Days incl 4GB nite", "3.N2000=9.2GB 30Days incl 4GB nite", "4.N2500=10.8GB 30Days incl 1GB nite", "5.More Plans", "6.Back"]
                [print(x) for x in code7]

                cross = int(input("Select an option: "))
                if cross == 1:
                    print(
                        "SORRY!Insufficient credit balance for the plan you want to buy.Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *321#")
                if cross == 2:
                    print(
                        "SORRY!Insufficient credit balance for the plan you want to buy.Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *321#")

                if cross == 3:
                    print(
                        "SORRY!Insufficient credit balance for the plan you want to buy.Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *321#")
                if cross == 4:
                    print(
                        "SORRY!Insufficient credit balance for the plan you want to buy.Please recharge your line or you can simply Borrow Data. To Borrow Data now, just dial *321#")
                if cross == 5:
                    code8 = ["1.N3000=14GB 30Days inc2 4GB nite", "2.N4000=18GB 30Days incl 4GB nite",
                             "3.N5000=24GB 30Days incl 4GB nite", "4.N8000=29.5GB 30Days incl 2GB nite",
                             "5.More Plans", "6.Back"]
                    [print(x) for x in code8]

# E-top section
if com == 3:
    print("Welcome to Glo e-Services "
          "Please select an option")
    code9 = ["1.Airtime", "2.Data", "0.Exit"]
    [print(x) for x in code9]

    uba = int(input("Please select type of Airtime: "))

    if uba == 1:
        code10 = ["1.5X Recharges", "2.Regular Recharges", "00.Back"]
        [print(x) for x in code10]

        unn = int(input("Airtime Purchase: "))
        if unn == 1:
            code11 = ["1. Self", "2.Third party", "00.Back"]
            [print(x) for x in code11]


            pat = int(input("Select 5X amount: "))
            if pat == 1:
                code12 = ["1.N120", "2.N220", "3.N320", "4.N420", "5.520", "6.N620", "7.N720", "8.more", "9.Back"]
                [print(x) for x in code12]

                dev = int(input("Pay from: "))
                if dev == 1:
                    code13 = ["1.Banks", "2.Card", "0.Exit"]
                    [print(x) for x in code13]

                    don = int(input("Please wait, your request has been sent for processing: "))
                    if don == 1:
                        code14 = ["1.ACCESS", "2.STERLING", "3.PROVIDUS", "4.JAIZ", "5.FCMB", "6.TAJ", "7.UNITY"]
                        [print(x) for x in code14]

                        acct = input("Enter your new ACCESS 10-digit Account Number: ")
                        if len(acct) == 10:
                            print("This mobile number is NOT tied to your bank account! Please contact your bank for assistance. Thank you.")
                        else:
                            print("Try again later!!!")

    if uba == 2:
        code16 = ["1.Self", "2.Third party", "00.Back"]
        [print(x) for x in code16]

        ict = int(input("Data Plan Purchase: "))
        if ict == 1:
            code17 = ["1.N100=105MB 1Day incl 15MB nite", "2.N200=350MB 2Days incl 110Mb nite", "3.n500=1.05GB 14Days incl 250MB nite", "4.N1000=2.5GB", "# Next"]
            [print(x) for x in code17]

            icp = int(input("Oga sim additional bonus: "))
            if icp == 1:
                code18 = ["1.Banks", "2.Card", "0.Exit"]
                [print(x) for x in code18]


        # unn = int(input("pls select"))
        #
        # if unn == 2:
        #     code19 = ["1.N100=105MB 1day incl 15MB nite", "2.N200=350MB 2Days incl 110MB nite", "3.N500=1.05GB 14Days 14Days incl 250MB nite", "4.N1000=2.5GB", "# Next"]
        #     [print(x) for x in code19]


#berekete

if com == 4:
    print("Enjoy 700% bonus to call all networks + Free Data on every recharge")
    code19 = ["1.Migrate Now", "2.Back", "3.Exit"]
    [print(x) for x in code19]

    dip = int(input("Select: "))
    if dip == 1:
        print("xxx")



# NIN Registration
if com == 1:
    code2 = ["1. Enter NIN", "2. Check NIN status", "0. Cancel"]
    [print(x) for x in code2]
    
usa = int(input("kindly select any option above: "))

if usa == 2:
    print("Dear subscriber you have already submitted your NIN")
if usa == 0:
    print("Thank you for using the service")

if usa == 1:
    print("Enter your 11 digit code")
usa = input()
if len(usa) == 11:
    print("Successful!!!")
else:
    print("Invalid")
































































