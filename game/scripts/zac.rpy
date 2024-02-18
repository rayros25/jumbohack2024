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
            $ already_clogged = False
            jump zac_01
        "Please clog my pipes":
            show jumbo
            j "I would love it if you would clog the pipes at my house."
            j "Make my basement flood because my pipes are busted!"
            j "(Yeah, right... I'd never accept 
            \"help\" from someone so fishy.)"
            hide jumbo
            show zmussel
            z "OH YEH!"
            z "THANKS SO MUCH FOR CONSIDERING OUR PIPE CLOGGING SERVICES"
            hide zmussel
        "I don't want that":
            show jumbo
            j "I don't want that. That sounds awful."
            j "However, what else are you offering?" 
            j "Are you solely a pipe clogging buisness?"
            hide jumbo
            show zmussel
            z "We're a tad hurt at that..."
            z "Maybe we should call up our associates,"
            z "Get them to attach themselves to your boat or something?"
            hide zmussel
    
    show zmussel
    z "But first, would you mind telling me your name, dear customer?"
    hide zmussel
    show jumbo
    j "Oh, my name is Jumbo."
    hide jumbo
    show zmussel
    z "A PLEASURE TO MEET YOU, JUMBO-CHAN!"
    z "We're Zac! The best zebra mussel sales-muscle to ever exist!"
    z "We're THE prime specimens of the Dreissena polymorpha species!"
    z "At least in this lake area."
    z "Though who are we kidding... We've barely got any sales recently"
    z "(Fred the accountant noises)"
    z "What's that, Fred?! Huh."
    z "We're at the market cap, so to say, so there isn't 
    anyone else to sell to in this area."
    z "Huh... Truly unfortunate..."
    hide zmussel
    
    menu zac_02:
        "What's left?":
            show jumbo
            j "So what's left for you now?"
            hide jumbo
            show zmussel
            z "Other than expanding our buisness, there's not much to do..."
            z "Though we have enjoyed attaching some of our smaller 
            zebra mussels onto other mussels in this lake!"
            z "Haven't really seen them around since..."
            z "IT WAS FUN while it last it lasted, though."
            z "WE'VE ALSO ENJOYED brainstorming ideas 
            on how to GROW OUR BUSINESS"
            z "Which is how we've met you!"
            hide zmussel
        "Try something else?":
            j "Have you considered trying something else?"
            # TODO
        "So that's why...":
            j "Oh, so that's why there's no customers."
            # TODO
