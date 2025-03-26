# H1D023051-PraktikumKB-Pertemuan3
# Penjelasan mengenai program takjil.py
- Menngunakan 2 library yaitu random dan datetime
  Random untuk memilih takjil secara acak dan datetime untuk menunjukan tanggal hari ini
- Membuat menu takjil (dictionary)
  takjil_menu menyimpan daftar takjil sebagai key dan harga nya sebagai value
- Menampilkan tanggal hari ini
  datetime.now itu untuk mengambil data hari ini, strftime('%d %B %Y') untuk menentukan format tanggal
  %d untuk tanggal
  %B untuk bulan
  %Y untuk tahun
- Menampilkan data menu takjil
  for index, (takjil, harga): index untuk menyimpan nomor urut, takjil menyimpan nama takjilnya, dan harga menyimpan harga takjil nya
  enumerate(takjil_menu.items(), 1): enumarate....,1 membuat nomor urut yang dimulai dari 1
  takjil_menu.items(): mengambil nama takjil dan harga nya
- Memilih takjil secara acak
  random.choice...: memilih satu menu takjil secara acak
  list...: mengubah nya menjadi list agar bisa di acak
  takjil_menu.keys: mengambil semua nama takjil dari dictionary
- Input jumlah pesanan
  input(...): meminta inputan dari pengguna
  int: mengubah string menjadi angka
- Menghitung total harga
  if jumlah > 0: mengecek apakah inputan dari pengguna itu sudah valid atau belum
  jumlah * takjil_menu[takjil_rekomendasi]: menghitung harga takjil dengan mengambil harga dari takjil yang di pilih
  else: apabila inputan dari pengguna tidak valid, maka akan keluar pesan seperti yang tertera
  
