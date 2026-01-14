import time

memo = {}

def tower_of_hanoi_memo(n, source, auxiliary, target):
    key = (n, source, auxiliary, target)
    if key in memo:
        return memo[key]

    if n == 1:
        result = [f"Pindahkan cakram 1 dari {source} ke {target}"]
    else:
        result = []
        result += tower_of_hanoi_memo(n-1, source, target, auxiliary)
        result.append(f"Pindahkan cakram {n} dari {source} ke {target}")
        result += tower_of_hanoi_memo(n-1, auxiliary, source, target)
    
    memo[key] = result
    return result

# Contoh penggunaan
start_time = time.time()
hasil = tower_of_hanoi_memo(3, 'A', 'B', 'C')
end_time = time.time()

for langkah in hasil:
    print(langkah)

print("\nWaktu eksekusi (dengan memoization):", end_time - start_time, "detik")
