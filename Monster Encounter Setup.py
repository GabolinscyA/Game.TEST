import random

player_hp = 1000


def monster_spawner():
    num_spawned_monsters = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
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
    if monster_ai == "boss":
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
    monster_encounter(monster_ai, ai_spawned, enter_word, ai_group_hp, nickname,ai_power,attacks)


def chose_attack_ai(attacks, monster_ai, ai_power, damage_done_ai):
    damage_done_ai = 0
    if monster_ai == "boss":
        Hammer_slam = [2 * ai_power, 2.1 * ai_power, 2.2 * ai_power, 2.3 * ai_power, 2.4 * ai_power, 2.5 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Hammer slam":
            random.shuffle(Hammer_slam)
            crit_chance = random.randint(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
            if crit_chance == 9 or 0:
                damage_done_ai = Hammer_slam[0] * 2
            else:
                damage_done_ai = Hammer_slam[0]
    elif monster_ai == "brothers":
        Beat_down = [1 * ai_power, 1.1 * ai_power, 1.2 * ai_power, 1.3 * ai_power, 1.4 * ai_power, 1.5 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Beat Down":
            random.shuffle(Beat_down)
            crit_chance = random.randint(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
            if crit_chance == 9 or 0:
                damage_done_ai = Beat_down[0] * 2
            else:
                damage_done_ai = Beat_down[0]
    if monster_ai == "triplets":
        Starlight_beam = [1.5 * ai_power, 1.6 * ai_power, 1.7 * ai_power, 1.8 * ai_power, 1.9 * ai_power, 2 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Starlight beam":
            random.shuffle(Starlight_beam)
            crit_chance = random.randint(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
            if crit_chance == 9 or 0:
                damage_done_ai = Starlight_beam[0] * 2
            else:
                damage_done_ai = Starlight_beam[0]
    if monster_ai == "troggies":
        Slash = [1.5 * ai_power, 1.6 * ai_power, 1.7 * ai_power, 1.8 * ai_power, 1.9 * ai_power, 2 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Slash":
            random.shuffle(Slash)
            crit_chance = random.randint(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
            if crit_chance == 9 or 0:
                damage_done_ai = Slash[0] * 2
            else:
                damage_done_ai = Slash[0]
    if monster_ai == "bug swarm":
        Scratch = [1 * ai_power, 1.1 * ai_power, 1.2 * ai_power, 1.3 * ai_power, 1.4 * ai_power, 1.5 * ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Scratch":
            random.shuffle(Scratch)
            crit_chance = random.randint(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
            if crit_chance == 9 or 0:
                damage_done_ai = Scratch[0] * 2
            else:
                damage_done_ai = Scratch[0]


def monster_encounter(monster_ai, ai_spawned, enter_word, ai_group_hp, nickname,ai_power,attacks):
    global ai_1_hp
    global ai_2_hp
    global ai_3_hp
    global ai_4_hp
    global ai_5_hp
    print("You encountered {} {}!".format(enter_word, monster_ai))
    if ai_spawned == 1:
        ai_1_hp = ai_group_hp
        ai_list = [ai_1_hp]
    elif ai_spawned == 2:
        ai_1_hp = ai_group_hp
        ai_2_hp = ai_group_hp
        ai_list = [ai_1_hp, ai_2_hp]
    elif ai_spawned == 3:
        ai_1_hp = ai_group_hp
        ai_2_hp = ai_group_hp
        ai_3_hp = ai_group_hp
        ai_list = [ai_1_hp, ai_2_hp, ai_3_hp]
    elif ai_spawned == 4:
        ai_1_hp = ai_group_hp
        ai_2_hp = ai_group_hp
        ai_3_hp = ai_group_hp
        ai_4_hp = ai_group_hp
        ai_list = [ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp]
    elif ai_spawned == 5:
        ai_1_hp = ai_group_hp
        ai_2_hp = ai_group_hp
        ai_3_hp = ai_group_hp
        ai_4_hp = ai_group_hp
        ai_5_hp = ai_group_hp
        ai_list = [ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp]
    player_1_turn(ai_list, player_hp, nickname, ai_spawned, ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp, monster_ai)


def player_1_turn(ai_list, player_hp, nickname, ai_spawned, ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp, monster_ai):
    if player_hp > 0:
        print("Player HP:{}".format(player_hp))
        fireball = [30, 31, 32, 33, 34, 35]
        player_1_turn_choice = input("What do you want to do:'Attack','End'")
        player_1_turn_choice = player_1_turn_choice.strip().lower()
        if player_1_turn_choice == "attack":
            if ai_spawned == 1:
                player_1_attack_choice = input("Which enemy would you like to interact with:{}".format(monster_ai))
            elif ai_spawned < 1:
                player_1_attack_choice = input(
                    "Which numbered enemy would you like to interact with:{}".format(nickname and len(ai_list)))
            else:
                print("Please enter a correct input")
                player_1_turn(ai_list, player_hp, nickname)
        elif player_1_turn_choice == "end":
            print("You passed your turn")
            damage_done_player = 0
            # pass to next turn
        else:
            print("Please enter a correct input")
            player_1_turn(ai_list, player_hp, nickname)
        player_1_attack_choice = player_1_attack_choice.strip().lower()
        player_1 = input("What attack would you like to preform:'fireball'")
        player_1.strip().lower()
        damage_done_player = 0
        if player_1 == "fireball":
            random.shuffle(fireball)
            crit_chance = random.randint(1, 2)
            if crit_chance == 2:
                damage_done_player = fireball[0] * 2
                print("You're fireball did critical damage and did {}!".format(damage_done_player))
            else:
                damage_done_player = fireball[0]
                print("You're fireball hit for {}!".format(damage_done_player))
        else:
            print("Please enter a correct input")
            player_1_turn(ai_list, player_hp, nickname, ai_spawned, ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp, monster_ai)
        if player_1_attack_choice == "1":
            ai_1_hp = ai_1_hp - damage_done_player
        elif player_1_attack_choice == "2":
            ai_2_hp = ai_2_hp - damage_done_player
        elif player_1_attack_choice == "3":
            ai_3_hp = ai_3_hp - damage_done_player
        elif player_1_attack_choice == "4":
            ai_4_hp = ai_4_hp - damage_done_player
        elif player_1_attack_choice == "5":
            ai_5_hp = ai_5_hp - damage_done_player
        AI_turn(ai_list, player_hp, nickname, ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp)
    else:
        print("Lose message")


def AI_turn(ai_list, player_hp, nickname, ai_1_hp, ai_2_hp, ai_3_hp, ai_4_hp, ai_5_hp):
    print("\n")
    for num in ai_list:
        print("{}{} HP: {}".format(nickname, len(ai_list), ai_list))
