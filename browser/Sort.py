# -*- coding: utf-8 -*-
from browser import logger
from Action import Action
import time

class Sort:
    def __init__(self):
        self.action = Action()

    def sort_by_create_time(self):
        self.action.click("current_project_sort_button")
        logger.info("tap current project sort")

    def sort_by_edit_time(self):
        self.action.click("current_project_sort_button")
        logger.info("tap current project sort")

    def sort_by_name(self):
        self.action.click("current_project_sort_button")
        logger.info("tap current project sort")

    def sort_by_folders_up(self):
        self.action.click("sorting_by_folder")
        logger.info("tap sorting by folders up")

    def sort_by_files_up(self):
        self.action.click("sorting_by_file")
        logger.info("tap sorting by files up")

    def sort_by_mixed(self):
        self.action.click("sorting_by_mixed")
        logger.info("tap sorting by mixed")


