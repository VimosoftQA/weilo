from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class AdjustmentsAction:

    # Adjustments 에서 사용되는 액션 정리
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # 접근성 아이디를 파라미터로 탭 액션 수행
    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    def tap_stepper(self, id, n = 3):
        for _ in range(n):
            self.tap_element(id)
            replace_id = id.replace("adjustments_", "").replace("_button", " stepper")  # 로그의 가독성을 위해 ID 변경
            self.logger.info(f"[Adjustments] {replace_id}")

    # 슬라이더 핸들 위치 변경
    def move_slider(self, id, horizontal_offset = 20):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform() # 슬라이더의 위치 변경
        replace_id = id.replace("adjustments_", "").replace("_slider_handle", "")
        self.logger.info(f"[Adjustments] move {replace_id} slider handle : {horizontal_offset}")

    # 텍스트 필드에 값 입력
    def input_textfield(self,id,value):
        text_field = self.driver.find_element(by=By.ID, value=id)  # 화면에서 텍스트 필드 찾기

        text_field.clear()  # 디폴트로 입력되어있던 값을 전부 지우기
        text_field.send_keys(value)  # 파라미터로 입력된 value 값을 입력함
        time.sleep(0.5)
        self.tap_element("Return")  # 가상 키보드에서 return 을 탭
        self.logger.info(f"[Adjustments] enter value : {value} into text field")

    # 하단에 위치한 옵션까지 자동화 하기 위해 세로로 스크롤
    def vertical_scroll(self,id,vertical_offset = -100):
        scroller = self.driver.find_element(by=By.ID, value=id)  #
        self.action.click_and_hold(scroller).move_by_offset(0, vertical_offset).release().perform()  # 세로로 스크롤하기
        self.logger.info("[Adjustments] vertical scroll")

class Adjustments:
    def __init__(self):
        self.adjustments_action = AdjustmentsAction()

    def open_edit_insepctor(self):
        self.adjustments_action.tap_element("edit_button")
        self.adjustments_action.logger.info("[Inspector] open edit inspector")

    def open_adjustements_container(self):
        self.adjustments_action.tap_element("inspector_adjustments_container_view")
        self.adjustments_action.logger.info("[Inspector] open adjustments container")

    def close_adjustments_container(self):
        # 기본 보정 컨테이너가 열려있다는 전제 하에 실행함
        self.adjustments_action.tap_element("inspector_adjustments_container_view")
        self.adjustments_action.logger.info("[Inspector] open adjustments container")

    # 클래스 생성 시 입력받은 option을 파라미터로 해서 중복되는 ID 처리
    def adjustments_plus_stepper(self,option):
        self.adjustments_action.tap_stepper(f"adjustments_{option}_plus_button")

    # 클래스 생성 시 입력받은 option을 파라미터로 해서 중복되는 ID 처리
    def adjustments_minus_stepper(self,option):
        self.adjustments_action.tap_stepper(f"adjustments_{option}_minus_button")

    def adjustments_reset_default(self,option):
        self.adjustments_action.tap_element(f"adjustments_{option}_default_button")
        self.adjustments_action.logger.info(f"[Adjustments] {option} default button")

    def adjustments_add_keyframe(self,option):
        self.adjustments_action.tap_element(f"adjustments_{option}_key_frame_iobutton")
        self.adjustments_action.logger.info(f"[Adjustments] {option} add keyframe")

    def adjustments_remove_keyframe(self,option):
        self.adjustments_action.tap_element(f"adjustments_{option}_key_frame_iobutton")
        self.adjustments_action.logger.info(f"[Adjustments] {option} remove keyframe")

    def adjustments_move_slider(self,option):
        value = -40
        self.adjustments_action.move_slider(f"adjustments_{option}_slider_handle",value)
        value = 30
        self.adjustments_action.move_slider(f"adjustments_{option}_slider_handle",value)

    def adjustments_input_textfield(self,option):
        value = 40
        self.adjustments_action.input_textfield(f"adjustments_{option}_value_text_field",value)
        value = -50
        self.adjustments_action.input_textfield(f"adjustments_{option}_value_text_field",value)

    def adjustments_scoll_next_category(self):
        id = "inspector dash ic"
        self.adjustments_action.vertical_scroll(id)

if __name__ == "__main__":
    options = [["light_contrast","light_highlights","light_shadows","light_brightness"],
               ["color_saturation","color_vibrance","color_temperature","color_tint","color_hue"],
               ["additional_sharpness"]]

    adj = Adjustments()
    adj.open_edit_insepctor()
    adj.open_adjustements_container()

    for opts in options:
        for opt in opts:
            adj.adjustments_plus_stepper(opt)
            adj.adjustments_minus_stepper(opt)
            adj.adjustments_reset_default(opt)
            adj.adjustments_move_slider(opt)
            adj.adjustments_input_textfield(opt)
            adj.adjustments_add_keyframe(opt)
            adj.adjustments_remove_keyframe(opt)
        adj.adjustments_scoll_next_category()
