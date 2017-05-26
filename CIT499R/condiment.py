print "Menu"
print "=" * 40
print "Hot Dog"
print "-" * 40
print "Toppings:"
print
bun = int(raw_input("Bun?\t\t (0 - No or 1 - Yes): "))
ketchup = int(raw_input("Ketchup?\t (0 - No or 1 - Yes): "))
mustard = int(raw_input("Mustard?\t (0 - No or 1 - Yes): "))
relish = int(raw_input("Relish?\t\t (0 - No or 1 - Yes): "))
print
print bun, ketchup, mustard, relish
for i in [bun]:
  for j in [ketchup]:
    for k in [relish]:
      for l in [mustard]:
        print i, j, k, l
