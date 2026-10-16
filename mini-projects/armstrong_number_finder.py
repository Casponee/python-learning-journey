

## Girilen sayının rakamlarını list olarak dışarı aktarır
def extract_digits(num: int) -> list[int]:
    result = []
    while num != 0:
        result.append(num % 10)
        num = num//10
    return result

## Armstrong sayısı: Bir sayının her bir rakamının, basamak sayısı kadar üssü alınıp toplandığında elde edilen sonuç sayının kendisine eşitse buna Armstrong sayısı denir.
## Bu fonksiyon da bunu hesaplıyor. bir for döngüsü ile listedeki her elemanın listedeki eleman sayısı kadar üssünü alıp topluyor.
def sum_digit_powers(digits: list[int]) -> int:
    result = 0
    for i in range(len(digits)):
        result += digits[i]**len(digits)
    return result

## Belirli bir aralıktaki armstrong sayılarını liste halinde çıkartıyor.
def find_armstrong_numbers(start_num: int, end_num: int) -> list[int]:
    armstrong_numbers = []
    for num in range(start_num, end_num):

        total_sum = sum_digit_powers(extract_digits(num))

        if num == total_sum:
            armstrong_numbers.append(num)

    return armstrong_numbers



start_num = input("Başlangıç Sayısı : ")
end_num = input("Bitiş Sayısı : ")

## Verilen değerler doğru mu diye kontrol eder eğer değilse programı durdurur doğruysa programı çalıştırır.
try:
    start_num = int(start_num)
    end_num = int(end_num)

    if(start_num > end_num):
        result = find_armstrong_numbers(end_num, start_num)
    else:
        result = find_armstrong_numbers(start_num, end_num)

    print(result)

except ValueError:
    print("Lütfen bir sayı girin.")

