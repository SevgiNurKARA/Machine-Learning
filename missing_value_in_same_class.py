# Veriyi dosyadan oku
with open('p2_data.txt', 'r') as file:
    data = [line.strip().split(',') for line in file]  # Her satırı virgüle göre ayır

# Geçerli sayısal değer olup olmadığını kontrol eden bir fonksiyon
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# String değerleri sayısal değerlere dönüştürmeye hazırlık
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != '?' and is_float(data[i][j]):  # Eğer eksik değilse ve sayısal ise
            data[i][j] = float(data[i][j])

# Son sütun hariç her sütun için eksik değerleri ortalama ile doldur
for col in range(len(data[0]) - 1):
    # Geçerli sayısal değerleri al
    valid_values = [row[col] for row in data if isinstance(row[col], float)]
    
    if valid_values:
        mean = sum(valid_values) / len(valid_values)  # Ortalamayı hesapla
        
        # Eksik olan '?' yerleri ortalama ile değiştir
        for row in data:
            if row[col] == '?':
                row[col] = mean

# Sonuçları dosyaya yaz
with open('p2_output.txt', 'w') as output_file:
    for row in data:
        output_file.write(','.join(map(str, row)) + '\n')

print("İşlem tamamlandı. Sonuçlar 'p2_output.txt' dosyasına kaydedildi.")
