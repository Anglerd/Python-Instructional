import card
from utils import get_input
import db_connector

def input_card(set_number):
    name = input("Enter the name of the card you would like to enter")
    category = card.check_enums("category")
    poke_type = card.check_enums("type")
    rarity = card.check_enums("rarity")
    return card.Card(set_number, name, category, poke_type, rarity)

def print_card(card_num, cards, poke_set):
    output_string = ""
    output_string += str(cards[card_num - 1])
    output_string += " this set is called "
    output_string += poke_set[cards[card_num - 1].set_number - 1].name
    print(output_string)
    # print(f"{cards[card_num - 1]} this set is called {poke_set[cards[card_num - 1].set_number - 1].name}")

def view_menu():
    print("------------------------------------")
    print("Pokemon card set viewer and updater")
    print("------------------------------------")
    print("Choose an option from the menu below")
    print("1. Exit/Quit (DOES NOT SAVE, to save choose to not continue)")
    print("2. Add a card to the database")
    print("3. Add a set to the database")
    print("4. View cards in a set")
    print("5. View all cards")
    print("6. View set names")
    print("7. View a specific card")

if __name__ == "__main__":
    all_sets, all_cards = db_connector.get_all_from_db()
    new_sets = []
    new_cards = []
    while True:
        # continue goes here and goes to the next step in the loop
        view_menu()
        user_input = get_input("", int)
        if user_input == 1:
            print("Goodbye")
            exit()
        if user_input in [2, 3]:
            set_used = True
            add_set = False
            if user_input == 2: # if adding a card
                set_number = get_input("Enter the set number to for this card", int)
                if len(all_sets) < set_number: # if the set is not already in all_sets
                    if len(all_sets) + 1 != set_number: # we do not add more than 1 set at a time
                        print(f"There are too many sets missing between what exists in memory and what you input, please input a lower set. The current highest set in memory is the {all_sets[-1].name} set, which is set number {len(all_sets)}")
                        set_used = False # we have failed to determine the set of this card
                    else:
                        add_set = True
            if user_input == 3 or add_set: # if adding a set or the set of the card is a new eligible set
                this_new_set = card.Set(input(f"Enter the name of set number {len(all_sets) + 1}"))
                all_sets.append(this_new_set)
                new_sets.append(this_new_set)
            if user_input == 2 and set_used:
                this_new_card = input_card(set_number)
                all_cards.append(this_new_card)
                new_cards.append(this_new_card)
        elif user_input == 4:
            set_to_view = get_input("Which set would you like to view?", int)
            for index, this_card in enumerate(all_cards):
                if this_card.set_number == set_to_view:
                    print_card(index + 1, all_cards, all_sets)
        elif user_input == 5:
            for index, this_card in enumerate(all_cards):
                print_card(index + 1, all_cards, all_sets)
        elif user_input == 6:
            for index, this_set in enumerate(all_sets):
                print(f"Set number {index + 1} is called {this_set.name}")
        elif user_input == 7:
            print_card(get_input("Enter the number of the card you would like to view", int), all_cards, all_sets)
        if "y" not in input("Would you like to continue?: y/n").lower():
            break
    # break goes down here
    for this_set in new_sets:
        print(f"{this_set.name} set added to db")
        db_connector.save_set(this_set.name)
    for index, this_card in enumerate(new_cards):
        print_card(index + 1, new_cards, all_sets)
        db_connector.save_card(this_card.set_number, this_card.name, this_card.category, this_card.type, this_card.rarity)
    