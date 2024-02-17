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

    menu flora_01:
        f "So what brings you here?"
        "I'm on a quest to defeat you?":
            f """
                Uhhh... Sure?
                No... Why are you actually here?
            """
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