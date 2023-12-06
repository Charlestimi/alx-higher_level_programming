#!/usr/bin/python3
def search_replace(my_list, search, replace):
   """ new_list()
    for element in my_list:
        if element == search
        my_list.append()
        else:
            my_list.append(new_list)
          return new_list"""
new_list = [replace if x == search else x for x in my_list]
