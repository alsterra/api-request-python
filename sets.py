my_set = {"January", "February", "March"}
for elem in my_set:
    print(elem)


my_set.add("April")
print(my_set)

my_set.remove("January")
print(my_set)

my_list = ["January", "February", "March", "January"]
my_list.remove("January")
print(my_list)