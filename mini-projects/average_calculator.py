
## Verilen girdi düzenlenir ve düzgün sayılar olarak listeye alınır.
def clean_input(raw_input: str) -> list:
    raw_items = raw_input.split(",")
    numbers_list = []
    for i in raw_items:
        i = i.strip()
        try:
            i = int(i)
            numbers_list.append(i)
        except ValueError:
            pass
    return numbers_list
## Listedeki elemanları toplar ve listedeki eleman sayısına böler.
def calculate_average(numbers: list):
    total_sum = 0
    for i in numbers:
        total_sum += i
    return total_sum / len(numbers) 

print('Sayıları bu şekilde yazın : "1, 2, 4, 8"')
user_input = input("sayilar girin : ")
numbers_list = clean_input(user_input)
if numbers_list != []:
    print(f"Sayıların Ortalaması: {calculate_average(numbers_list)}")
else:
    print("Hata: Lütfen en az bir geçerli sayı girin.")