import random

global ai_spawned
global AM
player_hp = 1000
ab_set = input("magic or ability")
ab_set = ab_set.strip().lower()
if ab_set == "magic":
    AM = "Magic"
elif ab_set == "ability":
    AM = "Ability"
num_spawned_monsters = [1, 2, 3, 4, 5]
random.shuffle(num_spawned_monsters)
if num_spawned_monsters[0] == 1:
    ai_type = ["boss"]  # will create variety later
elif num_spawned_monsters[0] == 2:
    ai_type = ["brothers"]  # will create variety later
elif num_spawned_monsters[0] == 3:
    ai_type = ["triplets"]  # will create variety later
elif num_spawned_monsters[0] == 4:
    ai_type = ["troggies"]  # will create variety later
elif num_spawned_monsters[0] == 5:
    ai_type = ["bug swarm"]  # will create variety later
random.shuffle(ai_type)
monster_ai = ai_type[0]
# Setting required variables depending on what enemy type is selected for the encounter
if monster_ai == "boss":
    # attack and ability list to be read by the chosen_attack_ai function
    attacks = ["Hammer slam"]  # will add more later
    ai_group_hp = 1500
    ai_power = 80
    ai_spawned = 1
    enter_word = "a"
    nickname = "Boss"
elif monster_ai == "brothers":
    attacks = ["Beat Down"]  # will add more later
    ai_group_hp = 750
    ai_power = 40
    ai_spawned = 2
    enter_word = "2"
    nickname = "Brother"
elif monster_ai == "triplets":
    attacks = ["Starlight beam"]  # will add more later
    ai_group_hp = 500
    ai_power = 25
    ai_spawned = 3
    enter_word = "the"
    nickname = "Triplet"
elif monster_ai == "troggies":
    attacks = ["Slash"]  # will add more later
    ai_group_hp = 375
    ai_power = 10
    ai_spawned = 4
    enter_word = "some"
    nickname = "Troggie"
elif monster_ai == "bug swarm":
    attacks = ["Scratch"]
    ai_group_hp = 300
    ai_power = 5
    ai_spawned = 5
    enter_word = "a"
    nickname = "Bug"

print("You encountered {} {}!".format(enter_word, monster_ai))
# nul variable set to be read by the encounter section to determine how many of what enemy to make selectable to attack and interact with
nul = "nul"
if ai_spawned == 1:
    ai_1_hp = ai_group_hp
    ai_2_hp = nul
    ai_3_hp = nul
    ai_4_hp = nul
    ai_5_hp = nul
elif ai_spawned == 2:
    ai_1_hp = ai_group_hp
    ai_2_hp = ai_group_hp
    ai_3_hp = nul
    ai_4_hp = nul
    ai_5_hp = nul
elif ai_spawned == 3:
    ai_1_hp = ai_group_hp
    ai_2_hp = ai_group_hp
    ai_3_hp = ai_group_hp
    ai_4_hp = nul
    ai_5_hp = nul
elif ai_spawned == 4:
    ai_1_hp = ai_group_hp
    ai_2_hp = ai_group_hp
    ai_3_hp = ai_group_hp
    ai_4_hp = ai_group_hp
    ai_5_hp = nul
elif ai_spawned == 5:
    ai_1_hp = ai_group_hp
    ai_2_hp = ai_group_hp
    ai_3_hp = ai_group_hp
    ai_4_hp = ai_group_hp
    ai_5_hp = ai_group_hp
else:
    print("something went wrong :(")
ai_1_hp = str(ai_1_hp)
ai_2_hp = str(ai_2_hp)
ai_3_hp = str(ai_3_hp)
ai_4_hp = str(ai_4_hp)
ai_5_hp = str(ai_5_hp)


def player_choice_menu():
    print("------------------------------------")
    print("Which action would you like to take?")
    print("Attack -- {} -- Recover".format(AM))
    menu_choice = input("Type which action you'd like to take (e.g 'Attack')")
    menu_choice = menu_choice.strip().lower()
    print("\n")
    if menu_choice == "attack":
        attack_list()
    elif menu_choice == AM:
        print("not yet finished")
        player_choice_menu()
    elif menu_choice == "recover":
        print("not yet finished")
        player_choice_menu()
    else:
        print("Please type a valid input")
        player_choice_menu()


