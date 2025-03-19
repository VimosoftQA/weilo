from selenium.common import NoSuchElementException
from selenium.webdriver.support.expected_conditions import none_of

from browser import logger, error_handler_class
from Action import *
import time
from DownloadItem import download_item
from RandomChoice import choice_random, find_category
from SourcePlayer import *

@error_handler_class
class Audio:
    def __init__(self):
        self.action = Action()
        self.source_player = SourcePlayer()

    def open_audio_browser(self):
        self.action.click("browser_audio_button")
        logger.info("[Browser > Audio] open Audio Browser")

    def close_audio_guide(self):
        AUDIO_GUIDE = "내 음원은 어디서 불러오나요?"
        try:
            if self.action.find(AUDIO_GUIDE): # 음원 가이드가 존재할 때 음원 가이드를 확인하고 닫는다
                self.action.click("inspector_close_line_ic")
                logger.info("[Browser > Audio] close Audio Guide")
        except:
            logger.info("[Browser > Audio] not exist Audio Guide")

    def close_audio_browser(self):
        self.action.click("browser_audio_button")
        time.sleep(1)
        logger.info("[Browser > Audio] close Audio Browser")


@error_handler_class
class BGM(Audio):

    def tap_BGM_category(self):
        self.action.click("menu_bgm")
        logger.info("[Audio > BGM] tap BGM Category")

    # def search_BGM(self):
    #     self.action.click("common search ic") # 효과음 검색
    #     logger.info("[Audio > BGM] search BGM")
    #     #TODO 검색 접근성 아이디 필요함

    def tap_BGM_sub_category(self):
        all_categories = [["browser_new_ic", "browser_recent_ic", "inspector_bookmark_ic", "일상", "Vlog", "카페"],
                      ["키즈 & 동물", "여행", "사랑", "웨딩 & 프로포즈"],
                      ["예능","광고", "영화","게임", "시즌", "뷰티 & 패션"],
                      ["파티 & 클럽"]]


        # TODO 시작 전 초기값으로 돌려주기 -> 검색 아이콘 활용
        # self.action.swipe(115, 134, 419, 134)
        search_x_y = self.action.find_element_coordinate("common search ic")
        self.action.swipe(search_x_y.get("x")+100, search_x_y.get("y"), 469,134)
        logger.info("[Audio > BGM] initialize BGM Sub Category")

        logger.info("[Audio > BGM] tap BGM Sub Category")
        for categories in all_categories:
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic" : category = "NEW"
                elif category == "browser_recent_ic" : category = "RECENT"
                elif category == "inspector_bookmark_ic" : category = "BOOKMARK"
                logger.info(f"[Audio > BGM] tap BGM Sub Category : {category}")

            self.action.swipe(419,134,288,134)
            time.sleep(1)

    def random_find_category(self):
        BGM_categories = ["일상", "Vlog", "카페","키즈 & 동물", "여행", "사랑", "웨딩 & 프로포즈", "예능","광고", "영화","게임", "시즌", "뷰티 & 패션", "파티 & 클럽"]
        random_category = choice_random(BGM_categories) #카테고리 랜덤 선택
        find_category(random_category)


    # 아이템 다운로드 후 소스플레이어 재생
    def download_BGM_items(self, num = 1 ):
        for _ in range(num):
            coordinate  = download_item()
            if coordinate:
                time.sleep(1)
                logger.info("[Audio > BGM] download BGM item")
                return coordinate
            else:
                time.sleep(1)
                logger.info("[Audio > BGM] fail to download BGM item")
                return None

    def play_source_player(self):
        coordinate = self.download_BGM_items()
        self.action.click_coordinate(coordinate)
        logger.info("[Audio > BGM] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()


    def set_bookmark(self):
        # 사전 조건 : BGM 다운로드가 되어있어야 함
        self.action.click("inspector_bookmark_ic") # 북마크 추가하기
        logger.info("[Audio > BGM] set bookmark")



class SFX(Audio):

    def __init__(self):
        super().__init__()
        self.all_categories = {
            "package_0" : "NEW",
            "package_1" : "RECENT",
            "package_2" : "BOOKMARK",
            "package_3" : "전환",
            "package_4" : "효과",
            "package_5" : "생활음",
            "package_6" : "만화",
            "package_7" : "사람",
            "package_8" : "발걸음",
            "package_9" : "자연",
            "package_10" : "동물",
            "package_11" : "박수 & 관중",
            "package_12" : "벨 & 사이렌",
            "package_13" : "악기",
            "package_14" : "액션 & 공포",
            "package_15" : "무기 & 전쟁",
            "package_16" : "교통수단"
        }


    def tap_SFX_category(self):
        self.action.click("menu_sfx")
        logger.info("[Audio > SFX] tap SFX Category")

    # def search_SFX(self):
    #     self.action.click("common search ic") # 효과음 검색
    #     logger.info("[Audio > SFX] search SFX")
    #     #TODO 검색 접근성 아이디 필요함

    def tap_SFX_sub_category(self):

        # 카테고리 맨 처음으로 돌아가는 코드 (초기화)
        search_icon_coordinate = self.action.find_element_coordinate("common search ic")
        while True:
            try:
                if self.action.find_name("package_0"): break
            except:
                self.action.swipe(search_icon_coordinate.get("x") + 200, search_icon_coordinate.get("y"), 469, 134)
        logger.info("[Audio > SFX] initialize SFX Sub Category")


        # 서브 카테고리 탭하기 TODO 탭하는 과정에서 좀 꼬인 거 같은데 나중에 수정하자
        logger.info("[Audio > SFX] tap SFX Sub Category")
        for key, value in self.all_categories.items():

            while True:
                try:
                    if self.action.find(key):
                        self.action.click(key)
                        logger.info(f"[Audio > SFX] tap SFX Sub Category : {value}")
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)
                    break
                except:
                    self.action.swipe(419, 134, 350, 134)
                    time.sleep(1)


    def random_find_category(self):
        # SFX_categories = ["package_1", "package_2", "package_3", "package_4", "package_5", "package_6", "package_7", "package_8", "package_9","package_10", "package_11","package_12", "package_13", "package_14", "package_15", "package_16"]

        random_category, category_original_name = choice_random(self.all_categories) #카테고리 랜덤 선택
        find_category(category_original_name)

    def download_SFX_items(self, num = 1 ):
        for _ in range(num):
            coordinate  = download_item()
            if coordinate:
                time.sleep(1)
                logger.info("[Audio > SFX] download SFX item")
                return coordinate
            else:
                time.sleep(1)
                logger.info("[Audio > SFX] fail to download SFX item")


    def play_source_player(self):
        coordinate = self.download_SFX_items()
        self.action.click_coordinate(coordinate)
        logger.info("[Audio > SFX] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_add_button()
        sourcePlayer.tap_screenshot()


    def set_bookmark(self):
        # 사전 조건 : SFX 다운로드가 되어있어야 함
        self.action.click("inspector_bookmark_ic") # 북마크 추가하기
        logger.info("[Audio > SFX] set bookmark")



if __name__ == "__main__":
    # bgm = BGM()
    # # bgm.open_bgm_browser()
    # # bgm.close_audio_guide()
    # # bgm.tap_BGM_category()
    # # bgm.tap_BGM_sub_category()
    # bgm.random_find_category()
    # coordinate = bgm.download_BGM_items()
    # # bgm.play_source_player(coordinate)
    # bgm.set_bookmark()
    sfx = SFX()
    sfx.random_find_category()