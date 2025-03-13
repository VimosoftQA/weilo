from automation import logger, error_handler_class
from Action import Action
import time
# from DownloadItem import download_item
from RandomChoice import choice_random, find_category
from SourcePlayer import *

# 필요한 기능
# 1. 글자 브라우저 탭 -> 2. 서브 카테고리 확인 -> 3. 임의의 카테고리 선택 후 가장 첫번째 아이템 탭하기 -> 4. 소스 플레이어에 추가 및 더블탭

@error_handler_class
class Text:
    def __init__(self):
        self.action = Action()
        self.source_player = SourcePlayer()

    def open_Text_browser(self):
        self.action.click("browser_text_button")
        logger.info("[Browser > Text] open Text Browser")

    def tap_Text_category(self):
        all_categories = [["browser_new_ic","기본","인트로","배경","네온 & 금속", "예능"],
                          ["이름표","디자인"]]

        self.action.swipe(58, 134, 419, 134) #TODO 좌표를 쓰지 않고 할 수 있는 방법 찾아보기
        logger.info("[Browser > Text] initialize Text Sub Category")

        for categories in all_categories:
            logger.info("[Browser > Text] tap Text Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic":
                    category = "NEW"
                logger.info(f"[Browser > Text] tap Text Sub Category : {category}")

            self.action.swipe(419, 134, 288, 134)
            time.sleep(1)

    def random_find_category_asset(self):
        text_categories = ["browser_new_ic","기본","인트로","배경","네온 & 금속","예능","이름표","디자인"]
        random_category = choice_random(text_categories) #카테고리 랜덤 선택
        find_category(random_category)
        idx = text_categories.index(random_category) + 1
        self.action.click(f"asset_{idx}_1")
        logger.info(f"[Browser > Text] choose {random_category} asset 1")
        time.sleep(1)


    def play_source_player(self,coordinate):
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



if __name__ == '__main__':
    text = Text()
    text.open_Text_browser()
    text.tap_Text_category()
    # text.text_double_tap("asset_1_1")