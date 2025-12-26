import argparse


def create_arguments():
    # создаем объект parsser для парсинга вводимых в консоль агрументов при запуске программы
    parser = argparse.ArgumentParser(description="Приложение для вычисления статистики температуры из CSV-файла.")
    # добавляем в parser аргумент указания пути к файлу
    parser.add_argument(
            "-f",
            "--file",
            help="Входной CSV-файл",
            required=False
    )
    # добавляем в parser аргумент указания месяца
    parser.add_argument(
            "-m",
            "--month",
            type=int,
            help="Номер месяца (1..12) для вывода статистики только по нему",
            required=False
    )
    return parser

# функция парсинга вводимых агрументов (проверяет есть ли агрументы и правильно ли они введены)
def parse_arguments(pars: argparse.ArgumentParser):
    args = pars.parse_args()
    if args.file is None:
        parser.print_help()
        return None, None
    else:
        filename = args.file
        month_filter = args.month
        if month_filter is not None:
            if not (1 <= month_filter <= 12):
                print("Ошибка: номер месяца должен быть от 1 до 12.")
                return None, None
            else:
                return filename, month_filter
        else:
            return filename, None

# функция разбирает строку, прочитанную из файла, и формирует на выходе словарь с данными из этой строки
def parse_line(row: list, line_no: int):
    for i in range(len(row)):
        row[i] = row[i].strip()
    # пробуем преобразовать данные в строке в число простым способом
    try:
        year = int(row[0])
        month = int(row[1])
        day = int(row[2])
        hour = int(row[3])
        minute = int(row[4])
        temperature = int(row[5])
    # если в данных строки ошибка то выводи строку и ее номер
    except Exception:
        print(f"WARNING: Строка {row}: не удалось преобразовать поля в числа -> пропуск.  Номер строки: {line_no}")
        return None
    return {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "temp": temperature,
    }

# функция чтения данных из файла и формирования списка нужных данных
def get_data_from_file(filename: str, month: int=None):
    line_datas = []
    # открываем файл для чтения через контекстный менеджер
    with open(filename) as f:
        line_number = 0
        for line in f:
            line_number += 1
            line = line.strip()
            if line == "":
                continue
            row = line.split(";")
            # получаем данные в виде словаря и добавляем в список
            line_data = parse_line(row, line_number)
            if line_data is not None:
                # если при запуске был указан месяц, то добавляем данные только по этому месяцу
                if month is not None:
                    if line_data["month"] == month:
                        line_datas.append(line_data)
                # иначе просто добавляем
                else:
                    line_datas.append(line_data)
    # возвращаем готовый список данных
    return line_datas

# функция подсчета статистики для списка данных
def get_states(datas: list):
    temp_count = 0
    temp_sum = 0
    temp_max = None
    temp_min = None
    for line in datas:
        new_temp = line['temp']
        temp_sum = temp_sum + new_temp
        temp_count = temp_count + 1
        if (temp_min is None) or (new_temp < temp_min):
            temp_min = new_temp
        if (temp_max is None) or (new_temp > temp_max):
            temp_max = new_temp
    temp_avg = temp_sum / temp_count

    return {
        "avg": temp_avg,
        "max": temp_max,
        "min": temp_min
    }

# функция получения статистики и вывода за месяц
def get_stats_month(filename: str, month: int):
    # получаем данные из файла в нужном представлении
    month_data = get_data_from_file(filename, month)
    if not month_data:
        print(f"WARNING: Нет данных для обработки за {month}-й месяц")
    else:
        # формируем статистику из данных
        states_data = get_states(month_data)
        print(f'==========={month}-й месяц=========== \n'
              f'СРЕДНЯЯ: {states_data.get("avg")}\n'
              f'МАКСИМАЛЬНАЯ: {states_data.get("max")}\n'
              f'МИНИМАЛЬНАЯ: {states_data.get("min")}\n'
              f'====================================')

# функция получения статистики и вывода за год
def get_stats_year(filename: str):
    # получаем данные из файла в нужном представлении
    year_data = get_data_from_file(filename)
    if not year_data:
        print("WARNING: Нет данных для обработки за год")
    else:
        # формируем статистику из данных
        states_data = get_states(year_data)
        print(f'================ГОД================= \n'
              f'СРЕДНЯЯ: {states_data.get("avg")}\n'
              f'МАКСИМАЛЬНАЯ: {states_data.get("max")}\n'
              f'МИНИМАЛЬНАЯ: {states_data.get("min")}\n'
              f'====================================')

# точка входа (запуск программы)
if __name__ == '__main__':
    # задание аргументов для выполнения программы
    parser = create_arguments()
    # чтение аргументов для выполнения
    file_name, month_filter = parse_arguments(parser)
    # если не указано имя файла - выход из программы
    if file_name is None:
        exit()
    # если указан месяц, то берем статистику по месяцу
    elif month_filter is not None:
        get_stats_month(file_name, month_filter)
    # если не указан месяц, то берем статистику за год
    else:
        get_stats_year(file_name)
    print('Программа завершена')

