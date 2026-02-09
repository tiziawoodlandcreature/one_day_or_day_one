MENU = {
    "espresso": {
        "price": 8.80,
        "needs": {"water_ml": 50, "milk_ml": 100, "coffee_g": 15}
    },
    "cappuccino": {
        "price": 5.20,
        "needs": {"water_ml": 50, "milk_ml": 200, "coffee_g": 15} 
    },
    "latte": {
        "price": 4.80,
        "needs": {"water_ml": 0, "milk_ml": 250, "coffee_g": 25} 
    }
}

ACCEPTED_COINS = [0.05, 0.10, 0.20, 1.00, 2.00]

resources = {
    "water_ml": 150,
    "milk_ml": 50,
    "coffee_g": 75,
    "money_eur": 35.50
}
# ---------------------
# Hilfsfunktionen
# ---------------------
def report():
    pass


# ---------------------
# Hauptprogramm
# ---------------------
def main():
    while True:
        print("=== Kaffeeautomat ===")
        print("Unsere Getränke: Espresso | Latte | Cappuccino\n")
        
        choice = input("Getränk auswählen: ")
        if choice == "off":
            print("Automat wird ausgeschaltet")
            break
        if choice == "report":
            report()
            continue
        if choice not in MENU:
            print("Ungültige Auswahl. Bitte 'Espresso', 'Latte' oder 'Cappuccino' eingeben.\n")

if __name__ == "__main__":
    main()