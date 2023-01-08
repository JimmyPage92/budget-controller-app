from dataclasses import dataclass
from typing import Callable

DiscountFunction = Callable[[int], int]


def percentage_discount(percentage: float) -> DiscountFunction:
    return lambda price: int(price * percentage)


def fixed_discount(fixed: int) -> DiscountFunction:
    return lambda _: fixed


def black_week_discount(_) -> DiscountFunction:
    return lambda price: int(price * .5)


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountFunction

    def compute_total(self) -> int:
        discount = self.discount(self.price * self.quantity)
        return self.price * self.quantity - discount


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=black_week_discount(0))
    print(order)
    print(f"Total: ${order.compute_total() / 100:.2f}")


if __name__ == '__main__':
    main()
