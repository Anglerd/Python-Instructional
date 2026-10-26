import input_insert, constructor, db_connector

def display_menu():
    while True:
        print("--------------------------------")
        print("DnD style narrative constructor")
        print("--------------------------------")
        print("1. Create a character")
        print("2. Record an action")
        print("3. Add adjective to database")
        print("4. Construct narrative")
        print("5. Exit")
        print("--------------------------------")
        choice = input_insert.my_num_input("")
        if choice == 1:
            packet_for_sql = input_insert.prompt_character()
            db_connector.save_character(**packet_for_sql)
        elif choice == 2:
            packet_for_sql = input_insert.prompt_action()
            db_connector.save_action(**packet_for_sql)
        elif choice == 3:
            packet_for_sql = input_insert.prompt_adjective()
            db_connector.save_adjective(**packet_for_sql)
        elif choice == 4:
            all_characters, all_actions, all_adjectives = db_connector.get_all_from_db()
            for action in all_actions:
                print(action.make_sentence(all_adjectives))
            if input_insert.my_input("Would you like to continue? (y/n): ").lower() != "y":
                print("Goodbye")
                break
        else:
            print("Goodbye")
            break

if __name__ == "__main__":
    display_menu()