from expense import Expense
import datetime
import calendar

def main():
    expense_file_path = "expenses.csv"
    budget = 2000

    while True:
        print("\nChoose an option:")
        print("1. Enter Data")
        print("2. View Data")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        print("\n"*100)
        if choice == '1':
            # Get user input for expense.
            expense = get_user_expense()
            # Write their expense to a file.
            save_expense_to_file(expense, expense_file_path)
        elif choice == '2':
            # Read file and summarize expense
            summarize_expense(expense_file_path, budget)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")    


def get_user_expense():
    print("get_user_expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "📦 Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")
        
        value_range =  f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
                )
            return new_expense
        else:
            print("Invalid category. Please try again")
        
        break


def save_expense_to_file(expense: Expense, expense_file_path):
    print("\n"*100)
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path, budget):
    print("-"*50)
    print("<--Summarizing User Expense-->")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expenses = Expense(
                name=expense_name,
                amount=float(expense_amount), 
                category=expense_category
            )
            expenses.append(line_expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses By Category :")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")
    
    total_spent = sum(x.amount for x in expenses)
    print(f"Total Spent: ${total_spent: .2f}")

    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${total_spent: .2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(f"Budget Per Day: ${daily_budget:.2f}")
    print("-"*50)



if __name__ == "__main__":
    main()
