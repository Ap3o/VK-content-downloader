import methods

what_to_download = int(input("1)Стикеры\n2)Подарки\nЧто будем скачивать? Вариант: "))

start_id = int(input("Начальный ID: "))

end_id = int(input("Последний ID: "))

download_method = int(input("1)Slow(1 поток)\n2)Fast(Со своим ограничением)\nСпособ загрузки: "))

custom_folder = input("Директория для загрузки(Вводить без последнего '/'. \
Можно оставить пустым, тогда будет скачиваться в content/):")

if custom_folder == '':
    custom_folder = 'content'

if what_to_download == 1:
    resolution = int(input("1)64x64\n2)128x128\n3)256x256\n4)512x512\nКачество скачиваемых стикеров: "))

    resolutions = ["64b", "128b", "256b", "512b"]

    if download_method == 1:
        methods.slow_method_for_sticker(start_id, end_id, resolutions[resolution - 1], custom_folder)
    else:
        max_thread = int(input("Максимальное количество потоков(Рекомендуется: 100): "))
        methods.fast_method_for_sticker(start_id, end_id, max_thread, resolutions[resolution - 1], custom_folder)

elif what_to_download == 2:
    resolution = int(input("1)256x256\n2)512x512\nКачество скачиваемых стикеров: "))

    resolutions = ["256", "512"]
    if download_method == 1:
        methods.slow_method_for_gifts(start_id, end_id, resolutions[resolution - 1], custom_folder)
    else:
        max_thread = int(input("Максимальное количество потоков(Рекомендуется: 100): "))
        methods.fast_method_for_gifts(start_id, end_id, max_thread, resolutions[resolution - 1], custom_folder)
