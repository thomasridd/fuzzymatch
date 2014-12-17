__author__ = 'hadoop'

from fuzzy import match_lists
import logging

def fuzzy_match_strings(match_string, to_string):

    match_list = match_string.replace('\n','').split('\r')
    to_list = to_string.replace('\n','').split('\r')

    logging.warning(match_list)
    logging.warning(to_list)
    results = match_lists(match_list, to_list)
    logging.warning(results)
    return_string = ''
    for result in results:
        return_string = '%s%s\t%s\n' % (return_string, result['left'], result['right'])

    logging.warning(return_string)
    return return_string

