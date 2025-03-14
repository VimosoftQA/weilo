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


class Sticker(Graphic):
    def open_frame_popup(self):
        self.action.click("menu_frame")
        logger.info("[Graphic > Sticker] open Sticker Browser")

    def tap_frame_category(self):
        all_categories = [["browser_new_ic","browser_recent_ic", "inspector_bookmark_ic","기본","선","필름","Vlog"],
                          ["패션","다이어리","시즌"]]

        self.action.swipe(58, 134, 419, 134)
        logger.info("[Graphic > Sticker] initialize Sticker Sub Category")

        for categories in all_categories:
            logger.info("[Graphic > Sticker] tap Sticker Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic" : category = "NEW"
                elif category == "browser_recent_ic" : category = "RECENT"
                elif category == "inspector_bookmark_ic" : category = "BOOKMARK"
                logger.info(f"[Graphic > Sticker] tap Sticker Sub Category : {category}")

            self.action.swipe(419,134,288,134)
            time.sleep(1)

    def random_find_category(self):
        frame_categories = ["기본","선","필름","Vlog","패션","다이어리","시즌"]
        random_category = choice_random(frame_categories) #카테고리 랜덤 선택
        find_category(random_category)

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

class Frame(Graphic):
    def open_frame_popup(self):
        self.action.click("menu_frame")
        logger.info("[Graphic > Frame] open Frame Browser")

    def tap_frame_category(self):
        all_categories = [["browser_new_ic","browser_recent_ic", "inspector_bookmark_ic","감정","메모","말풍선"],
                          ["SNS", "효과", "도형", "선", "ABC" , "123"],
                          ["지칭 & 포인터","평가","Vlog","패션","다이어리"],
                          ["여행","사랑","음식","시즌","귀여운","재미"],
                          ["스케치"]]

        self.action.swipe(58, 134, 419, 134)
        logger.info("[Graphic > Frame] initialize Frame Sub Category")

        for categories in all_categories:
            logger.info("[Graphic > Frame] tap Frame Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic" : category = "NEW"
                elif category == "browser_recent_ic" : category = "RECENT"
                elif category == "inspector_bookmark_ic" : category = "BOOKMARK"
                logger.info(f"[Graphic > Frame] tap Frame Sub Category : {category}")

            self.action.swipe(419,134,288,134)
            time.sleep(1)

    def random_find_category(self):
        frame_categories = ["감정","메모","말풍선","SNS", "효과", "도형", "선", "ABC" , "123","지칭 & 포인터","평가","Vlog","패션","다이어리","여행","사랑","음식","시즌","귀여운","재미","스케치"]
        random_category = choice_random(frame_categories) #카테고리 랜덤 선택
        find_category(random_category)

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

class Particle(Graphic):
    def open_particle_popup(self):
        self.action.click("menu_particle")
        logger.info("[Graphic > Particle] open Particle Browser")

    def tap_particle_category(self):
        all_categories = [["browser_new_ic","browser_recent_ic", "inspector_bookmark_ic","재미","반짝반짝","사랑"],
                          ["필름","시즌","축제"]]

        self.action.swipe(58, 134, 419, 134)
        logger.info("[Graphic > Particle] initialize Particle Sub Category")

        for categories in all_categories:
            logger.info("[Graphic > Particle] tap Particle Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic" : category = "NEW"
                elif category == "browser_recent_ic" : category = "RECENT"
                elif category == "inspector_bookmark_ic" : category = "BOOKMARK"
                logger.info(f"[Graphic > Particle] tap Particle Sub Category : {category}")

            self.action.swipe(419,134,288,134)
            time.sleep(1)

    def random_find_category(self):
        particle_categories = ["재미","반짝반짝","사랑","필름","시즌","축제"]
        random_category = choice_random(particle_categories) #카테고리 랜덤 선택
        find_category(random_category)

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
    def open_stock_popup(self):
        self.action.click("menu_stock")
        logger.info("[Graphic > Stock] open Stock Browser")

    def tap_stock_category(self):
        all_categories = [["browser_new_ic","browser_recent_ic", "inspector_bookmark_ic","인트로","아웃트로","전환"],
                          ["배경","프레임","글리터","그라디언트","카운트다운"],
                          ["게임","공상과학","혼합"]]

        self.action.swipe(58, 134, 419, 134)
        logger.info("[Graphic > Stock] initialize Stock Sub Category")

        for categories in all_categories:
            logger.info("[Graphic > Stock] tap Stock Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic" : category = "NEW"
                elif category == "browser_recent_ic" : category = "RECENT"
                elif category == "inspector_bookmark_ic" : category = "BOOKMARK"
                logger.info(f"[Graphic > Stock] tap Stock Sub Category : {category}")

            self.action.swipe(419,134,288,134)
            time.sleep(1)

    def random_find_category(self):
        stock_categories = ["인트로","아웃트로","전환","배경","프레임","글리터","그라디언트","카운트다운","게임","공상과학","혼합"]
        random_category = choice_random(stock_categories) #카테고리 랜덤 선택
        find_category(random_category)

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