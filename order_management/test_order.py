from models.order import Order

order1 = Order(order_id=1, customer_name="Ashraf", amount=250)

order1.display_info()
order1.confirm_order()
order1.cancel_order()

