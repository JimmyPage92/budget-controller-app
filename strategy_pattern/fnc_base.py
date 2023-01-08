from dataclasses import dataclass
from typing import Callable

DiscountFunction = Callable[[int], int]


def percentage_discount(price: int) -> int:
    return int(price * 0.2)


def fixed_discount(_: int) -> int:
    return 10_00


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountFunction

    def compute_total(self) -> int:
        discount = self.discount(self.price * self.quantity)
        return self.price * self.quantity - discount


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=percentage_discount)
    print(order)
    print(f"Total: ${order.compute_total() / 100:.2f}")


if __name__ == '__main__':
    main()
