import threading
import funks

def handle_task_1():
    mas_a = funks.gen_or_get_arr()
    mas_b = funks.gen_or_get_arr()
    print("Сумма (1) или разность (2)")
    x = int(input())
    if x == 1:
        print("Результат суммы:", funks.add_large_numbers(mas_a, mas_b))
    elif x == 2:
        print("Результат разности:", funks.subtract_large_numbers(mas_a, mas_b))
    else:
        print("Ошибка: неверный выбор")

def handle_task_2():
    arr1 = funks.gen_or_get_arr()
    arr2 = funks.gen_or_get_arr()
    print("Общие числа и перевёрнутые версии:", funks.count_common_numbers(arr1, arr2))

def handle_task_3():
    arr = funks.gen_or_get_arr()
    print("Введите число: ")
    num = int(input())
    print("Количество подмассивов с заданной суммой:", funks.count_subarrays_with_sum(arr, num))

def menu():
    while True:
        print("\nЗадачи:")
        print("1. Входные данные: 2 массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или разность массивов.")
        print("2. Входные данные: 2 массива с числами. Требуется проверить, сколько у массивов общих чисел, включая перевернутые версии.")
        print("3. Входные данные: массив и число. Требуется проверить, сколько подмассивов из массива в сумме могут давать это число.")
        print("4. Выход.")
        print("\nВыберите пункт меню:")
        try:
            point = int(input())
            if point == 1:
                threading.Thread(target=handle_task_1).start()
            elif point == 2:
                threading.Thread(target=handle_task_2).start()
            elif point == 3:
                threading.Thread(target=handle_task_3).start()
            elif point == 4:
                print("Выход из программы.")
                break
            else:
                print("Ошибка: неверный пункт меню.")
        except ValueError:
            print("Ошибка: введите корректный номер пункта меню.")

if __name__ == "__main__":
    menu()
