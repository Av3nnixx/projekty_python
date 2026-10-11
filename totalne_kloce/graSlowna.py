from random import shuffle
columns = [1,2,3]
rows = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","Z"]
new_row = []
def set_field():
    y = 0
    x = 5
    # setting field
    for c in range(5):
        shuffle(rows)
        print(rows[y:x])
        new_row.extend(rows[y:x])
        x += 5
        y += 5
def show_field():
    y = 0
    x = 5
    # showing field
    for c in range(5):
        print(new_row[y:x])
        x += 5
        y += 5


def search_value(letter):
    #give index of letter
    for index,litera in enumerate(new_row):
        if letter == litera:
            yield index

def place_symbol(symbol,place,selected_index):
    selected_index = selected_index - 1 #latwiejsze dla osob ktore chca zagrac
    # place to indexy - lista
    # change letters
    aiming_letter = place[selected_index] #position to number
    new_row[aiming_letter] = symbol
    show_field()
def play():
    set_field()
    while True:
        to_replace = input("Wprowadz litere którą chcesz zamienić: ").upper()# a-i
        symbol_to_place = input("Wprowadz litere którą chcesz dodać: ").upper()
        number,symbol = to_replace[1],to_replace[0]
        number = int(number) #by nie bylo errora
        place_symbol(symbol_to_place,list(search_value(symbol)),number)
play()