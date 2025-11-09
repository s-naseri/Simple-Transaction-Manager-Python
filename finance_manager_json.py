import json  # for saving and loading data

# Function to load transactions from file
def load_from_file(filename="transactions.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)  # read and return the list from file
    except FileNotFoundError:
        return []  # if file does not exist, return empty list

# Function to save transactions to file
def save_to_file(transactions, filename="transactions.json"):
    with open(filename, "w") as file:
        json.dump(transactions, file)  # write the list to file

# Load transactions when program starts
transactions = load_from_file()

def add_transaction():
    i = len(transactions) + 1  # start from next number
    while True:
        if input('do you have any new transaction?(y/n): ') == 'y':
            while True:
                try:
                    a = int(input(f'please enter your number {i} transaction amount: '))
                    break
                except ValueError:
                    print(f'please enter a number for your number {i} amount: ')
                    
            d = input(f'please enter your number {i} transaction description: ')
            c = input(f'please enter your number {i} transaction category: ')
            i += 1
            transaction = {
                'amount': a,
                'description': d,
                'category': c
            }
            transactions.append(transaction)
        else:
            break
    # Save updated transactions list to file
    save_to_file(transactions)
    return transactions

def view_transactions(transactions):
    for j in range(len(transactions)):
        print(f'{j+1}- amount={transactions[j]["amount"]} | '
              f'description={transactions[j]["description"]} | '
              f'category={transactions[j]["category"]}')

def get_total_expenses(transactions):
    total = 0
    for j in range(len(transactions)):
        total += transactions[j]['amount']
    print(f'total expenses are {total} dollars')

def category_filter(transactions):
    filtered_total = 0
    while True:
        c = input('do you have any category filter?(y/n)')
        if c == 'y':
            d = input('please type your filter: ')
            for j in range(len(transactions)):
                if transactions[j]['category'] == d:
                    filtered_total += transactions[j]['amount']
            print(f'your total filtered expenses are {filtered_total} dollars')
        else:
            break

# Main program loop
while True:
    h = input(
        'Hello. I hope you feel well. \n'
        'I am your transaction agent. feel free to share whit me your expenses. I am safe and reliable. \n'
        'what do you want to do  now? just enter the number \n'
        '1- add new expenses. | 2- view expenses in details | '
        '3- view total transactions | 4-filter categories | 5-exit '
    )
    if h == '1':
        transactions = add_transaction()
    elif h == '2':
        view_transactions(transactions)
    elif h == '3':
        get_total_expenses(transactions)
    elif h == '4':
        category_filter(transactions)
    elif h == '5':
        break
    else:
        print('incorrect input. please select a number between 1 and 5')