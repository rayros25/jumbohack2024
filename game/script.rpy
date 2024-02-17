# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Protagonist
define character.j = Character("Jumbo-chan", who_color="3E8EDE")
default j.mission = "none"

# Invasive species
define f = Character("Flora", who_color="C1CD23") # Multiflora Rose
define z = Character("Zac", who_color="5E4B3C") # Zebra Mussel
define l = Character("Luke", who_color="B1282E") # Spotted Lanternfly



# The game starts here.
label start:
    play music "duck.mp3" loop
    jump gamestart

label game_end:
    return
