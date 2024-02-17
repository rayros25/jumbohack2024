# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Protagonist
define character.j = Character("Jumbo-chan", who_color="3E8EDE")
# default j.rizz = 0

# Invasive species
define r = Character("Flora", who_color="C1CD23") # Multiflora Rose
define z = Character("Zebra Mussel", who_color="5E4B3C") # Zebra Mussel
define l = Character("Spotted Lanternfly", who_color="B1282E") # Spotted Lanternfly



# The game starts here.
label start:
    jump gamestart

label game_end:
    return
