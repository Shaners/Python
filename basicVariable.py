fruit = "orange"
fruit_count = 7
people = 2
fruit_consumed_per_person_per_day = 1


print("There are", people, "people in the house.")
print("We have", fruit_count, "{}(s).".format(fruit))
print(people * fruit_consumed_per_person_per_day, fruit, "will be consumed per day.")
print("We will run out of", fruit, "in", fruit_count / (people * fruit_consumed_per_person_per_day), "day(s)!")