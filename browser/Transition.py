from browser import logger, error_handler_class
from Action import Action
import time
from DownloadItem import download_item
from RandomChoice import choice_random, find_category
from SourcePlayer import *

# 필요한 기능
# 전환 브라우저 열기 > 전환 서브 카테고리 탭 > 싱글 탭 / 더블 탭 > 클립 추가

@error_handler_class
class Transition:
    def __init__(self):
        self.action = Action()
        self.source_player = SourcePlayer()
        self.all_categories = {
            "package_0" : "NEW",
            "package_1" : "기본",
            "package_2" : "모션",
            "package_3" : "회전",
            "package_4" : "슬라이드",
            "package_5" : "글리치",
            "package_6" : "빛",
            "package_7" : "블러",
            "package_8" : "마스크",
            "package_9" : "그래픽"
        }

    def open_transition_browser(self):
        self.action.click("browser_transition_button")
        logger.info("[Browser > Transition] open Transition Browser")

    def tap_Transition_category(self):

        self.action.swipe(58, 134, 419, 134) #TODO 좌표를 쓰지 않고 할 수 있는 방법 찾아보기
        logger.info("[Browser > Transition] initialize Transition Sub Category")

        for key, value in self.all_categories.items():
            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Browser > Transition] tap Transition Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)

    def random_find_category_asset(self):
        random_category = choice_random(self.all_categories)
        if find_category(random_category[1]) == 1 :
            idx = 1
            self.action.click(f"asset_{idx}_1")
            logger.info(f"[Browser > Transition] choose NEW asset 1")
        else:
            idx = int(random_category[1][-1]) +1
            self.action.click(f"asset_{idx}_1")
            logger.info(f"[Broswer > Transition] choose {random_category[0]} asset 1")
        time.sleep(1)

    def play_source_player(self):
        sourcePlayer = SourcePlayer()
        logger.info("[Browser > Transition] play source player")
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_add_button()
        sourcePlayer.tap_screenshot()


    def transition_double_tap(self,value):
        self.action.double_click(value)
        logger.info("[Browser > Transition] transition double tap")
        self.action.screenshot("transition_double_tap")
        logger.info("[Browser > Transition] screenshot transition double tap")


    def close_transition_browser(self):
        self.action.click("browser_transition_button")
        logger.info("[Browser > Transition] close Transition Browser")
