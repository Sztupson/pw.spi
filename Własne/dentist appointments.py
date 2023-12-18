import os
import datetime

class AppointmentManager:
    def validate_phone_number(phone_number:str):
        if len(phone_number) == 9 and phone_number.isdigit():
            return True
        
    def check_file_exists(file_path):
        try:
            if os.path.exists(file_path):
                return True
        except FileNotFoundError:
            print("File does not exist.")
            return False
        
    def get_appointments_from_file(file_path):
        if check_file_exists(file_path) == True:
            with open(file_path, 'r') as file:
                return file.readlines()
        return []

    def check_availability(appointments:list, date:str):
        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format (DD-MM-YYYY).")
            return False
        return sum(date in appointment for appointment in appointments) < 8
        
    def save_appointment(file_path, phone_number, date, time):
        if not validate_phone_number(phone_number):
            print("Invalid phone number.")
            return False
        appointments = get_appointments_from_file(file_path)
        if appointments not in check_availability(appointments, date):
            print("This appointment is not available.")
            return False
        if check_file_exists(file_path) == True:
            with open(file_path) as file:
                return file.writelines(f"{phone_number}")
        with open(file_path, 'a') as file:
            file.write(f"{phone_number};{date};{time} \n")
        print("Appointment saved.")
        return True

    def show_available_hours(appointments, date):
        appointments = get_appointments_from_file(file_path)
        if appointments not in check_availability(appointments, date):
            print("No available appointments for this day.")
            return False

        working_hours = [f"{hour}:00" for hour in range(9, 17)]
        booked_hours = [appt.split(';')[2].strip() for appt in appointments if date in appt]
        available_hours = [hour for hour in working_hours if hour not in booked_hours]
        if available_hours:
            print("Available hours:", ", ".join(available_hours))
        else:
            print("No available appointments for this day.")

file_path = "appointments.txt"
appointment_manager = AppointmentManager(file_path)
date = input("Podaj datę (YYYY-MM-DD):")
appointment_manager.show_available_hours(date)
time = input("Podaj godzinę (HH24:MI): ")
phone_number = input("Podaj numer telefonu (123456789): ")
appointment_manager.save_appointment(phone_number, date, time)