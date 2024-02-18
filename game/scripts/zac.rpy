label zac:
    scene lake
    show jumbo
    j "(I hear screaming coming from the lake...)"
    hide jumbo

    show zmussel
    z "OOOOOOH YEHHHHHH... BUY OUR WARES AND DON'T LEAVE ANY SPARES!"
    z "WE REALLY NEED TO EXPAND OUR BUISNESS TO THE NEXT LAKE!"
    hide zmussel

    show jumbo
    j "(Oh, they noticed me.)"
    hide jumbo

    show zmussel
    z "AND TO DO THAT we'll ned your help..."
    z "ARE YOU A CUSTOMER?????!?!?!?"
    hide zmussel

    $ config.menu_include_disabled = True
    $ already_clogged = True
    menu zac_01:
        z "DO you want your PIPES clogged?!"
        "My pipes are already clogged":
            show jumbo
            j "Uhhh... My pipes are already clogged. Thanks for your offer..."
            j "But I can't get water from them currently."
            j "So no for now..."
            hide jumbo
            show zmussel
            z "Ah, we see..."
            z "Well, we have plenty of other options that you can choose from."
            hide zmussel
            already_clogged = False
            jump zac_01
        "Please clog my pipes":
            # TODO
        "I don't want that":
            # TODO