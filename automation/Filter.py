# -*- coding: utf-8 -*-
from automation import logger
from automation import id
from Action import Action
import time

class Filter:
    def __init__(self):
        self.action = Action()

    def tap_filter_buttons(self):
        self.action.click("filter_button") # 임의의 값
        time.sleep(1)
        logger.info("tap filter button")

    def filter_all_items(self):
        self.tap_filter_buttons()
        self.action.click("all_item")
        time.sleep(1)
        logger.info("tap filter 모든 아이템")

    def filter_single_clip(self):
        self.tap_filter_buttons()
        self.action.click("single_clip")
        time.sleep(1)
        logger.info("tap filter 단일 클립")


    def filter_folder(self):
        self.tap_filter_buttons()
        self.action.click("folder")
        time.sleep(1)
        logger.info("tap filter 폴더")



class CurrentProjectFilter(Filter):
    def __init__(self):
        self.action = Action()

    def tap_filter_buttons(self):
        self.action.click("current_project_filter_button")
        time.sleep(1)
        logger.info("tap current project filter button")


class LibraryFilter(Filter):
    def __init__(self):
        self.action = Action()
        self.action.click("menu_library")

    def tap_filter_buttons(self):
        self.action.click("library_filter_button")
        time.sleep(1)
        logger.info("tap library filter button")



if __name__ == "__main__":
    c_filter = CurrentProjectFilter()
    c_filter.filter_all_items()
    c_filter.filter_single_clip()
    c_filter.filter_folder()
    l_filter = LibraryFilter()
    l_filter.filter_all_items()
    l_filter.filter_single_clip()
    l_filter.filter_folder()
