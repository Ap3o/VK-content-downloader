import methods

start_id = int(input("Начальный ID стикера: "))

end_id = int(input("Последний ID стикера: "))

resolution = int(input("1)64x64\n2)128x128\n3)256x256\n4)512x512\nКачество скачиваемых стикеров: "))

resolutions = ["64b", "128b", "256b", "512b"]

download_method = int(input("1)Slow(1 поток)\n2)Fast(Со своим ограничением)\nСпособ загрузки: "))

custom_folder = input("Директория для загрузки(Вводить без последнего '/'. \
Можно оставить пустым, тогда будет скачиваться в stickers/):")

if custom_folder == '':
    custom_folder = 'stickers'

if download_method == 1:
    methods.slow_method(start_id, end_id, resolutions[resolution-1], custom_folder)
else:
    max_thread = int(input("Максимальное количество потоков(Рекомендуется: 100): "))
    methods.fast_method(start_id, end_id, max_thread, resolutions[resolution-1], custom_folder)

