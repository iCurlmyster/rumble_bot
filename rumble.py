import random as r
from player import Player

def hit_det(strength, threshold):
    """
    hit_det determines what amount of hit points get dealt
    """
    if threshold < 0.5:
        return 0
    luck_threshold = r.random()
    luck = 1
    if luck_threshold >= 0.85:
        luck = 2
    return max(strength * threshold, 1) * luck

def fight_results(punching, taking, turns):
    """
    fight_results returns a summary of the fight
    """
    return f"It took {turns} turns for {punching.name} to take down {taking.name}"

def rumble(p1, p2):
    """
    rumble simulates a fight between two players and returns a summary of the results
    """
    turns = 0
    threshold = r.uniform(0,1)
    punching = p1
    taking = p2
    if threshold >= 0.5:
        punching, taking = taking, punching
    while True:
        threshold = r.uniform(0,1)
        hp = hit_det(punching.strength, threshold)
        taking.health = taking.health - hp
        if taking.health <= 0.0:
            return fight_results(punching, taking, turns)
        punching, taking = taking, punching
        turns = turns + 1

