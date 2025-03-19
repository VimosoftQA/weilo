from automation import logger, error_handler_class
from Action import Action
import time
from RandomChoice import choice_random, find_category
from SourcePlayer import SourcePlayer


@error_handler_class
class Graphic:
    def __init__(self):
        self.action = Action()
        self.source_player = SourcePlayer()

    def open_graphic_browser(self):
        self.action.click("browser_graphic_button")
        logger.info("[Browser > Graphic] open Graphic Browser")

    def close_graphic_browser(self):
        self.action.click("browser_graphic_button")
        self.action.click("browser_graphic_button")
        logger.info("[Browser > Graphic] close Graphic Browser")


@error_handler_class
class Drawing(Graphic):
    def open_drawing_popup(self):
        self.action.click("shape_select_drawing_button")
        logger.info("[Graphic > Drawing] open Drawing Popup")
        self.action.screenshot("shape_drawing_popup")
        logger.info("[Graphic > Drawing] screenshot drawing popup")

    def select_marker(self):
        self.action.click("마커")
        self.action.click("마커")
        logger.info("[Graphic > Drawing] select 마커")

    def test_drawing(self):
        self.action.swipe(195, 308, 133, 501)
        self.action.swipe(195, 308, 133, 501)
        self.action.swipe(133, 501, 296, 379)
        self.action.swipe(296, 379, 99, 378)
        self.action.swipe(99, 378, 265, 496)
        self.action.swipe(265, 496, 195, 308)
        self.action.click("완료")
        logger.info("[Graphic > Drawing] Drawing")

    def reset_drawing(self):
        self.action.click("inspector reset ic")
        self.action.screenshot("reset_drawing")
        logger.info("[Graphic > Drawing] reset Drawing")

    def cancel_drawing(self):
        # cancel 버튼에 accessibility ID 가 없음
        pass


@error_handler_class
class Pen(Graphic):
    # 접근성 아이디 적용이 안되어있음
    def open_pen_popup(self):
        self.action.click("shape_select_pen_button")
        logger.info("[Graphic > Pen] open Pen Popup")
        self.action.screenshot("shape_pen_popup")
        logger.info("[Graphic > Pen] screenshot pen popup")

    def test_pen(self):
        self.action.swipe(195, 308, 133, 501)
        self.action.swipe(195, 308, 133, 501)
        self.action.swipe(133, 501, 296, 379)
        self.action.swipe(296, 379, 99, 378)
        self.action.swipe(99, 378, 265, 496)
        self.action.swipe(265, 496, 195, 308)
        self.action.click("완료")
        logger.info("[Graphic > Pen] Pen")

    def reset_pen(self):
        self.open_pen_popup()
        self.action.click("inspector reset ic")
        self.action.screenshot("reset_pen")
        logger.info("[Graphic > Pen] reset Drawing")

    def cancel_pen(self):
        # cancel 버튼에 accessibility ID 가 없음
        pass

@error_handler_class
class BlankScene(Graphic):
    pass


