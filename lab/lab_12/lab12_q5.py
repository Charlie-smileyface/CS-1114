def add_entry(contacts, name, number):
    if name not in contacts:
        if number.isdigit() and len(number) == 10:
            contacts[name] = number
        else:
            print("Invalid number")
    else:
        print("name already exist")

def look_up(contracts, name):
    return contracts[name] if name in contracts else f"{name} does not exist in {contracts}"

def delete_entry(contracts, name):
    if name in contracts:
        del contracts[name]
    else:
        print(f"{name} not found in {contracts}")

def print_all(contracts):
    items = tuple(contracts.items())
    for item in items:
        print("\t".join(item))

def main():
    contracts = {}
    user_input = input("Enter an option: ")
    while user_input != 'Q':
        if user_input == "A":
            name = input("Enter a name: ")
            number = input("Enter a number: ")
            add_entry(contracts, name, number)
        elif user_input == "L":
            name = input("Enter a name: ")
            print(look_up(contracts, name))
        elif user_input == "D":
            name = input("Enter a name: ")
            delete_entry(contracts, name)
        elif user_input == "P":
            print_all(contracts)
        
        user_input = input("Enter an option: ")
main()