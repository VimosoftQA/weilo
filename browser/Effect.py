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
        logger.info("[Browser > Effect] open effect browser")

    def close_effect_browser(self):
        self.action.click("browser_effect_button")
        self.action.click("browser_effect_button")
        logger.info("[Browser > Effect] close effect browser")



class VideoEffect(Effect):
    def open_video_effect(self):
        self.action.click("menu_video_effect")
        logger.info("[Effect > Video] open Video effect")

    def tap_video_effect_sub_category(self):
        all_categories = [["browser_new_ic","컬러","블러","키잉","디자인", "노이즈"],
                          ["왜곡","렌즈"]]

        self.action.swipe(58, 134, 419, 134) #TODO 좌표를 쓰지 않고 할 수 있는 방법 찾아보기
        logger.info("[Effect > Video] Initialize Video Effect Sub Category")

        for categories in all_categories:
            logger.info("[Effect > Video] tap Video Effect Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic":
                    category = "NEW"
                logger.info(f"[Effect > Video] tap Video Effect Sub Category : {category}")

            self.action.swipe(419, 134, 288, 134)
            time.sleep(1)

    def random_find_category_asset(self):
        video_effect_categories = ["browser_new_ic","컬러","블러","키잉","디자인", "노이즈", "왜곡","렌즈"]
        random_category = choice_random(video_effect_categories) #카테고리 랜덤 선택
        find_category(random_category)
        idx = video_effect_categories.index(random_category) + 1
        self.action.click(f"asset_{idx}_1")
        logger.info(f"[Effect > Video]  choose {random_category} asset 1")
        time.sleep(1)


    def play_source_player(self,coordinate):
        self.action.click_coordinate(coordinate)
        logger.info("[Effect > Video] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()


    def video_effect_double_tap(self,value):
        self.action.double_click(value)
        logger.info("[Effect > Video] Video Effect double tap")
        self.action.screenshot("text_double_tap")
        logger.info("[Effect > Video] screenshot Video Effect double tap")

class AudioEffect(Effect):
    def open_audio_effect(self):
        self.action.click("menu_audio_effect")
        logger.info("[Effect > Audio] open Audio effect")

    def tap_audio_effect_sub_category(self):
        all_categories = [["필터 & EQ", "진폭", "효과"]]

        self.action.swipe(58, 134, 419, 134) #TODO 좌표를 쓰지 않고 할 수 있는 방법 찾아보기
        logger.info("[Effect > Video] Initialize Video Effect Sub Category")

        for categories in all_categories:
            logger.info("[Effect > Video] tap Video Effect Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic":
                    category = "NEW"
                logger.info(f"[Effect > Video] tap Video Effect Sub Category : {category}")

            self.action.swipe(419, 134, 288, 134)
            time.sleep(1)

    def random_find_category_asset(self):
        audio_effect_categories = ["필터 & EQ", "진폭", "효과"]
        random_category = choice_random(audio_effect_categories) #카테고리 랜덤 선택
        find_category(random_category)
        idx = audio_effect_categories.index(random_category) + 1
        self.action.click(f"asset_{idx}_1")
        logger.info(f"[Effect > Video]  choose {random_category} asset 1")
        time.sleep(1)

    def play_source_player(self,coordinate):
        self.action.click_coordinate(coordinate)
        logger.info("[Effect > Audio] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()


    def audio_effect_double_tap(self,value):
        self.action.double_click(value)
        logger.info("[Effect > Audio] Audio Effect double tap")
        self.action.screenshot("text_double_tap")
        logger.info("[Effect > Audio] screenshot Audio Effect double tap")
