.data 10
        a = 10
        b = 12
        c = 5
        d = 8
        bufor = ?
        wynik_min = ?
.code 20
begin:  CPA a
        SUB b
        BRN a_min
        CPA b
        STO bufor
        BRA nxt_val

a_min:  CPA a
        STO bufor

nxt_val:CPA c
        SUB d
        BRN c_min
        CPA d
        SUB bufor
        BRN wynik1
        CPA d
        STO wynik_min
        BRA stop

c_min:  CPA c
        SUB bufor
        BRN wynik1
        CPA c
        STO wynik_min
        BRA stop

wynik1: CPA bufor
        STO wynik_min

stop:   HLT
end