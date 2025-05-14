from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class GainAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    def tap_stepper(self, id, n=3):
        for _ in range(n):
            self.tap_element(id)
        replace_id = id.replace("button", "stepper")  # 로그의 가독성을 위해 ID 변경
        self.logger.info(f"[Gain] {replace_id} : {n}")

    def input_textfield(self, id, value):
        text_field = self.driver.find_element(By.ID, id)
        text_field.clear()
        text_field.send_keys(value)
        time.sleep(1)
        self.tap_element(id="Return")

    def move_slider(self, id, horizontal_offset=-10):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform()  # 슬라이더의 위치 변경
        self.logger.info("[Gain] move slider")


class Gain:
    def __init__(self):
        self.gain_action = GainAction()

    def open_gain_inspector(self):
        self.gain_action.tap_element("inspector_gain")
        self.gain_action.logger.info("[Gain] Open Gain Inspector")

    def add_gain_keyframe(self):
        self.gain_action.tap_element("gain_gain_key_frame_iobutton")
        self.gain_action.logger.info("[Gain] Add Gain Keyframe")

    def remove_gain_keyframe(self):
        self.gain_action.tap_element("gain_gain_key_frame_iobutton")
        self.gain_action.logger.info("[Gain] Remove Gain Keyframe")

    def reset_gain_default(self):
        self.gain_action.tap_element("gain_gain_default_button")
        self.gain_action.logger.info("[Gain] Reset Gain Default")

    def gain_plus_stepper(self):
        id = "gain_gain_plus_button"
        self.gain_action.tap_stepper(id)

    def gain_minus_stepper(self):
        id = "gain_gain_minus_button"
        self.gain_action.tap_stepper(id)

    def gain_input_textfield(self,value):
        self.gain_action.input_textfield("gain_gain_value_text_field",value)
        self.gain_action.logger.info(f"[Gain] Gain Input Textfield : {value}")

    def gain_move_slider(self):
        value = 50
        self.gain_action.move_slider("gain_gain_slider_handle",value)
        self.gain_action.logger.info(f"[Gain] move slider : {value}")

        value = -50
        self.gain_action.move_slider("gain_gain_slider_handle",value)
        self.gain_action.logger.info(f"[Gain] move slider : {value}")

    def close_gain_inspector(self):
        self.gain_action.tap_element("inspector_gain")
        self.gain_action.logger.info("[Gain] Close Pan Inspector")


if __name__ == '__main__':
    gain = Gain()
    gain.open_gain_inspector()
    gain.add_gain_keyframe()
    gain.remove_gain_keyframe()
    gain.reset_gain_default()
    gain.gain_plus_stepper()
    gain.gain_minus_stepper()
    gain.gain_input_textfield(20)
    gain.gain_move_slider()
    gain.close_gain_inspector()
