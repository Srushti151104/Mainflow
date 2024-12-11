#creating a list
my_list=[23,7,56,45,9,6]
#adding an element
my_list.append(31)
#removing an element
my_list.remove(9)
#modifying
my_list[1]=22
print("updated list:",my_list)


#creating a dictionary
my_dict={"name":"arun","age":23,"place":"banglore"}
#adding
my_dict["gender"]="male"
#removing
del my_dict["place"]
#modifying
my_dict["age"]=34
print("updated dictionary:",my_dict)


#creating a set
my_set={34,12,11,76,56}
#adding
my_set.add(16)
#removing
my_set.remove(11)
#modifying
my_set.discard(12)
my_set.add(22)

print("updated set:",my_set)