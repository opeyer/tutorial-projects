"""
This is the journal module.
"""

import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fileinput:
            for entry in fileinput.readlines():
                data.append(entry.rstrip())

    return data

def save(name, journal_data):
    filename = get_full_pathname(name)
    print("...Saving to: {}".format(filename))

    with open(filename, 'w') as fileout:
        for entry in journal_data:
            fileout.write(entry + '\n')

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename

def add_entry(text, journal_data):
    journal_data.append(text)
