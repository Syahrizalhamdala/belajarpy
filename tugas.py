import time

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Pindahkan cakram 1 dari {source} ke {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Pindahkan cakram {n} dari {source} ke {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

# Contoh penggunaan
start_time = time.time()
tower_of_hanoi(3, 'A', 'B', 'C')
end_time = time.time()

print("\nWaktu eksekusi (tanpa optimasi):", end_time - start_time, "detik")
