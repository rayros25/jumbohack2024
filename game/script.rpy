# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Protagonist
define character.j = Character("Jumbo-chan", who_color="3E8EDE", what_prefix='"', what_suffix='"')
default j.mission = "none"

# Invasive species
define f = Character("Flora", who_color="C1CD23", what_prefix='"', what_suffix='"') # Multiflora Rose
define z = Character("Zac", who_color="5E4B3C", what_prefix='"', what_suffix='"') # Zebra Mussel
define l = Character("Luke", who_color="B1282E", what_prefix='"', what_suffix='"') # Spotted Lanternfly

transform jumper:
    pause .05
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    # repeat
# modified from https://lemmasoft.renai.us/forums/viewtopic.php?t=48050


# The game starts here.
label start:
    play music "duck.mp3" loop
    jump gamestart

label game_end:
    return
