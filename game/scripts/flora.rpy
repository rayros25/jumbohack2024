label flora:
    scene bg forest

    show mrose
    f """
        Oh... Hello.

        It's rare to see visitors around in this grove...

        Though I've only moved here recently...

        Anyways... Please don't mind the mess, ehe.
    """
    hide mrose

    show jumbo
    j "Who are you?"
    hide jumbo

    show mrose
    f "Oh... I'm Flora... I'm a multiflora rose..." 
    f "Rosa Multiflora, if you care about those sorts of names..."
    hide mrose

    $ config.menu_include_disabled = True
    $ quest_to_defeat_you = True
    menu flora_01:
        f "So what brings you here?"
        "I'm on a quest to defeat you?" if quest_to_defeat_you:
            f """
                Uhhh... Sure?

                No... Why are you actually here?
            """
            $ quest_to_defeat_you = False
            jump flora_01
        "I was wandering through the woods and saw you":
            show jumbo
            j """
                I was wandering through the woods and saw you,

                and then I wanted to say hi.

                So, hi!
            """
            hide jumbo
            show mrose
            f """
                Well, nice to meet you...

                Ooh...

                If we are going to get to know each other, 

                I should let you know something about me...
            """
            hide mrose
        "I was looking at all the beautiful plants":
            show jumbo
            j """
                I was looking at all the beautiful plants,

                and then happened upon you.

                What a coincidence...
            """
            hide jumbo
            show mrose
            f """
                A- Yes, a coincidence...

                Plants really are quite...

                They're pretty cool...

                Speaking of...
            """
            hide mrose
    show mrose
    f """
        You see that crab apple tree over there...

        It's been providing me...

        Providing me really good support.

        If you know what I mean...
    """
    hide mrose

    show jumbo
    j "Uhuh. So... What do you like to do for fun?"
    hide jumbo

    show mrose
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
    hide mrose

    menu flora_02:
        f "What do you like to do for fun?"

        "Legendary plant destructor":
            show jumbo
            j """
                I like to dress up in a cardboard box and become

                the LEGENDARY PLANT DESTRUCTOR!

                Feared by the many plants who so happen to get in my way...
            """
            hide jumbo
            show mrose
            f """
                Hehe. Well, I wouldn't get in your way if you were to do that.

                In fact, you should take me along. 
                It'd be a nice change of pace.
            """
            hide mrose
        "Reading books":
            show jumbo
            j """
                I enjoy reading books outside.

                It's a nice way to pass the time, and explore other universes
                outside our own.
            """
            hide jumbo
            show mrose
            f """
                Ooh. I would love to read books together outside sometime.

                It's always nice to get to learn more about others...

                Especially you.
            """
            hide mrose
        "Exploring my environment":
            show jumbo
            j """
                I love exploring new places.

                I'm always looking out for new places to wander around.

                Especially if they're not too crowded...
            """
            hide jumbo
            show mrose
            f "Ooh... I would love to explore around with you..."
            f "I wonder where we could go together..."
            hide mrose
    show mrose
    f """
        Oh... I had an idea, let's go to the botanical gardens...

        The flowers there are quite pretty, so I've heard.

        Call it a date, if you will. ;)
    """
    hide mrose

    scene bg botgarden
    j """
    (Huh... It was easier to get her on a date than I thought...)

    (I didn't even have to ask myself.)

    (Well, time to find an empty place in the gardens, because...)

    (Iiiiiit's killing time!!!)
    """