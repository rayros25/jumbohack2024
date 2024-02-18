label zac:
    scene bg lake
    play music "cannery.mp3" loop

    show jumbo happy at center with easeinleft
    j "Wow, it's been a while since I've been to this beautiful lake."
    j @ neutral "..."
    j sad "Why do I hear screaming coming from the lake...?"

    show jumbo at left with move
    show zmussel happy at right with easeinright
    show zmussel at jumper
    z "OOOOOOH YEHHHHHH... BUY OUR WARES AND DON'T LEAVE ANY SPARES!"
    show zmussel at jumper
    z "WE REALLY NEED TO EXPAND OUR BUISNESS TO THE NEXT LAKE!"

    j "(Oh, they noticed me.)"

    show zmussel at jumper
    z "AND TO DO THAT we'll need your help..."
    show zmussel at jumper
    z "ARE YOU A CUSTOMER?????!?!?!?"
    show zmussel at jumper
    z "DO you want your PIPES clogged?!"

    $ config.menu_include_disabled = True
    $ already_clogged = True
    menu zac_01:
        "My pipes are already clogged" if already_clogged:
            j "Uhhh... My pipes are already clogged. Thanks for your offer..."
            j "But I can't get water from them currently."
            j "So no for now..."
            show jumbo neutral
            show zmussel at jumper
            z "Ah, we see..."
            show zmussel at jumper
            z "Well, we have plenty of other options that you can choose from."
            $ already_clogged = False
            jump zac_01
        "Please clog my pipes":
            show jumbo sad
            j "I would love it if you would clog the pipes at my house."
            j "Make my basement flood because my pipes are busted!"
            show jumbo neutral
            j "(Yeah, right... I'd never accept \"help\" from someone so fishy.)"
            show zmussel at jumper
            z "OH YEH!"
            z "THANKS SO MUCH FOR CONSIDERING OUR PIPE CLOGGING SERVICES"
        "I don't want that":
            show jumbo sad
            j "I don't want that. That sounds awful."
            j "However, what else are you offering?" 
            j "Are you solely a pipe clogging buisness?"
            show jumbo neutral
            show zmussel at jumper
            z "We're a tad hurt at that..."
            z "Maybe we should call up our associates,"
            z "Get them to attach themselves to your boat or something?"
    
    show zmussel at jumper
    z "But first, would you mind telling me your name, dear customer?"
    j @ sad "Oh, my name is Jumbo."
    show zmussel at jumper
    z "A PLEASURE TO MEET YOU, JUMBO-CHAN!"
    z "We're Zac! The best zebra mussel sales-muscle to ever exist!"
    show zmussel at jumper
    z "We're THE prime specimens of the Dreissena polymorpha species!"
    z "At least in this lake area."
    z "Though who are we kidding... We've barely got any sales recently"
    z "(Fred the accountant noises)"
    z "What's that, Fred?! Huh."
    z "We're at the market cap, so to say, so there isn't anyone else to sell to in this area."
    z "Huh... Truly unfortunate..."
    
    menu zac_02:
        "What's left?":
            j @ sad "So what's left for you now?"
            show zmussel at jumper
            z "Other than expanding our buisness, there's not much to do..."
            z "Though we have enjoyed attaching some of our smaller zebra mussels onto other mussels in this lake!"
            z "Haven't really seen them around since..."
            show zmussel at jumper
            z "IT WAS FUN while it last it lasted, though."
            show zmussel at jumper
            z "WE'VE ALSO ENJOYED brainstorming ideas on how to GROW OUR BUSINESS"
            show zmussel at jumper
        "Try something else?":
            j @ sad "Have you considered trying something else?"
            z "Yeh. Well if you'd believe it, I am interested in EATING A LOT OF ALGAE!"
            z "Though there's not too much around here any more..."
        "So that's why...":
            show jumbo
            j "Oh, so that's why there's no customers."
            show zmussel
            z "YEH! There's a limit to our customer attraction abilities."
            z "Since we're stuck in this lake our screams don't get very far..."
    show zmussel
    z "There IS one thing we've consistently enjoyed throughout our time here!"
    z "Tailoring the ecosystem of this lake to our business' liking!"
    z "The fish here are a bit foolish..."
    z "Simply remove some of the plankton from their food chain,"
    z "and they will leave the area for deeper waters where the plants survive."
    z "But in the process of this, we've grown a bit bored of this old lake..."
    z "Enough about us, tell us a bit about yourself."

    menu zac_03:
        z "What do you like to do for fun?"
        "Swimming":
            show jumbo
            j "I've enjoyed swimming since I was a child."
            j "Whenever I'm stressed I love to go for a swim in the river."
            show zmussel
            z "Sounds like a lot of fun, being able to float around in the water..."
            z "Maybe we could borrow an innertube and experience with you."
            z "That would be FUN!"
        "Watching sunsets over the river":
            show jumbo
            j "I love watching the sun set over the river."
            j "It's just such a tranquil feeling."
            show zmussel
            z "I know what you mean."
            z "Watching the sunset from this lake is just the BEST!"
            z "It's so pretty... Just like you ;)"
        "Eating sand":
            show jumbo
            j "I enjoy eating sand in the middle of the desert."
            show zmussel
            z "Can't say we've been to the desert, ourselves, but we have had sand before."
            z "It was quite grainy."
            z "So that's something we've shared."
    
    show zmussel
    z "(Andrew the assistant noises)"
    z "Oh, Andrew just had a GREAT idea!"
    z "Could we ask you for a teensy tiny favor?"
    z "Would you be willing to go on a date with all of us?"
    z "There's not all that many at this point... What are we at right now, Fred?"
    z "(Fred the accountant noises)"
    z "100,000! Rookie numbers still!"
    z "If you agree to take us somewhere, imagine the number of debts you'd have in your favor!"
    z "You'd literally be the queen of that other lake! Fred?"
    z "(Fred the accountant noises)"
    z "There'd be millions of us!"
    z "And, it's not like we'd need water for several days before we get to the next lake..."
    z "We could take our sweet time with the date. Just think about it."

    menu zac_04:
        "Refuse.":
            "Indeed, the choice not to spread this invasive species is the best one."
            "Congratulations. Congratulations. Congratulations."
            "Jumbo-chan has successfully prevented the spread of this species."
            jump route_choice
        "Accept.":
            "Jumbo-chan isn't sure she can kill all of them, 
            but she decides to accept the date and try..."
    

    ### NEW SCENE ###
    scene bg car
    show zmussel happy at right
    show jumbo neutral at left
    z "Oh, WOW! It's great to get to go to another place! TRULY GREAT!!!"
    "Zac attaches themselves to Jumbo-chan's car."
    z "You really look quite wonderful today."
    j "Likewise, you look very sharp today."
    show zmussel at jumper
    z "AIGHT!"
    z "SINCE this is A DATE!"
    z "Before we get to the next lake..."

    menu zac_05:
        z "Where should we go?"
        "Bleach Land":
            show jumbo
            j "I've been really wanting to see the wonders of the drive 
            in theme park full of disinfectants!"
            j "Let's go to Bleach Land!"
            "Jumbo-chan and Zac go to Bleach Land."
            show zmussel
            z "So what are we doing here?"
            show jumbo
            j "Don't mind it, just stay still..."
            "Jumbo-chan uses the bleach at Bleach Land to disinfect her car as thoroughly as she can."
            "She manages to kill most of Zac, but a part of them escapes anyway..."
            "Hopefully Bleach Land is far enough from any bodies of water that could be contaminated."
            "Congratulations, Jumbo-chan has eliminated the invasive species..."
            "Probably."
            jump route_choice
        "The Selfish Shellfish":
            "Jumbo-chan and Zac go to the Selfish Shellfish."
            show jumbo
            j "I'd love to order some mussels, but they said they were out..."
            show zmussel
            z "You could order something else?"
            show jumbo
            j "Wait a second, could you help me get some?"
            show zmussel
            z "Sure??? (There should be some at the next lake...)"
            show jumbo
            j "All righty, thanks for volunteering. I appreciate it."
            j "(Gotta do what I gotta do...)"
            "Jumbo-chan picks up Zac and chucks them through the window into a boiling pot of water."
            "Zac ends up MOSTLY cooked, but a piece of them escapes down the drain..."
            "Jumbo-chan does end up with cooked mussels, but is wary of the concentration of toxins, so does not eat them."
            "Also it would be weird to eat your date."
            "Congratulations, Jumbo-chan has eliminated the invasive species..."
            "Mostly."
            jump route_choice
        "Let's hurry to the next lake":
            "Jumbo-chan swims around the new lake while Zac watches."
            "Once Jumbo-chan gets out, the two try to play volleyball, but unfortunately Zac cuts it open with his shells."
            "Zac yells a lot in frustration, but they all have fun."
            "When the date ends, Jumbo-chan gently sets them down in the water."
            "As promised, Jumbo-chan has the dubious honor of becoming royalty of the new lake..."
            "Jumbo-chan has helped spread an invasive species."
            j "I'm definitely not getting that extra credit now..."
            jump route_choice
