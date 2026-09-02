# 🧾 Python Billing System

A simple **Billing System developed using Python**.  
This project allows users to select products, enter quantities, calculate the total price, apply a discount, calculate GST, and generate the final bill.

##  Features

-  Display available products and prices
-  Add products to the cart
-  Enter product quantity
-  Calculate individual product total
-  Calculate subtotal
-  Apply 10% discount
-  Calculate 5% GST
-  Calculate grand total
-  Exit the billing system
-  Handle invalid product choices

## Technologies Used

- **Python 3**
- Lists
- Tuples
- Dictionaries
- `while` loop
- `if-else` statements
- User input
- Basic arithmetic operations
- Formatted strings (f-strings)

## Products

| No. | Product | Price |
|---:|---|---:|
| 1 | Rice | ₹50 |
| 2 | Wheat | ₹30 |
| 3 | Sugar | ₹40 |
| 4 | Salt | ₹20 |
| 5 | Oil | ₹100 |
| 6 | Milk | ₹60 |
| 7 | Soap | ₹30 |
| 8 | Biscuits | ₹25 |
| 9 | Chocolate | ₹80 |
| 10 | Tea | ₹90 |

## How It Works

1. The program displays the available products.
2. The user selects a product using its number.
3. The user enters the required quantity.
4. The program calculates:

   `Total = Price × Quantity`

5. Products are added to the cart.
6. The program calculates the subtotal.
7. A **10% discount** is applied.
8. A **5% GST** is calculated on the discounted amount.
9. The final bill amount is displayed.

### Billing Formula

```text
Subtotal = Sum of all product totals

Discount = Subtotal × 10%

Amount After Discount = Subtotal - Discount

GST = Amount After Discount × 5%

Grand Total = Amount After Discount + GST
