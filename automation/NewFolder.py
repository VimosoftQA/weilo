# -*- coding: utf-8 -*-
from automation import logger, error_handler_class
from Action import Action
import time

@error_handler_class
class NewFolder:
    def __init__(self):
        self.action = Action()

    def create_new_folder(self):
        pass

@error_handler_class
class CurrentNewFolder(NewFolder):
    def create_new_folder(self):
        self.action.click("current_project_create_folder_button")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'current project create folder'")

@error_handler_class
class LibraryNewFolder(NewFolder):
    def create_new_folder(self):
        self.action.click("menu_library")
        logger.info("[Browser > MY] tap 'library'")
        self.action.click("library_create_folder_button")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'library create folder'")







if __name__ == "__main__":
    c_new_folder = CurrentNewFolder()
    c_new_folder.create_new_folder()
    l_new_folder = LibraryNewFolder()
    l_new_folder.create_new_folder()


