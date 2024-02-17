# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Protagonist
define j = Character("Jumbo-chan")

# Invasive species
define r = Character("Multiflora Rose")
define z = Character("Zebra Mussel")
define l = Character("Spotted Lanternfly")



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

    show mrose
    show zmussel
    show lfly

    r "We're evil!"
    z "We're so evil!!!"
    l "Actually I'm very chill, I'm not with these guys."




    # This ends the game.
    return
