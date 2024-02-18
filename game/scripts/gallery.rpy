define gal = Character('Gallery', kind=nvl, color="#c8c8ff")

init python:
    import json

    animal_list = []

    json_in = renpy.file("animal_data/Emerald Ash Borer- Agrilus planipennis.json")
    json_load = json.load(json_in)
    # the_name = json_load["name"]

    animal_list.append(json_load)

    list_of_files = renpy.list_files()
    for file in list_of_files:
        if file.startswith('animal_data/') and file.endswith('.json'):
            curr_file = renpy.file(file)
            if curr_file:
                curr_load = json.load(curr_file)
                animal_list.append(curr_load)

    # listofiles2 = renpy.open_file(directory="animal_data/")

label gallery:

    # dialogue = json.dumps(scene1_english.json)
    # renpy.say(dialogue[0].who, dialogue[0].what)
    # animal = json.dumps("Boxwood Blight - Cylindrocladium pseudonaviculatum.json")
    # renpy.say(animal.name)
    while len(animal_list) > 0:
        f "The name is [animal_list[0]['name']]"
        $ animal_list.pop(0)

    return
