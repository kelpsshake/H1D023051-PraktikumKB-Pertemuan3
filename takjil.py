import random
from datetime import datetime

takjil_menu = {
    "Es Kuwut": 8000,
    "Es Buah": 10000,
    "Gorengan": 3000,
    "Pukis": 7000,
    "Martabak": 9000,
}

print(f"Selamat berbuka puasa! Hari ini: {datetime.now().strftime('%d %B %Y')}")

print("Menu Takjil Ramadhan:")
for index, (takjil, harga) in enumerate(takjil_menu.items(), 1):
    print(f"{index}. {takjil} - Rp{harga}")

takjil_rekomendasi = random.choice(list(takjil_menu.keys()))
print(f"\nRekomendasi takjik hari ini: {takjil_rekomendasi}")

jumlah = int(input("Berapa porsi yang ingin kamu beli?"))

if jumlah > 0:
    total_harga = jumlah * takjil_menu[takjil_rekomendasi]
    print(f"Total harga untuk {jumlah} porsi {takjil_rekomendasi} adalah Rp{total_harga}")
else:
    print("Maaf jumlah pesanan tidak valid")

print("Terima kasih sudah membeli takjil disini, selamat berbuka😊")