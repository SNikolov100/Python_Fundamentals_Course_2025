import re
count_barcodes = int(input())
product = ""
for _ in range(count_barcodes):
    product_group = ""
    barcode = input()
    pattern = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)"
    product_name = re.findall(pattern, barcode)
    if not product_name:
        print("Invalid barcode")
        continue
    for data in product_name:
        product = data[1]
    new_pattern = r"[\d*]"
    product_number = re.findall(new_pattern, product)
    if not product_number:
        product_group = "00"
    for data in product_number:
        if data:
            product_group += data
    print(f"Product group: {product_group}")

