from automation import logger, error_handler_class
from Action import Action
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

    def search_BGM(self):
        self.action.click("common search ic") # 효과음 검색
        logger.info("[Audio > BGM] search BGM")
        #TODO 검색 접근성 아이디 필요함

    def tap_BGM_sub_category(self):
        all_categories = [["browser_new_ic", "browser_recent_ic", "inspector_bookmark_ic", "일상", "Vlog", "카페"],
                      ["키즈 & 동물", "여행", "사랑", "웨딩 & 프로포즈", "예능"],
                      ["광고", "영화","게임", "시즌", "뷰티 & 패션", "파티 & 클럽"]]

        self.action.swipe(58, 134, 419, 134)
        logger.info("[Audio > BGM] initialize BGM Sub Category")

        for categories in all_categories:
            logger.info("[Audio > BGM] tap BGM Sub Category")
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


    def play_source_player(self,coordinate):
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
    def tap_SFX_category(self):
        self.action.click("menu_sfx")
        logger.info("[Audio > SFX] tap SFX Category")

    def search_SFX(self):
        self.action.click("common search ic") # 효과음 검색
        logger.info("[Audio > SFX] search SFX")
        #TODO 검색 접근성 아이디 필요함

    def tap_SFX_sub_category(self):
        all_categories = [["browser_new_ic", "browser_recent_ic", "inspector_bookmark_ic", "전환", "효과", "생활음"],
                          ["만화","사람","발걸음","자연","동물","박수 & 관중"],
                          ["벨 & 사이렌","악기","액션 & 공포","무기 & 전쟁"],
                          ["교통수단"]]

        self.action.swipe(58, 134, 419, 134)
        logger.info("[Audio > SFX] initialize SFX Sub Category")

        for categories in all_categories:
            logger.info("[Audio > SFX] tap SFX Sub Category")
            for category in categories:
                self.action.click(category)
                if category == "browser_new_ic" : category = "NEW"
                elif category == "browser_recent_ic" : category = "RECENT"
                elif category == "inspector_bookmark_ic" : category = "BOOKMARK"
                logger.info(f"[Audio > SFX] tap SFX Sub Category : {category}")

            self.action.swipe(419,134,288,134)
            time.sleep(1)

    def random_find_category(self):
        SFX_categories = ["전환","효과","생활음","만화","사람","발걸음","자연","동물","박수 & 관중","벨 & 사이렌","악기","액션 & 공포","무기 & 전쟁","교통수단"]
        random_category = choice_random(SFX_categories) #카테고리 랜덤 선택
        find_category(random_category)

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


    def play_source_player(self,coordinate):
        self.action.click_coordinate(coordinate)
        logger.info("[Audio > SFX] play source player")
        sourcePlayer = SourcePlayer()
        time.sleep(1)
        sourcePlayer.tap_next_frame_button()
        sourcePlayer.tap_prev_frame_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_reset_button()
        sourcePlayer.tap_play_button()
        sourcePlayer.tap_screenshot()


    def set_bookmark(self):
        # 사전 조건 : SFX 다운로드가 되어있어야 함
        self.action.click("inspector_bookmark_ic") # 북마크 추가하기
        logger.info("[Audio > SFX] set bookmark")



if __name__ == "__main__":
    bgm = BGM()
    # bgm.open_bgm_browser()
    # bgm.close_audio_guide()
    # bgm.tap_BGM_category()
    # bgm.tap_BGM_sub_category()
    bgm.random_find_category()
    coordinate = bgm.download_BGM_items()
    # bgm.play_source_player(coordinate)
    bgm.set_bookmark()
