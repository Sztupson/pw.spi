# Dane: masa1, masa2, kąt Phi - 30 stopni
# v1k = (m1 - m2)/(m1 + m2)*v1p + 2*m2/(m1 + m2)*v2p
# v2k = (m2 - m1)/(m1 + m2)*v2p + 2*m1/(m1 + m2)*v1p
# m1*v1p = m1*v1k*cosPhi + m2*v2k*cosTheta
# 0 = m1*v1k*sinPhi - m2*v2k*sinTheta
import math
from sympy import Eq, symbols, solve, sin

cosPhi = math.cos(math.radians(30))

print("Podaj dane: \n")
masa1 = float(input("Masa pierwszej kuli: "))
masa2 = float(input("Masa drugiej kuli: "))
v1p = float(input("Podaj prędkość początkową kuli: "))

v1k, v2k, kąt = symbols('v1k v2k kąt')

eq1 = Eq((masa1 * (v1k**2))/2 + (masa2 * (v2k**2))/2, masa1 * (v1p**2) / 2)
eq2 = Eq(masa1 * v1k * cosPhi + masa2 * v2k * (1-sin(kąt)**2)**0.5, masa1 * v1p)
eq3 = Eq(masa1 * v1k * 0.5 - masa2 * v2k * sin(kąt), 0)

wynik = solve((eq1,eq2,eq3),(v1k, v2k, kąt))
wynik = wynik[0]

print(f"Prędkość końcowa pierwszej kuli: {wynik[0]}")
print(f"Prędkość końcowa drugiej kuli: {wynik[1]}")
print(f"Kąt odbicia kul: {wynik[2]}")