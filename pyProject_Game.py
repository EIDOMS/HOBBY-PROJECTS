from random import randint

###########################################################################################

class Player:
    def __init__(self, hp, shield, strength, dex, intelligence, agi):
        self.hp = hp
        self.shield = shield
        self.str = strength
        self.dex = dex
        self.int = intelligence
        self.agi = agi

    def base_health(self):
        base_hp = (self.hp * 5) + 50
        return round(base_hp,0)

    def base_shield(self):
        base_shield = self.shield * 2
        return round(base_shield,0)

    def base_mana(self):
        base_mana = self.int + 15
        return round(base_mana,0)

    def base_physical_dmg(self):
        physical_dmg = ((self.str + self.dex)/2) + 5
        return round(physical_dmg, 0)

    def base_magical_dmg(self):
        magical_dmg = self.int + 5
        return round(magical_dmg,0)

    def base_speed(self):
        base_spd = self.agi + 10
        return round(base_spd,0)

class Enemy:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def base_health(self):
        base_hp = 100 * self.multiplier
        return round(base_hp,0)

    def base_shield(self):
        base_shield = 50 * self.multiplier
        return round(base_shield,0)

    def base_physical_dmg(self):
        physical_dmg = 5 * self.multiplier
        return round(physical_dmg, 0)

    def base_speed(self):
        base_spd = 25 * self.multiplier
        return round(base_spd,0)

def fire_ball(magical_dmg):
    dmg = 2 + ((25/100) + magical_dmg)
    return round(dmg,0)

def fb_cost(fb_dmg):
    cost = fb_dmg/2
    return round(cost,0)

def water_blast(intelligence):
    dmg = 2 + ((25/100) + intelligence)
    return round(dmg,0)

def wb_cost(wb_dmg):
    cost = wb_dmg/2
    return round(cost,0)

def earth_bullet(strength):
    dmg = 2 + ((25/100) + strength)
    return round(dmg,0)

def eb_cost(eb_dmg):
    cost = eb_dmg/2
    return round(cost,0)

def lightning_burst(dex):
    dmg = 2 + ((25/100) + dex)
    return round(dmg, 0)

def lb_cost(lb_dmg):
    cost = lb_dmg / 2
    return round(cost, 0)

###########################################################################################

# print("[H=H=H=H=H=H=H=H=H=H]")
def health_bar(final_hp, init_hp):
    percent_0 = init_hp * (0/100)
    percent_10 = init_hp * (10/100)
    percent_20 = init_hp * (20/100)
    percent_30 = init_hp * (30/100)
    percent_40 = init_hp * (40/100)
    percent_50 = init_hp * (50/100)
    percent_60 = init_hp * (60/100)
    percent_70 = init_hp * (70/100)
    percent_80 = init_hp * (80/100)
    percent_90 = init_hp * (90/100)
    percent_100 = init_hp * (100/100)

    if final_hp <= percent_0:
        return "[]"

    elif final_hp > percent_0 and final_hp <= percent_10:
        return "[H]"

    elif final_hp > percent_10 and final_hp <= percent_20:
        return "[H=H]"

    elif final_hp > percent_20 and final_hp <= percent_30:
        return "[H=H=H]"

    elif final_hp > percent_30 and final_hp <= percent_40:
        return "[H=H=H=H]"

    elif final_hp > percent_40 and final_hp <= percent_50:
        return "[H=H=H=H=H]"

    elif final_hp > percent_50 and final_hp <= percent_60:
        return "[H=H=H=H=H=H]"

    elif final_hp > percent_60 and final_hp <= percent_70:
        return "[H=H=H=H=H=H=H]"

    elif final_hp > percent_70 and final_hp <= percent_80:
        return "[H=H=H=H=H=H=H=H]"

    elif final_hp > percent_80 and final_hp <= percent_90:
        return "[H=H=H=H=H=H=H=H=H]"

    elif final_hp > percent_90 and final_hp <= percent_100:
        return "[H=H=H=H=H=H=H=H=H=H]"