class Frame(Graphic):

    def __init__(self):
        super.__init__()
        self.all_categories = { #변경해야함
            "package_0" : "NEW",
            "package_1" : "RECENT",
            "package_2" : "BOOKMARK",
            "package_3" : "기본",
            "package_4" : "선",
            "package_5" : "필름",
            "package_6" : "Vlog",
            "package_7" : "패션",
            "package_8" : "다이어리",
            "package_9" : "시즌"
        }


    def open_frame_popup(self):
        self.action.click("menu_frame")
        logger.info("[Graphic > Frame] open Frame Browser")

    def tap_frame_category(self):

        new_icon_coordinate = self.action.find_element_coordinate("common search ic") # new 아이콘으로 변경되어야함
        while True:
            try:
                if self.action.find_name("package_0"): break
            except:
                self.action.swipe(new_icon_coordinate.get("x") + 200, new_icon_coordinate.get("y"), 469, 134)
        logger.info("[Graphic > Frame] initialize Frame Sub Category")

        logger.info("[Graphic > Frame] tap Frame Sub Category")
        for key, value in self.all_categories.items():

            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Graphic > Frame] tap Frame Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)

        # all_categories = [["browser_new_ic","browser_recent_ic", "inspector_bookmark_ic","기본","선","필름","Vlog"],
        #                   ["패션","다이어리","시즌"]]

        # self.action.swipe(58, 134, 419, 134)
        # logger.info("[Graphic > Frame] initialize Frame Sub Category")
        #
        # for categories in all_categories:
        #     logger.info("[Graphic > Frame] tap Frame Sub Category")
        #     for category in categories:
        #         self.action.click(category)
        #         if category == "browser_new_ic" : category = "NEW"
        #         elif category == "browser_recent_ic" : category = "RECENT"
        #         elif category == "inspector_bookmark_ic" : category = "BOOKMARK"
        #         logger.info(f"[Graphic > Frame] tap Frame Sub Category : {category}")
        #
        #     self.action.swipe(419,134,288,134)
        #     time.sleep(1)

    def random_find_category(self):
        random_category, category_original_name = choice_random(self.all_categories) #카테고리 랜덤 선택
        find_category(category_original_name)

    def play_source_player(self,coordinate):
        self.action.click_coordinate(coordinate)
        logger.info("[Graphic > Frame] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()

    def set_bookmark(self):
        self.action.click("inspector_bookmark_ic") # 북마크 추가하기
        logger.info("[Graphic > Frame] set bookmark")

class Sticker(Graphic):

    def __init__(self):
        super.__init__()
        self.all_categories = { "package_0" : "NEW",
                                "package_1" : "RECENT",
                                "package_2" : "BOOKMARK",
                                "package_3" : "감정",
                                "package_4" : "메모",
                                "package_5" : "말풍선",
                                "package_6" : "SNS",
                                "package_7" : "효과",
                                "package_8" : "도형",
                                "package_9" : "선",
                                "package_10" : "ABC",
                                "package_11" : "123",
                                "package_12" : "지칭 & 포인터",
                                "package_13" : "평가",
                                "package_14" : "Vlog",
                                "package_15" : "패션",
                                "package_16": "다이어리",
                                "package_17" : "여행",
                                "package_18" : "사랑",
                                "package_19" : "음식",
                                "package_20" : "시즌",
                                "package_21" : "귀여운",
                                "package_22" : "재미",
                                "package_23" : "스케치"}

    def open_sticker_popup(self):
        self.action.click("menu_sticker")
        logger.info("[Graphic > Sticker] open Sticker Browser")

    def tap_sticker_category(self):

        search_icon_coordinate = self.action.find_element_coordinate("common search ic")
        while True:
            try:
                if self.action.find_name("package_0"): break
            except:
                self.action.swipe(search_icon_coordinate.get("x") + 200, search_icon_coordinate.get("y"), 469, 134)
        logger.info("[Graphic > Sticker] initialize SFX Sub Category")


        # 서브 카테고리 탭하기 TODO 탭하는 과정에서 좀 꼬인 거 같은데 나중에 수정하자
        logger.info("[Graphic > Sticker] tap Sticker Sub Category")
        for key, value in self.all_categories.items():

            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Graphic > Sticker] tap Sticker Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)


    def random_find_category(self):
        random_category, category_original_name = choice_random(self.all_categories)  # 카테고리 랜덤 선택
        find_category(category_original_name)

    def play_source_player(self,coordinate):
        self.action.click_coordinate(coordinate)
        logger.info("[Graphic > Sticker] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()

    def set_bookmark(self):
        self.action.click("inspector_bookmark_ic") # 북마크 추가하기
        logger.info("[Graphic > Sticker] set bookmark")

class Particle(Graphic):
    def __init__(self):
        super.__init__()
        self.all_categories = { "package_0" : "NEW",
                                "package_1" : "RECENT",
                                "package_2" : "BOOKMARK",
                                "package_3" : "재미",
                                "package_4" : "반짝반짝",
                                "package_5" : "사랑",
                                "package_6" : "필름",
                                "package_7" : "시즌",
                                "package_8" : "축제"}

    def open_particle_popup(self):
        self.action.click("menu_particle")
        logger.info("[Graphic > Particle] open Particle Browser")

    def tap_particle_category(self):
        search_icon_coordinate = self.action.find_element_coordinate("common search ic") # search 가 아닌 다른 걸로 해야함
        while True:
            try:
                if self.action.find_name("package_0"): break
            except:
                self.action.swipe(search_icon_coordinate.get("x") + 200, search_icon_coordinate.get("y"), 469, 134)
        logger.info("[Graphic > Particle] initialize Particle Sub Category")


        # 서브 카테고리 탭하기
        logger.info("[Graphic > Particle] tap Particle Sub Category")
        for key, value in self.all_categories.items():

            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Graphic > Particle] tap Particle Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
        # all_categories = [["browser_new_ic","browser_recent_ic", "inspector_bookmark_ic","재미","반짝반짝","사랑"],
        #                   ["필름","시즌","축제"]]
        #
        # self.action.swipe(58, 134, 419, 134)
        # logger.info("[Graphic > Particle] initialize Particle Sub Category")
        #
        # for categories in all_categories:
        #     logger.info("[Graphic > Particle] tap Particle Sub Category")
        #     for category in categories:
        #         self.action.click(category)
        #         if category == "browser_new_ic" : category = "NEW"
        #         elif category == "browser_recent_ic" : category = "RECENT"
        #         elif category == "inspector_bookmark_ic" : category = "BOOKMARK"
        #         logger.info(f"[Graphic > Particle] tap Particle Sub Category : {category}")
        #
        #     self.action.swipe(419,134,288,134)
        #     time.sleep(1)

    def random_find_category(self):
        random_category, category_original_name = choice_random(self.all_categories) #카테고리 랜덤 선택
        find_category(category_original_name)

    def play_source_player(self,coordinate):
        self.action.click_coordinate(coordinate)
        logger.info("[Graphic > Particle] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()

    def set_bookmark(self):
        self.action.click("inspector_bookmark_ic") # 북마크 추가하기
        logger.info("[Graphic > Particle] set bookmark")

class Stock(Graphic):

    def __init__(self):
        super.__init__()
        self.all_categories = { "package_0" : "NEW",
                                "package_1" : "RECENT",
                                "package_2" : "BOOKMARK",
                                "package_3" : "인트로",
                                "package_4" : "아웃트로",
                                "package_5" : "전환",
                                "package_6" : "배경",
                                "package_7" : "프레임",
                                "package_8" : "글리터",
                                "package_9" : "그라디언트",
                                "package_10" : "카운트다운",
                                "package_11" : "게임",
                                "package_12" : "공상과학",
                                "package_13" : "혼합"}


    def open_stock_popup(self):
        self.action.click("menu_stock")
        logger.info("[Graphic > Stock] open Stock Browser")

    def tap_stock_category(self):
        # 카테고리 맨 처음으로 돌아가는 코드 (초기화)
        search_icon_coordinate = self.action.find_element_coordinate("common search ic") # new 버튼으로 교체
        while True:
            try:
                if self.action.find_name("package_0"): break
            except:
                self.action.swipe(search_icon_coordinate.get("x") + 200, search_icon_coordinate.get("y"), 469, 134)
        logger.info("[Graphic > Stock] initialize Stock Sub Category")


        # 서브 카테고리 탭하기 TODO 탭하는 과정에서 좀 꼬인 거 같은데 나중에 수정하자
        logger.info("[Graphic > Stock] tap Stock Sub Category")
        for key, value in self.all_categories.items():

            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Graphic > Stock] tap Stock Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)


    def random_find_category(self):
        random_category, category_original_name = choice_random(self.all_categories) #카테고리 랜덤 선택
        find_category(category_original_name)

    def play_source_player(self,coordinate):
        self.action.click_coordinate(coordinate)
        logger.info("[Graphic > Stock] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()

    def set_bookmark(self):
        self.action.click("inspector_bookmark_ic") # 북마크 추가하기
        logger.info("[Graphic > Stock] set bookmark")




if __name__ == '__main__':
    # drawing = Drawing()
    # drawing.open_drawing_popup()
    # drawing.select_marker()
    # drawing.test_drawing()

    pen = Pen()
    pen.open_pen_popup()
    pen.test_pen()
    pen.reset_pen()