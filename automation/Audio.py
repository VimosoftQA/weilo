from automation import logger, error_handler_class
from Action import Action
import time
from DownloadItem import download_item
from RandomChoice import choice_random, find_category

@error_handler_class
class Audio:
    def __init__(self):
        self.action = Action()

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

    # def open_source_player(self,coordinate : dict):
    #     X = coordinate.get("x")
    #     Y = coordinate.get("y")
    #
    #     self.action.tap_coordinate(X,Y,sec = 3)



    def close_audio_browser(self):
        self.action.click("browser_audio_button")
        time.sleep(1)
        logger.info("[Browser > Audio] close Audio Browser")


@error_handler_class
class BGM(Audio):

    def tap_BGM_category(self):
        self.action.click("menu_bgm")
        logger.info("[Audio > BGM] tap BGM Category")

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
                # print(self.action.find_element_location(category))
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
    def download_BGM_items(self, num = 3):
        for _ in range(num):
            item , coordinate  = download_item()
            if item:
                time.sleep(1)
                logger.info("[Audio > BGM] download BGM item")
                self.action.click_coordinate(coordinate)
                logger.info("[Audio > BGM] play source player")

            else:
                time.sleep(1)
                logger.info("[Audio > BGM] fail to download BGM item")



if __name__ == "__main__":
    bgm = BGM()
    # bgm.open_bgm_browser()
    # bgm.close_audio_guide()
    bgm.tap_BGM_category()
    # bgm.tap_BGM_sub_category()
    bgm.random_find_category()
    coordinate = bgm.download_BGM_items(1)
    # bgm.open_source_player(coordinate)