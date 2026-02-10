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
    "milk_ml": 150,
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
    print("-----------\n")

def euro_formater(amount: float) -> str:
    """Schöne Euro-Ausgabe"""
    # 35.50 -> 35,50 €
    # 24.2425 -> 24,24 €
    return f"{amount:.2f}".replace(".", ",") + " €"

# Tuple Beispiel: (True, [Milch, Apfel...])
# Tuple Beispiel: (True, "Gandalf")
def ingredients_ok(drink_key: str) -> tuple[bool, list[str]]:
    """
    Prüft, ob genug Zutaten für das Getränk vorhanden sind.
    Rückgabe:
    - (True, []) wenn alles vorhanden ist
    - (False, [liste_der_fehlenden_zutaten]) wenn etwas fehlt
    """
    missing_ingredients = []
    needs = MENU[drink_key]["needs"] # In "needs" ist {'water_ml': 50, 'milk_ml': 100, 'coffee_g': 15}
    for ing, amount_needed in needs.items():
        if resources[ing] < amount_needed:
            pretty = ing.replace("_ml", "").replace("_g", "")
            missing_ingredients.append(pretty)
    
    if missing_ingredients:
        return False, missing_ingredients
    return True, []
    
# ---------------------
# Hauptprogramm
# ---------------------
def main():
    while True:
        print("=== Kaffeeautomat ===")
        print("Unsere Getränke: Espresso | Latte | Cappuccino\n")
        
        choice = input("Getränk auswählen: ").lower().strip()
        if choice == "off":
            print("Automat wird ausgeschaltet")
            break
        if choice == "report":
            report()
            continue
        if choice not in MENU:
            print("Ungültige Auswahl. Bitte 'Espresso', 'Latte' oder 'Cappuccino' eingeben.\n")
            
        ok, missing = ingredients_ok(choice)
        if not ok:
            print("Folgende Zutaten fehlen für dieses Getränk:")
            for ingredient in missing:
                print(f"- {ingredient}")
            print()
            continue
    
        price = MENU[choice]["price"]
        print(f"\nDu hast gewählt: {choice.capitalize()}")
        print(f"Zu bezahlen: {euro_formater(price)}")

if __name__ == "__main__":
    main()