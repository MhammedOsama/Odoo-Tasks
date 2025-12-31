def log_action(func):
    def wrapper(self):
        print("[LOG] Before executing " + func.__name__ + "()")
        result = func(self)
        print("[LOG] After executing " + func.__name__ + "()")
        return result
    return wrapper


class Order:
    
    def __init__(self, order_id, customer_name, amount, status="draft"):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount
        self.status = status
    
    @log_action
    def confirm_order(self):
        self.status = "confirmed"
        print("Order confirmed!")
    
    @log_action
    def cancel_order(self):
        self.status = "cancelled"
        print("Order cancelled!")
    
    def display_info(self):
        print(
            "Order #" + str(self.order_id) +
            " for " + self.customer_name +
            " - Amount: " + str(self.amount) +
            " - Status: " + self.status
        )
