#!/usr/bin/env python

import json
import random

DHAMMAPADA_JSON_FILEPATH = "./dhammapada.json"

with open(DHAMMAPADA_JSON_FILEPATH, "r") as dhammapada_json_file:
    dhammapada_json = json.load(dhammapada_json_file)

keys = dhammapada_json.keys()
random_choice = random.choice(list(keys))

verse_numbers, verse = dhammapada_json[random_choice]

verses = ", ".join([str(verse_number) for verse_number in verse_numbers])
signature = f"— The Dhammapada, {verses}"

print(verse, signature, sep="\n\n")

#  $ ./display-dhammapada.py
#  Cut away the five (lower fetters), abandon the five (remaining fetters),
#  and then develop the five (faculties). The bhikkhu who has transcended
#  the five fetters is said to be "crossed over the flood".
#
#  — The Dhammapada, 370