def generate_rand_num():
    x = randint(0, 100)
    return x

###########################################################################################

def stage_1(health, shield, strength, dexterity, intelligence, agility, p_name, level):
    # - - - - - > Declare Constants
    global_multiplier = 1

    # - - - - - > Declare Classes and other things

    # - - - > Declare Player Variables
    player = Player(health, shield, strength, dexterity, intelligence, agility)

    init_p_hp = player.base_health()
    p_hp = init_p_hp
    p_shield = player.base_shield()
    p_mana = player.base_mana()
    p_physical_dmg = player.base_physical_dmg()
    p_magic_dmg = player.base_magical_dmg()
    p_spd = player.base_speed()

    p_fb = fire_ball(p_magic_dmg)
    p_wb = water_blast(intelligence)
    p_eb = earth_bullet(strength)
    p_lb = lightning_burst(dexterity)

    p_fb_cost = fb_cost(p_fb)
    p_wb_cost = wb_cost(p_wb)
    p_eb_cost = eb_cost(p_eb)
    p_lb_cost = lb_cost(p_lb)

    p_hp_bar = health_bar(p_hp, init_p_hp)

    # - - - > Declare Enemy Variables
    enemy = Enemy(global_multiplier)

    init_e_hp = enemy.base_health()
    e_hp = init_e_hp

    init_e_shield = enemy.base_shield()
    e_shield = init_e_shield

    e_physical_dmg = enemy.base_physical_dmg()
    e_speed = enemy.base_speed()

    e_hp_bar = health_bar(e_hp, init_e_hp)
    e_shield_bar = health_bar(e_shield, init_e_shield)

    p_heal_recharge = p_hp * (10/100)
    p_mana_recharge = p_mana * (10/100)

    ############################################################################################## Stage 1
    while True:
        print("==============================================================")
        print("Enemy: [ SILVER KNIGHT ]")
        print(f"Level: 5")
        print(f"Hp: {e_hp}" + e_hp_bar)
        print(f"Shield: {e_shield}" + e_shield_bar)
        print("--------------------------------------------------")
        print(f"Name: {p_name}")
        print(f"Level: {level}")
        print("--------------------------------------------------")
        print("Action: ")
        print("<1> Attack ")
        print("<2> Rest ")
        print("<3> Meditate ")
        print("<4> Flee ")
        p_action = str(input("Choice: "))
        print("--------------------------------------------------")

        if p_action == "1": # Player Attack
            print("Select Magic Spell: ")
            print(f"<1> FireBall       | MP Cost: {p_fb_cost}")
            print(f"<2> WaterBlast     | MP Cost: {p_wb_cost}")
            print(f"<3> EarthBullet    | MP Cost: {p_eb_cost}")
            print(f"<4> LightningBlast | MP Cost: {p_lb_cost}")
            p_select_spell = str(input("Choice: "))
            print("--------------------------------------------------")


        elif p_action == "2": # Player Rest (Heals Hp)
            print(f"{p_name} heals for ")

        elif p_action == "3": # Player Meditate (Recharge Mana)
            pass

        elif p_action == "4": # Run Away
            pass







    ############################################################################################## - - - - - > Return Value for Leveling
    return True

def stage_2(health, shield, strength, dexterity, intelligence, agility, p_name, level):
    # - - - - - > Declare Constants
    global_multiplier = 2

    # - - - - - > Declare Classes and other things

    # - - - > Declare Player Variables
    player = Player(health, shield, strength, dexterity, intelligence, agility)

    init_p_hp = player.base_health()
    p_hp = init_p_hp
    p_shield = player.base_shield()
    p_mana = player.base_mana()
    p_physical_dmg = player.base_physical_dmg()
    p_magic_dmg = player.base_magical_dmg()
    p_spd = player.base_speed()

    p_fb = fire_ball(p_magic_dmg)
    p_wb = water_blast(intelligence)
    p_eb = earth_bullet(strength)
    p_lb = lightning_burst(dexterity)

    p_fb_cost = fb_cost(p_fb)
    p_wb_cost = wb_cost(p_wb)
    p_eb_cost = eb_cost(p_eb)
    p_lb_cost = lb_cost(p_lb)

    p_hp_bar = health_bar(p_hp, init_p_hp)

    # - - - > Declare Enemy Variables
    enemy = Enemy(global_multiplier)
    init_e_hp = enemy.base_health()
    e_hp = init_e_hp
    e_shield = enemy.base_shield()
    e_physical_dmg = enemy.base_physical_dmg()
    e_speed = enemy.base_speed()

    e_hp_bar = health_bar(e_hp, init_e_hp)

    ############################################################################################## Stage 2







    ############################################################################################## - - - - - > Return Value for Leveling
    return True

