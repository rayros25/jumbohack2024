# TODO: improve movements
label flora:
    scene bg forest
    play music "trees.mp3" loop

    show mrose neutral
    f """
        Oh... Hello.

        It's rare to see visitors around in this grove...

        Though I've only moved here recently...

        Anyways... Please don't mind the mess, ehe.
    """

    show mrose at right with move
    show jumbo happy at left with easeinleft
    j "Who are you?"

    show mrose happy
    f "Oh... I'm Flora... I'm a multiflora rose..." 
    f "Rosa Multiflora, if you care about those sorts of names..."

    $ config.menu_include_disabled = True
    $ quest_to_defeat_you = True
    menu flora_01:
        # show mrose happy
        f "So what brings you here?"
        "I'm on a quest to defeat you?" if quest_to_defeat_you:
            # show mrose mad
            f @ mad """
                Uhhh... Sure?

                No... Why are you actually here?
            """
            $ quest_to_defeat_you = False
            jump flora_01
        "I was wandering through the woods and saw you":
            show jumbo happy at jumper
            j """
                I was wandering through the woods and saw you,

                and then I wanted to say hi.

                So, hi!
            """
            show mrose happy at jumper
            f """
                Well, nice to meet you...

                Ooh...

                If we are going to get to know each other, 

                I should let you know something about me...
            """
        "I was looking at all the beautiful plants":
            show jumbo happy at jumper
            j """
                I was looking at all the beautiful plants,

                and then happened upon you.

                What a coincidence...
            """
            show mrose talking at jumper
            f """
                A- Yes, a coincidence...

                Plants really are quite...

                They're pretty cool...

                Speaking of...
            """
    show mrose neutral
    f """
        You see that crab apple tree over there...

        It's been providing me...

        Providing me really good support.

        If you know what I mean...
    """

    j @ talking "Uhuh. So... What do you like to do for fun?"

    show mrose at jumper
    f """
        Oh. Hm... I really like to climb on top of other plants and get taller,

        because I love to see the world around me.

        Though I doubt the other plants really appreciate that...

        And my previous neighbors seem to keep dying once I've spent too long
        on top of them...

        Ooh...

        Another thing I'm interested in is growing these cute white flowers.

        They make me look really pretty, do you think?

        ...Though others tell me that my thorns can be a bit prickly.

        That doesn't matter too much, though, because I've blocked out 
        most of the people I don't like anyways!

        ...Um, I guess I'll ask you the same:
    """

    menu flora_02:
        f "What do you like to do for fun?"

        "Legendary plant destructor":
            show jumbo talking
            j """
                I like to dress up in a cardboard box and become

                the LEGENDARY PLANT DESTRUCTOR!

                Feared by the many plants who so happen to get in my way...
            """
            show mrose happy
            f """
                Hehe. Well, I wouldn't get in your way if you were to do that.

                In fact, you should take me along. 
                It'd be a nice change of pace.
            """
        "Reading books":
            j @ talking """
                I enjoy reading books outside.

                It's a nice way to pass the time, and explore other universes
                outside our own.
            """
            f @ talking """
                Ooh. I would love to read books together outside sometime.

                It's always nice to get to learn more about others...

                Especially you.
            """
        "Exploring my environment":
            j @ talking """
                I love exploring new places.

                I'm always looking out for new places to wander around.

                Especially if they're not too crowded...
            """
            f @ talking "Ooh... I would love to explore around with you..."
            f "I wonder where we could go together..."

    f """
        Oh... I had an idea, let's go to the botanical gardens...

        The flowers there are quite pretty, so I've heard.

        Call it a date, if you will. ;)
    """

    scene bg botgarden

    show mrose happy at right with easeinright
    show jumbo happy at left with easeinleft
    j """
        (Huh... It was easier to get her on a date than I thought...)

        (I didn't even have to ask myself.)

        (Well, it's time to find an empty place in the gardens)
    """

    j @ talking """
        Wow, look at all the pretty flowers.

        They aren't as pretty as you are though!

        Though I am curious... 
        
        Why do you keep trying to climb on top of all of them?

        It's a bit dangerous... 
        
        I'm the one who has to keep pulling you off them, you know.
    """

    f """
        Oh, sorry... Don't worry about me. 
    
        I'm just trying to get a better view of the gardens.
    """

    j """
        A view of the gardens, huh? You know what would give the best view...

        Getting on my shoulders. 
        
        I think that would let you get a higer viewpoint.
    """

    f """
        Ehe... If you don't mind?

        Just be sure to hold me tight so I don't fall... Okay?
    """

    j "All right. I promise I won't ever let you fall."

    j "(While she is nice, she is an invasive species, 
    so I gotta do what I gotta do.)"

    menu flora_03:
        "CUT HER IN TWAIN!":
            show jumbo happy
            show mrose sad
            "Jumbo-chan CUTS HER APART WITH THE SHEARS she just so happens to have in her trunk."
            hide mrose with dissolve
            show jumbo at center with move
# TODO: slice sound effect + visual effect?
            """
                Then she drops the pieces to the ground 
                and sprays herbicide on them.

                Jumbo-chan has eliminated an invasive species.

                Congratulations. Congratulations. Congratulations.
            """
            j "Well, I didn't let her fall."
        "SUPLEX HER INTO THE GROUND!":
            show jumbo sad
            show mrose sad
# TODO: rotate flora?
            """
                Jumbo-chan suplexes Flora into the ground...

                And leaves, flowers, stems, and seeds scatter everywhere.
            """
            hide mrose with dissolve
            show jumbo at center with move
            """

                Unfortunately, Jumbo-chan has helped her spread her influence 
                in a new environment... 
                
                She's scattered all through the botanical gardens.

                Jumbo-chan has failed to eliminate this invasive species, 
                and the noise brings more people around...
            """
            j "I'd better get out of here before I'm banned from 
            the botanical gardens for life."
        "Continue the date.":
            show jumbo neutral
            """
                Jumbo-chan and Flora continue the date, 

                with Jumbo-chan carrying her all around the botanical gardens.

                Flora eventually touches a lot of the plants there, 
                and drops seeds and stalks all around the gardens.
            """
            hide mrose with dissolve
            show jumbo at center with move
            j "Hopefully something doesn't happen from that... 
            But the date went well?"
    j "My trip to the woods was certainly eventful..."
    jump route_choice
