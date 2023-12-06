.data 1 
value:  a = ?
        b = ?
        ...
        n = ?
a_value:value     # value address
        wynik_min = ?
        ilosc_sprawdzanych_liczb = input

.code 200
begin:  CPA value
        STO wynik_min

petla:  DEC ilosc_sprawdzanych_liczb
        BRZF end

        CPA wynik_min
        INC a_value
        SUB [a_value]
        BRN petla
        CPA [a_value]
        STO wynik_min
        BRA petla
end:    HLT
