list = []

def sortPeople(x):

  for lkey, lvalue in enumerate(x):
    v =  lvalue['lastName'] + ", " + lvalue['firstName']
    list.append(v)
