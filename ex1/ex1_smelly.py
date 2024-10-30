class OrderValidator:
    def validate_order(self, order):
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")


class PriceCalculator:
    def calculate_total(self, items):
        return sum(item["price"] * item["quantity"] for item in items)

    def apply_discount(self, total_price, discount_code):
        if discount_code == "SUMMER20":
            return total_price * 0.8  # 20% discount
        elif discount_code == "WELCOME10":
            return total_price * 0.9  # 10% discount
        return total_price


class InventoryManager:
    def update_inventory(self, items):
        for item in items:
            print(
                f"Updating inventory for item {item['id']}, reducing stock by {item['quantity']}."
            )


class ReceiptGenerator:
    def generate_receipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt


class EmailService:
    def send_confirmation(self, customer_id, receipt):
        print(f"Sending email to customer {customer_id} with receipt:\n{receipt}")


class OrderProcessor:
    def __init__(self):
        self.validator = OrderValidator()
        self.calculator = PriceCalculator()
        self.inventory = InventoryManager()
        self.receipt_gen = ReceiptGenerator()
        self.email_service = EmailService()

    def process_order(self, order):
        # Step 1: Validate order details
        self.validator.validate_order(order)

        # Step 2: Calculate total price
        total_price = self.calculator.calculate_total(order["items"])

        # Step 3: Apply discounts if applicable
        total_price = self.calculator.apply_discount(
            total_price, order.get("discount_code")
        )

        # Step 4: Update inventory
        self.inventory.update_inventory(order["items"])

        # Step 5: Generate receipt
        receipt = self.receipt_gen.generate_receipt(order, total_price)

        # Step 6: Send confirmation email
        self.email_service.send_confirmation(order["customer_id"], receipt)

        return receipt
