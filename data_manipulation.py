def revise_salary(data, key="salary", increase_percent=15):
    """
    Increases the salary by a given percentage.

    Parameters:
    - data (list of dict): The dataset containing salary information.
    - key (str): The key representing the salary field.
    - increase_percent (float): The percentage increase.

    Returns:
    - list of dict: Updated dataset with revised salaries.
    """
    return [{**item, key: round(item[key] * (1 + increase_percent / 100), 2)} for item in data if key in item]

# Example Usage
data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000}
]

# Apply a 15% salary increase
updated_data = revise_salary(data, increase_percent=10)

print(updated_data)