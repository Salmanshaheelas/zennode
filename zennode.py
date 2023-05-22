# Product catalog
catalog = [
    {"name": "Product A", "price": 20},
    {"name": "Product B", "price": 40},
    {"name": "Product C", "price": 50}
]

# Discount rules
def flat_10_discount(total):
    return 10 if total > 200 else 0

def bulk_5_discount(price, quantity):
    return price * 0.05 if quantity > 10 else 0

def bulk_10_discount(total_quantity, total_price):
    return total_price * 0.1 if total_quantity > 20 else 0

def tiered_50_discount(total_quantity, quantity, price):
    return (quantity - 15) * price * 0.5 if total_quantity > 30 and quantity > 15 else 0

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

def calculate_order():
    # Initialize variables
    subtotal = 0
    total_quantity = 0
    total_price = 0
    discount_amount = 0
    shipping_fee = 0
    gift_wrap_total_fee = 0

    # Get quantity and gift wrap information for each product
    for product in catalog:
        quantity = int(input(f"Enter the quantity of {product['name']}: "))
        wrapped_as_gift = input(f"Is {product['name']} wrapped as a gift? (yes/no): ").lower() == 'yes'

        # Calculate product total
        product_price = product['price']
        product_total = quantity * product_price

        # Calculate gift wrap fee
        gift_wrap_fee_for_product = gift_wrap_fee * quantity
        gift_wrap_total_fee += gift_wrap_fee_for_product if wrapped_as_gift else 0

        # Calculate discount for each product
        discount_amount_product = bulk_5_discount(product_price, quantity)
        discount_amount_product = max(discount_amount_product, bulk_10_discount(total_quantity, total_price))
        discount_amount_product = max(discount_amount_product, tiered_50_discount(total_quantity, quantity, product_price))

        # Update overall totals
        subtotal += product_total
        total_quantity += quantity
        total_price += product_price * quantity
        discount_amount = max(discount_amount_product, discount_amount)

    # Calculate shipping fee
    shipping_fee = (total_quantity // items_per_package) * shipping_fee_per_package

    # Calculate the total amount
    total = subtotal - discount_amount + shipping_fee + gift_wrap_total_fee

    # Output the details
    print("\nOrder Details:")
    print("--------------------------")
    for product in catalog:
        quantity = int(input(f"Enter the quantity of {product['name']}: "))
        product_total = quantity * product['price']
        print(f"Product: {product['name']}")
        print(f"Quantity: {quantity}")
        print(f"Total: ${product_total}")
        print("--------------------------")
    print(f"Subtotal: ${subtotal}")
    print(f"Discount Applied: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_total_fee}")
    print(f"Total: ${total}")

calculate_order()
