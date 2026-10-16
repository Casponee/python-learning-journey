import random

lives = 4
level = 1
secret_number = random.randint(1,20)


print("SAYI TAHMİN OYUNU")
print(f"SEVİYE {level}, Kalan Can: {lives}")
while lives > 0:
    try:
        guess = int(input(f"{secret_number} | Tahmin: "))
    except ValueError:
        print("Lütfen Geçerli Bir Sayı Girin!")
        continue

    if guess < secret_number:
        lives -= 1
        print(f"SAYI YUKARIDA | Kalan Can: {lives}")
        
    elif guess > secret_number:
        lives -= 1
        print(f"SAYI AŞAĞIDA | Kalan Can: {lives}")
        
    else:
        level += 1
        lives += 3
        if level == 2:
            secret_number = random.randint(1,40)
            print(f"SEVİYE {level}, Kalan Can: {lives}")
        elif level == 3:
            secret_number = random.randint(1,80)
            print(f"SEVİYE {level}, Kalan Can: {lives}")
        elif level == 4:
            print("KAZANDIN!")
            break
        
if(lives == 0):
    print("KAYBETTİN!")