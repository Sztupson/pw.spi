# 192.168.128.1

def validate_ip(adres_IP):
    parts = adres_IP.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

# Test
print(validate_ip('2555.123.23.1')) # False
print(validate_ip('192.168.128.1')) # True
print(validate_ip('256.256.256.256')) # False

adres_IP = input('Podaj adres IP: ')

if validate_ip(adres_IP) == True:
        print("Adres IP prawidłowy.")
else:
        print('Adres IP nieprawidłowy.')