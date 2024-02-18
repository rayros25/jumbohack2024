label gamestart:
    scene bg westhall

    # show jumbo happy at jumper
    show jumbo happy

    j "Oh wow! What a beautiful day we're having!"
    j "A brisk 60 degrees Farenheit... in the middle of February!"

    show jumbo neutral at jumper

    j "So nice of the climate to change. I hated all that snow!"

    hide jumbo

    "Jumbo-chan sees a few posters."
    "WANTED: DEAD"
    "For crimes against the environment."
    "REWARD: Extra credit for Bio 14"
    "- Tufts Biology Department"

    menu posters:
        "Multiflora Rose":
            show mrose neutral
            "Multiflora roses have been smothering plants in the nearby Forest!"
            hide mrose neutral
            jump posters
        "Zebra Mussel":
            show zmussel neutral
            "Zebra mussels have been wreaking havoc in the Lake nearby!"
            hide zmussel neutral
            jump posters
        "Spotted Lanternfly":
            show lfly neutral
            "Spotted lanternflies have been eating plants in the Woods nearby!"
            hide lfly neutral
            jump posters
        "Done looking at the posters.":
            "Jumbo-chan finishes looking at the posters, 
            and reflects on what she's learned..."

    show jumbo sad
    # show jumbo sad
    j "Whoa! Crimes against the environment..."
    j "I wish there was something I could do about it."
    j "A bit of extra credit couldn't hurt, either."
    show jumbo neutral at jumper
    j "I should do some more reading about them!"

    $ j.mission = "M1-tisch"

    # jump go_to_map

    "Jumbo-chan heads to Tisch for research"

    scene bg tischroof
    show jumbo neutral at jumper
    j "Oh, now I get it!"
    j "What if I used my womanly charms against them, 
    and then eliminated them once their guard is down!"

    $ config.menu_include_disabled = True
    $ flora_route = True 
    $ luke_route = True 
    $ zac_route = True
    menu route_choice:
        j "I wonder where I should go to find the invasive species"
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
