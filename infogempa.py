from gempa import Gempa

# Membuat 5 objek gempa
gempa_banten = Gempa("banten", 1.2)
gempa_palu = Gempa("palu", 6.1)
gempa_cianjur = Gempa("cianjur", 5.6)
gempa_jayapura = Gempa("jayapura", 3.3)
gempa_garut = Gempa("garut", 4.0)

# Memanggil fungsi dampak() untuk masing-masing objek gempa
gempa_banten.dampak()
gempa_palu.dampak()
gempa_cianjur.dampak()
gempa_jayapura.dampak()
gempa_garut.dampak()