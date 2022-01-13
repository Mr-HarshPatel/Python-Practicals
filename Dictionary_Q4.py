#------ ID : 20CE082 NAME : HARSH PATEL -------#
# Q-4
# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
Dict = {
    1 :10,
    2 :20,
}
print("Sample Dictionary : ")
print(Dict)
print("Add a key to a dictionary :")
((Dict.update({3 : 30})))  # Adding a key and respective value to existing dictionary
print(Dict)