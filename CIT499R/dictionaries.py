#!/usr/bin/python

# Declare a complex dictionary.
person = {'firstName':'Peter'
         ,'lastName':'Quill'
         ,'address':'1111 Regency Street'
         ,'city':'Xandar'
         ,'state':'California'
         ,'zip':'94550'
         ,'phones':{'home':'(415) 555-1111'
                   ,'work':'(415) 666-2222'
                   ,'cell':'(415) 777-3333'}}
# Two key loops.
for i in person.keys():
  if len(i) < 7:
    gap = "\t\t"
  else:
    gap = "\t"
  # Check for an instance of a dictionary.
  if isinstance(person[i],dict):
    for j in person[i].keys():
      print "[" + i + "][" + j + "]\t" + person[i][j]
  else:
    print "[" + i + "]" + gap + person[i]
print
# A key loop and key/value pair loop.
for i in person.keys():
  if len(i) < 7:
    gap = "\t\t"
  else:
    gap = "\t"
  # Check for an instance of a dictionary.
  if isinstance(person[i],dict):
    for j, k in person[i].items():
      print "[" + i + "][" + j + "]\t" + k
  else:
    print "[" + i + "]" + gap + person[i]
print
# A key/value pair loops.
for i, j in person.items():
  if len(i) < 7:
    gap = "\t\t"
  else:
    gap = "\t"
  # Check for an instance of a dictionary.
  if isinstance(j,dict):
    for k, l in j.items():
      print "[" + i + "][" + k + "]\t" + l
  else:
    print "[" + i + "]" + gap + j
