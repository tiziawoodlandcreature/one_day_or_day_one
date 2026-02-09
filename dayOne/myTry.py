coffeebean(float)=500     #gramm
water(float)=2000         #millieliter
milk(float)=1000          #millieliter
money(float)=0            #gewicht des geldes nach den einzahlungen insgesamt

# ---------------------
# Dictonary
# ---------------------
drink = {
    "espresso": {
        "price": 8.80,
        "needs": {"water": 50, "milk": 100, "coffeebean": 15}
    },
    "cappuccino": {
        "price": 5.20,
        "needs": {"water": 50, "milk": 200, "coffeebean": 15} 
    },
    "latte": {
        "price": 4.80,
        "needs": {"water": 0, "milk": 250, "coffeebean": 25} 
    }
}

# ---------------------
# List
# ---------------------
nav = ["off","report"]

# ---------------------
# Hilfsfunktionen
# ---------------------
def report() -> None:
    """Gibt den aktuellen Status des Automaten aus."""

    print("\n--- REPORT ---")
    print(f"Wasser: {water} ml")
    print(f"Milch: {milk} ml")
    print(f"Kaffee: {coffeebean} g")
