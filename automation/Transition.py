from automation import logger, error_handler_class
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

    def open_transition_browser(self):
        self.action.click("browser_transition_button")
        logger.info("[Browser > Transition] open Transition Browser")

    def tap_Transition_category(self):
        all_categories = [["browser_new_ic","기본","모션","회전","슬라이드", "글리치"],
                          ["빛","블러","마스크","그래픽"]]

        self.action.swipe(58, 134, 419, 134) #TODO 좌표를 쓰지 않고 할 수 있는 방법 찾아보기
        logger.info("[Browser > Transition] initialize Transition Sub Category")

        for categories in all_categories:
            logger.info("[Browser > Transition] tap Transition Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic":
                    category = "NEW"
                logger.info(f"[Browser > Transition] tap Trnasition Sub Category : {category}")

            self.action.swipe(419, 134, 288, 134)
            time.sleep(1)

    def random_find_category_asset(self):
        transition_categories = ["browser_new_ic","기본","모션","회전","슬라이드", "글리치","빛","블러","마스크","그래픽"]
        random_category = choice_random(transition_categories) #카테고리 랜덤 선택
        find_category(random_category)
        idx = transition_categories.index(random_category) + 1
        self.action.click(f"asset_{idx}_1")
        logger.info(f"[Browser > Text] choose {random_category} asset 1")
        time.sleep(1)

    def play_source_player(self,coordinate):
        self.action.click_coordinate(coordinate)
        logger.info("[Browser > Transition] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()


    def transition_double_tap(self,value):
        self.action.double_click(value)
        logger.info("[Browser > Transition] transition double tap")
        self.action.screenshot("transition_double_tap")
        logger.info("[Browser > Transition] screenshot transition double tap")


