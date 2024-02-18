label gamestart:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg park

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show jumbo happy:
    #     yalign 100
    show jumbo happy:
        zoom 0.5

    # These display lines of dialogue.
    j "Oh wow! What a beautiful day we're having!"
    j "A brisk 60 degrees Farenheit... in the middle of February!"
    j "So nice of the climate to change. I hated all that snow!"

    hide jumbo

    show mrose
    f "We're evil!"
    hide mrose


    show zmussel
    z "We're so evil!!!"
    hide zmussel


    show lfly
    l "Actually I'm very chill, I'm not with these guys."
    hide lfly


    show jumbo sad:
        zoom 0.5
    # show jumbo sad
    j "Whoa! I can't believe the world is full of such evil beings!"
    j "I wish there was something I could do about it..."
    show jumbo neutral:
        zoom 0.5
    j "I should do some more reading about them!"

    $ j.mission = "M1-tisch"

    # jump go_to_map

    "I head to Tisch for research"

    scene bg tischroof
    show jumbo neutral:
        zoom 0.5
    j "Oh, now I get it!"

    j "What if I used my womanly charms against them....."

    jump flora

    # This ends the game.
    call game_end
