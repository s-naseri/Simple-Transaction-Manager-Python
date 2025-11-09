# Simple Transaction Manager (Python CLI)

## Project Overview
This is a straightforward command-line interface (CLI) application built with Python for personal financial transaction management. It enables users to perform basic operations such as adding new expenses, viewing a detailed list of all transactions, calculating total expenditures, and filtering transactions by category. A core feature of this application is its data persistence mechanism, which saves and loads all transaction data from a JSON file, ensuring that no information is lost when the program is closed and reopened.

This project represents a foundational step in my continuous learning journey in Python programming. It aims to solidify essential programming concepts that are crucial for my future exploration and specialization in LLM (Large Language Model) development and Machine Learning Engineering.

## Features
-   **Add New Transactions:** Easily input transaction amount, description, and category.
-   **View All Transactions:** Display a detailed list of all recorded expenses.
-   **Calculate Total Expenses:** Get a sum of all recorded transaction amounts.
-   **Filter by Category:** View total expenses for a specific category.
-   **Data Persistence:** Transactions are automatically saved to `transactions.json` and loaded upon application startup.
-   **Basic Error Handling:** Includes basic input validation for transaction amounts to ensure data integrity.

## How to Run
1.  **Prerequisites:**
    *   Ensure you have Python 3.x installed on your system.

2.  **Steps:**
    *   Clone this repository to your local machine using Git:
        ```bash
        git clone https://github.com/s-naseri/Simple-Transaction-Manager-Python.git
        ```
    *   Navigate into the cloned project directory:
        ```bash
        cd Simple-Transaction-Manager-Python
        ```
    *   Run the application using Python:
        ```bash
        python finance_manager_json.py
        ```

## How to Use
Once the program is running, you will be presented with an interactive menu:
-   `1`: Select this option to add new expenses. The program will prompt you to enter the amount, description, and category for each transaction.
-   `2`: Choose this to view a comprehensive list of all your recorded transactions.
-   `3`: Use this to see the total sum of all your expenses.
-   `4`: Filter your transactions by a specific category and view the aggregated total for that category.
-   `5`: Select this option to exit the application.

## Technologies Used
-   Python 3
-   `json` module (for efficient data serialization and deserialization)

## Future Enhancements
As part of my ongoing development, potential future enhancements for this project include:
-   Implementing functionalities to edit or delete existing transactions.
-   Adding advanced search capabilities to find transactions by keywords in description or category.
-   Developing simple financial reports (e.g., monthly spending summaries, category breakdowns).
-   Migrating the data storage solution to a more robust database like SQLite for enhanced querying capabilities.
-   Exploring the development of a graphical user interface (GUI) for a more user-friendly experience.

## My Learning Journey
This project has been an instrumental part of my learning process, helping me solidify a deeper understanding of:
-   Python fundamentals: Variables, data types (lists, dictionaries), control flow (loops, conditional statements).
-   Effective function definition and modular programming practices.
-   Basic error handling (`try-except` blocks) for robust applications.
-   File Input/Output (I/O) operations and data serialization using the `json` module.
-   Developing interactive command-line applications and managing user input.
-   Understanding and implementing application state management and data persistence across sessions.

These foundational programming and system design skills are critically important as I continue to pivot and specialize in the fields of LLM Development and Machine Learning Engineering. A strong grasp of these principles is essential for efficient data processing, successful model deployment, and building sophisticated intelligent systems.
