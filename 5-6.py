# List of favorite stores
favorite_stores = ["Target", "Best Buy", "Costco", "Amazon", "Walmart"]

# List of stores currently running sales
stores_on_sale = ["Amazon", "Costco", "Old Navy"]

# Loop through favorite stores and check if they are on sale
for store in favorite_stores:
    if store in stores_on_sale:
        print(f"{store} is having a sale!")
    else:
        print(f"{store} isn't currently running a sale.")