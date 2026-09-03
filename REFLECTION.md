# TDD Lab Retrospective

## 1. Test and Production Code Ratio
We currently have **6 tests** in `test_kitchen.py` and approximately **32 lines** of production code in `kitchen.py`. This gives a ratio of about 1 test for every 5 lines of production code, demonstrating how granular tests are driving the development of the codebase step by step.

## 2. Longest RED Phase
The RED phase was the longest during **Step A6**, dealing with `Expression`, `Sum`, and `Converter`. This step required introducing new structural concepts (like a standalone `Converter` class and a `Sum` node for an expression tree) before the test could pass. It required setting up the scaffolding of the expression tree logic so `Converter.reduce` could handle `Sum` objects, leading to an intermediate RED 2 phase that intentionally broke `Converter` to motivate implementing `reduce` across multiple classes.

## 3. TDD Patterns Used
- **Fake It:** Used in **Step A1**, where we hardcoded `self.amount = 600` inside `times()` to make the test pass quickly without implementing real logic.
- **Triangulate:** Used in **Step A2**, where we introduced `test_multiplication_by_two`. Having two different inputs forced us to replace the hardcoded `600` with actual multiplication logic `self.amount = self.amount * multiplier`.
- **Obvious Implementation:** Used in **Step A4** (Equality) where we directly implemented the `__eq__` and `__repr__` methods right away instead of faking equality first, because the exact implementation (`self.amount == other.amount`) was trivial and obvious.

## 4. Remaining Tasks on the Test List
The most significant item left on the test list is **cross-unit addition**, such as `grams(200).plus(ounces(1))`. Currently, our `Sum.reduce()` method blindly adds `left.amount + right.amount` without considering unit conversion. The `Converter` will need to be expanded to handle real conversion rates between different units (like grams and ounces).

## 5. Emergent Design (Quantity.reduce)
If this was designed upfront on paper, we likely would not have designed `Quantity.reduce` or `Sum` this way. A typical upfront design might have put an addition method directly on `Quantity` that performs an immediate conversion (e.g., converting everything to a base unit and returning a new `Quantity`). However, following TDD forced an **emergent design**: to support complex deferred conversions later, TDD led us to an **expression tree** (the `Sum` class). We then needed a polymorphic `reduce` method on both `Quantity` and `Sum` so the `Converter` could evaluate the expression node dynamically.
