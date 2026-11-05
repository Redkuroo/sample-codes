vehicles = {"Toyota": "Corolla", "Honda": "Civic"}

# 1. Loop through Keys only
for brand in vehicles.keys():
    print(f"Brand: {brand}")

# 2. Loop through Values only
for model in vehicles.values():
    print(f"Model: {model}")

# 3. Loop through BOTH (Key and Value)
for brand, model in vehicles.items():
    print(f"{brand} makes the {model}")
