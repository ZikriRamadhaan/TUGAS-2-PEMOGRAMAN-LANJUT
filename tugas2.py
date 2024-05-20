def cetak_kuadrat(n):
    for i in range(n):
        print(i ** 2)


n = int(input("Masukkan nilai n: "))

print("Nilai kuadrat dari 0 hingga", n-1, ":")
cetak_kuadrat(n)




def cetak_kuadrat_ganjil(n):
    for i in range(n):
        if i % 2 != 0: 
            print(i ** 2)


n = int(input("Masukkan nilai n: "))

print("Nilai kuadrat dari bilangan ganjil antara 0 hingga", n-1, ":")
cetak_kuadrat_ganjil(n)