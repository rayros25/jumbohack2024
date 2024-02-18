label zac:
    scene bg lake
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
    z "AND TO DO THAT we'll need your help..."
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
            hide zmussel
        "Try something else?":
            show jumbo
            j "Have you considered trying something else?"
            hide jumbo
            show zmussel
            z "Yeh. Well if you'd believe it, 
            I am interested in EATING A LOT OF ALGAE!"
            z "Though there's not too much around here any more..z"
            hide zmussel
        "So that's why...":
            show jumbo
            j "Oh, so that's why there's no customers."
            hide jumbo
            show zmussel
            z "YEH! There's a limit to our customer attraction abilities."
            z "Since we're stuck in this lake our screams don't get very far..."
            hide zmussel
    show zmussel
    z "There IS one thing we've consistently enjoyed throughout our time here!"
    z "Tailoring the ecosystem of this lake to our business' liking!"
    z "The fish here are a bit foolish..." 
    z "Simply remove some of the plankton from their food chain,"
    z "and they will leave the area for deeper waters where the plants survive."
    z "But in the process of this, we've grown a bit bored of this old lake..."
    z "Enough about us, tell us a bit about yourself."
    hide zmussel

    menu zac_03:
        z "What do you like to do for fun?"
        "Swimming":
            show jumbo
            j "I've enjoyed swimming since I was a child."
            j "Whenever I'm stressed I love to go for a swim in the river."
            hide jumbo
            show zmussel
            z "Sounds like a lot of fun, 
            being able to float around in the water..."
            z "Maybe we could borrow an innertube and experience with you."
            z "That would be FUN!"
            hide zmussel
        "Watching sunsets over the river":
            show jumbo
            j "I love watching the sun set over the river."
            j "It's just such a tranquil feeling."
            hide jumbo
            show zmussel
            z "I know what you mean."
            z "Watching the sunset from this lake is just the BEST!"
            z "It's so pretty... Just like you ;)"
            hide zmussel
        "Eating sand":
            show jumbo
            j "I enjoy eating sand in the middle of the desert."
            hide jumbo
            show zmussel
            z "Can't say we've been to the desert, ourselves, 
            but we have had sand before."
            z "It was quite grainy."
            z "So that's something we've shared."
            hide zmussel
    
    show zmussel
    z "(Andrew the assistant noises)"
    z "Oh, Andrew just had a GREAT idea!"
    z "Could we ask you for a teensy tiny favor?"
    z "Would you be willing to go on a date with all of us?"
    z "There's not all that many at this point... 
    What are we at right now, Fred?"
    z "(Fred the accountant noises)"
    z "100,000! Rookie numbers still!"
    z "If you agree to take us somewhere, 
    imagine the number of debts you'd have in your favor!"
    z "You'd literally be the queen of that other lake! Fred?"
    z "(Fred the accountant noises)"
    z "There'd be millions of us!"
    z "And, it's not like we'd need water for several days 
    before we get to the next lake..."
    z "We could take our sweet time with the date. Just think about it."
    hide zmussel

    menu zac_04:
        "Refuse.":
            "Indeed, the choice not to spread this 
            invasive species is the best one."
            "Congratulations. Congratulations. Congratulations."
            "Jumbo-chan has successfully prevented the spread of this species."
            jump route_choice
        "Accept.":
            "Jumbo-chan isn't sure she can kill all of them, 
            but she decides to accept the date and try..."
    
    scene bg car
    show zmussel
    z "Oh, WOW! It's great to get to go to another place! TRULY GREAT!!!"
    "Zac attaches themselves to Jumbo-chan's car."
    z "You really look quite wonderful today."
    hide zmussel
    show jumbo
    j "Likewise, you look very sharp today."
    hide jumbo
    show zmussel
    z "AIGHT!"
    z "SINCE this is A DATE!"
    z "Before we get to the next lake..."
    hide zmussel

    menu zac_05:
        z "Where should we go?"
        "Bleach Land":
            show jumbo
            j "I've been really wanting to see the wonders of the drive 
            in theme park full of disinfectants!"
            j "Let's go to Bleach Land!"
            hide jumbo
            # TODO good ending
            jump route_choice
        "The Selfish Shellfish":
            "TODO"
        "Let's hurry to the next lake":
            "TODO"