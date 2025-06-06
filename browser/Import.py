# -*- coding: utf-8 -*-
from browser import logger
from Action import Action
import time

from browser.Sort import Sort


#TODO 애플 컴포넌트에 대한 접근성 아이디 추가 후 다시 구현하기
class Importing:
    def __init__(self):
        self.action = Action()

    def import_by_photos(self):
        self.action.click("current_project_import_from_photos_button")
        logger.info("[Browser > MY] tap 'import from photos'")
        self.action.click("PXGGridLayout-Info") # 애플 컴포넌트에 대한 ID 부재로 임의로 값 지정
        self.action.click("Add")
        logger.info("[Browser > MY] add new photo")

    def import_by_files(self):
        self.action.click("current_project_import_from_files_button")
        logger.info("[Browser > MY] tap 'import from files'")
        self.action.click("Carly") # 자동화 테스트 폴더
        self.action.click("제목 없음, mp4") # 자동화 테스트 영상
        self.action.click("Open")
        logger.info("[Browser > MY] add new file")

    def import_by_other_projects(self):
        self.action.click("current_project_import_from_other_project")
        self.action.click("Cancel")
        logger.info("[Browser > MY] tap Cancel")
        self.action.click("current_project_import_from_other_project")
        logger.info("[Browser > MY] tap 'import from other projects'")
        self.action.click("import_from_other_project_sort_button")
        sort = Sort()
        sort.sort_by_folders_up()
        self.action.click("import_from_other_project_sort_button")
        sort.sort_by_files_up()
        self.action.click("import_from_other_project_sort_button")
        sort.sort_by_mixed()
        self.action.click("import_from_other_project_sort_button")
        sort.sort_by_name()
        self.action.click("import_from_other_project_sort_button")
        sort.sort_by_create_time()
        self.action.click("import_from_other_project_sort_button")
        sort.sort_by_edit_time()
        self.action.click("import_from_other_project_list_project_0") # 가장 첫번째 위치한 프로젝트 탭
        logger.info("[Browser > MY] tap first project")
        self.action.click("import_from_other_project_move_button")
        logger.info("[Browser > MY] tap Next move button")

        # select 버튼
        self.action.click("import_from_other_project_select_button")
        # logger.info("[Browser > MY] tap 'import from other projects'")

        sort.sort_by_name()
        sort.sort_by_create_time()
        sort.sort_by_edit_time()



#TODO 멀티 셀렉 버튼에 접근성 아이디 추가 후 다시 구현 필요
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

    def tap_single_item_options(self): # 추가한 첫번째 아이템에 대한 옵션
        self.action.click("current_project_item_0_option_button")
        time.sleep(1)
        logger.info("tap first item options")


if __name__ == "__main__":
    importing = Importing()
    importing.import_by_other_projects()
    # importing.import_by_files()
    # multiselect = MultiSelectOption()
    # multiselect.tap_item_options_add()