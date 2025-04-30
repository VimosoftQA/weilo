from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time


class RemoveBGAction:

    # Remove BG 에서 사용되는 액션 정리
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # 접근성 아이디를 파라미터로 탭 액션 수행
    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    def tap_stepper(self, id, n = 5):
        for _ in range(n):
            self.tap_element(id)
            replace_id = id.replace("_button", " stepper")  # 로그의 가독성을 위해 ID 변경
            self.logger.info(f"[Remove BG] {replace_id}")

    # 슬라이더 핸들 위치 변경
    def move_slider(self, id, horizontal_offset = 20):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform() # 슬라이더의 위치 변경
        replace_id = id.replace("_slider_handle", "")
        self.logger.info(f"[Remove BG] move {replace_id} slider handle : {horizontal_offset}")

    # 텍스트 필드에 값 입력
    def input_textfield(self,id,value):
        text_field = self.driver.find_element(by=By.ID, value=id)  # 화면에서 텍스트 필드 찾기

        text_field.clear()  # 디폴트로 입력되어있던 값을 전부 지우기
        text_field.send_keys(value)  # 파라미터로 입력된 value 값을 입력함
        time.sleep(0.5)
        self.tap_element("Return")  # 가상 키보드에서 return 을 탭
        self.logger.info(f"[Remove BG] enter value : {value} into text field")

    # 하단에 위치한 옵션까지 자동화 하기 위해 세로로 스크롤
    def vertical_scroll(self,id,vertical_offset = -100):
        scroller = self.driver.find_element(by=By.ID, value=id)  #
        self.action.click_and_hold(scroller).move_by_offset(0, vertical_offset).release().perform()  # 세로로 스크롤하기
        self.logger.info("[Remove BG] vertical scroll")

    def turn_toggle(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

class RemoveBG:
    def __init__(self):
        self.remove_bg_action = RemoveBGAction()

    def open_edit_insepctor(self):
        self.remove_bg_action.tap_element("edit_button")
        self.remove_bg_action.logger.info("[Inspector] open edit inspector")

    def open_remove_bg_container(self):
        self.remove_bg_action.tap_element("inspector_remove_bg_container_view")
        self.remove_bg_action.logger.info("[Inspector] open remove BG container")

    def close_remove_bg_container(self):
        # 기본 보정 컨테이너가 열려있다는 전제 하에 실행함
        self.remove_bg_action.tap_element("inspector_remove_bg_container_view")
        self.remove_bg_action.logger.info("[Inspector] open remove BG container")

    # 클래스 생성 시 입력받은 option을 파라미터로 해서 중복되는 ID 처리
    def remove_bg_plus_stepper(self):
        self.remove_bg_action.tap_stepper("remove_bg_remove_bg_intensity_plus_button",n=3)

    # 클래스 생성 시 입력받은 option을 파라미터로 해서 중복되는 ID 처리
    def remove_bg_minus_stepper(self):
        self.remove_bg_action.tap_stepper("remove_bg_remove_bg_intensity_minus_button")

    def remove_bg_reset_default(self):
        self.remove_bg_action.tap_element("remove_bg_remove_bg_intensity_default_button")
        self.remove_bg_action.logger.info(f"[Remove BG] tap default button")

    def remove_bg_move_slider(self):
        value = -100
        self.remove_bg_action.move_slider("remove_bg_remove_bg_intensity_slider_handle",value)
        value = 30
        self.remove_bg_action.move_slider("remove_bg_remove_bg_intensity_slider_handle",value)

    def remove_bg_input_textfield(self):
        value = 40
        self.remove_bg_action.input_textfield("remove_bg_remove_bg_intensity_value_text_field",value)
        value = -50
        self.remove_bg_action.input_textfield("remove_bg_remove_bg_intensity_value_text_field",value)

    def remove_bg_turn_on_toggle(self):
        self.remove_bg_action.turn_toggle("remove_bg_remove_bg_toggle_switch")
        self.remove_bg_action.logger.info(f"[Remove BG] turn on remove BG toggle")

    def remove_bg_turn_off_toggle(self):
        self.remove_bg_action.turn_toggle("remove_bg_remove_bg_toggle_switch")
        self.remove_bg_action.logger.info(f"[Remove BG] turn off remove BG toggle")


if __name__ == "__main__":

    rmbg = RemoveBG()
    rmbg.open_edit_insepctor()
    rmbg.open_remove_bg_container()

    rmbg.remove_bg_turn_on_toggle()
    rmbg.remove_bg_minus_stepper()
    rmbg.remove_bg_plus_stepper()
    rmbg.remove_bg_reset_default()
    rmbg.remove_bg_move_slider()
    rmbg.remove_bg_turn_off_toggle()

    rmbg.close_remove_bg_container()