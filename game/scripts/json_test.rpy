label json_test:
    # dialogue = json.dumps(scene1_english.json)
    # renpy.say(dialogue[0].who, dialogue[0].what)
    # animal = json.dumps("Boxwood Blight - Cylindrocladium pseudonaviculatum.json")
    # renpy.say(animal.name)
    $ import json
    $ json_in = renpy.file("animal_data/Emerald Ash Borer- Agrilus planipennis.json")
    $ text = json.load(json_in)
    # $ renpy.say(j, text["name"])
    $ listofiles = renpy.list_files()

    return

