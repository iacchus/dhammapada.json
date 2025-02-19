## the Dhammapada
### in `.json` format

two translations

generated with `./dhammapada-json.py`

### how to use

1. sort a number between 0 and 346
2. get a verse

### example script

```python
#!/usr/bin/env python

import json
import random

with open("./dhammapada.json", "r") as dhammapada_json_file:
    dhammapada_json = json.load(dhammapada_json_file)

keys = dhammapada_json.keys()
random_choice = random.choice(list(keys))

verse_numbers, verse = dhammapada_json[random_choice]

verses = ", ".join([str(verse_number) for verse_number in verse_numbers])
signature = f"— The Dhammapada, {verses}"

print(verse, signature, sep="\n\n")

#  $ python display-dhammapada.py
#  Cut away the five (lower fetters), abandon the five (remaining fetters),
#  and then develop the five (faculties). The bhikkhu who has transcended
#  the five fetters is said to be "crossed over the flood".
#
#  — The Dhammapada, 370
```

### files

```
.
├── README.md
├── dhammapada.f-max-muller.json
├── dhammapada.json
└── display-dhammapada.py

1 directory, 4 files
```
