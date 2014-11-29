__author__ = 'tom ridd'

from difflib import SequenceMatcher
from csv import reader


def match_files(left_file, right_file):
    left_list = []
    right_list = []

    with open(left_file, 'rb') as f:
        r = reader(f)
        for row in r:
            try:
                left_list.append(row[0])
            except:
                pass

    with open(right_file, 'rb') as f:
        r = reader(f)
        for row in r:
            try:
                right_list.append(row[0])
            except:
                pass

    return match_lists(left_list, right_list)

def match_lists(left_list, right_list):
# Use find_best_match to fully match the left list to items in the right
    result_list = []
    for item in left_list:
        matched_item, matched_strength = find_best_match(item, right_list)
        result_list.append({'left': item, 'right': matched_item,
                            'power': matched_strength, 'match_index': right_list.index(matched_item) + 1})
    return result_list

def find_best_match(item, from_list):
# Use variations of fuzzy matching
    if item in from_list:
        # Identical
        return item, 1.0
    else:
        # Simple sequence matching using difflib
        return find_best_match_using_sequence_matcher(item, from_list)

def find_best_match_using_sequence_matcher(item, from_list):
    # Simple sequence matching using difflib
    best_item = ''
    best_match = 0

    # Simple sequence matching using difflib
    for from_item in from_list:
        m = SequenceMatcher(a = item, b = from_item)
        if m.ratio() > best_match:
            best_match = m.ratio()
            best_item = from_item

    return best_item, best_match
