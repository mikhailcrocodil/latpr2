import hashlib
import itertools
import string
import time
import multiprocessing

def brute_force(hash_value, password_length, num_threads):
    start_time = time.time()

    # Генерируем все возможные комбинации паролей
    passwords = itertools.product(string.ascii_lowercase, repeat=password_length)

    # Разделяем пароли между потоками
    pool = multiprocessing.Pool(num_threads)
    results = pool.map(check_password, passwords)

    # Ищем пароль с совпадающим хэш-значением
    for password, password_hash in results:
        if password_hash == hash_value:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return password, elapsed_time

    return None, None

def check_password(password):
    password_str = ''.join(password)
    password_hash = hashlib.sha256(password_str.encode()).hexdigest()
    return password_str, password_hash

# Входные данные
hash_values = [
    "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad",
    "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b",
    "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"
]

password_length = 5

if __name__ == '__main__':
    num_threads = int(input("Введите количество потоков: "))
    # Запускаем перебор паролей
    for hash_value in hash_values:
        password, elapsed_time = brute_force(hash_value, password_length, num_threads)

        if password:
            print(f"Пароль: {password}")
            print(f"Затраченное время: {elapsed_time} секунд")
        else:
            print("Пароль не найден")