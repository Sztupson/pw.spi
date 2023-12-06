# # Zwrócenie bieżącej daty i godziny
# # import calendar
# # from datetime import timedelta
# from datetime import datetime

# # now = datetime.now()
# # print(now)
# # print(now.year)
# # print(now.strftime("%Y"))

# # # Wyświetl aktualny miesiąc jako nazwę, np. "Listopad"
# # print(now.strftime("%b"))

# # # Wyświetl aktualny dzien tygodnia jako nazwę, np. "Poniedziałek"
# # print(now.strftime("%A"))

# # # Konwertuj napis "2023-11-15" na obiekt daty
# # date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
# # print(date_object)

# # past_date = datetime(2023, 11, 15)
# # print(past_date)

# # # 2023-Nov-15
# # date_object2 = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
# # print(date_object2)

# # # Dodaj 5 dni do aktualnej daty
# # print(now + timedelta(days=5))

# # # Odejmij 2 tygodnie od aktualnej daty
# # print(now - timedelta(days=14))

# # # Wyświetl różnicę w dniach między 1 stycznia 2023 a dzisiaj
# # past_date = datetime(2023, 1, 1)
# # day = now - past_date
# # print(day.days)

# # # Sprawdź czy rok 2024 jest rokiem przestępnym.
# # new_year = calendar.isleap(2024)
# # print(new_year)

# # # Wyświetl numer bieżącego tygodnia roku.
# # print(now.strftime("%U"))

# # # Zmień format daty z "2023-11-15 00:00:00" na format RFC 2822.
# # rfc_date = datetime.strptime("2023-11-15 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%a, %d %b %Y %H:%M:%S %z")

# # print(rfc_date)

# # # Znajdź dzień tygodnia dla 4 lipca bieżącego roku.
# # date = datetime(now.year, 7, 4)
# # print(date.strftime("%A"))

# # # Oblicz czas, który upłynął od nowego roku do teraz w sekundach.
# # 


# # Porównaj, czy data "2023-11-15" jest wcześniejsza niż dzisiaj.
# now = datetime.now()
# # date = datetime(2023, 11, 15)
# # if now > date:  
# #     print("To wcześniejsza data niż dzisiaj.")
# # else:
# #     print("To nie jest wcześniejsza data niż dzisiaj.")

# # Formatuj datę "15/11/2023 14:30" do formatu "15 listopada 2023, godzina 14:30"
# date = datetime.strptime("15/11/2023 14:30", "%d/%m/%Y, %H:%M").strftime("%d %B %Y, godzina %H:%M")
# print(date)