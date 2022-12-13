uomy_list = {char for char in 'hello'}

my_list2 = {num for num in range(100)}

my_list3 = {num**2 for num in range(100)}

my_list4 = {num**2 for num in range(100)
           if num % 2 == 0}

# Dictionary Comprehension
simple_dict = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
  'e': 5,
  'f': 6
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0 }

print(my_dict)
list1 = [7,2,66,43,94,24,22,11,57]

another_dict = {num:num*2 for num in list1}

print(another_dict)