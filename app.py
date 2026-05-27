import random

def sonni_top():
    tasodifiy_son = random.randint(1, 100)
    urinishlar = 0
    print("🤖 Men 1 dan 100 gacha bo'lgan bitta son o'yladim.")
    print("Qani, topishga harakat qilib ko'ring!\n")

    while True:
        try:
            taxmin = int(input("Sizning taxminingiz: "))
            urinishlar += 1

            if taxmin < tasodifiy_son:
                print("⬆️ Kattaroq son kiriting.")
            elif taxmin > tasodifiy_son:
                print("⬇️ Kichikroq son kiriting.")
            else:
                print(f"🎉 Tabriklayman! Siz sonni {urinishlar} ta urinishda topdingiz.")
                break
        except ValueError:
            print("Iltimos, faqat raqam kiriting!")

if __name__ == "__main__":
    sonni_top()
