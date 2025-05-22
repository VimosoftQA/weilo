from browser import logger, error_handler_class
from Action import Action
import time
from DownloadItem import download_item
from RandomChoice import choice_random, find_category
from SourcePlayer import *

# 필요한 기능
# 1. 글자 브라우저 탭 -> 2. 서브 카테고리 확인 -> 3. 임의의 카테고리 선택 후 가장 첫번째 아이템 탭하기 -> 4. 소스 플레이어에 추가 및 더블탭

@error_handler_class
class Text:
    def __init__(self):
        self.action = Action()
        self.source_player = SourcePlayer()
        self.all_categories = {
            "package_0" : "NEW",
            "package_1" : "기본",
            "package_2" : "인트로",
            "package_3" : "배경",
            "package_4" : "네온 & 금속",
            "package_5" : "예능",
            "package_6" : "이름표",
            "package_7" : "디자인"
        }

    def open_Text_browser(self):
        self.action.click("browser_text_button")
        logger.info("[Browser > Text] open Text Browser")

    def tap_Text_category(self):
        # 카테고리 맨 처음으로 돌아가는 코드 (초기화)
        search_icon_coordinate = self.action.find_element_coordinate("common search ic")
        while True:
            try:
                if self.action.find_name("package_0"): break
            except:
                self.action.swipe(search_icon_coordinate.get("x") + 200, search_icon_coordinate.get("y"), 469, 134)
        logger.info("[Browser > Text] initialize Text Sub Category")


    def random_find_category_asset(self):
        # 서브 카테고리 탭하기
        logger.info("[Browser > Text] tap Text Sub Category")
        for key, value in self.all_categories.items():

            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Browser > Text] tap Text Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)

    def download_Text_items(self, num = 1 ):
        for _ in range(num):
            coordinate  = download_item()
            if coordinate:
                time.sleep(1)
                logger.info("[Browser > Text] download Text item")
                return coordinate
            else:
                time.sleep(1)
                logger.info("[Browser > Text] fail to download Text item")


    def play_source_player(self):
        coordinate = self.download_Text_items()
        self.action.click_coordinate(coordinate)
        logger.info("[Browser > Text] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()

    def text_double_tap(self,value):
        self.action.double_click(value)
        logger.info("[Browser > Text] text double tap")
        self.action.screenshot("text_double_tap")
        logger.info("[Browser > Text] screenshot text double tap")

    def close_Text_browser(self):
        self.action.click("browser_text_button")
        logger.info("[Browser > Text] close Text Browser")

if __name__ == '__main__':
    text = Text()
    text.open_Text_browser()
    text.tap_Text_category()
    # text.text_double_tap("asset_1_1")