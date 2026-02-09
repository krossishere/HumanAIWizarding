import time
import sys
import random
spells = []
aispells = []
print("""
-----Primary Spells-----
1. Fire Ball
2. Ice Chill
3. Electro Spark
-----Secondary Spells-----
1. Giant Snowball (Does NOT work well with Fireball.) (Works well with Ice Chill.)
2. Water splash (Works well with electro spark)(Works well with Ice Chill.)
3. Bolder Rain (Does NOT work well with Fireball and Electro Spark.)
---Finisher Spells---
1. All out Voltage
2. Dark Uranium
3. Elephants Foot""")
print("WARNING: TYPE THE SPELLS EXACTLY HOW THE ARE LISTED.")
spell1h = input("Choose you primary spell: ")
if spell1h == "Fire Ball":
    print("Chose the Fireball!")
    spells.append("Fire Ball")
elif spell1h == "Ice Chill":
    print("Chose Ice Chill!")
    spells.append("Ice Chill")
elif spell1h == "Electro Spark":
    print("Chose Electro Spark!")
    spells.append("Electro Spark")
else:
    print("Invalid spell choice!")
    time.sleep(1)
print("Now for the secondary spells!")
spell2h = input("Choose your secondary spell: ")
if spell2h== "Giant Snowball":
    print("Chose Giant Snowball!")
    spells.append("Giant Snowball")
elif spell2h== "Water Splash":
    print("Chose the Water Splash!")
    spells.append("Water Splash")
elif spell2h== "Bolder Rain":
    print("Chose Bolder Rain!")
    spells.append("Bolder Rain")
else:
    print("Invalid spell choice!")
    time.sleep(1)

# ^ Incase you didn't see, thats the spell choosing for Primary and Secondary.
print("Now your finisher move!")
spell3h=input("Choose your finishing spell: ")
if spell3h=="All Out Voltage":
    print("Chose all out voltage!")
    spells.append("All Out Voltage")
elif spell3h=="Dark Uranium":
    print("Chose Dark Uranium!")
    spells.append("Dark Uranium")
elif spell3h=="Elephants Foot":
    print("Chose Elephants Foot!")
    spells.append("Elephants Foot")
else:
    print("Invalid spell choice!")
    time.sleep(1)
print(spells)
print("The AI is choosing it's primary spell...")
if spell1h=="Fire Ball":
    aispells.append("Electro Spark")
elif spell1h=="Ice Chill":
    aispells.append("Fire Ball")
elif spell1h=="Electro Spark":
    aispells.append("Fire Ball")
else:
    print("AI could not find a Primary Spell. Ending Game Now...")
    sys.exit
print("AI is choosing it's secondary spell...")
if spell2h=="Giant Snowball":
    aispells.append("Bolder Rain")
elif spell2h=="Water Splash":
    aispells.append("Giant Snowball")
elif spell2h=="Bolder Rain":
    aispells.append("Water Splash")
else:
    print("AI could not find a Secondary Spell. Ending Game Now...")
    sys.exit
print("AI is choosing a finisher...")
aispells.append("Elephants Foot")
# ^ AI will always choose this unless it is changed. If you get finished by the AI just pack it up yo ✌️
print(aispells)
# Starting after this is the battle stuff. SP (Spell Points) will increase by 1 every turn, unless an effect is applied.
# Primary Spells cost 2 SP. Secondary Costs 1 SP. Finisher move is 5 SP and can be used when the enemy is < 10 health.
#-----Primary Spells-----
# 1. Fire Ball
# 2. Ice Chill
# 3. Electro Spark
# -----Secondary Spells-----
# 1. Giant Snowball (Does NOT work well with Fireball.) (Works well with Ice Chill.)
# 2. Water splash (Works well with electro spark)(Works well with Ice Chill.)
# 3. Bolder Rain (Does NOT work well with Fireball and Electro Spark.)
# ---Finisher Spells---
# 1. All out Voltage
# 2. Dark Uranium
# 3. Elephants Foot
aiactions = ["Primary", "Secondary"]
def aiinput(aiactions):
    return random.choice(aiactions)
