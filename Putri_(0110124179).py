{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOwxk1QIagxNDVL2qLkgy8v"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":3,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"5cyluRJ_KT_k","executionInfo":{"status":"ok","timestamp":1730071556675,"user_tz":-420,"elapsed":461,"user":{"displayName":"Putri Aisazahra","userId":"00417137215120813858"}},"outputId":"987fb99a-0bd4-4bae-f705-09971ea4f54e"},"outputs":[{"output_type":"stream","name":"stdout","text":["Kendaraan saya\n","['Honda Beat', 'Sepeda Motor', 120, 'Biru', 2]\n","=========\n","['Honda Beat', 'Sepeda Motor', 120, 'Biru', 2, 2000000, 'Metic']\n","=========\n","['Honda Beat', 'Sepeda Motor', 'Honda', 120, 'Biru', 2, 2000000, 'Metic']\n","=========\n"]}],"source":["# 1. Buat variabel list dengan value : [nama kendaraan,\n","# JenisKendaraan, cckendaraan, warna kendaraan, roda\n","# kendaraan]\n","\n","kendaraan = ['Honda Beat', 'Sepeda Motor', 120,'Biru', 2]\n","print(\"Kendaraan saya\")\n","print (kendaraan)\n","print (\"=========\")\n","# tambahkan dari liat tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]\n","# kendaraan.append(2000000)\n","# kendaraan.append(\"metic\")\n","kendaraan.extend([2000000, \"Metic\"])\n","print(kendaraan)\n","print(\"=========\")\n","# tambahkan setelah jenis kendaraan dengan value [merk kendaraankendaraan].\n","kendaraan.insert (2, 'Honda')\n","print(kendaraan)\n","print(\"=========\")"]},{"cell_type":"code","source":["pilih = int(input(\"\"\"Selamat datang diaplikasi menghitung\n","1. untuk menghitung luas persegi\n","2. untuk menghitung luas lingkaran\n","3. untuk menghitung luas segitiga\n","\n","Masukan pilihan anda: \\n\"\"\"))\n","\n","match pilih:\n","  case 1 :\n","    print(\"Kamu memilih 1 untuk luas persegi\")\n","    sisi = int(input(\"masukan sisi persegi\"))\n","    luaspsg = sisi*sisi\n","    print(\"luas persegi yang sisinya\", luaspsg)\n","  case 2 :\n","    print(\"Kamu memilih 2 untuk luas lingkaran\")\n","    jari2 = int(input(\"masukan jari-jari: \"))\n","    luaslk = 3.14 * jari2 * jari2\n","    print(\"luas lingkaran yang jari-jarinya\", jari2, \"adalah\", luaslk)\n","  case 3 :\n","    print(\"Kamu memilih 3 untuk luas segitiga\")\n","    alas = int(input(\"masukan alas segitiga: \"))\n","    tinggi = int(input(\"masukan tinggi segitiga: \"))\n","    luassegitiga = 0.5 * alas * tinggi\n","    print(\"luas segitiga dengan alas\",alas, \"dan tinggi\",tinggi, \"adalah\", luassegitiga)\n","  case _:\n","    print(\"Anda Salah Pilih\")"],"metadata":{"id":"S5PSMKexNcVC","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1730071598531,"user_tz":-420,"elapsed":15707,"user":{"displayName":"Putri Aisazahra","userId":"00417137215120813858"}},"outputId":"dfd2654f-0001-4951-96b2-de7222f8efe4"},"execution_count":4,"outputs":[{"output_type":"stream","name":"stdout","text":["Selamat datang diaplikasi menghitung\n","1. untuk menghitung luas persegi\n","2. untuk menghitung luas lingkaran\n","3. untuk menghitung luas segitiga \n","\n","Masukan pilihan anda: \n","2\n","Kamu memilih 2 untuk luas lingkaran\n","masukan jari-jari: 17\n","luas lingkaran yang jari-jarinya 17 adalah 907.46\n"]}]}]}