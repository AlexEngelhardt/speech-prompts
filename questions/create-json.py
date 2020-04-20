"""Takes the 366-smalltalk-prompts.txt and creates a .json file with the
contents prettified"""

import os
import json
import datetime

languages = ['en', 'de', 'fr']

questions = {}
for lang in languages:
    questions[lang] = open(f"questions-{lang}.txt", "r").read().split("\n")[:367]  # cut off last newline


def doy_to_date(doy):
    """Converts a day-of-year integer (from 1 to 366) to a date-string in mm-dd format (e.g. 04-20).
    It assumes a leap year, and doy starts at 0, not 1!"""
    jan1 = datetime.date(2020, 1, 1)
    new_date = jan1 + datetime.timedelta(days=doy)
    return new_date.strftime('%m-%d')


d = {
    doy_to_date(i): {
        lang: questions[lang][i] for lang in languages
    }
    for i in range(366)
}

# In the next block, I set `i` so that an output JSON file does not get
# overwritten. Instead, we append underscores until a non-existing filename
# is encountered.
# This is so that manually added translations don't accidentally get lost
# if you forgot to commit again :)
outfile = 'questions{}.json'
i = 0
while os.path.exists(outfile.format('_'*i)):
    i += 1

with open(outfile.format('_'*i), 'w', encoding='utf8') as fp:
    json.dump(d, fp, indent=4, ensure_ascii=False)
