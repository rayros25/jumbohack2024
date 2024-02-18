label luke:
    scene bg forest

    """
    I wander through the forest in search for the last creature on my list.

    Finally, my journey was nearing its end. With the end of the "Spotted Lanternfly", I would receive the extra credit I was due!

    It wasn't too long before I spotted it in the distance. The lanternfly's bright coloration gave it away.
    """
    show lfly
    l "Hmm? A stranger... whats your buisness with me?"

    """
    Woah. This guys must be it. That spotted cloak and hood totally gives him away. But...

    This guy... he's on another level! 

    That spotted cloak and that axe... He's like an executioner! I'm gonna need to get on his good side if I want to get close.
    """
  
    l "Oi. What're you starin at me like that for eh? You got a death wish or something?"
    
    hide lfly
    
    "Eep! Gotta say something fast!"

    show jumbo

        
    $ config.menu_include_disabled = True
    $ squish = True
    menu luke_1:
        "I'm here to squish some bugs! "if squish: 
            j "Oh no particular reason. I'm just goin around squishing bugs!"
            "Wait what?! I'm supposed to be getting close to these species so I can kill them!"
            "I can't just go around admitting that!"
            hide jumbo
            show lfly
            l "Oh I see..."
            l "Good thing I'm not a bug then. Thanks for taking out the competition"
            "Oh thank god. Lets say some something else"
            $ squish = False
            hide lfly
            jump luke_1
        "I'm just drifiting around.":
            j "I'm just kinda drifting around, you know what I mean. I'm uhh a drifter."
            "Real smooth of me."
            hide jumbo
            show lfly
            l "Really huh. I'm also a bit of a drifter. I go from plant to plant, cutting each down for my next meal"
            l "Once i'm done with one, I go after the one next to it. And then the next"
            l "This trip's taken me all across the states."
            l "Guess we'll be getting along then huh."
            "Well that went better than I thought."
            hide lfly
        "I'm looking for new species in my area.":
            j "I'm looking for new species in my area. Mind telling me where I might find some?"
            "Oh yeah. Going for the flirty approach never fails. Men are desperate after all."
            hide jumbo
            show lfly
            l "Well I guess you could say I'm new. I've come all the way from the east."
            l "Specifically, China's where I'm from. I like here a whooooole lot better though. Foods great here."
            l "You ever try any yet?"
            "Welp, I guess this one's only desperate for food"
            hide lfly
    show lfly
    l "Oops. I forgot to introduce myself. Names Lycorma delicatula. But thats a mouthful."
    l "You can call me Luke the lanternfly. Good to meet you."
    hide lfly
    show jumbo
    j "Nice to meet you too!"
    j "Say... I'm not really doing anything right now. Maybe we could go get something to eat?"
    hide jumbo
    show lfly
    "I can't read Luke's expression under his hood. He doesn't say anything for a little bit, staring at the ground."
    l "Why not. I guess I could use the company. I know a place."
    hide lfly

    # scene bg orchard

    """
    Luke and I travel to an vineyard nearby. The grapes shone in the light of the sun.

    The wind was nice and breezy, but the air was hot enough to where we wouldn't get cold.

    We walked through the vineuard for a little bit, talking and chatting a bit.
    """

    show lfly
    l "During this time of the year, I love to come places like these to eat"
    "Luke inspects a nearby fine, full of grapes"
    l "Lots of great trees and plants, and plenty of fruit."
    l "Couldn't really ask for more."

    """
    Schwing! Luke takes his axe and slashes at the vines, severing multiple of them.

    Then, he grabs their remains and pulled them towards his face. 

    Luke openes his mouth, revealing a set of razor sharp teeth. 

    He then devoured the vines, plant and grape whole, spraying bits of plant matter and grape juices everywhere.

    It was a bit of a grizzly sight. After he was done, Luke licked his lips.
    """

    l "Aaaah... Nothing like a bit of fruit after a long walk."
    "Luke picks up some uneaten vines off the ground."
    l "You want any?"
    hide lfly
    show jumbo
    menu luke_2:
        "Enthusastically eat them": 
            j "Hell yeah I'll have them"
            "I take the whole bunch and attempt to shove them into my own mouth"
            "They were a little to long, so I scrunched them up into a ball, and barely managed to fit it in"
            "I try chewing. Its very difficult, but I barely manage to finish the mass of plants in my mouth. It actually wasn't so bad!"
            j "ugh... I'm never doing that again..."
            show lfly
            l "Heh. I like the way eat girl. Always like a good appetite"
            j "R-Really? Thanks (I guess)!"
            "This guy's got some real weird taste"
        "Take one":
            j "I'm not the hungry, so I'll just take one."
            "I take a vine from Luke's bundle and snack on it on the same way he did."
            "The grapes tasted good, and their sweet taste helped contrast with the more bitter vine"
            "It was actually pretty good! I couldn't imagine shoving them into my mouth like Luke did though"
            j "Mmmm... That was pretty good. I kinda see why you like doing this"
            show lfly
            l "Glad you enjoyed it."
        "Politely refuse":
            j "Sorry I cant eat this I'm uhh... a carnivore?"
            "What an amazing excuse"
            show lfly
            l "Hmm?"
            "Luke raises his eyebrows in suscipsion"
            l "A carnivourous elephant huh... I didn't know those existed. You're quite the character aren't you."\
            j "Huh? Oh... yeah! There's only a few of us out there you know."
            "Phew"    
        "Luke showed a smile. I can sense the bond between us growing. Unfortunately for him, that bond would have to be ending soon."

        l "Alright miss. I gotta do something by this tree before we get going. You're welcome to watch of course."