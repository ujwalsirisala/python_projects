wallet = 500
item_cost = 150
tax_percent = .03
tax_amount = item_cost * tax_percent
price = item_cost + tax_amount

print (price)
remaining_price = wallet - price
print (remaining_price)


print (500 - 150 - (150 * .03))