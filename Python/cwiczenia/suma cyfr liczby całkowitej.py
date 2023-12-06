# def sum_number(digits:str) -> int:
#     total = 0
#     for digit in digits:
#         total += int(digit)
#     return total

# try:
#     number = input('Enter a number: ')
#     if number.isdigit():
#         result = sum_number(number)
#         print(f"Suma cyfr liczby {number} wynosi: {result}.")
#     else:
#         print('Please enter only digits.')
# except ValueError:
#     print("Invalid input")

# Napisz program obliczający wskaźnik masy ciała (BMI) na podstawie wzrostu i wagi użytkownika:

waga = int(input("Podaj swoją wagę: "))
wzrost = float(input("Podaj swój wzrost (W METRACH!): "))
bmi = waga / (wzrost**2)
print(bmi)
if bmi < 18.5:
    print("Niedowaga")
elif 18.5 <= bmi < 24.9:
    print("Waga prawidłowa")
elif 25 <= bmi < 29.9: 
    print("Nadwaga")
else:
    print("Otyłość")