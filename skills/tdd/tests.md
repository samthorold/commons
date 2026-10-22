# Good and Bad Tests

Examples are Python (pytest); the Stack's Guide says how its tests are written.

## Good Tests

**Integration-style**: Test through real interfaces, not mocks of internal parts.

```python
# GOOD: Tests observable behavior
def test_user_can_check_out_a_valid_cart():
    cart = Cart()
    cart.add(product)
    result = checkout(cart, payment_method)
    assert result.status == "confirmed"
```

Characteristics:

- Tests behavior users/callers care about
- Uses public API only
- Survives internal refactors
- Describes WHAT, not HOW
- One logical assertion per test

## Bad Tests

**Implementation-detail tests**: Coupled to internal structure.

```python
# BAD: Tests implementation details
def test_checkout_calls_payment_service(monkeypatch):
    calls = []
    monkeypatch.setattr(payments, "process", lambda total: calls.append(total))
    checkout(cart, payment_method)
    assert calls == [cart.total]
```

Red flags:

- Mocking or patching internal collaborators
- Testing private (`_underscore`) functions
- Asserting on call counts/order
- Test breaks when refactoring without behavior change
- Test name describes HOW not WHAT
- Verifying through external means instead of interface

```python
# BAD: Bypasses interface to verify
def test_create_user_saves_to_database(db):
    create_user(name="Alice")
    row = db.execute("SELECT * FROM users WHERE name = ?", ("Alice",)).fetchone()
    assert row is not None

# GOOD: Verifies through interface
def test_created_user_is_retrievable():
    user = create_user(name="Alice")
    assert get_user(user.id).name == "Alice"
```

## Tests where exact assertions are hard

For stochastic or search-heavy code (simulations, game search), assert on what must hold, under a seed:

```python
def test_energy_is_conserved_over_a_seeded_run():
    world = World.initial(rng=random.Random(42))
    before = world.total_energy()
    for _ in range(1_000):
        world = world.step()
    assert world.total_energy() == pytest.approx(before)
```

The Archetype's Guide, where there is one, says which invariants and properties count as evidence.
