import sys
from datetime import datetime

sekarang = datetime.now()

pilihan = 'y'
while pilihan == 'y':
    print("""
    selamat datang di toko kalianda optik
    =====================================
    berikut produk yang tersedia:
    =====================================
    1. kacamata minus
    2. kacamata plus
    3. kacamata silinder
    4. Kacamata Sunglasses
    5. softlens
    6. Aksesoris kacamata dan softlens
    7. Kacamata Renang
    8. Kacamata Pelindung
    ====================================""")
    pesan = input("Masukkan pilihan kacamata yang ingin Anda beli (1-8): ").strip().lower()
    matriks_kacamata = ['kacamata minus', 'kacamata plus', 'kacamata silinder', 'kacamata sungalesses', 'softlens', 'Aksesoris Kacamata ', 'kacamata Renang', 'Kacamata Pelindung']
    matriks_kacamata = matriks_kacamata[int(pesan) - 1] if '1' <= pesan <= '8' else "Pilihan tidak valid"
    if pesan == '1':
        print("Anda memilih kacamata minus.")
        print("""
        
        ===================================================
        Berikut adalah daftar kacamata minus yang tersedia:
        ===================================================
        1. minus 0.25
        2. minus 0.75
        3. minus 1
        4. minus 2
        5. minus 3
        6. minus 4
        7. minus 5
        8. minus 6
        9. minus 7
        10. minus 8
        11. minus 9
        12. minus 10
        13. minus 11
        14. minus 12
        15. minus 13
        16. minus 14
        17. minus 15
        18. minus 16
        =================================================""")
        pesan2 = input("Masukkan pilihan kacamata minus yang ingin Anda beli (1-18): ")
        matriks_minus = ["minus 0.25", "minus 0.75", "minus 1", "minus 2", "minus 3", "minus 4", "minus 5", "minus 6", "minus 7", "minus 8", "minus 9", "minus 10", "minus 11", "minus 12", "minus 13", "minus 14", "minus 15", "minus 16"]
        matriks_minus = matriks_minus[int(pesan2) - 1] if 1 <= int(pesan2) <= 18 else "Pilihan tidak valid"
        matriks_harga_minus = [250000, 250000, 250000, 250000, 250000, 250000,250000, 250000, 250000, 250000, 300000, 300000,300000, 300000, 300000, 300000, 300000, 300000]
        matriks_harga_minus = matriks_harga_minus[int(pesan2) - 1] if 1 <= int(pesan2) <= 18 else 0
        
        if pesan2.isdigit() and 0 <= int(pesan2) <= 18:
            indeks_pilihan = int(pesan2) - 1
            print("""
            Anda memilih kacamata minus 
            ===================================================================
            berikut Frame yang tersedia:
            ===================================================================
                                     FRAME PLASTIK
                        1. Frame plastik              (Rp 150.000)
                        2. Frame plastik Boss         (Rp 150.000)
                        3. Frame plastik Gucci        (Rp 150.000)
                        4. Frame plastik rodenstock   (Rp 150.000)
                        5. Frame plastik xinshisang   (Rp 150.000)
                        6. Frame plastik saturdays    (Rp 150.000)
                        7. Frame plastik SPY+         (Rp 150.000)
                        8. Frame plastik hualing      (Rp 150.000)
                        8. Frame plastik Dolbi        (Rp 150.000)
                        9. Frame plastik carla        (Rp 150.000)
                        10. Frame plastik geck         (Rp 150.000)
                        11. Frame plastik maple        (Rp 150.000)
                        12. Frame plastik oaks         (Rp 150.000)
                        13. Frame plastik nvg opthalmic (Rp 150.000)
                        14. Frame plastik bvlgari      (Rp 150.000)
                        15. Frame plastik elegant      (Rp 150.000)
                        16. Frame plastik giordano     (Rp 150.000)
                        17. Frame plastik corsella     (Rp 150.000)
                        19. Frame plastik acapulco     (Rp 150.000)
                        20. Frame plastik level up     (Rp 150.000)
                        21. Frame plastik filla        (Rp 150.000)
                        22. Frame plastik ack          (Rp 150.000)
                        23. Frame plastik kadishi      (Rp 150.000)
                        24. Frame plastik lullaby      (Rp 150.000)
                        25. Frame plastik freedom      (Rp 150.000)
                        26. Frame plastik fells        (Rp 150.000)
                        27. Frame plastik gucci        (Rp 150.000)
                        28. Frame plastik celine       (Rp 150.000)
                        29. Frame plastik mitu         (Rp 150.000)
                        30. Frame plastik burnerry     (Rp 150.000)
                        31. Frame plastik louis vuitton (Rp 150.000)
                        32. Frame plastik adibos       (Rp 150.000)
                                  FRAME BESI
                        33. Frame besi biasa           (Rp 300.000)
                        34. Frame besi elements      (Rp 1.500.000)
                        35. Frame besi bulgary       (Rp 1.500.000)
                        36. Frame besi amaya         (Rp 1.500.000)
                        37. Frame besi moscot        (Rp 1.500.000)
                        38. Frame besi givenchy      (Rp 1.500.000)
             ===================================================================
            """)
            pesanframe1 = input("Masukkan pilihan frame yang ingin Anda beli (1-38): ").strip().lower()
            matriks_frame1 = ['Frame plastik bisas', 'Frame plastik boss', 'Frame plastik gucci', 'Frame plastik rodenstock', 'Frame plastik xinshisang', 'Frame plastik saturdays', 'Frame plastik SPY+', 'Frame plastik hualing', 'Frame plastik Dolbi', 'Frame plastik carla', 'Frame plastik geck', 'Frame plastik maple', 'Frame plastik oaks', 'Frame plastik nvg opthalmic', 'Frame plastik bvlgari', 'Frame plastik elegant', 'Frame plastik giordano', 'Frame plastik corsella', 'Frame plastik acapulco', 'Frame plastik level up', 'Frame plastik filla', 'Frame plastik ack', 'Frame plastik kadishi', 'Frame plastik lullaby', 'Frame plastik freedom', 'Frame plastik fells', 'Frame plastik gucci', 'Frame plastik celine', 'Frame plastik mitu', 'Frame plastik burnerry', 'Frame plastik louis vuitton', 'Frame plastik adibos', 'Frame besi biasa', 'Frame besi elements', 'Frame besi bulgary', 'Frame besi amaya', 'Frame besi moscot', 'Frame besi givenchy']
            matriks_frame1 = matriks_frame1[int(pesanframe1) - 1] if 1 <= int(pesanframe1) <= 38 else "Pilihan tidak valid"                           
            matriks_harga_frame1 = [150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 300000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000]
            matriks_harga_frame1 = matriks_harga_frame1[int(pesanframe1) - 1] if 1 <= int(pesanframe1) <= 38 else 0
           

            if pesanframe1.isdigit() and 0 <= int(pesanframe1) <= 38:
                indeks_frame = int(pesanframe1) - 1
                print("""
                Anda memilih Frame A.
                ====================================================
                berikut fitur lapisan yang tersedia:
                ====================================================
                1. Anti-Radiasi / Blue Light Filter  (Rp 200.000)
                2. Photocromic (Transisi)            (Rp 350.000)
                3. Bluechromic                       (Rp 400.000)
                4. Lensa biasa                       (Rp 150.000)
                ====================================================
                """)
                pesanlapisan1 = input("Masukkan pilihan lapisan yang ingin Anda beli (1-4): ").strip().lower()
                matriks_lapisan1 = ['Anti-Radiasi / Blue Light Filter', 'Photocromic (Transisi)', 'UV Protection', 'Anti-Glare (Anti-Reflektif)', 'Polarized', 'Lapisan Anti-Gores & Hidrofobik']
                matriks_lapisan1 = matriks_lapisan1[int(pesanlapisan1) - 1] if 1 <= int(pesanlapisan1) <= 6 else "Pilihan tidak valid"
                matriks_harga_lapisan1 = [200000, 350000, 400000, 150000]
                matriks_harga_lapisan1 = matriks_harga_lapisan1[int(pesanlapisan1) - 1] if 1 <= int(pesanlapisan1) <= 6 else 0


                if pesanlapisan1.isdigit() and 0 <= int(pesanlapisan1) <= 6:
                    indeks_bentuk = int(pesanlapisan1) - 1
                    print("""
                    Anda memilih bentuk kacamata 
                    ====================================================
                    berikut kacamata yang tersedia:
                    ====================================================
                    1. kacamata persegi panjang
                    2. kacamata kotak
                    3. kacamata bulat            
                    4. kacamata aviator                    
                    5. kacamata cat-eye
                    6. kacamata wayfarer
                    7. kacamata oval                  
                    ====================================================
                    """)
                    bentukkacamata = input("Masukkan pilihan bentuk kacamata yang ingin Anda beli (1-6): ").strip().lower()
                    matriks_bentuk = ['kacamata persegi panjang', 'kacamata kotak', 'kacamata bulat', 'kacamata aviator', 'kacamata cat-eye', 'kacamata wayfarer', 'kacamata oval']
                    matriks_bentuk = matriks_bentuk[int(bentukkacamata) - 1] if 1 <= int(bentukkacamata) <= 7 else "Pilihan tidak valid"
                 

                    if bentukkacamata.isdigit() and 0 <= int(bentukkacamata) <= 7:
                       indeks_bentuk = int(bentukkacamata) - 1
                       print("")
                       print("===================================================================")
                       print("Total Pembayaran")
                       print("===================================================================")
                       print("Tanggal               :", sekarang.strftime("%d-%m-%Y"))
                       print("Waktu                 :", sekarang.strftime("%H:%M:%S"))
                       print("kacamata yang dipilih :", matriks_kacamata,)
                       print("bentuk kacamata yang dipilih :", matriks_bentuk)
                       print("minus yang dipilih    :", matriks_minus, "dengan harga Rp.", matriks_harga_minus)
                       print("Frame yang dipilih    :", matriks_frame1, "dengan harga Rp.", matriks_harga_frame1)
                       print("Lapisan yang dipilih  :", matriks_lapisan1, "dengan harga Rp.", matriks_harga_lapisan1)
                       jumlahpesan = int(input("Masukkan jumlah kacamata yang ingin dibeli: "))
                       total_pembayaran = (matriks_harga_minus + matriks_harga_frame1 + matriks_harga_lapisan1) * jumlahpesan

                       print("===================================================================")
                       print("Total pembayaran yang harus dibayarkan adalah Rp", total_pembayaran)
                    else:
                        print('pilihan tidak valid')
                        sys.exit()
                else:
                    print('pilihan tidak valid')
                    sys.exit()
            else:
                print('pilihan tidak valid')
                sys.exit()
        else:
            print('pilihan tidak valid')
            sys.exit()
   

    elif pesan == '2':
        print("Anda memilih kacamata plus.")
        print("""
        ===================================================
        Berikut adalah daftar kacamata plus yang tersedia:
        ===================================================
        1. plus 0.25
        2. plus 0.75
        3. plus 1
        4. plus 2
        5. plus 3
        6. plus 4
        7. plus 5
        8. plus 6
        9. plus 7
        10. plus 8
        11. plus 9
        12. plus 10
        13. plus 11
        14. plus 12
        15. plus 13
        16. plus 14
        17. plus 15
        18. plus 16
        ==================================================
        """)
        pesan2 = input("Masukkan pilihan kacamata plus yang ingin Anda beli (1-18): ")
        matriks_plus = ["plus 0.25", "plus 0.75", "plus 1", "plus 2", "plus 3", "plus 4",
                         "plus 5", "plus 6", "plus 7", "plus 8", "plus 9", "plus 10",
                         "plus 11", "plus 12", "plus 13", "plus 14", "plus 15", "plus 16"]
        matriks_plus = matriks_plus[int(pesan2) - 1] if 1 <= int(pesan2) <= 18 else "Pilihan tidak valid"
        matriks_harga_plus = [250000, 250000, 250000, 250000, 250000, 250000,250000, 250000, 250000, 300000, 300000, 300000,300000, 300000, 300000, 300000, 300000, 300000]    
        matriks_harga_plus = matriks_harga_plus[int(pesan2) - 1] if 1 <= int(pesan2) <= 18 else 0
        if pesan2.isdigit() and 1 <= int(pesan2) <= 18:
            indeks_pilihan = int(pesan2) - 1
            print("""
            Anda memilih kacamata plus 0.25.
            =========================================================
            berikut Frame yang tersedia:
            =========================================================
                                  FRAME PLASTIK
                    1. Frame plastik              (Rp 150.000)
                    2. Frame plastik Boss         (Rp 150.000)
                    3. Frame plastik Gucci        (Rp 150.000)
                    4. Frame plastik rodenstock   (Rp 150.000)
                    5. Frame plastik xinshisang   (Rp 150.000)
                    6. Frame plastik saturdays    (Rp 150.000)
                    7. Frame plastik SPY+         (Rp 150.000)
                    8. Frame plastik hualing      (Rp 150.000)
                    8. Frame plastik Dolbi        (Rp 150.000)
                    9. Frame plastik carla        (Rp 150.000)
                    10. Frame plastik geck         (Rp 150.000)
                    11. Frame plastik maple        (Rp 150.000)
                    12. Frame plastik oaks         (Rp 150.000)
                    13. Frame plastik nvg opthalmic (Rp 150.000)
                    14. Frame plastik bvlgari      (Rp 150.000)
                    15. Frame plastik elegant      (Rp 150.000)
                    16. Frame plastik giordano     (Rp 150.000)
                    17. Frame plastik corsella     (Rp 150.000)
                    19. Frame plastik acapulco     (Rp 150.000)
                    20. Frame plastik level up     (Rp 150.000)
                    21. Frame plastik filla        (Rp 150.000)
                    22. Frame plastik ack          (Rp 150.000)
                    23. Frame plastik kadishi      (Rp 150.000)
                    24. Frame plastik lullaby      (Rp 150.000)
                    25. Frame plastik freedom      (Rp 150.000)
                    26. Frame plastik fells        (Rp 150.000)
                    27. Frame plastik gucci        (Rp 150.000)
                    28. Frame plastik celine       (Rp 150.000)
                    29. Frame plastik mitu         (Rp 150.000)
                    30. Frame plastik burnerry     (Rp 150.000)
                    31. Frame plastik louis vuitton (Rp 150.000)
                    32. Frame plastik adibos       (Rp 150.000)
                              FRAME BESI
                    33. Frame besi biasa           (Rp 300.000)
                    34. Frame besi elements      (Rp 1.500.000)
                    35. Frame besi bulgary       (Rp 1.500.000)
                    36. Frame besi amaya         (Rp 1.500.000)
                    37. Frame besi moscot        (Rp 1.500.000)
                    38. Frame besi givenchy      (Rp 1.500.000)
            ===========================================================
            
            """)
            pesanframe2 = input("Masukkan pilihan frame yang ingin Anda beli (1-38): ")
            matriks_frame2 = ['Frame plastik', 'Frame plastik boss', 'Frame plastik gucci', 'Frame plastik rodenstock', 'Frame plastik xinshisang', 'Frame plastik saturdays', 'Frame plastik SPY+', 'Frame plastik hualing', 'Frame plastik Dolbi', 'Frame plastik carla', 'Frame plastik geck', 'Frame plastik maple', 'Frame plastik oaks', 'Frame plastik nvg opthalmic', 'Frame plastik bvlgari', 'Frame plastik elegant', 'Frame plastik giordano', 'Frame plastik corsella', 'Frame plastik acapulco', 'Frame plastik level up', 'Frame plastik filla', 'Frame plastik ack', 'Frame plastik kadishi', 'Frame plastik lullaby', 'Frame plastik freedom', 'Frame plastik fells', 'Frame plastik gucci', 'Frame plastik celine', 'Frame plastik mitu', 'Frame plastik burnerry', 'Frame plastik louis vuitton', 'Frame plastik adibos', 'Frame besi biasa', 'Frame besi elements', 'Frame besi bulgary', 'Frame besi amaya', 'Frame besi moscot', 'Frame besi givenchy']
            matriks_frame2 = matriks_frame2[int(pesanframe2) - 1 if 1 <= int(pesanframe2) <= 38 else "Pilihan tidak valid"]
            matriks_harga_frame2 = [150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 300000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000]
            matriks_harga_frame2 = matriks_harga_frame2[int(pesanframe2) - 1] if 1 <= int(pesanframe2) <= 38 else 0
            if pesanframe2.isdigit() and 1 <= int(pesanframe2) <= 38:
                indeks_frame = int(pesanframe2) - 1
                print("""
                Anda memilih Frame A.
                ====================================================
                berikut fitur lapisan yang tersedia:
                ====================================================
                1. Anti-Radiasi / Blue Light Filter  (Rp 200.000)
                2. Photocromic (Transisi)            (Rp 350.000)
                3. Bluechromic                       (Rp 400.000)
                4. Lensa biasa                       (Rp 150.000)
                ====================================================
                """)
                pesanlapisan2 = input("Masukkan pilihan lapisan yang ingin Anda beli (1-4): ")
                matriks_lapisan2 = ['Anti-Radiasi / Blue Light Filter', 'Photocromic (Transisi)', 'Bluechromic', 'Lensa biasa']
                matriks_lapisan2 = matriks_lapisan2[int(pesanlapisan2) - 1] if 1 <= int(pesanlapisan2) <= 4 else "Pilihan tidak valid"
                matriks_harga_lapisan2 = [200000, 350000, 400000, 150000]
                matriks_harga_lapisan2 = matriks_harga_lapisan2[int(pesanlapisan2) - 1] if 1 <= int(pesanlapisan2) <= 4 else 0
                if pesanlapisan2.isdigit() and 1 <= int(pesanlapisan2) <= 4:
                    indeks_lapisan = int(pesanlapisan2) - 1
                    print("""
                          Anda memilih bentuk kacamata 
                          ====================================================
                          berikut kacamata yang tersedia:
                          ====================================================
                          1. kacamata persegi panjang
                          2. kacamata kotak
                          3. kacamata bulat            
                          4. kacamata aviator                    
                          5. kacamata cat-eye
                          6. kacamata wayfarer
                          7. kacamata oval                  
                         ====================================================
                                        """)
                    bentukkacamata = input("Masukkan pilihan bentuk kacamata yang ingin Anda beli (1-6): ").strip().lower()
                    matriks_bentuk = ['kacamata persegi panjang', 'kacamata kotak', 'kacamata bulat', 'kacamata aviator', 'kacamata cat-eye', 'kacamata wayfarer', 'kacamata oval']
                    matriks_bentuk = matriks_bentuk[int(bentukkacamata) - 1] if 1 <= int(bentukkacamata) <= 7 else "Pilihan tidak valid"
                    if bentukkacamata.isdigit() and 1 <= int(bentukkacamata) <= 7:

                      indeks_lapisan = int(bentukkacamata) - 1
                      print("")
                      print("===================================================================")
                      print("Total Pembayaran")
                      print("===================================================================")
                      print("Tanggal               :", sekarang.strftime("%d-%m-%Y"))
                      print("Waktu                 :", sekarang.strftime("%H:%M:%S"))
                      print("kacamata yang dipilih :", matriks_kacamata,)
                      print("bentuk kacamata yang dipilih :", matriks_bentuk)
                      print("plus yang dipilih     :", matriks_plus, "dengan harga Rp", matriks_harga_plus)
                      print("Frame yang dipilih    :", matriks_frame2, "dengan harga Rp", matriks_harga_frame2)
                      print("Lapisan yang dipilih  :", matriks_lapisan2, "dengan harga Rp", matriks_harga_lapisan2)
                      jumlahpesan = int(input("Masukkan jumlah kacamata yang ingin dibeli: "))
                      total_pembayaran = (matriks_harga_plus + matriks_harga_frame2 + matriks_harga_lapisan2) * jumlahpesan
                      print("===================================================================")
                      print("Total pembayaran yang harus dibayarkan adalah Rp", total_pembayaran)
                    else:
                      print('pilihan tidak valid')
                      sys.exit()
                else:
                    print('pilihan tidak valid')
                    sys.exit()
            else:
                print('pilihan tidak valid')
                sys.exit()
        else:
            print('pilihan tidak valid')
            sys.exit()
        
    elif pesan == '3':
        print("Anda memilih kacamata silinder.")
        print("""
        ===================================================
        Berikut adalah daftar kacamata silinder yang tersedia:
        ===================================================
        1. silinder 0.25
        2. silinder 0.75
        3. silinder 1
        4. silinder 2
        5. silinder 3
        6. silinder 4
        7. silinder 5
        8. silinder 6
        9. silinder 7
        10. silinder 8
        11. silinder 9
        12. silinder 10
        13. silinder 11
        14. silinder 12
        15. silinder 13
        16. silinder 14
        17. silinder 15
        18. silinder 16
        ==================================================""")
        pesan2 = input("Masukkan pilihan kacamata silinder yang ingin Anda beli (1-18): ")
        matriks_silinder = ["silinder 0.25", "silinder 0.75", "silinder 1", "silinder 2", "silinder 3", "silinder 4",
                         "silinder 5", "silinder 6", "silinder 7", "silinder 8", "silinder 9", "silinder 10",
                         "silinder 11", "silinder 12", "silinder 13", "silinder 14", "silinder 15", "silinder 16"]
        matriks_silinder = matriks_silinder[int(pesan2) - 1] if 1 <= int(pesan2) <= 18 else "Pilihan tidak valid"
        matriks_harga_silinder = [250000, 250000, 250000, 250000, 250000, 250000,250000, 250000, 300000, 300000, 300000, 300000,300000, 300000, 300000, 300000, 300000, 300000]
        matriks_harga_silinder = matriks_harga_silinder[int(pesan2) - 1] if 1 <= int(pesan2) <= 18 else 0
        if pesan2.isdigit() and 1 <= int(pesan2) <= 18:
            indeks_pilihan = int(pesan2) - 1
            print("""
            Anda memilih kacamata silinder 
            ===========================================
            berikut Frame yang tersedia:
            ===========================================
                    FRAME PLASTIK
            1. Frame plastik              (Rp 150.000)
            2. Frame plastik Boss         (Rp 150.000)
            3. Frame plastik Gucci        (Rp 150.000)
            4. Frame plastik rodenstock   (Rp 150.000)
            5. Frame plastik xinshisang   (Rp 150.000)
            6. Frame plastik saturdays    (Rp 150.000)
            7. Frame plastik SPY+         (Rp 150.000)
            8. Frame plastik hualing      (Rp 150.000)
            8. Frame plastik Dolbi        (Rp 150.000)
            9. Frame plastik carla        (Rp 150.000)
            10. Frame plastik geck         (Rp 150.000)
            11. Frame plastik maple        (Rp 150.000)
            12. Frame plastik oaks         (Rp 150.000)
            13. Frame plastik nvg opthalmic (Rp 150.000)
            14. Frame plastik bvlgari      (Rp 150.000)
            15. Frame plastik elegant      (Rp 150.000)
            16. Frame plastik giordano     (Rp 150.000)
            17. Frame plastik corsella     (Rp 150.000)
            19. Frame plastik acapulco     (Rp 150.000)
            20. Frame plastik level up     (Rp 150.000)
            21. Frame plastik filla        (Rp 150.000)
            22. Frame plastik ack          (Rp 150.000)
            23. Frame plastik kadishi      (Rp 150.000)
            24. Frame plastik lullaby      (Rp 150.000)
            25. Frame plastik freedom      (Rp 150.000)
            26. Frame plastik fells        (Rp 150.000)
            27. Frame plastik gucci        (Rp 150.000)
            28. Frame plastik celine       (Rp 150.000)
            29. Frame plastik mitu         (Rp 150.000)
            30. Frame plastik burnerry     (Rp 150.000)
            31. Frame plastik louis vuitton (Rp 150.000)
            32. Frame plastik adibos       (Rp 150.000)
                      FRAME BESI
            33. Frame besi biasa           (Rp 300.000)
            34. Frame besi elements      (Rp 1.500.000)
            35. Frame besi bulgary       (Rp 1.500.000)
            36. Frame besi amaya         (Rp 1.500.000)
            37. Frame besi moscot        (Rp 1.500.000)
            38. Frame besi givenchy      (Rp 1.500.000)
            ===================================================================
            """)
            pesanframe3 = input("Masukkan pilihan frame yang ingin Anda beli (1-38): ")
            matriks_frame3 = ['Frame plastik', 'Frame plastik boss', 'Frame plastik gucci', 'Frame plastik rodenstock', 'Frame plastik xinshisang', 'Frame plastik saturdays', 'Frame plastik SPY+', 'Frame plastik hualing', 'Frame plastik Dolbi', 'Frame plastik carla', 'Frame plastik geck', 'Frame plastik maple', 'Frame plastik oaks', 'Frame plastik nvg opthalmic', 'Frame plastik bvlgari', 'Frame plastik elegant', 'Frame plastik giordano', 'Frame plastik corsella', 'Frame plastik acapulco', 'Frame plastik level up', 'Frame plastik filla', 'Frame plastik ack', 'Frame plastik kadishi', 'Frame plastik lullaby', 'Frame plastik freedom', 'Frame plastik fells', 'Frame plastik gucci', 'Frame plastik celine', 'Frame plastik mitu', 'Frame plastik burnerry', 'Frame plastik louis vuitton', 'Frame plastik adibos', 'Frame besi biasa', 'Frame besi elements', 'Frame besi bulgary', 'Frame besi amaya', 'Frame besi moscot', 'Frame besi givenchy']
            matriks_frame3 = matriks_frame3[int(pesanframe3) - 1 if 1 <= int(pesanframe3) <= 38 else "Pilihan tidak valid"]
            matriks_harga_frame3 = [150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 150000, 300000, 1500000, 1500000, 1500000, 1500000, 1500000, 1500000]
            matriks_harga_frame3 = matriks_harga_frame3[int(pesanframe3) - 1] if 1 <= int(pesanframe3) <= 38 else 0
            if pesanframe3.isdigit() and 1 <= int(pesanframe3) <= 38:
                indeks_frame = int(pesanframe3) - 1
                print("""
                Anda memilih Frame A.
                ====================================================
                berikut fitur lapisan yang tersedia:
                ====================================================
                1. Anti-Radiasi / Blue Light Filter  (Rp 200.000)
                2. Photocromic (Transisi)            (Rp 350.000)
                3. Bluechromic                       (Rp 400.000)
                4. Lensa biasa                       (Rp 150.000)
                ====================================================
                """)
                pesanlapisan3 = input("Masukkan pilihan lapisan yang ingin Anda beli (1-6): ")
                matriks_lapisan3 = ['Anti-Radiasi / Blue Light Filter', 'Photocromic (Transisi)', 'Bluechromic', 'Lensa biasa']
                matriks_lapisan3 = matriks_lapisan3[int(pesanlapisan3) - 1] if '1' <= pesanlapisan3 <= '4' else "Pilihan tidak valid"
                matriks_harga_lapisan3 = [200000, 350000, 400000, 150000]
                matriks_harga_lapisan3 = matriks_harga_lapisan3[int(pesanlapisan3) - 1] if '1' <= pesanlapisan3 <= '4' else 0
                if pesanlapisan3.isdigit() and 0 <= int(pesanlapisan3) <= 4:
                    indeks_lapisan = int(pesanlapisan3) - 1
                    print("""
                          Anda memilih bentuk kacamata 
                          ====================================================
                          berikut kacamata yang tersedia:
                          ====================================================
                          1. kacamata persegi panjang
                          2. kacamata kotak
                          3. kacamata bulat            
                          4. kacamata aviator                    
                          5. kacamata cat-eye
                          6. kacamata wayfarer
                          7. kacamata oval
                          ====================================================
                          """)
                    bentukkacamata = input("Masukkan pilihan bentuk kacamata yang ingin Anda beli (1-6): ").strip().lower()
                    matriks_bentuk = ['kacamata persegi panjang', 'kacamata kotak', 'kacamata bulat', 'kacamata aviator', 'kacamata cat-eye', 'kacamata wayfarer', 'kacamata oval']
                    matriks_bentuk = matriks_bentuk[int(bentukkacamata) - 1] if '1' <= bentukkacamata <= '7' else "Pilihan tidak valid"
                    if bentukkacamata.isdigit() and 0 <= int(bentukkacamata) <= 4:
                       indeks_lapisan = int(bentukkacamata) - 1
                       print("")
                       print("===================================================================")
                       print("Total Pembayaran")
                       print("===================================================================")
                       print("Tanggal               :", sekarang.strftime("%d-%m-%Y"))
                       print("Waktu                 :", sekarang.strftime("%H:%M:%S"))
                       print("kacamata yang dipilih :", matriks_kacamata,)
                       print("bentuk kacamata yang dipilih :", matriks_bentuk)
                       print("silinder yang dipilih :", matriks_silinder, "dengan harga Rp", matriks_harga_silinder)
                       print("Frame yang dipilih    :", matriks_frame3, "dengan harga Rp", matriks_harga_frame3)
                       print("Lapisan yang dipilih  :", matriks_lapisan3, "dengan harga Rp", matriks_harga_lapisan3)
                       jumlahpesan = int(input("Masukkan jumlah kacamata yang ingin dibeli: "))
                       total_pembayaran = (matriks_harga_silinder + matriks_harga_frame3 + matriks_harga_lapisan3) * jumlahpesan
                       print("===================================================================")
                       print("Total pembayaran yang harus dibayarkan adalah Rp", total_pembayaran)

                    else:
                      print("Pilihan tidak valid.")
                      sys.exit()
                else:
                    print("Pilihan tidak valid.")
                    sys.exit()
            else:
                print('pilhan tidak valid')
                sys.exit()
        else:
            print('pilihan tidak valid')
            sys.exit()

    elif pesan == '4':
        print("Anda memilih kacamata sunglasses.")
        print("""
        ===================================================
        berikut yang tersedia:
        ===================================================
        1. kacamata sunglasses kotak           (Rp 300.000)
        2. kacamata sunglasses premium kotak   (Rp 400.000)
        ===================================================
        """)
        pesan2 = input("Masukkan pilihan kacamata sunglasses yang ingin Anda beli (1-2): ")
        matriks_sunglasses = ["kacamata sunglasses kotak", "kacamata sunglasses premium kotak"]
        matriks_sunglasses = matriks_sunglasses[int(pesan2) - 1] if '1' <= pesan2 <= '2' else "Pilihan tidak valid"
        matriks_harga_sunglasses = [300000, 400000]
        matriks_harga_sunglasses = matriks_harga_sunglasses[int(pesan2) - 1] if '1' <= pesan2 <= '2' else 0
        if pesan2.isdigit() and 0 <= int(pesan2) <= 2:
            indeks_pilihan = int(pesan2)-1
            print(" ")
            print("===================================================================")
            print("Total Pembayaran")
            print("===================================================================")
            print("Tanggal                            :", sekarang.strftime("%d-%m-%Y"))
            print("Waktu                              :", sekarang.strftime("%H:%M:%S"))
            print("kacamata yang dipilih              :", matriks_kacamata,)
            print("sunglasses yang dipilih            :", matriks_sunglasses, "dengan harga Rp", matriks_harga_sunglasses)
            jumlahpesan = int(input("Masukkan jumlah kacamata yang ingin dibeli: "))
            total_pembayaran = matriks_harga_sunglasses * jumlahpesan
            print("===================================================================")
            print("Total pembayaran yang harus dibayarkan adalah Rp", total_pembayaran)
            print("===================================================================")

        else:
            print("Pilihan tidak valid.")
            sys.exit()

    elif pesan == '5':
        print("Anda Memilih Softlens")
        print("""
              =======================================================
              Berikut Produk yang tersedia
              =======================================================
              1. softlens 2 pasang (-0.50)               (Rp 150.000)
              2. softlens 2 pasang (-0.75)               (Rp 150.000)
              3. softlens 2 pasang (-1.50)               (Rp 150.000)
              4. softlens 2 pasang (-2.00)               (Rp 150.000)
              5. softlens 2 pasang (-2.75)               (Rp 150.000)
              6. softlens color Mistique                 (Rp 50.000)
              7. softlens color Exoticon K-pop           (Rp 50.000)
              8. softlens color Exoticon MAC             (Rp 50.000)
              9. softlens color Exoticon Itaewon Series  (Rp 75.000)
              =======================================================
              """)     
        pesan2 = input("Masukkan pilihan kacamata sunglasses yang ingin Anda beli (1-9): ")
        matriks_softlens = ["softlens (-0.50)", "softlens (-0.75)", "softlens (-1.50)", "softlens (-2.00)", "softlens (-2.75)", "softlens color Mistique", "softlens color Exoticon K-pop", "softlens color Exoticon MAC", "softlens color Exoticon Itaewon Series" ]
        matriks_softlens = matriks_softlens[int(pesan2) - 1] if '1' <= pesan2 <= '9' else "Pilihan tidak valid"
        matriks_harga_softlens = [150000, 150000, 150000, 150000, 150000, 50000, 50000, 50000, 75000]
        matriks_harga_softlens = matriks_harga_softlens[int(pesan2) - 1] if '1' <= pesan2 <= '9' else 0    
        if pesan2.isdigit() and 0 <= int(pesan2) <= 9:
                    indeks_pilihan = int(pesan2)-1
                    print(" ")
                    print("===================================================================")
                    print("Total Pembayaran")
                    print("===================================================================")
                    print("Tanggal                            :", sekarang.strftime("%d-%m-%Y"))
                    print("Waktu                              :", sekarang.strftime("%H:%M:%S"))
                    print("kacamata yang dipilih              :", matriks_kacamata,)
                    print("sunglasses yang dipilih            :", matriks_softlens, "dengan harga Rp", matriks_harga_softlens)
                    jumlahpesan = int(input("Masukkan jumlah kacamata yang ingin dibeli: "))
                    total_pembayaran = matriks_harga_softlens * jumlahpesan
                    print("===================================================================")
                    print("Total pembayaran yang harus dibayarkan adalah Rp", total_pembayaran)
                    print("===================================================================")
        
        else:
            print("Pilihan tidak valid.")
            sys.exit()

    elif pesan == '6':
        print(" Aksosoris kacamata dan softlens")
        print("""
            ======================================================================================
            Berikut produk yang tersedia:
            ======================================================================================
            1. X2 Comfort Extra 60 ml (softlens)                          =  (Rp 35.000)
            2. X2 Contacts Moisturizing and Comfort Drops 15 ml (softlens)=  (Rp 50.000)
            3. New Glow Lens Cleaner (kacamata)                           =  (Rp 30.000)
            4. Nashoo Self-Cleaning (kacamata)                            =  (Rp 50.000)
            ======================================================================================
            """)
        pesan2 = input("Masukkan pilihan kacamata sunglasses yang ingin Anda beli (1-4): ")
        matriks_aksesoris = ["X2 Comfort Extra 60 ml (softlens)", "X2 Contacts Moisturizing and Comfort Drops 15 ml (softlens)", "New Glow Lens Cleaner (kacamata)", "Nashoo Self-Cleaning (kacamata)"]
        matriks_aksesoris = matriks_aksesoris[int(pesan2) - 1] if '1' <= pesan2 <= '4' else "Pilihan tidak valid"
        matriks_harga_aksesoris = [35000, 50000, 30000, 50000]
        matriks_harga_aksesoris = matriks_harga_aksesoris[int(pesan2) - 1] if '1' <= pesan2 <= '4' else 0    
        if pesan2.isdigit() and 0 <= int(pesan2) <= 4:
            indeks_pilihan = int(pesan2)-1
            print(" ")
            print("===================================================================")
            print("Total Pembayaran")
            print("===================================================================")
            print("Tanggal                            :", sekarang.strftime("%d-%m-%Y"))
            print("Waktu                              :", sekarang.strftime("%H:%M:%S"))
            print("kacamata yang dipilih              :", matriks_kacamata,)
            print("sunglasses yang dipilih            :", matriks_aksesoris, "dengan harga Rp", matriks_harga_aksesoris)
            jumlahpesan = int(input("Masukkan jumlah kacamata yang ingin dibeli: "))
            total_pembayaran = matriks_harga_aksesoris * jumlahpesan
            print("===================================================================")
            print("Total pembayaran yang harus dibayarkan adalah Rp", total_pembayaran)
            print("===================================================================")
                
        else:
            print("Pilihan tidak valid.")
            sys.exit()
    elif pesan == '7':
        print("Anda memilih Kacamata Renang")
        print("""
              =========================================================================
              Produk yuang tersedia:
              =========================================================================
              1. Kacamata Renang                                            (Rp 30.000)
              =========================================================================
              """)
        pesan2 = input("Masukan pilihan kacamata Renang yang ingin anda pilih: ")
        matriks_Renang = ['Kacamata Renang']
        matriks_harga_renang = [30000]
        if pesan2.isdigit() and 0 <= int(pesan2) <= 1:
                    indeks_pilihan = int(pesan2)-1
                    nama_produk = matriks_Renang[indeks_pilihan]
                    harga_produk = matriks_harga_renang[indeks_pilihan]
                    print(" ")
                    print("===================================================================")
                    print("Total Pembayaran")
                    print("===================================================================")
                    print("Tanggal                            :", sekarang.strftime("%d-%m-%Y"))
                    print("Waktu                              :", sekarang.strftime("%H:%M:%S"))
                    print("kacamata yang dipilih              :", matriks_kacamata,)
                    print("sunglasses yang dipilih            :", nama_produk, "dengan harga Rp", harga_produk)
                    jumlahpesan = int(input("Masukkan jumlah kacamata yang ingin dibeli: "))
                    total_pembayaran = harga_produk * jumlahpesan
                    print("===================================================================")
                    print("Total pembayaran yang harus dibayarkan adalah Rp", total_pembayaran)
                    print("===================================================================")

    elif pesan == '8':
            print("Anda memilih Kacamata Pelindung")
            print("""
                  =========================================================================
                  Produk yuang tersedia:
                  =========================================================================
                  1. Kacamata Pelindung                                         (Rp 30.000)
                  =========================================================================
                  """)
            pesan2 = input("Masukan pilihan kacamata Renang yang ingin anda pilih: ")
            matriks_Renang = ['Kacamata Renang']
            matriks_harga_renang = [30000]
            if pesan2.isdigit() and 1 <= int(pesan2) <= len(matriks_Renang):
                        indeks_pilihan = int(pesan2)-1
                        nama_produk = matriks_Renang[indeks_pilihan]
                        harga_produk = matriks_harga_renang[indeks_pilihan]
                        print(" ")
                        print("===================================================================")
                        print("Total Pembayaran")
                        print("===================================================================")
                        print("Tanggal                            :", sekarang.strftime("%d-%m-%Y"))
                        print("Waktu                              :", sekarang.strftime("%H:%M:%S"))
                        print("kacamata yang dipilih              :", matriks_kacamata,)
                        print("sunglasses yang dipilih            :", nama_produk, "dengan harga Rp", harga_produk)
                        jumlahpesan = int(input("Masukkan jumlah kacamata yang ingin dibeli: "))
                        total_pembayaran = harga_produk * jumlahpesan
                        print("===================================================================")
                        print("Total pembayaran yang harus dibayarkan adalah Rp", total_pembayaran)
                        print("===================================================================")

    else:
        print("Pilihan tidak valid.")
        sys.exit()


    print("Terima kasih telah berbelanja di toko kami!")
    pilihan = input("Apakah Anda ingin beli lagi (y/n): ")
    if pilihan == "y":
        print("\nPESAN LAGI SANA SAMA YANG JUAL...\n")
        pilihan = "y"
    elif pilihan == "n":
        print("\nselamat tinggal, sampai jumpa lagi di toko kami!\n")
        print("DADAHHHHH")
        pilihan = "n"
    else:
        print("\nInput tidak valid. Program otomatis berhenti.")
        pilihan = "n"