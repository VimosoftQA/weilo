# -*- coding: utf-8 -*-
from automation import logger
from Action import Action
import time


#TODO 애플 컴포넌트에 대한 접근성 아이디 추가 후 다시 구현하기
class Importing:
    def __init__(self):
        self.action = Action()

    def import_by_photos(self):
        self.action.click("current_project_import_from_photos_button")
        logger.info("[Browser > MY] tap 'import from photos'")
        self.action.click("PXGGridLayout-Info") #TODO 범용성이 있는 폴더 및 이름이 필요함
        self.action.click("Add")
        logger.info("[Browser > MY] add new photo")

    def import_by_files(self):
        self.action.click("current_project_import_from_files_button")
        logger.info("[Browser > MY] tap 'import from files'")
        self.action.click("Carly") # TODO 범용성이 있는 이름으로 변경이 필요함
        self.action.click("제목 없음, mp4") #TODO 범용성이 있는 이름으로 변경이 필요함
        self.action.click("Open")
        logger.info("[Browser > MY] add new file")

    def import_by_other_projects(self):
        self.action.click("current_project_import_from_other_project")
        logger.info("[Browser > MY] tap 'import from other projects'")
        self.action.click("import_from_other_project_list_project_0") # 가장 첫번째 위치한 폴더 탭
        self.action.click("Next")
        #TODO 임의의 프로젝트 탭하기
        self.action.click("Import")


#TODO 접근성 아이디 추가 후 다시 구현해야함
class MultiSelectOption:
    def __init__(self):
        self.action = Action()

    def tap_item_options(self):
        # 다중 선택 시 보여지는 옵션 버튼 (맨 처음 클립 추가 시 보여지는 버튼과 동일)
        # 갤러리에서 클립 선택 후 옵션 버튼을 누른다는 가정
        self.action.click("selected_option_button")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'item options'")

    def tap_item_options_create_new_folder(self):
        self.tap_item_options()
        self.action.click("clip_options_new_folder")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'item options create new folder'")

    def tap_item_options_move(self):
        self.tap_item_options()
        self.action.click("clip_options_move")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'item options move'")

    def tap_item_options_duplicate(self):
        self.tap_item_options()
        self.action.click("clip_options_duplicate")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'item options duplicate'")

    def tap_item_options_delete(self):
        self.tap_item_options()
        self.action.click("clip_options_delete")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'item options delete'")

    def tap_item_options_save_library(self):
        self.tap_item_options()
        self.action.click("clip_options_save_library")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'item options save library'")

    def tap_item_options_add(self):
        self.action.click("insert_button")
        time.sleep(1)
        logger.info("[Browser > MY] tap 'insert'")

    def tap_single_item_options(self): # 방금 추가한 0번째 아이템의 옵션을 확인한다.
        self.action.click("current_project_item_0_option_button")
        time.sleep(1)
        logger.info("tap first item options")


if __name__ == "__main__":
    importing = Importing()
    importing.import_by_files()
    multiselect = MultiSelectOption()
    multiselect.tap_item_options_add()