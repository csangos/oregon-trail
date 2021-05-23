"""
Functionality based on 1975 HP2000 BASIC Source Code from:
MINNESOTA EDUCATIONAL COMPUTING CONSORTIUM STAFF
PROGRAMMING REVISIONS BY DON RAWITSCH - 1975
DATED - 3/27/75

Python 3.9 version 1.03 James LaPlaine 05/23/2021
"""

import time
import datetime
import random

logo = """
██████████████████████▀████████████████████████████████████████████
█─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄─█▄─▀█▄─▄███─▄─▄─█▄─▄▄▀██▀▄─██▄─▄█▄─▄███
█─██─██─▄─▄██─▄█▀█─██▄─█─██─██─█▄▀─██████─████─▄─▄██─▀─███─███─██▀█
▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀
"""


def print_instructions():
    print("\n\nTHIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM")
    print("INDEPENDENCE, MISSOURI TO OREGON CITY, OREGON IN 1847.")
    print("YOUR FAMILY OF FIVE WILL COVER THE 2000 MILE OREGON TRAIL")
    print("IN 5-6 MONTHS --- IF YOU MAKE IT ALIVE.\n")

    print("YOU HAD SAVED $900 TO SPEND FOR THE TRIP, AND YOU'VE JUST")
    print("   PAID $200 FOR A WAGON.")
    print("YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE")
    print("   FOLLOWING ITEMS:\n")

    print("     OXEN - YOU CAN SPEND $200-$300 ON YOUR TEAM")
    print("            THE MORE YOU SPEND, THE FASTER YOU'LL GO")
    print("               BECAUSE YOU'LL HAVE BETTER ANIMALS\n")

    print("     FOOD - THE MORE YOU HAVE, THE LESS CHANCE THERE")
    print("               IS OF GETTING SICK\n")

    print("     AMMUNITION - $1 BUYS A BELT OF 50 BULLETS")
    print("            YOU WILL NEED BULLETS FOR ATTACKS BY ANIMALS")
    print("               AND BANDITS, AND FOR HUNTING FOOD\n")

    print("     CLOTHING - THIS IS ESPECIALLY IMPORTANT FOR THE COLD")
    print("               WEATHER YOU WILL ENCOUNTER WHEN CROSSING")
    print("               THE MOUNTAINS\n")

    print("     MISCELLANEOUS SUPPLIES - THIS INCLUDES MEDICINE AND")
    print("               OTHER THINGS YOU WILL NEED FOR SICKNESS")
    print("               AND EMERGENCY REPAIRS\n")

    print("YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -")
    print("OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG")
    print("THE WAY WHEN YOU RUN LOW.  HOWEVER, ITEMS COST MORE AT")
    print("THE FORTS.  YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET")
    print("MORE FOOD.")
    print("WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,")
    print("YOU WILL SEE THE WORDS: TYPE BANG.  THE FASTER YOU TYPE")
    print("IN THE WORD 'BANG' AND HIT THE 'RETURN' KEY, THE BETTER")
    print("LUCK YOU'LL HAVE WITH YOUR GUN.\n")

    print("WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A '$'.\n")
    print("GOOD LUCK!!!\n")


def get_spend(spend_min, spend_max, question):
    spend = int(input(question))
    if spend < spend_min:
        print("NOT ENOUGH")
        spend = get_spend(spend_min, spend_max, question)
    if spend_max != 0 and spend > spend_max:
        print("TOO MUCH")
        spend = get_spend(spend_min, spend_max, question)
    return spend


def end_game(message):
    print(message)
    print("\nDO TO YOUR UNFORTUNATE SITUATION, THERE ARE A FEW")
    print("FORMALITIES WE MUST GO THROUGH\n")
    input("WOULD YOU LIKE A MINISTER? ")
    input("WOULD YOU LIKE A FANCY FUNERAL? ")
    answer = input("WOULD YOU LIKE US TO INFORM YOUR NEXT OF KIN? ").lower()
    if answer == "n" or answer=="no":
        print("YOUR AUNT NELLIE IN ST. LOUIS IS ANXIOUS TO HEAR")
    print("\nWE THANK YOU FOR THIS INFORMATION AND WE ARE SORRY YOU")
    print("DIDN'T MAKE IT TO THE GREAT TERRITORY OF OREGON")
    print("BETTER LUCK NEXT TIME\n\n")
    print("\t\t\tSINCERELY")
    print("\t\t\tTHE OREGON CITY CHAMBER OF COMMERCE")
    exit()


