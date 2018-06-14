import datetime

class MessageUser:
    user_details = []
    messages = []
    base_message = """Hi {name}

Thank yoy for your purchase on {date}.
Your total was ${total}

Liv

------------------------------------
"""
    def add_user(self, name, amount, email=None):
        name = name.title()
        amount = "%.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount
        }
        current_date = datetime.date.today()
        current_datestr = "{current_date.month}/{current_date.day}/{current_date.year}".format(current_date=current_date)
        detail["date"] = current_datestr
        if email is not None:
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messages.append(new_msg) 
            return self.messages
        return []
    # def make_messages(self):
    #     if len(self.user_details) > 0:
    #         for detail in self.get_details():
    #             sname = detail["name"]
    #             samount = detail["amount"]
    #             sdate = detail["date"]
    #             message = self.base_message
    #             new_msg = message.format(
    #                 name = sname,
    #                 date = sdate,
    #                 total = samount
    #             )
    #             self.messages.append(new_msg)
    #         return self.messages
    #     return []

# names = ["Pastry", "Chocolate", "bear claw", "caramels", "chupa chups", "danish", "carrot cake", "jelly bean"]
# amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.123323, 32.4, 99.99]

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


# base_message = """Hi {name}

# Thank yoy for your purchase on {date}.
# Your total was ${total}

# Liv

# ------------------------------------
# """
# message = base_message
# new_msg = message.format(
#     name = "a",
#     date = "b",
#     total = "c"
# )


class Person:
    dob = datetime.date.today()
    @property
    def str_dob(self):
        return '{self.dob.month}/{self.dob.day}/{self.dob.year}'.format(self=self)


class Animal():
    noise = "Grunt"
    size = "latge"
    color = "bronw"
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise

dog = Animal()
dog.make_noise()


class Dog(Animal):
    name = "Jonhn"
    
