
def find_top_seller(products: dict, sales: dict) -> str:
    max_tushum = 0
    top_product = ""

    for mahsulot in products:
        tushum = products[mahsulot] * sales[mahsulot]

        if tushum > max_tushum:
            max_tushum = tushum
            top_product = mahsulot

    return top_product


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10, "Banan": 5, "Uzum": 8}
))
