#!/usr/bin/env python3

import sys          # used for getting object size in bytes
import pprint       # used for testing
import random       # used for generating random guids for testing
import time         # used to update last_used value in cache entry and
                    #    generating last_used times for testing

"""
clear && curl -X POST -d '{"subject_matter": "Literature", "response_size": "2"}' 
"http://45.55.235.198:9000/edchain/courses/" -H "Content-type: application/json"

[
  {
    "content_address": "QmXNSa3nkMLu2fehyAQsGBmFB5qfjMf1NAMMvAzeHLidb2", 
    "copyright_holder": "MIT", 
    "course_title": "Contemporary Literature: Literature, Development, and Human Rights", 
    "instructor_name": "Prof. Sarah Brouillette", 
    "publication_date": "Spring 2008", 
    "subject_matter": "Literature", 
    "unique_identifier": "315"
  }, 
  {
    "content_address": "QmdzzeqihbRCx41giyzYRcpFK2BbcNXTNojPHmC4fHeN9N", 
    "copyright_holder": "MIT", 
    "course_title": "Media in Cultural Context: Popular Readerships", 
    "instructor_name": "Prof. Sarah Brouillette", 
    "publication_date": "Fall 2007", 
    "subject_matter": "Literature", 
    "unique_identifier": "913"
  }
]
"""

cache = {}
"""
    Sample Cache Entry:
    
        course_title = "Media in Cultural Context: Popular Readerships"
        instructor_name = "Prof. Sarah Brouillette"
        publication_date = "Fall 2007"
        subject_matter = "Literature"
        guids = [random.randint(1, 100000) for x in range(num_guids)]
        now = time.time()
        hit_count = random.randint(1, 100000)
        key_list = [course_title, instructor_name, publication_date, subject_matter]
        key = '~'.join(key_list)

        single_entry = {}
        single_entry[key] = dict(guids=guids, hit_count=35, last_used=now)
"""
cache_max_size = {type: 'count', 'num_entry': 10}


def add_to_cache(course_title='',
                 instructor_name='',
                 publication_date='',
                 subject_matter='',
                 guids=[]):
    """
    :param course_title:     Course title search criteria used
                                 Example: "Media in Cultural Context: Popular Readerships"
    :param instructor_name:  Instructor name search criteria used
                                 Example: "Prof. Sarah Brouillette"
    :param publication_date: Course publication date search criteria used
                                 Example: "Fall 2007"
    :param subject_matter:   Subject matter search criteria used
                                Example: "Literature"
    :param guids:            Unique Identifiers returned from search
                                Example: [ 315, 913 ]

    :return:                 True if successfully added to cache, else False
    """
    try:
        key_list = [course_title, instructor_name, publication_date, subject_matter]
        key = '~'.join(key_list)
        # key is already in cache, increment hit_count and update last_used
        if key in cache:
            cache[key]['hit_count'] += 1
            cache[key]['last_used'] = time.time()
        else:
            cache[key] = dict(guids=guids, hit_count=1, last_used=time.time())
            if cache_is_too_big():
                resize_cache()
        return True
    except:
        return False


def cache_is_too_big():
    """
    :return:  True if cache size > maximum cache size, else False
    """
    # Get current cache size
    cur_cache_size = -1
    if cache_max_size['type'].lower() == 'count':
        cur_cache_size = len(cache)

    elif cache_max_size['type'].lower() == 'bytes':
        cur_cache_size = get_size(cache)

    # If current cache size > max allowed return True
    return cur_cache_size > cache_max_size['num_entry']


def get_from_cache(course_title='',
                   instructor_name='',
                   publication_date='',
                   subject_matter=''):
    """
    :param course_title:     Course title to search for in cache (dictionary)
                                 Example: "Media in Cultural Context: Popular Readerships"
    :param instructor_name:  Instructor name to search for in cache
                                 Example: "Prof. Sarah Brouillette"
    :param publication_date: Course publicate date to search for in cache
                                 Example: "Fall 2007"
    :param subject_matter:   Subject matter to search for in cache
                                Example: "Literature"

    :return guids:           Unique identifiers found in cache matching search criteria
                             If not found this will be an empty list
    """
    key_list = [course_title, instructor_name, publication_date, subject_matter]
    key = '~'.join(key_list)
    if key in cache:
        return cache[key]['guids']
    return []


