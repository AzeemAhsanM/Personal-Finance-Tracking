from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt,allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("invalid format. please enter date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("enter the amount: "))
        if amount <= 0:
            raise ValueError("amount must be positive")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()



def get_category():
    category = input("enter the category ('I' for income or 'E' for expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("invalid category, 'I' for income or 'E' for expense")
    return get_category()


def get_description():
    return input("enter a description(optional): ")