import threading
import time

import NeoDLib

threads = 0


def slow_method_for_sticker(start_id, end_id, resolution, folder):
    while start_id <= end_id:
        sticker = NeoDLib.Sticker(start_id, resolution, folder)
        sticker.get_request()
        try:
            sticker.download()
            start_id += 1
        except NeoDLib.ContentNotFound as e:
            print(e)
            start_id += 1


def fast_method_for_sticker(start_id, end_id, max_thread, resolution, folder):
    global threads

    def create_stick(id_start, resol, folder):
        global threads
        sticker = NeoDLib.Sticker(id_start, resol, folder)
        sticker.get_request()
        try:
            sticker.download()
        except NeoDLib.ContentNotFound:
            pass
        threads -= 1
    while start_id <= end_id:
        if max_thread >= threads:
            Thread_ = threading.Thread(target=create_stick, args=(start_id, resolution, folder))
            Thread_.start()
            threads += 1
            start_id += 1
        else:
            print("Потоков больше {0}, останавливаю работу на секунду.".format(max_thread))
            time.sleep(1)


def slow_method_for_gifts(start_id, end_id, resolution, folder):
    while start_id <= end_id:
        gift = NeoDLib.Gift(start_id, resolution, folder)
        try:
            gift.get_request()
            gift.download()
            start_id += 1
        except NeoDLib.ContentNotFound as e:
            print(e)
            start_id += 1


def fast_method_for_gifts(start_id, end_id, max_thread, resolution, folder):
    global threads

    def create_gift(id_start, resol, folder):
        global threads
        gift = NeoDLib.Gift(id_start, resol, folder)
        try:
            gift.get_request()
            gift.download()
        except NeoDLib.ContentNotFound:
            pass
        threads -= 1

    while start_id <= end_id:
        if max_thread >= threads:
            Thread_ = threading.Thread(target=create_gift, args=(start_id, resolution, folder))
            Thread_.start()
            threads += 1
            start_id += 1
        else:
            print("Потоков больше {0}, останавливаю работу на секунду.".format(max_thread))
            time.sleep(1)
