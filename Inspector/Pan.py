from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class PanAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # ID 로 값 탭하기
    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    # 스텝퍼 탭하기
    def tap_stepper(self, id, n=3):
        for _ in range(n):
            self.tap_element(id)
        replace_id = id.replace("button", "stepper")  # 로그의 가독성을 위해 ID 변경
        self.logger.info(f"[Pan] {replace_id} : {n}")

    # 텍스트 필드에 입력하기
    def input_textfield(self, id, value):
        text_field = self.driver.find_element(By.ID, id)
        text_field.clear()
        text_field.send_keys(value)
        time.sleep(1)
        self.tap_element(id="Return")

    # 슬라이더 이동
    def move_slider(self, id, horizontal_offset=-10):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform()  # 슬라이더의 위치 변경
        self.logger.info("[Pan] move slider")


class Pan:
    def __init__(self):
        self.pan_action = PanAction()

    # 패닝 인스펙터 열기
    def open_pan_inspector(self):
        self.pan_action.tap_element("inspector_pan")
        self.pan_action.logger.info("[Pan] Open Pan Inspector")

    # 패닝 키프레임 추가
    def add_pan_keyframe(self):
        self.pan_action.tap_element("pan_pan_key_frame_iobutton")
        self.pan_action.logger.info("[Pan] Add Pan Keyframe")

    # 패닝 키프레임 제거
    def remove_pan_keyframe(self):
        self.pan_action.tap_element("pan_pan_key_frame_iobutton")
        self.pan_action.logger.info("[Pan] Remove Pan Keyframe")

    # 패닝 기본값으로 리셋
    def reset_pan_default(self):
        self.pan_action.tap_element("pan_pan_default_button")
        self.pan_action.logger.info("[Pan] Reset Pan Default")

    # 패닝 플러스 스텝퍼 탭 (기본 n = 3)
    def pan_plus_stepper(self):
        id = "pan_pan_plus_button"
        self.pan_action.tap_stepper(id)

    # 패닝 마이너스 스텝퍼 탭 (기본 n = 3)
    def pan_minus_stepper(self):
        id = "pan_pan_minus_button"
        self.pan_action.tap_stepper(id)

    # 패닝 텍스트 필드 값 입력
    def pan_input_textfield(self,value):
        self.pan_action.input_textfield("pan_pan_value_text_field",value)
        self.pan_action.logger.info(f"[Pan] Pan Input Textfield : {value}")

    # 패닝 슬라이더 이동
    def pan_move_slider(self):
        value = 50
        self.pan_action.move_slider("pan_pan_slider_handle",value)
        self.pan_action.logger.info(f"[Pan] move slider : {value}")

        value = -50
        self.pan_action.move_slider("pan_pan_slider_handle",value)
        self.pan_action.logger.info(f"[Pan] move slider : {value}")

    # 패닝 인스펙터 닫기
    def close_pan_inspector(self):
        self.pan_action.tap_element("inspector_pan")
        self.pan_action.logger.info("[Pan] Close Pan Inspector")


if __name__ == '__main__':
    pan = Pan()
    pan.open_pan_inspector()
    pan.add_pan_keyframe()
    pan.remove_pan_keyframe()
    pan.reset_pan_default()
    pan.pan_plus_stepper()
    pan.pan_minus_stepper()
    pan.pan_input_textfield(20)
    pan.pan_move_slider()
    pan.close_pan_inspector()
