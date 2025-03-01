book_title = "Book title"
book_price = 20
book_quantity = 5

tax_rate = 0.08

def calculate_total_price (book_price, book_quantity, tax_rate):
    total_price = book_price * book_quantity
    total_price_with_tax = total_price + (total_price * tax_rate)
    return total_price_with_tax


def greet_customer():
    print("Welcome to the bookstore")

"""
Phyton comment 
mitme reaga
"""

purchase_amount = 100

if purchase_amount >= 50:
    print("you qualify for 10% discount")
else:
    print("no discount available")

books = ["Book 1", "Book 2", "Book 3"]

for book in books:
    print(book)

#kasutan loopse siin

discounted_prices = []
for price in [100, 150, 200]:
    discounted_prices.append(price * 0.9)

discounted_prices = [price * 0.9 for price in [100, 150, 200]]
print(discounted_prices)

#error handling (try-except blocks)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("you cannot divide by zero")

#writing readable code

#bad example 

def process_order(order):
    total = 0
    for item in order:
        price = item["price"]
        discount = item["discount"]
        discounted_prices = price - (price * discount / 100)
        total += discounted_prices
        print("Total price: {total}")

#good example

def calculate_discount_price(price, discount):
    return price - (price * discount / 100)

def get_order_total(order):
    total = sum(calculate_discounted_price(item["price"], item["discount"]) for item in order)
    return total

def print_order_total(order):
    total = get_order_total(order)
    print(total)

#avoid deep nesting

#bad example (too many nested levels)

def process_scores(scores):
    for score in scores:
        if score >= 50:
            if score >= 17:
                if score >= 90:
                    print("excellent score")
                else:
                    print("good score")
            else:
                print("passed")
        else:
            print("failed")

# good example

def process_scores(scores):
    for score in scores:
        if score < 50:
            print("fail")
        if score < 70:
                print("pass")
        if score < 90:
                print("good")
                continue
        print("excellent")

#restoranimenüü ülesanne

def get_menu():
    return ["Salad", "pizza", "pasta"]

def take_order(dish):
    return f"Order taken dish {dish}"

def process_payment(amount):
    return f"payment of dish {amount}"

def main():
    items = menu.get_menu()
    print("Menu", items)

    order_taken = order.take_order(items[0]
    print(order_taken))

    total_amount = 15
    payment_status = payment.process_payment(total_amount)
    print(payment_status)

#ühe faili teise faili saatmine
if __name__ == "__name":
    main()

#Võib olla suuremas moodulis või väiksemas.
def plan_birthday_party()
    print("ordering cake")
    print("sending invitations")
    print("preparing decorations")
    print("getting gifts")

def order_cake():
    print(order_cake)


