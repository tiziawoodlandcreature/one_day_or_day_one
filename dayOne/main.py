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
def report() -> None:
    """Gibt den aktuellen Status des Automaten aus."""
    print("\n--- REPORT ---")
    print(f"Wasser: {resources['water_ml']} ml")
    print(f"Milch: {resources['milk_ml']} ml")
    print(f"Kaffee: {resources['coffee_g']} g")
    print(f"Geld: {euro_formater(amount=resources['money_eur'])}")

def euro_formater(amount: float) -> str:
    """Schöne Euro-Ausgabe"""
    # 35.50 -> 35,50 €
    # 24.2425 -> 24,24 €
    return f"{amount:.2f}".replace(".", ",") + " €"



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

        elif choice == "report":
            report()
            continue

        elif choice not in MENU:
            print("Ungültige Auswahl. Bitte 'Espresso', 'Latte' oder 'Cappuccino' eingeben.\n")

if __name__ == "__main__":
    main()