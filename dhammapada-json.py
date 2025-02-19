#!/usr/bin/env python

import json
import subprocess
import re


LAST_VERSE = 423

def remove_numbers_from_str(string):
    space = ' '
    comma = ','

    new_string = re.sub(r'[0-9]+', '', string)
    new_string = re.sub(r' ,', '', new_string)
    new_string = re.sub(r'\n\W*\n\W*\n', '\n\n', new_string)
    new_string = re.sub(r'\n\W*$', '', new_string)

    return new_string.strip(f'{space}{comma}')


def get_verse(verse_number):

    command = ['display-dhammapada', '-m', str(verse_number)]
    verse = subprocess.run(command, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, text=True).stdout.strip()
    return verse


def get_numbers(string):
    number_list = [int(number) for number in re.findall(r'\d+', string)]
    return tuple(number_list)


verses_dict = dict()

for verse_number in range(LAST_VERSE + 1):

    verse = get_verse(verse_number=verse_number)
    numbers = get_numbers(verse)
    verse_without_numbers = remove_numbers_from_str(verse)

    verses_dict.update({numbers: verse_without_numbers})

final_dict = dict()

#  for idx, item in enumerate(json_dict.items()):
for idx, (verse_number, verse) in enumerate(verses_dict.items()):
    final_dict.update({idx: (verse_number, verse)})

json_str = json.dumps(final_dict, indent=2)

print(json_str)

with open("dhammapada.f-max-muller.json", "w") as file_descriptor:
    file_descriptor.write(json_str)