fire_ball_dmg = 15
fire_ball_effect = "Burning"
ice_chill_dmg = 9
ice_chill_effect = "Freezing"
elec_spark_dmg = 10
elec_spark_effect = "Shocked"
giant_snowball_dmg = 8
giant_snowball_effect = "Slowed"
water_splash_dmg = 7
water_splash_effect = "Wet"
bolder_rain_dmg = 12
bolder_rain_effect = "Stunned"
all_out_voltage_dmg = 20
all_out_voltage_effect = "Paralyzed"
dark_uranium_dmg = 25
dark_uranium_effect = "Poisoned"
elephants_foot_dmg = 30
elephants_foot_effect = "Obliterated"
humanhp = 100
aihp = 100
humanstartsp = 5
aistartsp = 5
spgainperturn = random.randint(2, 4)
turn = 0
curaiinput = aiinput
# curhumaneffects = []
# curaieffects = []
# ^ Later Update, I can't figure this out.
curinput = ""
def hturnprompt():
    global humanstartsp, aihp, turn
    print("The turn is "+str(turn))
    print("Current SP (Spell Points) amount: "+str(humanstartsp))
    print("Current SP gain: " +str(spgainperturn))
    print("Current Health: " +str(humanhp))
    print("Current AI heath: " +str(aihp))
    curinput = input ("Primary spell or secondary spell? ")
    if curinput in ["Primary", "Primary Spell"]:
        humanstartsp -= 2
        humanstartsp += spgainperturn
        turn + 1
        
        if "Fire Ball" in spells:
            aihp -= fire_ball_dmg
            print("Dealt 15 damage to the Enemy using fireball!")
            # Convert to string to avoid a TypeError
            print("Current SP now: " + str(humanstartsp))
        elif "Ice Chill" in spells:
            aihp -= ice_chill_dmg
            print("Dealt 9 Damage to Enemy using Ice Chill!")
            # Convert to string to avoid a TypeError
            print("Current SP now: " + str(humanstartsp))
        elif "Electro Spark" in spells:
            aihp -= elec_spark_dmg
            print("Dealt 10 damage to Enemy using Electro Spark!")
        else:
            print("Error Occured.")
            print("Ending game now...")
            sys.exit
    if curinput in ["Secondary", "Secondary Spell", "Secondary Spells"]:
        humanstartsp -= 1
        if  "Giant Snowball" in spells:
            aihp -= giant_snowball_dmg
            print("Dealt 8 damage to Enemy with Giant Snowball!")
        elif "Water Splash" in spells:
            aihp -= water_splash_dmg
            print("Dealt"+str(water_splash_dmg)+" damage to Enemy with Water Splash!")
        elif "Bolder Rain" in spells:
            aihp -= bolder_rain_dmg
            print("Dealt"+str(bolder_rain_dmg)+"damage to Enemy with Bolder Rain!")
        else:
            print("Error occured.")
            print('Ending game now...')
            sys.exit
    return aihp

def aiturn():
    global humanhp
    print("AI is taking it's turn...")
    if curaiinput in ["Primary", "Primary Spell"]:
        aistartsp -= 2
        aistartsp += spgainperturn
        
        if "Fire Ball" in aispells:
            humanhp -= fire_ball_dmg
            # Convert to string to avoid a TypeError
        elif "Ice Chill" in aispells:
            humanhp -= ice_chill_dmg
        elif "Electro Spark" in aispells:
            humanhp -= elec_spark_dmg
        else:
            print("Error Occured.")
            print("Ending game now...")
            sys.exit
    if curaiinput in ["Secondary", "Secondary Spell", "Secondary Spells"]:
        aistartsp -= 1
        if  "Giant Snowball" in aispells:
            humanhp -= giant_snowball_dmg
        elif "Water Splash" in aispells:
            humanhp -= water_splash_dmg
        elif "Bolder Rain" in aispells:
            humanhp -= bolder_rain_dmg
        else:
            print("Error occured.")
            print('Ending game now...')
            sys.exit
    return humanhp

def run_battle():
    global aihp, humanhp
    
    # Repeat until either hp = 0
    while aihp > 0 and humanhp > 0:
        # Call human turn, wait for it to finish (happens sequentially)
        aihp = hturnprompt()
        
        # Check condition immediately after first action
        if aihp <= 0:
            print("AI defeated! Human wins.")
            break
            
        # Call AI turn, wait for it to finish
        humanhp = aiturn()
        
        # Check condition immediately after second action
        if humanhp <= 0:
            print("Human defeated! AI wins.")
            break

        if humanstartsp <= 0:
            print("Human lost....")
            break
        
        if aistartsp <0:
            print("Human won!!")
            break
            
        print("-" * 20) # Divider for turns

# Start Game
run_battle()

"""
TO-DO:
Add effects for every spell
Add More Primary Spells and Secondary Spells
Fix the problem that may be happening with the SP gain. (Done)
Implement the finisher spells (It's easy, I'm just toooooooo lazy).
Publish on GitHub (Done)
Turn it into RPG???

"""
            
