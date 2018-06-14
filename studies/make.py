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