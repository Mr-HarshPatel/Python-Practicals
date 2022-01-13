#------ ID : 20CE082 NAME : HARSH PATEL -------#
###### Q-3 Write a Python program to sum all the items in a dictionary.


dict = {
    'a' : 100,
    'b' : 200,
    'c' : 250
}
sum = 0
for i in dict.values() :     #logic for sum
    sum = sum +i

print("Sum of values",sum)