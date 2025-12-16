import os
import re

# Название папки с фото
FOLDER_NAME = "Images"
# Файл, куда запишем список изменений
OUTPUT_FILE = "images_map.txt"

# Словарь для транслитерации (ГОСТ-подобный + упрощение)
TRANS_MAP = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
    'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch',
    'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
}


def clean_filename(filename):
    # Разделяем имя и расширение
    name, ext = os.path.splitext(filename)

    # Транслитерация
    new_name = ""
    for char in name:
        new_name += TRANS_MAP.get(char, char)

    # Приводим к нижнему регистру
    new_name = new_name.lower()

    # Заменяем пробелы на дефисы
    new_name = new_name.replace(" ", "-")

    # Оставляем только латинские буквы, цифры и дефисы (убираем кавычки, скобки и т.д.)
    new_name = re.sub(r'[^a-z0-9-]', '', new_name)

    # Убираем дублирующиеся дефисы (например, если был пробел и скобка)
    new_name = re.sub(r'-+', '-', new_name)

    # Убираем дефисы по краям
    new_name = new_name.strip('-')

    return new_name + ext.lower()  # Возвращаем с расширением в нижнем регистре


def main():
    # Проверяем, существует ли папка
    if not os.path.exists(FOLDER_NAME):
        print(f"Ошибка: Папка '{FOLDER_NAME}' не найдена рядом со скриптом.")
        return

    files = [f for f in os.listdir(FOLDER_NAME) if os.path.isfile(os.path.join(FOLDER_NAME, f))]
    mapping_list = []

    print(f"Найдено файлов: {len(files)}")
    print("-" * 40)

    for filename in files:
        # Пропускаем скрытые файлы (на маке часто бывает .DS_Store)
        if filename.startswith('.'):
            continue

        old_path = os.path.join(FOLDER_NAME, filename)
        new_filename = clean_filename(filename)
        new_path = os.path.join(FOLDER_NAME, new_filename)

        # Переименовываем
        try:
            os.rename(old_path, new_path)
            # Добавляем в список для отчета: Старое Имя -> Новое Имя
            mapping_list.append(f"{filename} | {new_filename}")
            print(f"Переименовано: {filename} -> {new_filename}")
        except OSError as e:
            print(f"Ошибка при переименовании {filename}: {e}")

    # Записываем файл-отчет
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in mapping_list:
            f.write(line + "\n")

    print("-" * 40)
    print(f"Готово! Список изменений сохранен в файл '{OUTPUT_FILE}'.")
    print("Пришлите содержимое этого файла мне.")


if __name__ == "__main__":
    main()