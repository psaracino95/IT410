# Disallowed characters 
disallowed_name_chars = set('!"@#$%^&*()_=+,<>/?;:{}[]\\')
disallowed_email_chars = set('!"\'#$%^&*()=+,<>/?;:{}[]\\')
disallowed_address_chars = set('!"\'@$%^&*_=+<>?;:{}[]')

# This function checks if a string contains any disallowed characters
def disallowed_characters(input_str, disallowed_set):
    return any(char in disallowed_set for char in input_str)

# List to store employee dictionaries
employees = []

# Loop to collect info for up to 5 employees
for i in range(5):
    print(f"\n--- Enter information for Employee #{i+1} ---")
    employee = {}

    # Validate Employee ID
    while True:
        employee_id = input("Enter Employee ID (up to 7 digits): ")
        if employee_id.isdigit() and len(employee_id) <= 7:
            employee['id'] = employee_id
            break
        print("Invalid ID. Must be a number with up to 7 digits.")

    # Validate Employee Name
    while True:
        employee_name = input("Enter Employee Name: ")
        if employee_name.replace(" ", "").isalpha() and not disallowed_characters(employee_name, disallowed_name_chars):
            employee['name'] = employee_name
            break
        print("Invalid Name. Must be alphabetic and free of disallowed special characters.")

    # Validate Employee Email Address
    while True:
        employee_email = input("Enter Employee Email Address: ")
        cleaned_email = employee_email.replace(".", "").replace("@", "")
        if cleaned_email.isalnum() and not disallowed_characters(employee_email, disallowed_email_chars):
            employee['email'] = employee_email
            break
        print("Invalid Email. Avoid special characters and ensure it's mostly alphanumeric.")

    # Validate Optional Address
    while True:
        employee_address = input("Enter Employee Address (optional): ").strip()
        if not employee_address:
            employee['address'] = None
            break
        elif employee_address.replace(" ", "").isalnum() and not disallowed_characters(employee_address, disallowed_address_chars):
            employee['address'] = employee_address
            break
        print("Invalid Address. Avoid disallowed special characters.")

    # Add the valid employee dictionary to the list
    employees.append(employee)

    # Ask to continue if under 5 entries
    if i < 4:
        more = input("Do you want to enter another employee? (y/n): ").lower()
        if more != 'y':
            break

# Print all employee information
print("\n=== Employee Records ===")
for emp in employees:
    print(f"\nHello, {emp['name']}. Your Employee ID is {emp['id']}, and your email address is {emp['email']}.")
    if emp['address']:
        print(f"Your address is {emp['address']}.")
    else:
        print("You did not provide an address.")

# Print raw data
print("\nEmployee List (Raw Data):")
print(employees)
