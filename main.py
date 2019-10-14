import requests

start = int(input("Начальный ID стикера: "))

end = int(input("Последний ID стикера: "))

resolution = int(input("1)64x64\n2)128x128\n3)256x256\n4)512x512\nКачество скачиваемых стикеров: "))

resolutions = ["64b", "128b", "256b", "512b"]

errors = 0

while (start <= end) and (errors != 1000):
    p = requests.get("https://vk.com/sticker/1-{0}-{1}-9".format(start, resolutions[resolution - 1]))
    if p.status_code == 404:
        print(str(start) + " skip. Have an error")
        start += 1
        errors += 1
        continue
    out = open("stickers/64x64/" + str(start) + "-{0}.png".format(resolutions[resolution - 1]), "wb")
    out.write(p.content)
    out.close()
    print(str(start) + " downloaded")
    start += 1

print("Скачано стикеров:", end - start, sep=' ')
print("Ошибок при скачивании:", errors, sep=' ')
