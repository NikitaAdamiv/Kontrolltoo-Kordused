#1
n = int(input("Sisesta majade arv (1–9): "))

house = [
"  ~~~~~",
" /_____\\",
" | []  |",
"  -----"
]

for i in range(len(house)):
    for j in range(n):
        print(house[i], end="   ")
    print()

#2
n = int(input("Õpilaste arv klassis: "))

sum1 = 0
sum2 = 0

print("Sisesta 1. klassi hinded:")
for i in range(n):
    sum1 += int(input())

print("Sisesta 2. klassi hinded:")
for i in range(n):
    sum2 += int(input())

print("1. klassi keskmine:", sum1 / n)
print("2. klassi keskmine:", sum2 / n)


#3
n = int(input("Õpilaste arv: "))

h = int(input("Sisesta hinne: "))
min_hinne = h
max_hinne = h

for i in range(n - 1):
    h = int(input("Sisesta hinne: "))
    if h < min_hinne:
        min_hinne = h
    if h > max_hinne:
        max_hinne = h

print("Minimaalne hinne:", min_hinne)
print("Maksimaalne hinne:", max_hinne)

#4
import random

kokku_elanikke = 0
kokku_pindala = 0

for i in range(12):
    elanikud = random.randint(1, 50) * 1000
    pindala = random.randint(50, 500)

    kokku_elanikke += elanikud
    kokku_pindala += pindala

keskmine_tihedus = kokku_elanikke / kokku_pindala
print("Keskmine rahvastikutihedus:", round(keskmine_tihedus, 2), "in/km²")

#5
xmin = float(input("Min x: "))
xmax = float(input("Max x: "))
step = float(input("Samm: "))

x = xmin
while x <= xmax:
    y = -0.5 * x + x
    print(f"x = {x:.2f} | y = {y:.2f}")
    x += step
