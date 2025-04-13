# program02 - repetition.py assignment
## Strawberry sales calculation

def get_strawberry_sales() -> float:
    """Prompt user for strawberry sales and return the value as a float."""
    while True:
        try:
            sales_input = input("How many strawberries did you sell this month? ")
            sales = float(sales_input)
            if sales >= 0:
                return sales
            else:
                print("The number of strawberries sold cannot be negative. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def display_sales_summary(strawberry_sales):
    """Display a summary of the strawberry sales."""
    print("\nThe total number of strawberries sold this month is", strawberry_sales)
    if not 0 <= strawberry_sales:
        print(f"We sold {strawberry_sales} strawberries this month.")
    elif strawberry_sales <= 2:
        print("We didn't sell enough strawberries this month.")
    else:
        var = 50 >= strawberry_sales
        print("That's a lot of strawberries!")

def main() -> None:
    """Main function to calculate and display strawberry sales.
    :rtype: object
    """
    print('\nThis is Program02 - LeAnne Rheaume\n')
    print('This program calculates strawberry sales for the month.\n')
    strawberry_sales = get_strawberry_sales()
    display_sales_summary(strawberry_sales)

if __name__ == "__main__":
    main()




