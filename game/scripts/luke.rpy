label luke:
    scene bg forest
    play music "griphop.mp3" loop

    show jumbo neutral

    """
    I wander through the forest in search for one of the creatues on my list.

    "Spotted Lanternfly"

    Known for spreading all across forests in America, and wreaking havoc on crops and plants. This one would definetly have to go.

    It wasn't too long before I spotted it in the distance. The lanternfly's bright coloration gave it away.
    """
    show jumbo at left with move
    show lfly happy at right with easeinright
    l "Hmm? A stranger... whats your buisness with me?"

    """
    Woah. This guys must be it. That spotted cloak and hood totally gives him away. But...

    This guy... he's on another level! 

    That spotted cloak and that axe... He's like an executioner! I'm gonna need to get on his good side if I want to get close.
    """
  
    l "Oi. What're you starin at me like that for eh? You got a death wish or something?"
    
    
    "Eep! Gotta say something fast!"


        
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
            jump luke_1
        "I'm just drifiting around.":
            j "I'm just kinda drifting around, you know what I mean. I'm uhh a drifter."
            "Real smooth of me."
            show lfly
            l "Really huh. I'm also a bit of a drifter. I go from plant to plant, cutting each down for my next meal"
            l "Once i'm done with one, I go after the one next to it. And then the next"
            l "This trip's taken me all across the states."
            l "Guess we'll be getting along then huh."
            "Well that went better than I thought."
        "I'm looking for new species in my area.":
            j "I'm looking for new species in my area. Mind telling me where I might find some?"
            "Oh yeah. Going for the flirty approach never fails. Men are desperate after all."
            show lfly
            l "Well I guess you could say I'm new. I've come all the way from the east."
            l "Specifically, China's where I'm from. I like here a whooooole lot better though. Foods great here."
            l "You ever try any yet?"
            "Welp, I guess this one's only desperate for food"
    show lfly
    l "Oops. I forgot to introduce myself. Names Lycorma delicatula. But thats a mouthful."
    l "You can call me Luke the lanternfly. Good to meet you."
    show jumbo
    j "Nice to meet you too!"
    j "Say... I'm not really doing anything right now. Maybe we could go get something to eat?"
    show lfly
    "I can't read Luke's expression under his hood. He doesn't say anything for a little bit, staring at the ground."
    l "Why not. I guess I could use the company. I know a place."

    scene bg grapeyard

    """
    Luke and I travel to an vineyard nearby. The grapes shone in the light of the sun.

    The wind was nice and breezy, but the air was hot enough to where we wouldn't get cold.

    We walked through the vineyard for a little bit, talking and chatting a bit.
    """

    show lfly happy
    l "During this time of the year, I love to come places like these to eat"
    "Luke inspects a nearby fine, full of grapes"
    l "Lots of great trees and plants, and plenty of fruit."
    l "Couldn't really ask for more."

    """
    Schwing! Luke takes his axe and slashes at a nearby grape plant, sending grapevines flying.

    Then, he grabs their remains and pulled them towards his face. 

    Luke openes his mouth, revealing a set of razor sharp teeth. 

    He then devoured the vines, plant and grape whole, spraying bits of plant matter and grape juices everywhere.

    It was a bit of a grizzly sight. After he was done, Luke licked his lips.
    """

    show lfly at right with move
    show jumbo sad at left with easeinleft

    l "Aaaah... Nothing like a bit of fruit after a long walk."
    "Luke picks up some uneaten vines off the ground."
    l "You want any?"
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
            l "A carnivourous elephant huh... I didn't know those existed. You're quite the character aren't you."
            j "Huh? Oh... yeah! There's only a few of us out there you know."
            "Phew"    
    "Luke showed a smile. I can sense the bond between us growing. Unfortunately for him, that bond would have to be ending soon."
    l "Well, time to eat a couple more. I've just gotten started"
    j "Just... gotten started?"

    """
    Before I could say more, Luke started to hack and slash at more of the plants with startling speed.

    Then, as the leaves fell to the ground, he grabbed and shoved them into his mouth like a starving lion.

    Then he did it again, and again, until a whole row of the plants had been destroyed and devoured.
    """
    
    show lfly
    l "Aahh that hit the spot. Nothing like a nice meal in the afternoon eh?"
    j "y-yeah, you ate a whole lot there. Do you even have any room for later"
    l "Of course I do. That was like an average lunch for me, so I'll probably be back here later"

    "Huh. No wonder these guys are considered invasive. I'm starting to see the problem here."

    l "Alright miss. I gotta do something by this tree before we get going. You're welcome to watch if you want."
    j "Oh sure! I'd love to see whatever you're doing"
    "Sound like my chance to strike!"

    scene bg tree

    show lfly happy at right with easeinleft
    show jumbo neutral at left with easeinleft

    l "You're about to witness something pretty special, i'd reckon."
    l "You see... Us lanternflys have a bit of a plan."
    l "Ever since we've gotten here from China, our goal has been to spread as far as possible here."
    l "And to do that... there's gotta be more of us. So, I'll have to lay down some eggs here."
    l "Its uh... a little embarrassing to be honest. But I'm glad you're here to see it."


    j "Im happy to be here to see it to Luke. Its been really fun being here with you today."
    "I flash him a fake smile, knowing exactly what I would be doing next."
    "Its a bit of a pity, but Luke still is an invasive species. If I let him spread, that grapeyard wouldn't be the only thing he would destroy."


    l "Alright. I'll carve out a nice place to put them right here."

    "Luke starts to hack at the tree with his axe. His back is turned to me."
    "Seeing the opportuntiy, I decide to act."

    menu luke_3:
        "Use Pesticide":
            "I pull the can of pesticide out of my bag and give it a little shake"
            "Then, I aim and spray at the person in front of me"
            show lfly sad
            l "Argh! P-Pesticide?"
            l "I-I thought we-"
            "Before Luke can finish his sentence, the axe slips from his hand."
            "He crumples to the ground, leaving only a gash in the tree in front of him."
            hide lfly with dissolve

            """
                My task is complete! But Pesticide was probably a bit overkill...

                To kill one lanternfly isn't too hard to do with just my hands, and pesticides would kill all bugs who came here next.

                Perhaps I could have done this differently...

                I shrugged, and departed the grizzly scene. At least what's done is done.
            """

        "Squish!":
            show jumbo happy
            "From my bag, I pull out something sure to end the invasive species on front of me."
            "My comically large hammer"
            "I raise it above my head, and let loose the final words that Luke would hear."
            
            j "Sorry MC, prepare to be hammered!"
            
            show lfly mad

            l "...but aren't {i}you{/i} the main character?"

            "{i}{b}CLANG{/b}{/i}" 

            hide lfly with dissolve
            
            "I bring the might hammer down onto luke, turning him into a pancake. Looks like his journey is over"

            """
                My task is complete! I managed to eliminate the species with minimal collateral damage.
                I turned and left with a smile on my face. A job well done! 
                Sayonara, pancakefly.
            """

        "Let Luke continue":
            "Ugh... I just cant do it. I can't bring myself to kill Luke, even if he's invasive."
            "Begrudgingly, I let him continue his process until he was done."
            "Hours passed by..."
            show lfly happy

            l "Alright. I'm finished."

            "Luke drops his axe and turns to me."
            l "Thanks again for being here with me."
            "He looks at me with a happy smile on his face"
            "I smile back, though as for whether it was fake or real, I didn't know..."
            j "Of course. I guess I'll be seeing you then."
            l "Yeah. I've got places to be. I'll be heading to Connecticut next."
            l "Though..."
            l "I'm glad I met you."

            hide lfly with easeoutright
            "With that, Luke grabbed his axe, and walked away."
            "As he left, I couldn't help but feel a pang of regret for what I had done."
            "Or rather, what I hadn't done."
            "Nevertheless, I finished my date with Luke."

    "Seeing as I was done here, I left the tree"
    jump route_choice
