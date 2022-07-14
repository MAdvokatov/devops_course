#TASK 3.4

import logging
import random

logging.basicConfig(level=logging.INFO)

some_list = [100 , 10 , "10" , 5]
some_list2 = [100 , 10 , "10" , 5]


def test_division():
    try:
        print(random.choice(some_list) / random.choice(some_list2) )
        logging.info("IT WORKS")
    except TypeError:
        logging.error("TRYING TO DIVIDE INTEGER WITH A STRING OR THE OPPOSITE")


test_division()
