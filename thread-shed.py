daily_sales_replaced = daily_sales.replace(";,;", ";")

daily_transactions = daily_sales_replaced.split(",")
print(daily_transactions)

daily_transactions_split = []
for transaction in daily_transactions:
  daily_transactions_split.append(transaction.split(";"))

print(daily_transactions_split)

transactions_clean = []
for transaction in daily_transactions_split:
  transaction_clean = []
  for data_point in transaction:
    transaction_clean.append(data_point.strip())
  transactions_clean.append(transaction_clean)

print(transactions_clean)

customers = []
sales = []
thread_sold = []

for transaction in transactions_clean:
  customers.append(transaction[0])
  sales.append(transaction[1])
  thread_sold.append(transaction[2])

total_sales = 0
for sale in sales:
  total_sales += float(sale.strip("$"))

print(total_sales)

print(thread_sold)

thread_sold_split = []
for sale in thread_sold:
  for color in sale.split("&"):
    thread_sold_split.append(color)

def color_count(color):
  count = 0
  for item_color in thread_sold_split:
    if item_color == color:
      count += 1
  return count

color_counter = color_count('white')
print(color_counter)

colors = ['red','yellow','green','white','black','blue','purple']
for color in colors:
  print("Thread Shed sold {} threads of {} thread today.".format(color_count(color), color))
