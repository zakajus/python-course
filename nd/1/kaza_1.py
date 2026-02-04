import random

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


"""
1. 	Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
"""
print(f"{'-'*5} 1 uždavinys {'-'*5}")

intervalas = np.linspace(-1.3, 2.5, 64)
print(intervalas)


"""
2. 	Sukonstruokite pasikartojantį masyvą pagal duotą N.
Duotas masyvas [1, 2, 3, 4] ir N = 3
Rezultatas [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Masyvas gali būti bet kokio dydžio ir atsitiktinai sugeneruojamas.
"""
print(f"{'-'*5} 2 uždavinys {'-'*5}")

N = 3
duotas = np.array([x for x in range(random.randint(0, 4), random.randint(7, 10))])
rezultatas = np.tile(duotas, N) # jei nubutu numpy.ndarray tiesiog: masyvas * N

print(f"Duotas:     {duotas}")
print(f"Rezultatas: {rezultatas}")


"""
3. 	Sukurkite masyvą iš pasikartojančių elementų.
Duotas sąrašas [3, 4] ir pasikartojimų skaičius 4.
Rezultatas [3, 3, 3, 3, 4, 4, 4, 4]
"""
print(f"{'-'*5} 3 uždavinys {'-'*5}")
sarasas = [3, 4]
pasikartojimu_skaicius = 4
rezultatas = np.repeat(sarasas, pasikartojimu_skaicius)
print(rezultatas)


"""
4. 	Sukurkite masyvą dydžio 10 x 10 iš nulių "įrėmintų" vienetais.
Užuomina - pad.
"""
print(f"{'-'*5} 4 uždavinys {'-'*5}")
matrix = np.pad(np.ones((8, 8)), 1, constant_values=0)
print(matrix)


"""
5. 	Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka.
"""
print(f"{'-'*5} 5 uždavinys {'-'*5}")
arr = np.zeros((8, 8))
arr[::2, ::2] = 1   # lyginai i,j
arr[1::2, 1::2] = 1 # nelyginiai i,j
print(arr)


"""
6. 	Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j.
"""
print(f"{'-'*5} 6 uždavinys {'-'*5}")
n = 10
arr = np.fromfunction(lambda i, j: (i + j), (n, n))
print(arr)


"""
7. 	Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. 
Užuominos - slicing, argsort, indexing.
"""
print(f"{'-'*5} 7 uždavinys {'-'*5}")
arr = np.random.rand(5, 5)
i = np.argsort(arr[:, 1]) # grazina eiluciu indeksus, pagal didejancia antra stulpeli
arr = arr[i]
print(arr)


"""
8. 	Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių.
"""
print(f"{'-'*5} 8 uždavinys {'-'*5}")
tikrines_reiksmes, tikrinis_vektorius = np.linalg.eig(arr)
print(f"Tikrines reikšmes:        {tikrines_reiksmes}")
print(f"Tikrinis vektorius(-iai): {tikrinis_vektorius}")


"""
9. 	Apskaičiuokite funkcijos 0.5*x**2 + 5 * x + 4 išvestines su numpy ir sympy paketais.
Užuominos - poly1d, deriv, diff
"""
print(f"{'-'*5} 9 uždavinys {'-'*5}")

# Numpy
f = np.poly1d([0.5, 5, 4])
f_dx = f.deriv()
print(f"Nympy funkcija:  {f}")
print(f"Numpy išvestinė: {f_dx}")

# Sympy
x = sp.symbols('x')
f = 0.5*x**2 + 5 * x + 4
f_dx = sp.diff(f, x)
print(f"Sympy funkcija:  {f}")
print(f"Sympy išvestinė: {f_dx}")


"""
10. 	Apskaičiuokite funkcijos e-x apibrėžtinį, intervale [0,1], ir neapibrėžtinį integralus.
"""
print(f"{'-'*5} 10 uždavinys {'-'*5}")
x = sp.symbols('x')
f = sp.exp(-x)
print(f"Neapibrėžtinis: {sp.integrate(f, x)}")
print(f"Apibrėžtinis:   {sp.integrate(f, (x, 0, 1))}")


"""
11. 	Pasinaudodami polinėmis koordinatėmis nupieškite kardioidę.
"""
print(f"{'-'*5} 11 uždavinys {'-'*5}")


"""
12. 	Sugeneruokite masyvą iš 1000 atsitiktinių skaičių, pasiskirsčiusių pagal normalųjį dėsnį su duotais vidurkiu V ir dispersija D. Nupieškite jų histogramą
"""
print(f"{'-'*5} 12 uždavinys {'-'*5}")
