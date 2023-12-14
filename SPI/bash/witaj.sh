
# #!/bin/bash
# echo "Witaj świecie"

# nazwa=Jan

# echo "Witaj, $nazwa"

a=10
b=10

if [ $a -eq $b ]; then
    echo "Równe"
else
    echo "Różne"
fi


for i in {1..5}; do
    echo "Number:  $i"
done

i=1
while [ $i -le 5 ]; do
    echo "Licz: $i"
    ((i++))
done


powitanie() {
    echo "Witaj, $1"
}

powitanie $1


if [ -f "Jan.txt" ]; then
    echo "Plik istnieje"
fi