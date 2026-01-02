orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
juft_orders = []
for order in orders:
    if order[0] % 2 == 0:
        juft_orders.append(order)
print(juft_orders)