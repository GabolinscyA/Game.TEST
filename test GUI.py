from tkinter import *
from tkinter import ttk
import random


class Monster:
    def __init__(self,name,nickname,enter_word,group_hp,power,spawned,attacks):
        self.name = name
        self.nickname = nickname
        self.enter_word = enter_word
        self.group_hp = group_hp
        self.power = power
        self.spawned = spawned
        self.attacks = attacks


boss_attack_list = ["Hammer Slam"]
brother_attack_list = ["Beat Down"]
triplets_attack_list = ["Starlight Beam"]
troggies_attack_list = ["Slash"]
bug_swarm_attack_list = ["Scratch"]


Boss = Monster("Big Boss", "Boss", "The", 1500, 80, 1, boss_attack_list)
Brothers = Monster("The Brothers","Brother", "The", 750, 40, 2, brother_attack_list)
Triplets = Monster("Star Triplets", "Triplet", "The", 500, 25, 3, triplets_attack_list)
Troggies = Monster("Troggie Bunch", "Troggie", "A", 375, 10, 4, troggies_attack_list)
Bug_Swarm = Monster("Bug Swarm", "Bug", "A", 300, 5, 5, bug_swarm_attack_list)

def create_name_list():
    name_list = []

def monster_encounter():
    global monster_ai
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
    monster_ai = monster_ai.capitalize()
monster_encounter()

root = Tk()
root.title("Python Project")

top_frame = ttk.LabelFrame(root, text="Battle Screen")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

monster_name_message = StringVar()
monster_name_message.set(monster_ai)

monster_name = ttk.Label(top_frame, textvariable=monster_name_message)
monster_name.grid(row=0, column=0)
root.mainloop()
