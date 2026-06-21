products ={
  "Laptop": 1800,
  "Mouse": 25,
  "Keyboard": 75,
  "Monitor": 300, 
  "Headphones": 150
}
value = max(products.values())
for key in products.keys():
  if products[key]==value:
    print(f"The product with the highest price is {key} : ${value}.")