def hunt():
    start_hunt = time.time()
    entry = input("\nTYPE BANG: ")
    stop_hunt = time.time()
    if entry == "BANG" or "bang":
        return int(stop_hunt - start_hunt)
    else:
        return 7


def get_illness():
    global mileage
    global supplies
    global illness
    global south_pass_mileage
    if random.randint(0, 100) < 10 + 35 * (eating - 1):
        print("MILD ILLNESS---MEDICINE USED")
        mileage -= 5
        supplies -= 2
    elif random.randint(0, 100) < 100 - (40 / 4 ** (eating - 1)):
        print("BAD ILLNESS---MEDICINE USED")
        mileage -= 5
        supplies -= 5
    else:
        print("SERIOUS ILLNESS---")
        print("YOU MUST STOP FOR MEDICAL ATTENTION")
        supplies -= 10
        illness = True
    if supplies < 0:
        if injury:
            msg = "INJURIES"
        else:
            msg = "PNEUMONIA"
        print("YOU RAN OUT OF MEDICAL SUPPLIES")
        end_game(f"YOU DIED OF {msg}")
    if blizzard:
        if mileage <= 950:
            south_pass_mileage = True


print(logo)

instructions = input("\nDO YOU NEED INSTRUCTIONS  (YES/NO): ")
if instructions[0].lower() == "y":
    print_instructions()

# Initialize vars
dates = [
    "MARCH 29", "APRIL 12", "APRIL 26", "MAY 10", "MAY 24", "JUNE 7", "JUNE 21", "JULY 5", "JULY 19",
    "AUGUST 2", "AUGUST 16", "AUGUST 31", "SEPTEMBER 13", "SEPTEMBER 27", "OCTOBER 11",
    "OCTOBER 25", "NOVEMBER 8", "NOVEMBER 22"
]
event_data = [6, 11, 13, 15, 17, 22, 32, 35, 37, 42, 44, 54, 64, 69, 95, 100]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
fort_flag = -1
injury = False
illness = False
south_pass = False
blue_mountains = False
mileage = 0
mileage_prev = 0
south_pass_mileage = False
turn_number = -1
ammunition = 0
blizzard = False
insufficient_clothing = False
event_counter = event_random = 0
exit_mountains = False

while True:
    animals = get_spend(200,300,"HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM: ")
    food = get_spend(1,0,"HOW MUCH DO YOU WANT TO SPEND ON FOOD: ")
    ammunition = get_spend(1, 0, "HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION: ")
    clothing = get_spend(1, 0, "HOW MUCH DO YOU WANT TO SPEND ON CLOTHING: ")
    supplies = get_spend(1, 0, "HOW MUCH DO YOU WANT TO SPEND ON MISCELLANEOUS SUPPLIES :")
    cash = 700 - animals - food - ammunition - clothing - supplies
    if cash < 0:
        print("YOU OVERSPENT--YOU ONLY HAD $700 TO SPEND.  BUY AGAIN\n")
    else:
        break

ammunition *= 50 # Multiple by 50 to get bullet count

print(f"\nAFTER ALL YOUR PURCHASES, YOU NOW HAVE {cash} DOLLARS LEFT\n")

