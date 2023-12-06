filename = "book.txt"

phone_number = input("Enter phone number: ")

def validate_phone_number(phone_number):
    if phone_number.isdigit() and len(phone_number) == 9:
        return "Phone number is correct."
    else:
        return False
print(validate_phone_number(phone_number))

# def check_file_exists(file_path):


# def get_appointments_from_file(file_path):

# def check_availability(appointments, date):

# def save_appointment(file_path, phone_number, date, time):

# def show_available_hours(appointments, date):