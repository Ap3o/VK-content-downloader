import requests


class NotASticker(Exception):
    pass


class Sticker(object):

    def __init__(self, serial_number, resolution, folder="stickers"):
        self.serial_number = serial_number
        self.resolution = resolution
        self.folder = folder

    def get_request(self):
        self.page = requests.get("https://vk.com/sticker/1-{0}-{1}-9".format(self.serial_number, self.resolution))

    def download(self):
        if self.page.status_code == 404:
            raise NotASticker("Page returned 404 response, {0} sticker not found".format(self.serial_number))
        out = open(self.folder + "/" + str(self.serial_number) + "-{0}.png".format(self.resolution), "wb")
        out.write(self.page.content)
        out.close()