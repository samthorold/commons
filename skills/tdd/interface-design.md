# Interface Design for Testability

Good interfaces make testing natural:

1. **Accept dependencies, don't create them**

   ```python
   # Testable
   def process_order(order: Order, gateway: PaymentGateway) -> None: ...

   # Hard to test
   def process_order(order: Order) -> None:
       gateway = StripeGateway()
   ```

2. **Return results, don't produce side effects**

   ```python
   # Testable
   def calculate_discount(cart: Cart) -> Discount: ...

   # Hard to test
   def apply_discount(cart: Cart) -> None:
       cart.total -= discount
   ```

3. **Take randomness and time as parameters**

   ```python
   # Testable: the test passes random.Random(42)
   def shuffle_deck(deck: Deck, rng: random.Random) -> Deck: ...

   # Hard to test
   def shuffle_deck(deck: Deck) -> Deck:
       random.shuffle(deck.cards)
   ```

4. **Small surface area**
   - Fewer methods = fewer tests needed
   - Fewer params = simpler test setup
