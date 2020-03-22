from db import *
from peewee import *
import random as r
import datetime

class Player(BaseModel):
    """
    Player defines out the attributes that are needed for a rumble
    """
    discord_id = IntegerField(unique=True)
    name = CharField()
    strength = IntegerField(default=1)
    health = IntegerField(default=100)
    last_workout = DateTimeField(default=datetime.datetime.now)

def get_player(did, n):
    """
    get_player returns the player with the associated discord id from the database
        or generates a new player if one does not already exist.
    """
    pl = Player.select().where(Player.discord_id == did)
    if len(pl) == 0:
        pl = [Player.create(discord_id=did,name=n)]
    ret_pl = pl[0]
    # update name if changed
    if ret_pl.name != n:
        ret_pl.name = n
        ret_pl.save()
    return ret_pl

# TODO maybe invite the possibilty to vary the percentages based on how much they workout within a time frame
def increase_health(did, n):
    """
    increase_health simulates a workout for the player and may or may not increase
        the players strength.
    """
    pl = get_player(did, n)
    if pl.strength > 70:
        return f"You are already at the max strength of {pl.strength}."
    success = r.uniform(0,1)
    prev_strength = pl.strength
    # we use 80.0 to allow a reasonable percentage chance as you get closer to 70
    if success <= (pl.strength/80.0):
        return f"You didn't beat your PR this time! Strength: {prev_strength} -> {pl.strength}"
    wild_card = r.uniform(0,1)
    message = ""
    if wild_card >= 0.95:
        pl.strength = min(70, pl.strength + 2)
        message = f"Workout went better than normal! Strength: {prev_strength} -> {pl.strength}"
    elif wild_card <= 0.05:
        pl.strength = max(1, pl.strength - 1)
        message = f"You injured yourself during the workout! Strength: {prev_strength} -> {pl.strength}"
    else:
        pl.strength = pl.strength + 1
        message = f"Workout went well! Strength: {prev_strength} -> {pl.strength}"
    pl.last_workout = datetime.datetime.now()
    pl.save()
    return message

def player_summary(did, n):
    """
    player_summary generates a stat summary of the given player.
    """
    pl = get_player(did, n)
    last_w = pl.last_workout.strftime("%A, %d. %B %Y %I:%M%p")
    message = f"Rumble Player: {n}\nStrength: {pl.strength}\nLast Workout: {last_w}"
    return message

if __name__ == '__main__':
    with db:
        db.create_tables([Player])

