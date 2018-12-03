#!/usr/bin/env python

import bs4 as bs
import requests
from multiprocessing import Pool
import sys
import argerr

#use command line argument for starting url
STARTING_URL = sys.argv[1]
PROCESS_AMOUNT = 50

#check for the right amount of arguments
if argerr.argerr(2, "invalid arguments"):
    sys.exit(1)

#function that gets the href from its inputs
#and in case of a local link joins it with the starting url
def handle_link(link):
    try:
        handled = link.get('href')
        if handled[0] == ('/'):
            return ''.join([STARTING_URL, handled])
        else:
            return handled
    except TypeError as e:
        print(e)
        return ''
    except IndexError as e:
        print(e)
        return ''
    except AttributeError as e:
        print(e)
        return ''
    except requests.exceptions.InvalidSchema as e:
        print(e)
        return ''

#gets links from the source url and ands them to a set
def get_links(link):
    try:
        r = requests.get(link)
        soup = bs.BeautifulSoup(r.text, "lxml")
        links = set([])
        for url in soup.find_all('a'):
            new_link = handle_link(url)
            links.add(new_link)
            print(new_link)

        return links
    except TypeError as e:
        print(e)
        return ''
    except IndexError as e:
        print(e)
        return ''
    except AttributeError as e:
        print(e)
        return '' 
    except requests.exceptions.InvalidSchema as e:
            print(e)
            return ''

#uses multi processing to crawl starting
#from the url given as command line parameter
def spider():
    p = Pool(processes=PROCESS_AMOUNT)
    first_links = get_links(STARTING_URL)

    x = p.map(get_links, [link for link in first_links])
    p.close()
    
    return x

print(spider())