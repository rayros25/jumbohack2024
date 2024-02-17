# screen planets: #Preparing the imagemap
#     imagemap:
#         ground "planets-no-earth.jpg"
#         hover "planets-hover.png"
#         idle "earth.png"
#
#         hotspot (62, 399, 90, 91) clicked Jump("mercury")
#         hotspot (227, 302, 141, 137) clicked Jump("venus")
#         if not earth_destroyed:
#             hotspot (405, 218, 164, 118) clicked Jump("earth")
#         hotspot (591, 78, 123, 111) clicked Jump("mars")
#
# init python:
#     earth_destroyed = False
#
# # The game starts here.
# label start:
#     "This is an imagemap tutorial."
#     jump solar_system
#
# label solar_system:
#     call screen planets #Displaying the imagemap
#
# label mercury:
#     "It is Mercury."
#     jump solar_system
#
# label venus:
#     "It is Venus."
#     jump solar_system
#
# label earth:
#     "It is Earth."
#     "As soon as you quit it, it is destroyed!"
#     $ earth_destroyed = True
#     jump solar_system
#
# label mars:
#     "It is Mars."
#     jump solar_system
#


# code is from https://lemmasoft.renai.us/forums/viewtopic.php?t=22410

screen worldmap:
    imagemap:
        # all placeholders
        ground "bg forest.png"
        hover "bg davis.png"
        idle "bg tischroof.png"

        hotspot (62, 399, 90, 91) clicked Jump("tisch")
        hotspot (227, 302, 141, 137) clicked Jump("dewick")
        if not earth_destroyed:
            hotspot (405, 218, 164, 118) clicked Jump("carm")
        hotspot (591, 78, 123, 111) clicked Jump("olin")

init python:
    earth_destroyed = False

label go_to_map:
    call screen worldmap # Display the image map

label tisch:
    "It's Tisch."
    jump go_to_map

label dewick:
    call m1_check
    "It's Dewick-Macphie Dining Hall."
    jump go_to_map

label carm:
    call m1_check
    "It's Carmichael."
    jump go_to_map

label olin:
    call m1_check
    "It's Olin."
    jump go_to_map


label m1_check:
    if j.mission == "M1-tisch":
        "I can't go here, I'm supposed to go to Tisch."
        jump go_to_map
    else:
        return