def attack_list():
    global damage_done_player
    fireball = [30, 31, 32, 33, 34, 35]
    print("-----------------")
    print("List of attacks:")
    print("Fireball")
    attack_choice = input("Type which attack you'd like to use (e.g 'Fireball')")
    attack_choice = attack_choice.strip().lower()
    if attack_choice == "fireball":
        random.shuffle(fireball)
        crit_chance = random.randint(1, 2)
        if crit_chance == 2:
            damage_done_player = 0
            damage_done_player = fireball[0] * 2
            print("You're fireball did critical damage and did {}!".format(damage_done_player))
            player_2enemy_target(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
        else:
            damage_done_player = 0
            damage_done_player = fireball[0]
            print("You're fireball hit for {}!".format(damage_done_player))
            player_2enemy_target(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
    else:
        print("Please type a valid input")
        attack_list()


def player_2enemy_target(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp):
    global attackable_ai_1
    global attackable_ai_2
    global attackable_ai_3
    global attackable_ai_4
    global attackable_ai_5
    print("------------------------------------")
    print("Which enemy would you like to attack:")
    if ai_spawned != 1 and ai_1_hp != 0:
        print(nickname + " 1:" + ai_1_hp)
        attackable_ai_1 = 1
    elif ai_spawned == 1 and ai_1_hp != 0:
        print(nickname + ":" + ai_1_hp)
        attackable_ai_1 = 1
    else:
        attackable_ai_1 = 0

    if ai_2_hp != "nul":
        if ai_2_hp != 0:
            print(nickname + " 2:" + ai_2_hp)
            attackable_ai_2 = 1
        elif ai_2_hp <= 0:
            print(nickname + " 2:Dead")
            attackable_ai_2 = 0
    elif ai_2_hp == "nul":
        attackable_ai_2 = 0

    if ai_3_hp != "nul":
        if ai_3_hp != 0:
            print(nickname + " 3:" + ai_3_hp)
            attackable_ai_3 = 1
        elif ai_3_hp <= 0:
            print(nickname + " 3:Dead")
            attackable_ai_3 = 0
    elif ai_3_hp == "nul":
        attackable_ai_3 = 0

    if ai_4_hp != "nul":
        if ai_4_hp != 0:
            print(nickname + " 4:" + ai_4_hp)
            attackable_ai_4 = 1
        elif ai_4_hp <= 0:
            print(nickname + " 4:Dead")
            attackable_ai_4 = 0
    elif ai_4_hp == "nul":
        attackable_ai_4 = 0

    if ai_5_hp != "nul":
        if ai_5_hp != 0:
            print(nickname + " 5:" + ai_5_hp)
            attackable_ai_5 = 1
        elif ai_5_hp <= 0:
            print(nickname + " 5:Dead")
            attackable_ai_5 = 0
    elif ai_5_hp == "nul":
        attackable_ai_5 = 0
    player_attack_choice_check(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)


def player_attack_choice_check(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp):
    global attacked_target
    if ai_spawned == 1:
        player_attack_choice = input("Please type which enemy you'd like to attack (e.g '{}')".format(nickname))
    else:
        player_attack_choice = input("Please type which enemy you'd like to attack (e.g '{} 2')".format(nickname))
    player_attack_choice = player_attack_choice.strip().lower()
    if ai_spawned == 1:
        if player_attack_choice == nickname and attackable_ai_1 == 1:
            print("target worked")
            ai_1_hp = ai_1_hp - damage_done_player
            attack_list()
        else:
            print("something when horribly wrong")
    elif ai_spawned != 1:
        if player_attack_choice == nickname + " 1" and attackable_ai_1 == 1:
            print("target worked")
            ai_1_hp = ai_1_hp - damage_done_player
            attack_list()
        elif player_attack_choice == nickname + " 1" and attackable_ai_1 == 0:
            print("This monster is dead. Please select a valid target")
            player_attack_choice_check(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
        if player_attack_choice == nickname + " 2" and attackable_ai_2 == 1:
            print("target worked")
            ai_2_hp = ai_2_hp - damage_done_player
            attack_list()
        elif player_attack_choice == nickname + " 2" and attackable_ai_2 == 0:
            print("This monster is dead. Please select a valid target")
            player_attack_choice_check(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
        if player_attack_choice == nickname + " 3" and attackable_ai_3 == 1:
            print("target worked")
            ai_3_hp = ai_3_hp - damage_done_player
            attack_list()
        elif player_attack_choice == nickname + " 3" and attackable_ai_3 == 0:
            print("This monster is dead. Please select a valid target")
            player_attack_choice_check(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
        if player_attack_choice == nickname + " 4" and attackable_ai_4 == 1:
            print("target worked")
            ai_4_hp = ai_4_hp - damage_done_player
            attack_list()
        elif player_attack_choice == nickname + " 4" and attackable_ai_4 == 0:
            print("This monster is dead. Please select a valid target")
            player_attack_choice_check(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
        if player_attack_choice == nickname + " 5" and attackable_ai_5 == 1:
            print("target worked")
            ai_5_hp = ai_5_hp - damage_done_player
            attack_list()
        elif player_attack_choice == nickname + " 5" and attackable_ai_5 == 0:
            print("This monster is dead. Please select a valid target")
            player_attack_choice_check(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
    else:
        print("That is not a valid target")
        player_attack_choice_check(ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)


player_choice_menu()
