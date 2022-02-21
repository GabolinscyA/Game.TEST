import random

ai_hp = 500
player_hp = 500


def player_1_turn(ai_hp, player_hp):
    if player_hp > 0:
        print("Player HP:{}".format(player_hp))
        fireball = [30, 31, 32, 33, 34, 35]
        player_1 = input("Ability usage: 'fireball','end'")
        player_1.strip().lower()
        if player_1 == "fireball":
            random.shuffle(fireball)
            crit_chance = random.randint(1, 2)
            if crit_chance == 2:
                damage_done_player = 0
                damage_done_player = fireball[0] * 2
                print("You're fireball did critical damage and did {}!".format(damage_done_player))
                ai_hp = ai_hp - damage_done_player
                AI_1(ai_hp, player_hp)
            else:
                damage_done_player = 0
                damage_done_player = fireball[0]
                print("You're fireball hit for {}!".format(damage_done_player))
                ai_hp = ai_hp - damage_done_player
                AI_1(ai_hp, player_hp)
        elif player_1 == "end":
            print("You passed your turn")
            damage_done_player = 0
            AI_1(ai_hp, player_hp)
        else:
            print("Please enter a correct input")
            player_1_turn(ai_hp, player_hp)
    else:
        print("Lose message")

def AI_1(ai_hp, player_hp):
    print("\n")
    if ai_hp > 0:
        print("Monster HP:{}".format(ai_hp))
        scratch = [10, 20, 30, 40, 50]
        ai_attack_used = random.randint(1, 2)
        if ai_attack_used == 1 or 2:
            random.shuffle(scratch)
            crit_chance = random.randint(1, 2)
            if crit_chance == 2:
                damage_done_ai = 0
                damage_done_ai = scratch[0] * 2
                print("Monsters scratch hit crit for {}".format(damage_done_ai))
                player_hp = player_hp - damage_done_ai
            else:
                damage_done_ai = 0
                damage_done_ai = scratch[0]
                print("Monsters scratch hit for {}".format(damage_done_ai))
                player_hp = player_hp - damage_done_ai
        print("The monster passed its turn")
        print("------------------------")
        player_1_turn(ai_hp, player_hp)
    else:
        print("Victory message")


player_1_turn(ai_hp, player_hp)
#hi
