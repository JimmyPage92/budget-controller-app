from dataclasses import dataclass


@dataclass
class Order:
    price: int
    quantity: int

    def compute_total(self, discount_type: str) -> int:
        if discount_type == "percentage":
            discount = int(self.price * self.quantity * .2)
        elif discount_type == "fixed":
            discount = 10_00
        else:
            discount = 0
        return self.price * self.quantity - discount


def main() -> None:
    order = Order(price=100_00, quantity=2)
    print(order)
    print(f"Total: ${order.compute_total('percentage') / 100:.2f}")


if __name__ == '__main__':
    main()
