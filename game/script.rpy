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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg park

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show jumbo

    # These display lines of dialogue.
    j "Oh wow! What a beautiful day we're having!"
    j "A brisk 60 degrees Farenheit... in the middle of February!"
    j "So nice of the climate to change. I hated all that snow!"

    hide jumbo

    show mrose
    r "We're evil!"
    hide mrose


    show zmussel
    z "We're so evil!!!"
    hide zmussel


    show lfly
    l "Actually I'm very chill, I'm not with these guys."
    hide lfly


    show jumbo
    j "Whoa! I can't believe the world is full of such evil beings!"
    j "I wish there was something I could do about it..."
    j "What if I used my womanly charms against them....."


    # This ends the game.
    call game_end

label game_end:
    return
