# When to Mock

Mock at **system boundaries** only:

- External APIs (payment, email, etc.)
- Databases (sometimes - prefer a test DB, or SQLite in `tmp_path`)
- Time/randomness
- File system (sometimes - prefer `tmp_path`)

Don't mock:

- Your own classes/modules
- Internal collaborators
- Anything you control

## Designing for Mockability

At system boundaries, design interfaces that are easy to replace:

**1. Use dependency injection**

Pass external dependencies in rather than creating them internally:

```python
# Easy to replace: the test passes a fake client
def process_payment(order: Order, client: PaymentClient) -> Receipt:
    return client.charge(order.total)

# Hard to replace: only patching can reach it
def process_payment(order: Order) -> Receipt:
    client = StripeClient(os.environ["STRIPE_KEY"])
    return client.charge(order.total)
```

A fake is a small class with the boundary's interface; a `typing.Protocol` keeps it honest:

```python
class PaymentClient(Protocol):
    def charge(self, amount: Decimal) -> Receipt: ...

class FakePaymentClient:
    def __init__(self) -> None:
        self.charged: list[Decimal] = []

    def charge(self, amount: Decimal) -> Receipt:
        self.charged.append(amount)
        return Receipt(status="confirmed")
```

**2. Prefer SDK-style interfaces over generic fetchers**

Create specific functions for each external operation instead of one generic function with conditional logic:

```python
# GOOD: each operation is independently fakeable
class ShopApi(Protocol):
    def get_user(self, user_id: str) -> User: ...
    def get_orders(self, user_id: str) -> list[Order]: ...
    def create_order(self, data: NewOrder) -> Order: ...

# BAD: a fake needs conditional logic on the endpoint
class ShopApi(Protocol):
    def request(self, method: str, path: str, body: dict | None = None) -> dict: ...
```

The SDK approach means:
- Each fake returns one specific shape
- No conditional logic in test setup
- Easier to see which operations a test exercises
- Type checking per operation
