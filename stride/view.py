#!/usr/bin/env python3


def display_msg(msg):
    try:
        print(msg)
        return True
    except (KeyboardInterrupt, OSError, RuntimeError) as ex:
        #
        # KeyboardInterrupt = user hits the interrupt key
        # OSError           = system function returns a system-related error, including I/O failures
        #                     such as “file not found” or “disk full” (not for illegal argument types
        #                     or other incidental errors)
        # RuntimeError      = error is detected that doesn’t fall in any of the other categories
        #
        return False

