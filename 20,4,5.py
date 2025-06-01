import json
from collections import defaultdict

def analyze_orders(filepath="orders_july_2023.json"):

    with open(filepath, "r") as f:
        orders = json.load(f)

    max_price = 0
    max_price_order = ""
    max_quantity = 0
    max_quantity_order = ""
    daily_orders = defaultdict(int)
    user_orders = defaultdict(int)
    user_total_spent = defaultdict(float)
    total_order_cost = 0
    total_items = 0

    for order_num, order_data in orders.items():
        date = order_data["date"]
        user_id = order_data["user_id"]
        quantity = order_data["quantity"]
        price = order_data["price"]

        if price > max_price:
            max_price = price
            max_price_order = order_num

        if quantity > max_quantity:
            max_quantity = quantity
            max_quantity_order = order_num

        daily_orders[date] += 1

        user_orders[user_id] += 1
        user_total_spent[user_id] += price

        total_order_cost += price
        total_items += quantity

    most_popular_date = max(daily_orders, key=daily_orders.get)

    most_frequent_user = max(user_orders, key=user_orders.get)

    top_spender = max(user_total_spent, key=user_total_spent.get)

    average_order_value = total_order_cost / len(orders)
    average_item_value = total_order_cost / total_items

    results = {
        "Номер самого дорогого заказа за июль": max_price_order,
        "номер заказа с самым большим количеством товаров": max_quantity_order,
        "День в июле С самым большими количеством товара": most_popular_date,
        "Пользователь с наибольшим числом заказов": most_frequent_user,
        "Пользователь с наибольшей суммой заказов": top_spender,
        "Средняя стоимость заказ": average_order_value,
        "Средняя стоимиость одного товара": average_item_value,
    }

    return results

if name == "main":
    results = analyze_orders()
    print(results)