def get_key_to_remove():
    """
        Finds key in cache that has
        1 - smallest hit_count
        2 - oldest (smallest) last_used
    :return: cache (dictionary) key
    """

    # set minimum hit count to max integer &
    # oldest last_used to max epoch date time
    #     d = '2038-01-19 03:14:07'
    #     p = '%Y-%m-%d %H:%M:%S'
    #     os.environ['TZ'] = 'UTC'
    #     epoch = int(time.mktime(time.strptime(d, p)))
    min_hit_count = sys.maxsize
    min_last_used = 2147483647  # 19-Jan-2038  03:14:07 UTC
    key_to_remove = ''

    # loop over all cache items
    for key, value in cache.items():
        # is this hit_count <= current minimum?
        if value['hit_count'] <= min_hit_count:
            # yes, set new minimum hit count
            min_hit_count = value['hit_count']

            # this is the key to remove
            key_to_remove = key

            # if this hit_count matches current minimum hit count and
            # this one is older, it becomes the key to remove
            if value['hit_count'] == min_hit_count and value['last_used'] < min_last_used:
                min_last_used = value['last_used']
                key_to_remove = key

    return key_to_remove


def get_size(obj, seen=None):
    """
    :param obj:  Object for which to find size in bytes
    :param seen: Only check object once
    :return:     Object size in bytes
    """
    size = sys.getsizeof(obj)

    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def resize_cache():
    """
    Removes entries from cache until cache size falls within cache_maxsize constraint
    1 - smallest hit_count
    2 - oldest last_used
    :return:
    """
    kountr = 1
    # while the cache size is too big....
    while cache_is_too_big() and kountr <= 1000:
        # get dictionary key to remove
        key_to_remove = get_key_to_remove()

        # for safety, make sure key is in dictionary
        if key_to_remove in cache:
            del cache[key_to_remove]

        # if we can't fit to current size in 1000 attempts something is wrong
        # also, prevents an infinite loop
        kountr += 1

    return kountr < 1000


def set_cache_size_(new_size, units='count'):
    """
    :param new_size:   Integer - maximum size of cache in 'type' units
    :param units:      { 'count' | 'bytes' } - Units for cache max size
                       count = number of entries
                       bytes = size in bytes
    :return:           True on success, else False

    Additional Info for setting max_size:
        With a single sample cache entry:
        # Uniqud Ids    Cache Entry Size
        ============    ================
        100 guids       4674 bytes
        200 guids       8234 bytes
        300 guids       11898 bytes
        400 guids       15466 bytes
        500 guids       19234 bytes
        600 guids       23258 bytes
        700 guids       26794 bytes
        800 guids       30418 bytes
        900 guids       34146 bytes
        1000 guids      37986 bytes
    """
    cache_max_size['num_entry'] = new_size
    # is cache size expressed in count (number of entries) or bytes?
    if units.lower() == 'count':
        cache_max_size['type'] = 'count'

    elif units.lower() == 'bytes':
        cache_max_size['type'] = 'bytes'

    else:
        return False

    # has cache size changed such that cache needs to be re-sized?
    if cache_is_too_big():
        return resize_cache()

    return True


def test_size():

    for num_guids in range(100, 1100, 100):
        course_title = "Media in Cultural Context: Popular Readerships"
        instructor_name = "Prof. Sarah Brouillette"
        publication_date = "Fall 2007"
        subject_matter = "Literature"
        guids = [random.randint(1, 100000) for x in range(num_guids)]
        now = time.time()
        hit_count = random.randint(1, 100000)
        key_list = [course_title, instructor_name, publication_date, subject_matter]
        key = '~'.join(key_list)

        single_entry = {}
        single_entry[key] = dict(guids=guids, hit_count=hit_count, last_used=now)

        size = get_size(single_entry)
        print('{0} guids: {1} bytes'.format(num_guids, size))


def main():
    cache_max_size['type'] = 'count'
    cache_max_size['num_entry'] = 4

    guids = [18099, 28155, 30901, 38606, 52214, 86571]

    add_to_cache(course_title="Media in Cultural Context: Popular Readerships-1",
                 guids=guids)
    time.sleep(3)

    add_to_cache(course_title="Media in Cultural Context: Popular Readerships-2",
                 instructor_name="Prof. Sarah Brouillette",
                 guids=guids)
    time.sleep(3)

    add_to_cache(course_title="Media in Cultural Context: Popular Readerships-3",
                 instructor_name="Prof. Sarah Brouillette",
                 publication_date="Fall 2007",
                 guids=guids)
    time.sleep(3)

    add_to_cache(course_title="Media in Cultural Context: Popular Readerships-4",
                 instructor_name="Prof. Sarah Brouillette",
                 publication_date="Fall 2007",
                 subject_matter="Literature",
                 guids=guids)
    time.sleep(3)

    add_to_cache(course_title="Media in Cultural Context: Popular Readerships-1",
                 guids=guids)
    time.sleep(3)

    add_to_cache(course_title="Media in Cultural Context: Popular Readerships-5",
                 instructor_name="Prof. Sarah Brouillette",
                 publication_date="Fall 2007",
                 subject_matter="Literature",
                 guids=guids)
    time.sleep(3)


if __name__ == '__main__':
    main()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(cache)