def stage_3(health, shield, strength, dexterity, intelligence, agility, p_name, level):
    # - - - - - > Declare Constants
    global_multiplier = 3

    # - - - - - > Declare Classes and other things

    # - - - > Declare Player Variables
    player = Player(health, shield, strength, dexterity, intelligence, agility)

    init_p_hp = player.base_health()
    p_hp = init_p_hp
    p_shield = player.base_shield()
    p_mana = player.base_mana()
    p_physical_dmg = player.base_physical_dmg()
    p_magic_dmg = player.base_magical_dmg()
    p_spd = player.base_speed()

    p_fb = fire_ball(p_magic_dmg)
    p_wb = water_blast(intelligence)
    p_eb = earth_bullet(strength)
    p_lb = lightning_burst(dexterity)

    p_fb_cost = fb_cost(p_fb)
    p_wb_cost = wb_cost(p_wb)
    p_eb_cost = eb_cost(p_eb)
    p_lb_cost = lb_cost(p_lb)

    p_hp_bar = health_bar(p_hp, init_p_hp)

    # - - - > Declare Enemy Variables
    enemy = Enemy(global_multiplier)
    init_e_hp = enemy.base_health()
    e_hp = init_e_hp
    e_shield = enemy.base_shield()
    e_physical_dmg = enemy.base_physical_dmg()
    e_speed = enemy.base_speed()

    e_hp_bar = health_bar(e_hp, init_e_hp)

    ############################################################################################## Stage 3









    ############################################################################################## - - - - - > Return Value for Leveling
    return True

###########################################################################################

