# Strategy Pattern looks like decorator
from abc import ABC, abstractmethod

#Strategy Interface
class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, base_price):
        pass

# Concrete Strategies
class SummerPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price * 0.90 # 10% discount

class AutumnPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price * 0.80 # 20% discount

class RegularPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price

class Thing:
    def __init__(self, name, base_price, pricing_strategy):
        self.name = name
        self.base_price = base_price
        self.pricing_strategy = pricing_strategy

    def get_price(self):
       return self.pricing_strategy.calculate(self.base_price)

    def set_pricing_strategy(self, pricing_strategy: PricingStrategy):
        self.pricing_strategy = pricing_strategy

thing = Thing("Laptop", 100, RegularPricing())
# print(thing.base_price)
print((f'Base price: {thing.get_price()}'))

thing.set_pricing_strategy(SummerPricing())
print((f'Summer price: {thing.get_price()}'))

thing.set_pricing_strategy(AutumnPricing())
print((f'Autumn price: {thing.get_price()}'))