from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class ChannelAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # ID로 아이템 탭하기
    def tap_element(self, id):
        self.driver.find_element(by=By.ID, value=id).click()

    # 드롭다운 열기
    def open_drop_down(self, id):
        self.driver.find_element(by=By.ID, value=id).click()

class Channel:
    def __init__(self):
        self.channel_action = ChannelAction()

    # 채널 인스펙터 열기
    def open_channel_inspector(self):
        self.channel_action.tap_element("inspector_channel")
        self.channel_action.logger.info("[Channel] Open Channel Inspector")

    # 채널 드롭다운 열기
    def open_channel_dropdown(self):
        self.channel_action.tap_element("channel_channel_dropdown")

    # 채널 옵션 선택하기 : "오른쪽_소리를_채우기" 와 같이 언더바로 연결한다.
    def select_channel_option(self, option = "stereo"):
        self.channel_action.tap_element("dropdown_item_" + option)
        self.channel_action.logger.info("[Channel] Select Channel Option : " + option)

    # 채널 적용 후 재생 및 일시정지
    def play_and_pause(self):
        self.channel_action.tap_element("play_button")
        self.channel_action.logger.info("[Channel] Play")
        time.sleep(1)
        self.channel_action.tap_element("play_button")
        self.channel_action.logger.info("[Channel] Pause")

    # 채널 인스펙터 닫기
    def close_channel_inspector(self):
        self.channel_action.tap_element("inspector_channel")
        self.channel_action.logger.info("[Channel] Close Channel Inspector")

if __name__ == "__main__":
    channel = Channel()
    channel.open_channel_inspector()
    channel.open_channel_dropdown()
    channel.select_channel_option("stereo")
    channel.play_and_pause()
    channel.open_channel_dropdown()
    channel.select_channel_option("왼쪽_소리를_채우기")
    channel.play_and_pause()
    channel.open_channel_dropdown()
    channel.select_channel_option("오른쪽_소리를_채우기")
    channel.play_and_pause()
