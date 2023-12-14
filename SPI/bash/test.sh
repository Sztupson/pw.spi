#!/bin/bash

# echo "Jak masz na imie?"
# read imie
# echo "Cześć, $imie!"


echo "Podaj liczbe"
read liczba
if [ $liczba -gt 10 ]
then
    echo "Liczba wieksza od 10"
else
    echo "Liczba mniejsza lub rowna 10"
fi

for ((i=1; i<=$liczba; i++))
do
    echo "Iteracja $i"
done

while [ $liczba -le 5 ]
do
    echo "Liczba: $liczba"
    ((liczba++))
done

liczenie() {
while [ $1 -le 5 ]
do
    echo "Liczba: $1"
    ((liczba++))
done
}

liczenie $liczba

if [ -f "$1" ]
then
    echo "Plik istnieje $1"
else
    echo "Plik nie istnieje $1"
fi