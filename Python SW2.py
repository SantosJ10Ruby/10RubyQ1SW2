restaurant_name = "Lova Pizza"
owner_name = "Johann Santos"

year_established = 2025

tax_rate = 0.09  # 9% tax

has_delivery = True
is_dine_in = False

product_names = ["Pepperoni Cheese Lava 11″", "Magma Mozarella 11″", "Classic Margherita 11″, "Ham and Mushroom 11″", "Cheese Lover’s Dream 11″, "Nutella Pizza 11″"]

business_hours = "7:00 a.m. - 11:00 p.m."

menu_prices = {
    "Pepperoni Cheese Lava 11″": 660.00,
    "Magma Mozarella 11″": 735.00,
    "Classic Margherita 11″": 660.00,
    "Ham and Mushroom 11″": 550.00,
    "Cheese Lover’s Dream 11″": 660.00,
    "Nutella Pizza 11″": 550.00
}

common_allergens = ["Dairy", "Gluten", "Nuts"]

display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Established {year_established}", target="Established")
display(f"Menu Pricelist", target="heading1")

display(product_names[0], target="prod1")
display(f"₱{menu['Pepperoni Cheese Lava 11']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Magma Mozarella 11']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Classic Margherita 11']:.2f}", target="price3")
display(product_names[3], target="prod4")
display(f"₱{menu['Ham and Mushroom 11']:.2f}", target="price4")
display(product_names[4], target="prod5")
display(f"₱{menu['Cheese Lover’s Dream 11']:.2f}", target="price5")
display(product_names[5], target="prod6")
display(f"₱{menu['Nutella Pizza 11']:.2f}", target="price6")

display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

display(f"Delivery Always Available", target="orderType")