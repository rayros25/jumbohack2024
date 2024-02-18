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

    # TODO: delete this
    # call gallery

    # show jumbo happy at jumper:
    #     zoom 0.5

    show flora test:
        zoom 0.5

    show zac test:
        zoom 0.5

    # These display lines of dialogue.
    j "Oh wow! What a beautiful day we're having!"
    j "A brisk 60 degrees Farenheit... in the middle of February!"
    j "So nice of the climate to change. I hated all that snow!"

    hide jumbo


    # WE SHALL CONQUER THE ECOSYSTEM
    show mrose
    f "We're evil!"
    hide mrose


    show zmussel
    z "We're so evil!!!"
    hide zmussel


    show lfly
    l "Actually I'm very chill, I'm not with these guys. (I'm very evil)"
    hide lfly


    show jumbo sad at jumper:
        zoom 0.5
    # show jumbo sad
    j "Whoa! I can't believe the world is full of such evil beings!"
    j "I wish there was something I could do about it..."
    show jumbo neutral at jumper:
        zoom 0.5
    j "I should do some more reading about them!"

    $ j.mission = "M1-tisch"

    # jump go_to_map

    "I head to Tisch for research"

    scene bg tischroof
    show jumbo neutral at jumper:
        zoom 0.5
    j "Oh, now I get it!"

    j "What if I used my womanly charms against them....."

    $ config.menu_include_disabled = True
    $ flora_route = True 
    $ luke_route = True 
    $ zac_route = True
    menu route_choice:
        j "I wonder where I should go"
        "The forest" if flora_route:
            $ flora_route = False
            jump flora
        "The woods" if luke_route:
            $ luke_route = False
            jump luke
        "The lake" if zac_route:
            $ zac_route = False
            jump zac

    # This ends the game.
    call game_end
