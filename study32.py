from study31 import MessageUser, random_function, random_two, make_messages

# print("abc")
obj = MessageUser()
obj.add_user("Pastry", 123.32, "email@email.com")
obj.add_user("Chocolate", 94.23)
obj.add_user("bear claw", 124.32)
obj.add_user("caramels", 323.4)
obj.add_user("chupa chups", 23)
obj.add_user("danish", 322.123323)
obj.add_user("carrot cake", 32.4)
obj.add_user("jelly bean", 99.99)
obj.get_details()

# print(obj.make_messages())

# random_two()

names = ["Pastry", "Chocolate", "bear claw", "caramels", "chupa chups", "danish", "carrot cake", "jelly bean"]
amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.123323, 32.4, 99.99]

make_messages(names, amounts)
