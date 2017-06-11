#!/usr/bin/python

from lib import *

people = [ {'firstName':"Bruce",  'lastName':"Wayne"},
           {'firstName':"James",  'lastName':"Gordon"},
           {'firstName':"Dick",   'lastName':"Grayson"},
           {'firstName':"Alfred", 'lastName':"Pennyworth"},
           {'firstName':"Ellen",  'lastName':"Yin"},
           {'firstName':"Barbara",'lastName':"Gordon" }]


sortPeople(people)
list2 = sorted(list)
for i, e in enumerate(list2):
  print "[" + str(i) + "][" + list2[i] + "]"