def game_env(player_name):
    level = 0
    points = 0
    health = 0
    shield = 0
    strength = 0
    dexterity = 0
    intelligence = 0
    agility = 0

    while True:
        player = Player(health, shield, strength, dexterity, intelligence, agility)

        p_hp = player.base_health()
        p_shield = player.base_shield()
        p_mana = player.base_mana()
        p_physical_dmg = player.base_physical_dmg()
        p_magic_dmg = player.base_magical_dmg()
        p_spd = player.base_speed()

        p_fb = fire_ball(p_magic_dmg)
        p_wb = water_blast(intelligence)
        p_eb = earth_bullet(strength)
        p_lb = lightning_burst(dexterity)

        print("=============================================")
        print("---------------------------------------------")
        print(f"Name: {player_name}")
        print(f"Class: Mage")
        print("Select Action: ")
        print("<1> Enter Dungeon")
        print("<2> Level Up ")
        print("<3> View Stats ")
        action = str(input("Choice: "))
        print("---------------------------------------------")

        if action == "1": #< - - - - - Enter Dungeon
            print("Select Stage: ")
            print("<1> Stage 1 ")
            print("<2> Stage 2 ")
            print("<3> Stage 3 ")
            select_stage = str(input("Choice: "))
            print("---------------------------------------------")
            print("=============================================")
            #stage_1(health, shield, strength, dexterity, intelligence, agility):
            if select_stage == "1":
                if stage_1(health, shield, strength, dexterity, intelligence, agility, player_name, level):
                    print("1 stat Point Gained")
                    points += 1

            elif select_stage == "2":
                if stage_2(health, shield, strength, dexterity, intelligence, agility, player_name, level):
                    print("2 stat Point Gained")
                    points += 2

            elif select_stage == "3":
                if stage_3(health, shield, strength, dexterity, intelligence, agility, player_name, level):
                    print("3 stat Point Gained")
                    points += 3

        elif action == "2": #< - - - - - Level Up
            try:
                print("=============================================")
                print("             [ LEVELING SHEET ]          ")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f"Points: {points}")
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("---------------------------------------------")
                print("Select Stat To Level Up: ")
                print(f"<1> Health: {health}")
                print(f"<2> Shield: {shield} ")
                print(f"<3> Strength: {strength} ")
                print(f"<4> Dexterity: {dexterity}")
                print(f"<5> Intelligence: {intelligence}")
                print(f"<6> Agility: {agility}")
                stat_choice = str(input("Choice: "))
                print("---------------------------------------------")
                print("=============================================")

                if stat_choice == "1":
                    print("Allocate how much Points to <health> ?")
                    allocate = int(input("Points: "))
                    if allocate <= points and not(allocate < 0):
                        health += allocate
                        level += allocate
                        points -= allocate


                    else:
                        print("Not Enough Points")

                elif stat_choice == "2":
                    print("Allocate how much Points to <shield> ?")
                    allocate = int(input("Points: "))
                    if allocate <= points and not (allocate < 0):
                        shield += allocate
                        level += allocate
                        points -= allocate

                    else:
                        print("Not Enough Points")

                elif stat_choice == "3":
                    print("Allocate how much Points to <strength> ?")
                    allocate = int(input("Points: "))
                    if allocate <= points and not (allocate < 0):
                        strength += allocate
                        level += allocate
                        points -= allocate

                    else:
                        print("Not Enough Points")

                elif stat_choice == "4":
                    print("Allocate how much Points to <dexterity> ?")
                    allocate = int(input("Points: "))
                    if allocate <= points and not (allocate < 0):
                        dexterity += allocate
                        level += allocate
                        points -= allocate

                    else:
                        print("Not Enough Points")

                elif stat_choice == "5":
                    print("Allocate how much Points to <intelligence> ?")
                    allocate = int(input("Points: "))
                    if allocate <= points and not (allocate < 0):
                        intelligence += allocate
                        level += allocate
                        points -= allocate

                    else:
                        print("Not Enough Points")

                elif stat_choice == "6":
                    print("Allocate how much Points to <agility> ?")
                    allocate = int(input("Points: "))
                    if allocate <= points and not (allocate < 0):
                        agility += allocate
                        level += allocate
                        points -= allocate

                    else:
                        print("Not Enough Points")

            except:
                print("")
                print("Invalid Input. . .")

        elif action == "3": #< - - - - - View Stats
            print("=============================================")
            print("               [ STAT SHEET ]                ")
            print(f"Name: {player_name}")
            print(f"Level: {level}")
            print(f"Points: {points}")
            print("---------------------------------------------")
            print(f"Health: {p_hp}")
            print(f"Shield: {p_shield}")
            print(f"Mana: {p_mana}")
            print(f"Physical Damage: {p_physical_dmg}")
            print(f"Magic Damage: {p_magic_dmg}")
            print(f"Speed: {p_spd}")
            print("---------------------------------------------")
            print(f"FireBall: {p_fb}")
            print(f"WaterBlast: {p_wb}")
            print(f"LightningBurst: {p_lb}")
            print(f"EarthBullet: {p_eb}")
            print("---------------------------------------------")
            print("=============================================")

def front():
    print("---------------------------------------------")
    print("- - - > ROGUE-LIKE DUNGEON DELVER < - - - ")
    print("---------------------------------------------")
    name_choice = str(input("Input Character Name: "))
    game_env(name_choice)

def main_env():
    while True:
        # - - - > Body
        front()
        # - - - > Enable Loop Termination
        try:
            break_loop = str(input("Terminate Session? <Y/N>: "))
            if break_loop == "Y" or break_loop == "y":
                pass
            elif break_loop == "N" or break_loop == "n":
                pass
        except:
            print("")
            print("Error Found. . .")

main_env()