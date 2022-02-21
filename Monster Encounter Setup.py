import random
ai_hp = 0
ai_power = 0
def monster_spawner(ai_hp, ai_power):
    num_spawned_monsters = [1,1,1,1,1,2,2,2,2,3,3,3,4,4,5]
    random.shuffle(num_spawned_monsters)
    if num_spawned_monsters[0] == 1:
        ai_type = ["boss"]#will create variety later
    elif num_spawned_monsters[0] == 2:
        ai_type = ["brothers"]#will create variety later
    elif num_spawned_monsters[0] == 3:
        ai_type = ["triplets"]#will create variety later
    elif num_spawned_monsters[0] == 4:
        ai_type = ["troggies"]#will create variety later
    elif num_spawned_monsters[0] == 5:
        ai_hp = 300
        ai_power = 5
        ai_spawned = 5
        ai_type = ["bug swarm"]#will create variety later

    random.shuffle(ai_type)
    monster_ai = ai_type[0]
    if monster_ai == "boss":
        attacks = ["Hammer slam"]#will add more later
        ai_hp = 1500
        ai_power = 80
        ai_spawned = 1
    elif monster_ai == "brothers":
        attacks = ["Beat Down"]#will add more later
        ai_hp = 750
        ai_power = 40
        ai_spawned = 2
    elif monster_ai == "triplets":
        attacks = ["Starlight beam"]#will add more later
        ai_hp = 500
        ai_power = 25
        ai_spawned = 3
    elif monster_ai == "troggies":
        attacks = ["Slash"]#will add more later
        ai_hp = 375
        ai_power = 10
        ai_spawned = 4


def chose_attack_ai(attacks,monster_ai,ai_power,damage_done_ai):
    damage_done_ai = 0
    if monster_ai == "boss":
        Hammer_slam = [2*ai_power,2.1*ai_power,2.2*ai_power,2.3*ai_power,2.4*ai_power,2.5*ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Hammer slam":
            random.shuffle(Hammer_slam)
            crit_chance = random.randint(1,2,3,4,5,6,7,8,9,0)
            if crit_chance == 9 or 0:
                damage_done_ai = Hammer_slam[0]*2
            else:
                damage_done_ai = Hammer_slam[0]
    elif monster_ai == "brothers":
        Beat_down = [1*ai_power,1.1*ai_power,1.2*ai_power,1.3*ai_power,1.4*ai_power,1.5*ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Beat Down":
            random.shuffle(Beat_down)
            crit_chance = random.randint(1,2,3,4,5,6,7,8,9,0)
            if crit_chance == 9 or 0:
                damage_done_ai = Beat_down[0]*2
            else:
                damage_done_ai = Beat_down[0]
    if monster_ai == "triplets":
        Starlight_beam = [1.5*ai_power,1.6*ai_power,1.7*ai_power,1.8*ai_power,1.9*ai_power,2*ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Starlight beam":
            random.shuffle(Starlight_beam)
            crit_chance = random.randint(1,2,3,4,5,6,7,8,9,0)
            if crit_chance == 9 or 0:
                damage_done_ai = Starlight_beam[0]*2
            else:
                damage_done_ai = Starlight_beam[0]
    if monster_ai == "troggies":
        Slash = [1.5*ai_power,1.6*ai_power,1.7*ai_power,1.8*ai_power,1.9*ai_power,2*ai_power]
        random.shuffle(attacks)
        if attacks[0] == "Slash":
            random.shuffle(Slash)
            crit_chance = random.randint(1,2,3,4,5,6,7,8,9,0)
            if crit_chance == 9 or 0:
                damage_done_ai = Slash[0]*2
            else:
                damage_done_ai = Slash[0]
