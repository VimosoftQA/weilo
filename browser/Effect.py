from browser import logger, error_handler_class
from Action import Action
import time
from DownloadItem import download_item
from RandomChoice import choice_random, find_category
from SourcePlayer import *


@error_handler_class
class Effect:
    def __init__(self):
        self.action = Action()
        self.source_player = SourcePlayer()

    def open_effect_browser(self):
        self.action.click("browser_effect_button")
        logger.info("[Browser > Effect] open Effect browser")

    def close_effect_browser(self):
        self.action.click("browser_effect_button")
        logger.info("[Browser > Effect] close Effect browser")


class VideoEffect(Effect):
    def __init__(self):
        super().__init__()
        self.all_categories = {
            "package_0": "NEW",
            "package_1": "컬러",
            "package_2": "블러",
            "package_3": "키잉",
            "package_4": "디자인",
            "package_5": "노이즈",
            "package_6": "왜곡",
            "package_7": "렌즈"
        }

    def open_video_effect(self):
        self.action.click("menu_video_effect")
        logger.info("[Effect > Video Effect] open Video effect")

    def tap_video_effect_sub_category(self):
        new_icon_coordinate = self.action.find_element_coordinate("browser_new_ic")
        while True:
            try:
                if self.action.find_name("package_0"): break
            except:
                self.action.swipe(new_icon_coordinate.get("x") + 200, new_icon_coordinate.get("y"), 469, 134)
        logger.info("[Effect > Video Effect] initialize Video Effect Sub Category")


        # 서브 카테고리 탭하기 TODO 탭하는 과정에서 좀 꼬인 거 같은데 나중에 수정하자
        logger.info("[Effect > Video Effect] tap Video Effect Sub Category")
        for key, value in self.all_categories.items():
            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Effect > Video Effect] tap Video Effect Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)



    def random_find_category_asset(self):
        random_category = choice_random(self.all_categories) #카테고리 랜덤 선택 (카테고리 명, 카테고리 package 명)
        if find_category(random_category[1]) == 1 :
            idx = 1
            self.action.click(f"asset_{idx}_1")
            logger.info(f"[Effect > Video Effect] choose NEW asset 1")
        else:
            idx = int(random_category[1][-1]) +1
            self.action.click(f"asset_{idx}_1")
            logger.info(f"[Effect > Video Effect]  choose {random_category[0]} asset 1")
        time.sleep(1)


    def play_source_player(self):
        sourcePlayer = SourcePlayer()
        logger.info("[Effect > Video Effect] play source player")
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_add_button()
        sourcePlayer.tap_screenshot()

    def video_effect_double_tap(self,value):
        self.action.double_click(value)
        logger.info("[Effect > Video Effect] Video Effect double tap")
        self.action.screenshot("text_double_tap")
        logger.info("[Effect > Video Effect] screenshot Video Effect double tap")

class AudioEffect(Effect):
    def __init__(self):
        super().__init__()
        self.all_categories = {
            "package_0" : "필터 & EQ",
            "package_1" : "진폭",
            "package_2" : "효과"
        }


    def open_audio_effect(self):
        self.action.click("menu_audio_effect")
        logger.info("[Effect > Audio Effect] open Audio Effect")

    def tap_audio_effect_sub_category(self):

        first_category_coordinate = self.action.find_element_coordinate("package_0")
        while True:
            try:
                if self.action.find_name("package_0"): break
            except:
                self.action.swipe(first_category_coordinate.get("x") + 200, first_category_coordinate.get("y"), 469, 134)
        logger.info("[Effect > Audio Effect] initialize Audio Effect Sub Category")


        # 서브 카테고리 탭하기 TODO 탭하는 과정에서 좀 꼬인 거 같은데 나중에 수정하자
        logger.info("[Effect > Audio Effect] tap Audio Effect Sub Category")
        for key, value in self.all_categories.items():

            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Effect > Audio Effect] tap Audio Effect Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)

    def random_find_category_asset(self):
        random_category = choice_random(self.all_categories) #카테고리 랜덤 선택 (카테고리 명, 카테고리 package 명)
        if find_category(random_category[1]) == 1 :
            idx = 1
            self.action.click(f"asset_{idx}_1")
            logger.info(f"[Effect > Audio Effect] choose NEW asset 1")
        else:
            idx = int(random_category[1][-1]) +1
            self.action.click(f"asset_{idx}_1")
            logger.info(f"[Effect > Audio Effect]  choose {random_category[0]} asset 1")
        time.sleep(1)

    def play_source_player(self):
        sourcePlayer = SourcePlayer()
        logger.info("[Effect > Audio Effect] play source player")
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_add_button()
        sourcePlayer.tap_screenshot()


    def audio_effect_double_tap(self,value):
        self.action.double_click(value)
        logger.info("[Effect > Audio Effect] Audio Effect double tap")
        self.action.screenshot("text_double_tap")
        logger.info("[Effect > Audio Effect] screenshot Audio Effect double tap")
