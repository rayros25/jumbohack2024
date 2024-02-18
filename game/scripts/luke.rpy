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
            show lfly
            l "Really huh. I'm also a bit of a drifter. I go from tree, cutting each down for my next meal"
            l "Once i'm done with one, I go after the one next to it. And then the next"
            l "This trip's taken me all across the states."
            l "Guess we'll be getting along then huh."
            "Well that went better than I thought."
            hide lfly
        "I'm looking for new species in my area.":
            j "I'm looking for new species in my area. Mind telling me where I might find some?"
            "Oh yeah. Going for the flirty approach never fails. Men are desperate after all."
            show lfly
            l "Well I guess you could say I'm new. I've come all the way from the east."
            l "Specifically, China's where I'm from. I like here a whooooole lot better though. Foods great here."
            l "You ever try any yet?"
            "Welp, I guess this one's only desperate for food"
            hide lfly            
    l "Oops. I forgot to introduce myself. Names Lycorma delicatula. But thats a mouthful."
    l "You can call me Luke the lanternfly."

   
