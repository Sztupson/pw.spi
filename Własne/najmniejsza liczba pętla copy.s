.data 1 
value:  a = ? # kolejne wartośći do sprawdzenia przez pętle #
        b = ?
        ...
        n = ? # ostatnia wartość #
a_value:value     # adres pod którym znajduje się pierwsza wartość do sprawdzenia #
        wynik_min = ? # komórka pamięci działająca jako bufor oraz jako komórka w której zapiszemy głowny wynik #
        ilosc_sprawdzanych_liczb = input # tutaj będzie podana łączna ilość liczb do sprawdzenia #

.code 200
begin:  CPA value     # wypisanie pierwszej wartości #
        STO wynik_min # zapisanie pierwszej wartości w buforze, którym jest też komórka z wynikiem #

petla:  DEC ilosc_sprawdzanych_liczb # zabraliśmy jedną wartość, dlatego zmniejszam ilość sprawdzanych wartości o jeden #                     
        BRZF end                     # jeżeli ilość sprawdzanych wartości będzie równa 0 skocz do end #

        CPA wynik_min # przywołanie wartości którą wcześniej zapisałem w wynik_min #
        INC a_value   # podniesienie o jeden adresu value, aby wskazywał na kolejną komórkę z kolejną wartością #
        SUB [a_value] # odjęcie kolejnej komórki znajdującej się pod adresem a_value (teraz jest to adres value+1) #
        BRN petla     # powrót do pętli jeśli wynik odejmowania jest mniejszy od 0 - pierwsza wartość jest mniejsza #
        CPA [a_value] # jeżeli nie skoczyliśmy w poprzedniej instrukcji, to oznacza, że druga wartość jest mniejsza
                      # i zapisujemy ją z powrotem w akumulatorze #
        STO wynik_min # zapisujemy tą wartość tym razem w buforze, którym jest wynik_min #
        BRA petla     # wracamy do pętli
end:    HLT
