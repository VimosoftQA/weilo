from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class FadeAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def tap_element(self,id):
        self.driver.find_element(by = By.ID,value = id).click()

    def input_textfield(self,id,value):
        text_field = self.driver.find_element(By.ID, id)
        text_field.clear()
        text_field.send_keys(value)
        time.sleep(1)
        self.tap_element(id = "Return")

    def tap_stepper(self, id, n = 3):
        for _ in range(n):
            self.tap_element(id)
        replace_id = id.replace("button", "stepper")  # 로그의 가독성을 위해 ID 변경
        self.logger.info(f"[Fade] {replace_id}")

    def move_slider(self, id, horizontal_offset = -10):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform() # 슬라이더의 위치 변경
        self.logger.info("[Fade] move slider")


class Fade:
    def __init__(self):
        self.fade_action = FadeAction()

    def open_fade_inspector(self):
        self.fade_action.tap_element("inspector_fade")
        self.fade_action.logger.info("[Fade] Open Fade Inspector")

    def activate_fade_in_checkbox(self):
        self.fade_action.tap_element("fade_fade_in_checkbox")
        self.fade_action.logger.info("[Fade] Activate Fade In Checkbox")

    def deactivate_fade_in_checkbox(self):
        self.fade_action.tap_element("fade_fade_in_checkbox")
        self.fade_action.logger.info("[Fade] Deactivate Fade In Checkbox")

    def reset_fade_in_seconds(self):
        self.fade_action.tap_element("fade_fade_in_duration_default_button")

    def set_fade_in_plus_stepper(self):
        self.fade_action.tap_stepper("fade_fade_in_duration_plus_button")

    def set_fade_in_minus_stepper(self):
        self.fade_action.tap_stepper("fade_fade_in_duration_minus_button")

    def set_fade_in_input_textfield(self, value):
        self.fade_action.input_textfield("fade_fade_in_duration_value_text_field",value)

    def move_fade_in_slider(self):
        self.fade_action.move_slider("fade_fade_in_duration_slider_handle")

    def activate_fade_out_checkbox(self):
        self.fade_action.tap_element("fade_fade_out_checkbox")
        self.fade_action.logger.info("[Fade] Activate Fade Out")

    def deactivate_fade_out_checkbox(self):
        self.fade_action.tap_element("fade_fade_out_checkbox")
        self.fade_action.logger.info("[Fade] Deactivate Fade Out")

    def reset_fade_out_seconds(self):
        self.fade_action.tap_element("fade_fade_out_duration_default_button")

    def set_fade_out_plus_stepper(self):
        self.fade_action.tap_stepper("fade_fade_out_duration_plus_button")

    def set_fade_out_minus_stepper(self):
        self.fade_action.tap_stepper("fade_fade_out_duration_minus_button")

    def set_fade_out_input_textfield(self, value):
        self.fade_action.input_textfield("fade_fade_out_duration_value_text_field",value)

    def move_fade_out_slider(self):
        self.fade_action.move_slider("fade_fade_out_duration_slider_handle")

    def close_fade_inspector(self):
        self.fade_action.tap_element("inspector_fade")
        self.fade_action.logger.info("[Fade] Close Fade Inspector")


if __name__ == "__main__":
    fade = Fade()
    fade.activate_fade_out_checkbox()
    fade.set_fade_out_plus_stepper()
    fade.set_fade_out_minus_stepper()
    fade.reset_fade_out_seconds()
    fade.set_fade_out_input_textfield(19)
    fade.move_fade_out_slider()