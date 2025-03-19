# -*- coding: utf-8 -*-
from browser import logger, error_handler_class
from Action import Action
import time

@error_handler_class
class Filter:
    def __init__(self):
        self.action = Action()

    def tap_filter_buttons(self):
        pass

    def filter_all_items(self):
        self.tap_filter_buttons()
        self.action.click("all_item")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'filter : all item'")

    def filter_single_clip(self):
        self.tap_filter_buttons()
        self.action.click("single_clip")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'filter : single clip'")

    def filter_folder(self):
        self.tap_filter_buttons()
        self.action.click("folder")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'filter : folder'")


@error_handler_class
class CurrentProjectFilter(Filter):
    def __init__(self):
        self.action = Action()

    def tap_filter_buttons(self):
        self.action.click("current_project_filter_button")
        time.sleep(1)
        logger.info("[Browswer > MY] tap 'current project filter'")


@error_handler_class
class LibraryFilter(Filter):
    def __init__(self):
        self.action = Action()
        self.action.click("menu_library")
        logger.info("[Browser > MY] tap 'library'")

    def tap_filter_buttons(self):
        self.action.click("library_filter_button")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'library filter'")



if __name__ == "__main__":
    c_filter = CurrentProjectFilter()
    c_filter.filter_all_items()
    c_filter.filter_single_clip()
    c_filter.filter_folder()
    l_filter = LibraryFilter()
    l_filter.filter_all_items()
    l_filter.filter_single_clip()
    l_filter.filter_folder()
