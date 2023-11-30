def catalog():
    ''' Prints to the console a catalog of items, their prices and the offers available. i.e, 10% discount for a purchase of 2 unique products and 25% for 3 products '''
    # A dictionary containing the values of items.
    products = {
        "item_1" : 200,
        "item_2" : 400,
        "item_3" : 600,    
    }
    # Computing the discounted price after purchasing 2 products. Subtracts the discount (10%) from the total amount payable.
    combo_1 = (products["item_1"] + products["item_2"]) - ((10/100) * (products["item_1"] + products["item_2"]))

    combo_2 = (products["item_2"] + products["item_3"]) - ((10/100) * (products["item_2"] + products["item_3"]))
    
    combo_3 = (products["item_1"] + products["item_3"]) - ((10/100) * (products["item_1"] + products["item_3"]))

    # Computing the discounted price after purchasing 3 products. Subtracts the discount (25%) from the total amount payable.
    combo_4 = (products["item_1"] + products["item_2"] + products["item_3"]) - ((25/100) * (products["item_1"] + products["item_2"]+products["item_3"]))

    # Printing the main ending, the hyphens-separator and the column endings.
    print("Online Store\n-------------------------------\nProduct(s)" + " "*29 + "Price")

    # A loop to get all the key value pairs in the dictionary. Use of string methods on the keys to get the desired names to display.
    for item, price in products.items():
        print(item.capitalize().replace("_", " ") + (" "*32), price)
    
    # Printing the Combo deals. I.e, the discounted price after purchasing more than one unique product.
    print("Combo 1(Item 1 + 2)" + " "* 19, combo_1)
    print("Combo 1(Item 2 + 3)" + " "* 19, combo_2)
    print("Combo 1(Item 1 + 3)" + " "* 19, combo_3)
    print("Combo 1(Item 1 + 2 + 3)" + " "* 15, combo_4, "\n" + "-"*30)

    # Printing the company's contact information.
    print("For delivery Contact: 98764678899")
    
# Calling the function.
catalog()

#Output:
'''
    Online Store
    -------------------------------
    Product(s)                             Price
    Item 1                                 200
    Item 2                                 400
    Item 3                                 600
    Combo 1(Item 1 + 2)                    540.0
    Combo 1(Item 2 + 3)                    900.0
    Combo 1(Item 1 + 3)                    720.0
    Combo 1(Item 1 + 2 + 3)                900.0
    ------------------------------
    For delivery Contact: 98764678899
'''