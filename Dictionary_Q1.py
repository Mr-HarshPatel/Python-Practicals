#------ ID : 20CE082 NAME : HARSH PATEL -------#
###### Q-1 Write a Python script to check whether a given key already exists in a dictionary.
def check(a):
    if a in emp:
         print("Entered key is available and value of key is",emp[a])
    else:
         print("Entered key not available")

emp ={
     1: 82,
     2: 'harsh',
     3: 'Got key 1',
     4: 'Got key 2'
}
b = int(input("Enter any key name:"))
check(b)