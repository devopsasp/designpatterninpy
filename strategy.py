# Strategy interface
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError('Payment strategy must implement pay method')


# Concrete strategies
class CreditCardStrategy(PaymentStrategy):
    def __init__(self, number, expiration):
        self.number = number
        self.expiration = expiration

    def pay(self, amount):
        print(f'Paying {amount} using credit card {self.number} expiring {self.expiration}')


class PayPalStrategy(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f'Paying {amount} using PayPal account {self.email}')


# Context
class PaymentGateway:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


# Client code
credit_card_strategy = CreditCardStrategy('1234-5678-9012-3456', '12/25')
paypal_strategy = PayPalStrategy('user@example.com')

payment_gateway = PaymentGateway(credit_card_strategy)
payment_gateway.pay(100)  # Paying 100 using credit card 1234-5678-9012-3456 expiring 12/25

payment_gateway.set_strategy(paypal_strategy)
payment_gateway.pay(200)  # Paying 200 using PayPal account user@example.com