# Start of the turn
while mileage < 2040 and turn_number <= 17:
    turn_number += 1
    print("\n--------------------")
    print(f"MONDAY {dates[turn_number]} 1847")
    # Debug stat line
    # print(f"[T:{turn_number+1} EC:{event_counter} ER:{event_random}]")
    if food < 12:
        print("YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!")
    mileage_prev = mileage
    if illness or injury:
        print("DOCTOR'S BILL IS $20")
        cash -= 20
        injury = illness = False
        if cash < 0:
            cash = 0
            print("YOU CAN'T AFFORD A DOCTOR")
            if injury:
                msg = "YOU DIED OF INJURIES"
            else:
                msg = "YOU DIED OF PNEUMONIA"
            end_game(msg)
    if south_pass_mileage:
        print(f"TOTAL MILEAGE IS 950")
        south_pass_mileage = False
    else:
        print(f"TOTAL MILEAGE IS {mileage}")
    print("FOOD, BULLETS, CLOTHING, SUPPLIES, CASH")
    print(f"{food:=5} {ammunition:=8} {clothing:=9} {supplies:=9} {cash:=4}")

    # Check to see if this turn has a fort option
    if fort_flag == -1:
        prompt = "\nDO YOU WANT TO (1) HUNT, OR (2) CONTINUE: "
    else:
        prompt = "\nDO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT, OR (3) CONTINUE: "
    action = int(input(prompt))
    # If there is NO fort option, add 1 to the action number entered
    if action == 1 and fort_flag == -1:
        action = 2
    elif fort_flag == -1:
        action = 3
    fort_flag *= -1

    if action == 1:  # Visit a fort
        print("ENTER WHAT YOU WANT TO SPEND ON THE FOLLOWING")
        food_spend = get_spend(0, cash, "FOOD: ")
        food = food + int(2 / 3 * food_spend)
        cash -= food_spend

        ammunition_spend = get_spend(0, cash, "AMMUNITION: ")
        ammunition = ammunition + int(2 / 3 * ammunition_spend * 50)
        cash -= ammunition_spend

        clothing_spend = get_spend(0, cash, "CLOTHING: ")
        clothing = clothing + int(2 / 3 * clothing_spend)
        cash -= clothing_spend

        supplies_spend = get_spend(0, cash, "MISCELLANEOUS SUPPLIES: ")
        supplies = supplies + int(2 / 3 * supplies_spend)
        cash -= supplies_spend

    elif action == 2:  # Hunt
        if ammunition > 39:
            mileage -= 45
            reaction_time = hunt()
            if reaction_time <= 1:
                print("RIGHT BETWEEN THE EYES---YOU GOT A BIG ONE!!!!")
                food += (52 + random.randint(0, 6))
                ammunition -= (10 + random.randint(0, 4))
            elif random.randint(0, 100) < 13 * reaction_time:
                print("SORRY NO LUCK TODAY")
            else:
                print("NICE SHOT--RIGHT THROUGH THE NECK--FEAST TONIGHT!!")
                food += (48 - 2 * reaction_time)
                ammunition += (-10 - 3 * reaction_time)
        else:
            print("TOUGH---YOU NEED MORE BULLETS TO GO HUNTING")

    if food < 13:
        end_game("YOU RAN OUT OF FOOD AND STARVED TO DEATH")

    # Eating
    eating = 0
    while eating == 0:
        eating = int(input("DO YOU WANT TO EAT (1) POORLY  (2) MODERATELY OR (3) WELL: "))
        if eating > 3 or eating < 1:
            eating = 0
        if food - 8 - 5 * eating < 0:
            print("YOU CAN'T EAT THAT WELL")
            eating = 0
        food = food - 8 - 5 * eating
        mileage += 200 + (animals - 220) / 5 + random.randint(0, 10)

    blizzard = insufficient_clothing = False

    # Raider event
    if random.randint(0, 10) <= ((mileage/100-4)**2+72)/((mileage/100-4)**2+12)-1:
        raiders_friendly = 0
        if random.random() <= 0.2:
            msg = "DON'T "
            raiders_friendly = 1
        else:
            msg = ""
        tactics = 0
        while tactics == 0:
            print(f"\nRIDERS AHEAD.  THEY {msg}LOOK HOSTILE")
            print("TACTICS")
            print("(1) RUN  (2) ATTACK  (3) CONTINUE  (4) CIRCLE WAGONS")
            print("IF YOU RUN YOU'LL GAIN TIME BUT WEAR DOWN YOUR OXEN")
            print("IF YOU CIRCLE YOU'LL LOSE TIME")
            tactics = int(input("CHOICE: "))
            if tactics < 1 or tactics > 4:
                tactics = 0
        if random.random() <= 0.2:
            raiders_friendly = 1 - raiders_friendly
        if raiders_friendly:
            print("RAIDERS WERE FRIENDLY, BUT CHECK FOR POSSIBLE LOSSES")
            if tactics == 1:
                mileage += 15
                animals -= 10
            elif tactics == 2:
                mileage -= 5
                ammunition -= 100
            # If tactic is continue, there is nothing to do
            elif tactics == 4:
                mileage -= 20
        else: # raiders are not friendly
            print("RAIDERS WERE HOSTILE--CHECK FOR LOSSES")
            if tactics == 1:
                mileage += 20
                supplies -= 15
                ammunition -= 150
                animals -= 40
            elif tactics == 3:
                if random.random() <=0.2:
                    print("THEY DID NOT ATTACK")
                else:
                    ammunition -= 150
                    supplies -= 15
            elif tactics == 4:
                mileage -= 25
            # If attacking or circling wagons, we have a shoot out to resolve
            if tactics == 2 or tactics == 4:
                reaction_time = hunt()
                if tactics == 2:
                    bullet_factor = 40
                else:
                    bullet_factor = 30
                ammunition = ammunition - reaction_time * bullet_factor - 80
                if reaction_time <= 1:
                    print("NICE SHOOTING---YOU DROVE THEM OFF")
                elif reaction_time <= 4:
                    print("KINDA SLOW WITH YOUR COLT .45")
                else:
                    print("LOUSY SHOT---YOU GOT KNIFED")
                    print("YOU HAVE TO SEE OL' DOC BLANCHARD")
                    injury = True
            if ammunition<0:
                end_game("YOU RAN OUT OF BULLETS AND GOT MASSACRED BY THE RIDERS")

    # Random events
    event_counter = 1
    minutes = datetime.datetime.now().minute
    event_random = random.randint(minutes, 100)
    while event_random > event_data[event_counter-1] and event_counter <= 16:
        event_counter += 1
    if event_counter == 1:
        print("WAGON BREAKS DOWN--LOSE TIME AND SUPPLIES FIXING IT")
        mileage -= random.randint(15, 20)
        supplies -= 8
    elif event_counter == 2:
        print("OX INJURES LEG---SLOWS YOU DOWN REST OF TRIP")
        mileage -= 25
        animals -= 20
    elif event_counter == 3:
        print("BAD LUCK---YOUR DAUGHTER BROKE HER ARM")
        print("YOU HAD TO STOP AND USE SUPPLIES TO MAKE A SLING")
        mileage -= random.randint(5, 9)
        supplies -= random.randint(2, 5)
    elif event_counter == 4:
        print("OX WANDERS OFF---SPEND TIME LOOKING FOR IT")
        mileage -= 17
    elif event_counter == 5:
        print("YOUR SON GETS LOST---SPEND HALF THE DAY LOOKING FOR HIM")
        mileage -= 10
    elif event_counter == 6:
        print("UNSAFE WATER--LOSE TIME LOOKING FOR CLEAN SPRING")
        mileage -= random.randint(2, 12)
    elif event_counter == 7:
        if mileage <= 950:
            print("HEAVY RAINS---TIME AND SUPPLIES LOST")
            food -= 10
            ammunition -= 500
            supplies -= 15
            mileage -= random.randint(5, 15)
        else:
            if clothing <= 22+random.randint(0, 4):
                msg = "DON'T "
                insufficient_clothing = True
            else:
                msg =""
            print(f"COLD WEATHER---BRRRRRRR!---YOU {msg}HAVE ENOUGH CLOTHING TO KEEP YOU WARM")
            if insufficient_clothing:
                get_illness()
    elif event_counter == 8:
        print("BANDITS ATTACK")
        reaction_time = hunt()
        ammunition -= 20*reaction_time
        if ammunition < 0:
            print("YOU RAN OUT OF BULLETS---THEY GOT LOTS OF CASH")
            cash /= 3
        if reaction_time > 1:
            print("YOU GOT SHOT IN THE LEG AND THEY TOOK ONE OF YOUR OXEN")
            injury = True
            print("BETTER HAVE A DOC LOOK AT YOUR WOUND")
            supplies -= 5
            animals -= 20
        else:
            print("QUICKEST DRAW OUTSIDE OF DODGE CITY!!!")
            print ("YOU GOT 'EM!")
    elif event_counter == 9:
        print("THERE WAS A FIRE IN YOUR WAGON--FOOD AND SUPPLIES DAMAGED")
        food -= 40
        ammunition -= 400
        supplies -= random.randint(3, 11)
        mileage -= 15
    elif event_counter == 10:
        print("LOSE YOUR WAY IN HEAVY FOG---TIME IS LOST")
        mileage -= random.randint(5, 15)
    elif event_counter == 11:
        print("YOU KILLED A POISONOUS SNAKE AFTER IT BIT YOU")
        ammunition -= 10
        supplies -= 5
        if supplies < 0:
            end_game("YOU DIE OF SNAKEBITE SINCE YOU HAVE NO MEDICINE")
    elif event_counter == 12:
        print("WAGON GETS SWAMPED FORDING RIVER--LOSE FOOD AND CLOTHES")
        food -= 30
        clothing -= 20
        mileage -= random.randint(20, 40)
    elif event_counter == 13:
        print("WILD ANIMALS ATTACK!")
        reaction_time = hunt()
        if ammunition <= 39:
            print("YOU WERE TOO LOW ON BULLETS--")
            print("THE WOLVES OVERPOWERED YOU")
            injury = True
            end_game("YOU DIED OF INJURIES")
        else:
            if reaction_time <= 2:
                print("NICE SHOOTIN' PARDNER---THEY DIDN'T GET MUCH")
            else:
                print("SLOW ON THE DRAW---THEY GOT AT YOUR FOOD AND CLOTHES")
            ammunition -= 20*reaction_time
            clothing -= 4*reaction_time
            food -= 8*reaction_time
    elif event_counter == 14:
        print("HAIL STORM---SUPPLIES DAMAGED")
        mileage -= random.randint(5, 15)
        ammunition -= 200
        supplies -= random.randint(4, 7)
    elif event_counter == 15:
        if eating == 1:
            get_illness()
        elif eating == 2:
            if random.random() > 0.25:
                get_illness()
        else:
            if random.random() < 0.5:
                get_illness()
    elif event_counter == 16:
        print("HELPFUL NATIVE AMERICANS SHOW YOU WHERE TO FIND MORE FOOD")
        food += 14

    # The Mountains
    if mileage > 950:
        if random.randint(0, 10) <= 9 - ((mileage / 100 - 15) ** 2 + 72) / ((mileage / 100 - 15) ** 2 + 12):
            print ("RUGGED MOUNTAINS")
            if random.random()<=0.1:
                print("YOU GOT LOST---LOSE VALUABLE TIME TRYING TO FIND TRAIL!")
                mileage -= 60
                # 3175
            else:
                if random.random() <= 0.11:
                    print("WAGON DAMAGED!---LOST TIME AND SUPPLIES")
                    supplies -= 5
                    ammunition -= 200
                    mileage -= random.randint(20, 50)
                else:
                    print("THE GOING GETS SLOW")
                    mileage = int(mileage - 45 - random.random()/0.02)

        if not south_pass:
            south_pass = True
            if random.random() >= 0.8:
                print("YOU MADE IT SAFELY THROUGH SOUTH PASS--NO SNOW")
            else:
                print("BLIZZARD IN MOUNTAIN PASS--TIME AND SUPPLIES LOST")
                blizzard = True
                food -= 25
                supplies -= 10
                ammunition -= 300
                mileage -= random.randint(30, 70)
                if clothing < random.randint(2, 20):
                    get_illness()
                if mileage <= 950:
                    south_pass_mileage = True
                exit_mountains = True
        if mileage < 1700 and not exit_mountains:
            if mileage <= 950:
                south_pass_mileage = True
        elif not exit_mountains:
            if blue_mountains:
                if mileage <= 950:
                    south_pass_mileage = True
            else:
                blue_mountains = True
                if random.random() >= 0.7:
                    if mileage <= 950:
                        south_pass_mileage = True
                else:
                    print("BLIZZARD IN MOUNTAIN PASS--TIME AND SUPPLIES LOST")
                    blizzard = True
                    food -= 25
                    supplies -= 10
                    ammunition -= 300
                    mileage -= random.randint(30, 70)
                    if clothing < random.randint(2, 20):
                        get_illness()
                    if mileage <= 950:
                        south_pass_mileage = True

