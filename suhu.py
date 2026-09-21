# Menu
print("KONVERSI SUHU")
print("1. Celsius (C)")
print("2. Fahrenheit (F)")
print("3. Kelvin (K)")

# Input suhu dan pilihan (tetap berupa string untuk kemudahan validasi)
suhu = float(input("\nMasukkan angka suhu: "))
awal = input("Masukkan satuan suhu awal (1/2/3): ")
akhir = input("Masukkan satuan suhu akhir (1/2/3): ")

hasil = None
satuan_awal = ""
satuan_akhir = ""

# Label awal
if awal == "1":
  satuan_awal = "°C"
elif awal == "2":
  satuan_awal = "°F"
elif awal == "3":
  satuan_awal = "K"
# Label akhir
if akhir == "1":
  satuan_akhir = "°C"
elif akhir == "2":
  satuan_akhir = "°F"
elif akhir == "3":
  satuan_akhir = "K"

# Logika Percabangan Konversi
if awal == akhir and awal in ["1", "2", "3"]:
  hasil = suhu

# Dari Celsius
elif awal == "1":
  if akhir == "2":
    hasil = (suhu * 9 / 5) + 32
  elif akhir == "3":
    hasil = suhu + 273.15
# Dari Fahrenheit
elif awal == "2":
  if akhir == "1":
    hasil = (suhu - 32) * 5 / 9
  elif akhir == "3":
    hasil = (suhu - 32) * 5 / 9 + 273.15
# Dari Kelvin
elif awal == "3":
  if akhir == "1":
    hasil = suhu - 273.15
  elif akhir == "2":
    hasil = (suhu - 273.15) * 9 / 5 + 32

# Output
if hasil is not None:
  print(f"\nHasil konversi: {suhu} {satuan_awal} = {hasil:.2f} {satuan_akhir}")
else:
  print("\nSatuan tidak valid!")