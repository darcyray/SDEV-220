#this module will help randomly pick a restaurant from a list of restaurants
#2 things we need to know
# 1 - how to grab a module from the python standard libary/elsewhere
# 2 - how to implement our own custom modules

#to import any module or package we use the import keyword
#import an external package from std python called random.  Random will randomly generate numbers or pick from a list
#we also use the from keyword to import from a package and then specify the function or module we want

from random import choice

#list of restaurants
places = ["McDonald's","KFC","Arby's","Pizza Hut"]

def pick():
    return choice(places)