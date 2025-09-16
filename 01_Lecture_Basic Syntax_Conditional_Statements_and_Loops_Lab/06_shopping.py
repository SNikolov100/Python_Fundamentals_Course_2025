budget = int(input())

while True:

    price_product = input()
    if price_product == "End":
        print("You bought everything needed.")
        break
    else:
        budget -= int(price_product)
        if budget < 0:
            print("You went in overdraft!")
            break
