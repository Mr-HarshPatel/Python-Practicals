#------ ID : 20CE082 NAME : HARSH PATEL -------#
###### Q-4 Write a Python program to convert a tuple to a string.
def conversion(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
tuple = ('H', 'A', 'R', 'S', 'H',' ','P' ,'A' , 'T', 'E', 'L')
str = conversion(tuple)
print(str)