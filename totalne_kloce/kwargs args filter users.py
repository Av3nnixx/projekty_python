
users1 = [
    {"name": "Antek", "age": 17, "city": "Lodz"},
    {"name": "Kuba", "age": 20, "city": "Warszawa"},
    {"name": "Ola", "age": 19, "city": "Lodz"},
    {"name": "Maja", "age": 22, "city": "Krakow"}
]
def filter_users(users, *restriction,**kwargs):
    def add_user():
        for kwarg in kwargs.values():
            print(kwarg)
            users1.append(kwarg)
    def filter_restriction(user):
        if user["age"] < 18:
            print(f"Osoba {user['name']} jest niepełnoletnia")
            return False
        for res in restriction:
            if res(user):
                return False
        return True
    add_user()
    wynik = filter(filter_restriction ,users)
    print(list(us["name"] for us in wynik))
filter_users(users1,lambda x: x["city"] == "Lodz",lambda x: x["name"].startswith("G"),new_user = {"name": "Andrzej", "age": 41, "city": "Lublin"})
