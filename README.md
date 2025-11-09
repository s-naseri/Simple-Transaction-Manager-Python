# Personal Finance Transaction Manager (CLI)

## Project Overview
This is a simple command-line interface (CLI) application built with Python to help users manage their personal financial transactions. It allows for adding new expenses, viewing a detailed list of all transactions, calculating total expenses, and filtering transactions by category. A key feature is data persistence, where all transaction data is saved to and loaded from a JSON file, ensuring data is not lost when the program closes.

This project was developed as part of my continuous learning journey in Python programming and foundational concepts crucial for future explorations in LLM (Large Language Model) development and Machine Learning Engineering.

## Features
- **Add New Transactions:** Easily input transaction amount, description, and category.
- **View All Transactions:** Display a detailed list of all recorded expenses.
- **Calculate Total Expenses:** Get a sum of all recorded transaction amounts.
- **Filter by Category:** View total expenses for a specific category.
- **Data Persistence:** Transactions are automatically saved to `transactions.json` and loaded upon startup.
- **Error Handling:** Basic input validation for transaction amounts.

## How to Run
1.  **Prerequisites:**
    *   Python 3.x installed on your system.

2.  **Steps:**
    *   Clone this repository to your local machine:
        ```bash
        git clone https://github.com/YOUR_GITHUB_USERNAME/Personal-Finance-CLI.git
        ```
    *   Navigate to the project directory:
        ```bash
        cd Personal-Finance-CLI
        ```
    *   Run the application:
        ```bash
        python transaction_manager.py # Or whatever you named your Python file
        ```

## How to Use
Upon running the program, you will be presented with a menu of options:
- `1`: Add new expenses. The program will prompt you for amount, description, and category.
- `2`: View all recorded transactions.
- `3`: View the total sum of all expenses.
- `4`: Filter transactions by a specific category and see the total for that category.
- `5`: Exit the application.

## Technologies Used
- Python 3
- `json` module for data persistence

## Future Enhancements (Optional, but good to show thought process)
- Implement options to edit or delete existing transactions.
- Add functionality to search transactions by keyword.
- Generate simple reports (e.g., monthly spending summary).
- Migrate data storage to a more robust solution like SQLite.
- Develop a graphical user interface (GUI).

## My Learning Journey
This project helped me solidify my understanding of:
- Python fundamentals: variables, data types (lists, dictionaries), control flow (loops, conditionals).
- Function definition and usage.
- Basic error handling (`try-except`).
- File I/O operations and data serialization (`json` module).
- Building interactive command-line applications.
- Managing application state and data persistence.

These foundational skills are crucial as I pivot towards LLM Development and Machine Learning Engineering, where strong programming principles are essential for data processing, model deployment, and building intelligent systems.
