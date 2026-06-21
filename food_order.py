menu = {
    "pizza": 200,
    "burger": 120,
    "fries": 80,
    "coke": 50
}

def food_list(menu):
    print("\n----- MENU -----")
    for food, price in menu.items():
        print(f"{food} - ₹{price}")

food_list(menu)

total = 0

while True:
    choice = input("\nEnter food you like: ").strip().lower()

    if choice in menu:
        print(f"{choice} added to your order.")
        total += menu[choice]
    else:
        print("Sorry, that's not available.")

    more = input("Do you want to order more? (yes/no): ").lower()

    if more != "yes":
        print("\nThank you for your order!")
        break

print(f"Total bill = ₹{total}")