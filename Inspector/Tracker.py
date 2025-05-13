from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time


class TrackerAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def find(self,id):
        self.driver.find_element(by=By.ID, value=id)

    def tap_element(self,id):
        self.driver.find_element(By.ID, id).click()

    def input_textfield(self,id,value):
        text_field = self.driver.find_element(By.ID, id)
        text_field.clear()
        text_field.send_keys(value)
        time.sleep(0.5)
        self.tap_element("Return")

    def return_textfield_value(self):
        textfield = self.driver.find_elements(by=By.CLASS_NAME, value="XCUIElementTypeTextField")
        if textfield:
            value = textfield[0].get_attribute("value")
            return value

    def mover_indicator(self,id,horizontal_offset = -100):
        slider = self.driver.find_element(by=By.ID, value=id)
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform()

class Tracker:
    def __init__(self):
        self.tracker_action = TrackerAction()

    # 트래커 컨테이너뷰 열기
    def open_tracker_inspector(self):
        self.tracker_action.tap_element("inspector_tracker_container_view")
        self.tracker_action.logger.info("[Tracker] Open Tracker Inspector")

    # Tracker 뎁스 나가기 버튼에 접근성 ID가 존재하지 않음

    # 트래커 추가
    def add_tracker_inspector(self):
        self.tracker_action.tap_element("add_new_tracker_add_new_tracker_button")
        self.tracker_action.logger.info("[Tracker] Add New Tracker Inspector")

    # Tracker 프리뷰 위에 그려지는 Transform 핸들에 접근성 ID가 존재하지 않음

    # '트래킹 중' 화면에서 트래킹 생성하기
    def create_tracker(self):
        self.tracker_action.tap_element("export_button")
        self.tracker_action.logger.info("[Tracker] Create Tracker")
        time.sleep(3)

    # '트래킹 중' 화면 나가기
    def exit_tracker_view(self):
        self.tracker_action.tap_element("home_button")
        self.tracker_action.logger.info("[Tracker] Exit Tracker View")

    # 트래킹 구간 수정 및 추가하기
    def edit_tracker_section(self,offset= -100):
        self.tracker_action.tap_element("tracker_1_edit_tracker_button")
        self.tracker_action.mover_indicator("layer_waveform_area_view",offset)
        self.tracker_action.tap_element("export_button")
        self.tracker_action.logger.info("[Tracker] Edit Tracker Section")

    # 생성된 트래커의 옵션 열기
    def open_tracker_option(self):
        self.tracker_action.tap_element("inspector_tracker_1_right_button")
        self.tracker_action.logger.info("[Tracker] Open Tracker Option")

    # 트래커 이름 변경
    def rename_tracker(self,value):
        self.tracker_action.tap_element("이름 변경")
        original_tracker_name = self.tracker_action.return_textfield_value()
        self.tracker_action.input_textfield(original_tracker_name,value)
        self.tracker_action.tap_element("완료")
        self.tracker_action.logger.info("[Tracker] Rename Tracker")

    # 트래커 삭제
    def remove_tracker(self):
        self.tracker_action.tap_element("삭제")
        self.tracker_action.tap_element("삭제")
        self.tracker_action.logger.info("[Tracker] Remove Tracker")

    # Tracker 뷰에서 재생, 프레임 이동 접근성 ID가 존재하지 않음

    # '자녀 클립 추가' 버튼을 탭하는 동작
    def add_following_clip(self):
        self.tracker_action.tap_element("tracker_1_add_following_clip_button")
        self.tracker_action.logger.info("[Tracker] Add Following Clip")

    # 트래커의 자녀 클립 추가하기
    def complete_add_following_clip(self):
        self.tracker_action.tap_element("완료")
        self.tracker_action.logger.info("[Tracker] Complete Add Following Clip")

    # 트래커의 자녀 클립 추가 취소하기
    def cancel_add_following_clip(self):
        self.tracker_action.tap_element("취소")
        self.tracker_action.logger.info("[Tracker] Cancel Add Following Clip")




if __name__ == "__main__":
    tracker = Tracker()
    tracker.open_tracker_inspector()
    tracker.add_tracker_inspector()
    tracker.create_tracker()
    tracker.edit_tracker_section(-150)
    tracker.open_tracker_option()

    tracker.rename_tracker("이름 바꾼 tracker")
    tracker.open_tracker_option()
    tracker.remove_tracker()

