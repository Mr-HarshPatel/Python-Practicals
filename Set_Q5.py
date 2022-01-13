#------ ID : 20CE082 NAME : HARSH PATEL -------#
###### Q-5 Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

#For list
def most_frequent(List):
    return max(set(List), key = List.count)
List = [82, 10, 82, 82, 100, 33]
a=most_frequent(List)
print(a,List.count(a))
#FOR tuple
def most_frequent(List):
    return max(set(List), key = List.count)
List = list((82, 19, 22, 82, 82, 39,))  #converted tuple to list
a=most_frequent(List)
print(a,List.count(a))
#For dictionary
def most_frequent(List):
    return max(set(List), key = List.count)
dict={1:11,2:22,3:33,4:11,5:11}
List = list(dict.values())
a=most_frequent(List)
print(a,List.count(a))