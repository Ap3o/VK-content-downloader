import requests


class ContentNotFound(Exception):
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
            raise ContentNotFound("Page returned 404 response, {0} sticker not found".format(self.serial_number))
        out = open(self.folder + "/" + str(self.serial_number) + "-{0}.png".format(self.resolution), "wb")
        out.write(self.page.content)
        out.close()


# Если честно, мне было лень перепиливать первый класс, поэтому сделал так)


class Gift(object):
    def __init__(self, serial_number, resolution, folder="content"):
        self.serial_number = serial_number
        self.resolution = resolution
        self.folder = folder
        self.request = None
        self.format = ''

    def get_request(self):
        self.request = requests.get(
            "https://vk.com/images/gift/{0}/{1}{2}".format(self.serial_number, self.resolution, ".jpg"))

        if self.request.status_code == 404:
            self.request = None
        else:
            self.format = ".jpg"

        self.second_request = requests.get(
            "https://vk.com/images/gift/{0}/{1}{2}".format(self.serial_number, self.resolution, ".png"))

        if self.second_request.status_code == 404:
            self.second_request = None
        else:
            self.second_format = ".png"

        if self.request is None and self.second_request is None:
            raise ContentNotFound("Page returned 404 response, {0} gift not found".format(self.serial_number))

    def download(self):
        if self.request is not None:
            out = open(self.folder + "/" + str(self.serial_number) + "-{0}{1}".format(self.resolution, self.format),
                       "wb")
            out.write(self.request.content)
            out.close()
        if self.second_request is not None:
            out = open(
                self.folder + "/" + str(self.serial_number) + "-{0}{1}".format(self.resolution, self.second_format),
                "wb")
            out.write(self.second_request.content)
            out.close()
