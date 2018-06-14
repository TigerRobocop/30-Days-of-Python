import datetime

# print("hello world")
names = ["Pastry", "Chocolate", "bear claw", "caramels", "chupa chups", "danish", "carrot cake", "jelly bean"]
amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.123323, 32.4, 99.99]

# message = """Tart gummies topping cake chocolate bar donut oat cake. Apple pie chocolate cake tootsie roll fruitcake. Oat cake fruitcake biscuit. Danish jelly beans gingerbread croissant danish sesame snaps. Bear claw lemon drops marzipan. Lemon drops gummies apple pie tart gingerbread marshmallow macaroon. Gingerbread marzipan liquorice sesame snaps marzipan. Bear claw cupcake halvah biscuit sugar plum chupa chups sesame snaps candy. Gingerbread bonbon toffee danish. Pastry powder danish cupcake tart fruitcake fruitcake cookie. Candy cake cheesecake souffle. Sesame snaps chupa chups jelly lemon drops ice cream tart cake fruitcake cake."""
unf_message = """Hi {name}

Thank yoy for your purchase on {date}.
Your total was ${total}

Liv

------------------------------------
"""



def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        new_date = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            new_msg = unf_message.format(
                name = name.title(),
                date = new_date,
                total = "%.2f" %(amounts[i])
            )
            i += 1
            print(new_msg)

make_messages(names, amounts)
