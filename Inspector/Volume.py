from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class VolumeAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # ID로 값 찾아서 탭하기
    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    # 스텝퍼 탭하기
    def tap_stepper(self, id, n=3):
        for _ in range(n):
            self.tap_element(id)
        replace_id = id.replace("button", "stepper")  # 로그의 가독성을 위해 ID 변경
        self.logger.info(f"[Volume] {replace_id} : {n}")

    # 텍스트 필드 값 입력
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
        self.logger.info("[Volume] move slider")


class Volume:
    def __init__(self):
        self.volume_action = VolumeAction()

    # 볼륨 인스펙터 열기
    def open_volume_inspector(self):
        self.volume_action.tap_element("inspector_volume")
        self.volume_action.logger.info("[Volume] Open Volume Inspector")

    # 볼륨 키프레임 추가
    def add_volume_keyframe(self):
        self.volume_action.tap_element("volume_volume_key_frame_iobutton")
        self.volume_action.logger.info("[Volume] Add Volume Keyframe")

    # 볼륨 키프레임 제거
    def remove_volume_keyframe(self):
        self.volume_action.tap_element("volume_volume_key_frame_iobutton")
        self.volume_action.logger.info("[Volume] Remove Volume Keyframe")

    # 볼륨 기본값 리셋
    def reset_volume_default(self):
        self.volume_action.tap_element("volume_volume_default_button")
        self.volume_action.logger.info("[Volume] Reset Volume Default")

    # 볼륨 플러스 스텝퍼 탭 (기본 n = 3)
    def volume_plus_stepper(self):
        id = "volume_volume_plus_button"
        self.volume_action.tap_stepper(id)

    # 볼륨 마이너스 스텝퍼 (기본 n = 3)
    def volume_minus_stepper(self):
        id = "volume_volume_minus_button"
        self.volume_action.tap_stepper(id)

    # 볼륨 값 입력
    def volume_input_textfield(self,value):
        self.volume_action.input_textfield("volume_volume_value_text_field",value)
        self.volume_action.logger.info(f"[Volume] Volume Input Textfield : {value}")

    # 볼륨 슬라이더 조정
    def volume_move_slider(self):
        value = 50
        self.volume_action.move_slider("volume_volume_slider_handle",value)
        self.volume_action.logger.info(f"[Volume] move slider : {value}")

        value = -50
        self.volume_action.move_slider("volume_volume_slider_handle",value)
        self.volume_action.logger.info(f"[Volume] move slider : {value}")

    # 볼륨 컨테이너 닫기
    def close_volume_inspector(self):
        self.volume_action.tap_element("inspector_volume")
        self.volume_action.logger.info("[Volume] Close Volume Inspector")


if __name__ == '__main__':
    volume = Volume()
    volume.open_volume_inspector()
    volume.add_volume_keyframe()
    volume.remove_volume_keyframe()
    volume.reset_volume_default()
    volume.volume_plus_stepper()
    volume.volume_minus_stepper()
    volume.volume_input_textfield(20)
    volume.volume_move_slider()
    volume.close_volume_inspector()
