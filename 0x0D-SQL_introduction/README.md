# SQL Scripts Repository

## Overview

This repository contains a collection of SQL scripts for various database operations, ranging from basic database management to more complex data manipulation and analysis tasks.

## Script Categories

### Database Management

- `0-list_databases.sql`: List all databases
- `1-create_database_if_missing.sql`: Create a database if it doesn't exist
- `2-remove_database.sql`: Remove an existing database

### Table Operations

- `3-list_tables.sql`: List tables in a database
- `4-first_table.sql`: Create an initial table
- `5-full_table.sql`: Create a comprehensive table
- `9-full_creation.sql`: Complete table creation script

### Data Manipulation

- `6-list_values.sql`: List values in a table
- `7-insert_value.sql`: Insert values into a table
- `8-count_89.sql`: Count specific records
- `10-top_score.sql`: Retrieve top scores
- `11-best_score.sql`: Find the best score
- `12-no_cheating.sql`: Filtering out specific records
- `13-change_class.sql`: Update class information

### Data Analysis

- `14-average.sql`: Calculate averages
- `15-groups.sql`: Grouping data
- `16-no_link.sql`: Perform joins or link-related operations

### Advanced Operations

- `100-move_to_utf8.sql`: Convert database to UTF-8 encoding
- `101-avg_temperatures.sql`: Calculate average temperatures
- `102-top_city.sql`: Find top cities
- `103-max_state.sql`: Find maximum state-related information

## Usage

1. Ensure you have a MySQL/SQL database setup
2. Run these scripts in order or as needed for your specific database management and analysis tasks
3. Modify connection strings and database names as necessary

## Prerequisites

- MySQL or compatible SQL database
- Basic understanding of SQL syntax
- Database connection with appropriate permissions

## Recommended Execution Order

While scripts can be run independently, for a complete database setup, consider the following sequence:

1. Create database
2. Create tables
3. Insert initial values
4. Perform analysis and manipulations

## Notes

- Always backup your database before running destructive operations
- Test scripts in a staging environment first
- Some scripts may require modification based on your specific database schema
