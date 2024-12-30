# SQLAlchemy and MySQL Database Interaction Scripts

This repository contains various Python scripts and SQL files for interacting with a MySQL database using SQLAlchemy. The scripts perform different operations such as querying, filtering, inserting, updating, and deleting records in the database.

## Files

### Python Scripts

1. **0-select_states.py**

   - Selects all states from the database and prints them.

2. **1-filter_states.py**

   - Selects all states with a name starting with 'N' and prints them.

3. **2-my_filter_states.py**

   - Selects and prints states with a name that matches the argument.

4. **3-my_safe_filter_states.py**

   - Similar to `2-my_filter_states.py` but safe from SQL injection.

5. **4-cities_by_state.py**

   - Lists all cities from the database, ordered by state.

6. **5-filter_cities.py**

   - Lists all cities of a given state.

7. **7-model_state_fetch_all.py**

   - Lists all `State` objects from the database using SQLAlchemy.

8. **8-model_state_fetch_first.py**

   - Fetches the first `State` object from the database.

9. **9-model_state_filter_a.py**

   - Lists all `State` objects that contain the letter 'a'.

10. **10-model_state_my_get.py**

    - Prints the `State` object with the name passed as an argument.

11. **11-model_state_insert.py**

    - Adds a new `State` object to the database.

12. **12-model_state_update_id_2.py**

    - Updates the name of a `State` object where id = 2.

13. **13-model_state_delete_a.py**

    - Deletes all `State` objects with a name containing the letter 'a'.

14. **14-model_city_fetch_by_state.py**
    - Fetches all `City` objects by state.

### SQL Files

1. **0-select_states.sql**
   - SQL script to create and populate the states table.

## Models

1. **model_city.py**

   - Defines the `City` class which maps to the `cities` table in the database.

2. **model_state.py**
   - Defines the `State` class which maps to the `states` table in the database.

## Requirements

- Python 3.x
- MySQL server
- SQLAlchemy
- MySQLdb

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies:**

   ```sh
   pip install SQLAlchemy MySQLdb
   ```

3. **Set up the database:**

   - Start MySQL server.
   - Run `0-select_states.sql` to create and populate the `states` table:

     ```sh
     mysql -u root -p < 0-select_states.sql
     ```

4. **Run the scripts:**

   - Ensure the MySQL server is running.
   - Execute the Python scripts as needed. For example:

     ```sh
     python3 0-select_states.py your-username your-password your-database-name
     ```

## Usage

Each script has a specific purpose and can be executed independently. They all connect to the MySQL database using SQLAlchemy and perform the specified operations.

## Notes

- Ensure that your MySQL server is running and accessible before running the scripts.
- Modify the database connection parameters in each script as needed to match your setup.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- Olumide (iamloumie) - [GitHub Profile](https://github.com/iamloumie)

---
