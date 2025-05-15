from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class FadeAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # ID로 아이템 탭하기
    def tap_element(self,id):
        self.driver.find_element(by = By.ID,value = id).click()

    # 텍스트 필드에 값 입력
    def input_textfield(self,id,value):
        text_field = self.driver.find_element(By.ID, id)
        text_field.clear()
        text_field.send_keys(value)
        time.sleep(1)
        self.tap_element(id = "Return")

    # 스텝퍼 탭하기 ( 파라미터 n의 값을 바꾸면 스텝퍼 이동 단위를 변경할 수 있습니다)
    def tap_stepper(self, id, n = 3):
        for _ in range(n):
            self.tap_element(id)
        replace_id = id.replace("button", "stepper")  # 로그의 가독성을 위해 ID 변경
        self.logger.info(f"[Fade] {replace_id}")

    # 슬라이더 이동
    def move_slider(self, id, horizontal_offset = -10):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform() # 슬라이더의 위치 변경
        self.logger.info("[Fade] move slider")


class Fade:
    def __init__(self):
        self.fade_action = FadeAction()

    # 페이드 인스펙터 열기
    def open_fade_inspector(self):
        self.fade_action.tap_element("inspector_fade")
        self.fade_action.logger.info("[Fade] Open Fade Inspector")

    # 페이드인 체크박스 활성화
    def activate_fade_in_checkbox(self):
        self.fade_action.tap_element("fade_fade_in_checkbox")
        self.fade_action.logger.info("[Fade] Activate Fade In Checkbox")

    # 페이드인 체크박스 비활성화
    def deactivate_fade_in_checkbox(self):
        self.fade_action.tap_element("fade_fade_in_checkbox")
        self.fade_action.logger.info("[Fade] Deactivate Fade In Checkbox")

    # 페이드인 시간 기본값으로 리셋
    def reset_fade_in_seconds(self):
        self.fade_action.tap_element("fade_fade_in_duration_default_button")

    # 페이드인 시간 늘리는 스텝퍼 (기본 n = 3)
    def set_fade_in_plus_stepper(self):
        self.fade_action.tap_stepper("fade_fade_in_duration_plus_button")

    # 페이드인 시간 줄이는 스텝퍼 (기본 n = 3)
    def set_fade_in_minus_stepper(self):
        self.fade_action.tap_stepper("fade_fade_in_duration_minus_button")

    # 페이드인 값 직접 입력
    def set_fade_in_input_textfield(self, value):
        self.fade_action.input_textfield("fade_fade_in_duration_value_text_field",value)

    # 페이드인 슬라이더 이동
    def move_fade_in_slider(self):
        self.fade_action.move_slider("fade_fade_in_duration_slider_handle")

    # 페이드 아웃 체크박스 활성화
    def activate_fade_out_checkbox(self):
        self.fade_action.tap_element("fade_fade_out_checkbox")
        self.fade_action.logger.info("[Fade] Activate Fade Out")

    # 페이드 아웃 체크박스 비활성화
    def deactivate_fade_out_checkbox(self):
        self.fade_action.tap_element("fade_fade_out_checkbox")
        self.fade_action.logger.info("[Fade] Deactivate Fade Out")

    # 페이드 아웃 시간 기본값으로 리셋
    def reset_fade_out_seconds(self):
        self.fade_action.tap_element("fade_fade_out_duration_default_button")

    # 페이드 아웃 시간 늘리는 스텝퍼 (기본 n = 3)
    def set_fade_out_plus_stepper(self):
        self.fade_action.tap_stepper("fade_fade_out_duration_plus_button")

    # 페이드 아웃 시간 줄이는 스텝퍼 (기본 n = 3)
    def set_fade_out_minus_stepper(self):
        self.fade_action.tap_stepper("fade_fade_out_duration_minus_button")

    # 페이드 아웃 값 직접 입력
    def set_fade_out_input_textfield(self, value):
        self.fade_action.input_textfield("fade_fade_out_duration_value_text_field",value)

    # 페이드 아웃 슬라이더 이동
    def move_fade_out_slider(self):
        self.fade_action.move_slider("fade_fade_out_duration_slider_handle")

    # 페이드 인스펙터 닫기
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