import requests

start = int(input("Начальный ID стикера: "))

end = int(input("Последний ID стикера: "))

resolution = int(input("1)64x64\n2)128x128\n3)256x256\n4)512x512\nКачество скачиваемых стикеров: "))

resolutions = ["64b", "128b", "256b", "512b"]

while start <= end:
    p = requests.get("https://vk.com/sticker/1-{0}-{1}-9".format(start, resolutions[resolution]))
    out = open("stickers/" + str(start) + ".png", "wb")
    out.write(p.content)
    out.close()
    print(str(start) + " downloaded")
    start += 1
