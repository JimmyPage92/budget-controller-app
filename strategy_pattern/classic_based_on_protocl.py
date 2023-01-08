from dataclasses import dataclass
from typing import Protocol


class DiscountStrategy(Protocol):
    def compute(self, price: int) -> int:
        """Compute the discount for the give price."""


class PercentageDiscount:
    def compute(self, price: int) -> int:
        return int(price * 0.20)


class FixedDiscount:
    def compute(self, _: int) -> int:
        return 10_00


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountStrategy

    def compute_total(self) -> int:
        discount = self.discount.compute(self.price * self.quantity)
        return self.price * self.quantity - discount


def main() -> None:
    order = Order(price=100_00, quantity=2, discount=PercentageDiscount())
    print(order)
    print(f"Total: ${order.compute_total() / 100:.2f}")


if __name__ == '__main__':
    main()