# Final turn
turn_number += 1
final_turn_fraction = (2040-mileage_prev)/(mileage-mileage_prev)
food += int((1-final_turn_fraction)*(8+5*eating))

print("\n--------------------")
print("\nYOU FINALLY ARRIVED AT OREGON CITY")
print("AFTER 2040 LONG MILES---HOORAY!!!!!\n")

final_turn_fraction = int(final_turn_fraction*14)
turn_number = turn_number * 14 + final_turn_fraction
final_turn_fraction += 1
print(days_of_week[final_turn_fraction%7])

day = turn_number
if turn_number > 216:
    day = turn_number - 216
    print(f"NOVEMBER {day} 1847")
elif turn_number > 185:
    day = turn_number - 185
    print(f"OCTOBER {day} 1847")
elif turn_number > 155:
    day = turn_number - 155
    print(f"SEPTEMBER {day} 1847")
elif turn_number > 124:
    day = turn_number - 124
    print(f"AUGUST {day} 1847")
else:
    day = turn_number - 93
    print(f"JULY {day} 1847")

print("FOOD, BULLETS, CLOTHING, SUPPLIES, CASH")
print(f"{food:=5} {ammunition:=8} {clothing:=9} {supplies:=9} {cash:=4}\n")

print("PRESIDENT JAMES K. POLK SENDS YOU HIS HEARTIEST CONGRATULATIONS")
print("AND WISHES YOU A PROSPEROUS LIFE AHEAD")
print("AT YOUR NEW HOME")
