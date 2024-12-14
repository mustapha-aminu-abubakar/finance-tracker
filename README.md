# FUNDaMENTAL - Personal Finance Tracker

This project is a **Personal Finance Tracker** built with Flask, allowing users to manage and monitor their financial activities efficiently. Users can record, update, view, and delete income and expense entries, while browsing their financial history through a paginated interface.

---

## Features

1. **Add Income and Expenses**  
   - Log your income sources and expenses with details like date, description, and amount.
   
2. **View Financial Records**  
   - Browse all income and expenses, or filter by type (income/expense), with a paginated display.

3. **Update Entries**  
   - Modify details of any financial record, including the amount, description, source (for income), or beneficiary (for expenses).

4. **Delete Entries**  
   - Remove any unwanted financial record from the system.

5. **User-Friendly Interface**  
   - Responsive templates for managing finances.

---

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/mustapha-aminu-abubakar/fudamental.git
   cd fudamental
   ```

2. **Set Up a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**  
   - Install and configure **MongoDB**.
   - Create a database named `finances` and a collection named `finances`.

5. **Run the Application**  
   ```bash
   python run.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

---

## Endpoints

1. **Homepage (View Finances)**  
   - **URL**: `/`  
   - **Method**: `GET`  
   - **Description**: Displays paginated financial records (all, income-only, or expense-only).  
   - **Query Parameters**:
     - `page` (default: 1): The page number.
     - `type_`: Filter by "income" or "expense".

2. **Add Income**  
   - **URL**: `/add_income`  
   - **Method**: `GET, POST`  
   - **Description**: Add a new income record.

3. **Add Expense**  
   - **URL**: `/add_expense`  
   - **Method**: `GET, POST`  
   - **Description**: Add a new expense record.

4. **Update Record**  
   - **URL**: `/update/<id>`  
   - **Method**: `GET, POST`  
   - **Description**: Update an income or expense record.

5. **Delete Record**  
   - **URL**: `/delete/<id>`  
   - **Method**: `GET`  
   - **Description**: Delete a financial record.

---

## File Structure

```
personal-finance-tracker/
│
├── application/
│   ├── __init__.py         # Initializes the Flask app and database connection
│   ├── routes.py           # Defines the application routes
│   ├── forms.py            # Form classes for input validation
│   ├── templates/          # HTML templates for the app
│ 
│
├── requirements.txt        # Python dependencies
├── config.py               # Configuration for the Flask app
├── fake_data.py            # Inserts sythetic data into MongoDB database
└── run.py                  # Entry point for the app
```

---

To incorporate the `fake_data.py` script into the README, we can describe its purpose and usage for populating the database with mock data for testing and development. Here's the updated section for the README:

---

## Populating the Database with Fake Data - optional

The project includes a `fake_data.py` script to generate mock financial records for testing and development purposes. This script uses the **Faker** library to create random, realistic data for income and expenses.

### How It Works

- **Generates Fake Data**:
  - Random amounts between 5 and 5000.
  - Descriptions and names sourced from the `Faker` library.
  - Randomly assigns entries as income or expenses.
  - Includes realistic sources, beneficiaries, and timestamps within the current year.

- **Populates the Database**:
  - The generated data is inserted into the `finances` collection of the MongoDB database.

### Usage

1. Ensure MongoDB is running locally and the `fundamental` database exists.
2. Run the script with the following command:

   ```bash
   python fake_data.py
   ```

   By default, it generates and inserts 8 records.

3. To generate a different number of records, modify the `size` parameter in the `add_fake_data()` function call:

   ```python
   add_fake_data(size=20)  # Generates 20 records
   ```

---

Including this script simplifies the process of testing the application without manually adding entries, making development and debugging more efficient.

---

## Technologies Used

- **Flask**: Web framework for the application.
- **MongoDB**: NoSQL database to store financial records.
- **WTForms**: For form handling and validation.
- **HTML/CSS**: For the frontend interface.

---

## Future Enhancements

- Add **authentication** for multiple users.
- Include **data visualization** (e.g., charts for income vs. expenses).
- Implement **export functionality** (e.g., CSV or PDF).
- Allow users to set **budgets** and track goals.



## License

This project is licensed under the MIT License.
