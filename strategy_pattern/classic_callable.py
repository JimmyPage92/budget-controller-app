from dataclasses import dataclass
from typing import Callable

DiscountFunction = Callable[[int], int]


@dataclass
class PercentageDiscount:
    percentage: float

    def __call__(self, price: int) -> int:
        return int(price * self.percentage)


@dataclass
class FixedDiscount:
    fixed: int

    def __call__(self, _: int) -> int:
        return self.fixed


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountFunction

    def compute_total(self) -> int:
        discount = self.discount(self.price * self.quantity)
        return self.price * self.quantity - discount


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=PercentageDiscount(0.2))
    print(order)
    print(f"Total: ${order.compute_total() / 100:.2f}")


if __name__ == '__main__':
    main()
