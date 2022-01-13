#------ ID : 20CE082 NAME : HARSH PATEL -------#
###### Q-3 Write a Python program to add an item in a tuple.

tpl=(12,45,67,98)
print(tpl)
newtpl=list(tpl)   # converted tuple into list to give append command
print(newtpl)
newtpl.append(100)
print(newtpl)
finalans=tuple(newtpl) # after append
print(finalans)
