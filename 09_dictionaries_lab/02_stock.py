stock_list = input().split()
product_for_search = input().split()

stock_dict = {}

for index in range(0, len(stock_list), 2):
    product = stock_list[index]
    quantity = stock_list[index + 1]
    stock_dict[product] = quantity

for data in product_for_search:
    if data in stock_dict.keys():
        print(f"We have {stock_dict[data]} of {data} left")
    else:
        print(f"Sorry, we don't have {data}")

