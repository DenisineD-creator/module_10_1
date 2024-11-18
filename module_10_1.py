import threading
from time import sleep, time

def measure_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = round(seconds % 60, 6)
    return f'{hours:02}:{minutes:02}:{seconds:06}'

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_funcs = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_funcs = time()

print(f'Время выполнения функций: {measure_time(end_funcs - start_funcs)}')

start_threads = time()

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread4.start()
thread4.join()

end_threads = time()

print(f'Работа потоков: {measure_time(end_threads - start_threads)}')