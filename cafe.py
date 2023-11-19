# This program will store details about stock items in a cafe, and calculate the total stock value of the cafe.

########## List of cafe items ################
list_menu = ["steak", "tortilla", "peppers", "haggis"]

########## Dictionary of stock amoounts #############
dict_stock = {'steak': 200,
        'tortilla': 150,
        'peppers': 400,
        'haggis': 1
}

########## Distionary of stock prices #################
dict_price = {'steak': 3,
              'tortilla': 2,
              'peppers': 0.5,
              'haggis': 500
}

######## Calculate total stock value in cafe ##################

i = 0
total_stock = 0
while i < len(list_menu):
    total_stock = total_stock + (dict_stock[list_menu[i]] * dict_price[list_menu[i]])
    i = i + 1

print(f"The total value of stock in the cafe is £" + str(total_stock) + ".\n")
