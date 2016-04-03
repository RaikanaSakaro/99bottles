#Setting up loop with range.
for number in range(99, 0, -1):
  print "{0} bottles of beer on the wall, {0} bottles of beer...\nIf one of those bottles should happen to fall, {1} bottles of beer on the wall.".format(number, number-1)
