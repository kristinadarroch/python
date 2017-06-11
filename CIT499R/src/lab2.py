#!/usr/bin/python

people = [
{'firstName': "Bruce", 'lastName': "Wayne"},
{'firstName': "James", 'lastName': "Gordon"},
{'firstName': "Dick", 'lastName': "Grayson"},
{'firstName': "Alfred", 'lastName': "Pennyworth"},
{'firstName': "Ellen", 'lastName': "Yin"},
{'firstName': "Barbara", 'lastName': "Gordon"}
]
# def sortPeople():
for lkey, lvalue in enumerate(people):
    print lvalue['lastName'] + " " + lvalue['firstName']
sorted(people)
