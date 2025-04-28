from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time


class OpacityAction:

    # Opacity 컨테이너 구현을 위한 초기 세팅
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # 접근성 아이디를 파라미터로 클릭 액션 실행
    def click_element(self, id):
        self.driver.find_element(by=By.ID, value=id).click()

    # 스텝퍼 탭하는 액션 정의
    def tap_stepper(self, id, n = 3):
        for _ in range(n):
            self.click_element(id)
            replace_id = id.replace("opacity_&_blending", "").replace("button", "stepper")  # 로그의 가독성을 위해 ID 변경
            self.logger.info(f"[Opacity & Blending] {replace_id}")

    # 불투명도 조절에 사용될 슬라이더 움직이기
    def move_slider(self, id, horizontal_offset = 0.5):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform() # 슬라이더의 위치 변경
        self.logger.info("[Opacity & Blending] move slider")

    # 혼합 모드 드롭다운 열기
    def open_drop_down(self, id):
        self.click_element(id)

    # 불투명도 값을 조절하는 텍스트 박스에 값 입력
    def input_textfield(self,id, value = 50):
        text_field = self.driver.find_element(by=By.ID, value=id)  # 화면에서 텍스트 필드 찾기

        text_field.clear()  # 디폴트로 입력되어있던 값을 전부 지우기
        text_field.send_keys(value)  # 파라미터로 입력된 value 값을 입력함
        time.sleep(0.5)
        self.click_element("Return")  # 가상 키보드에서 return 을 탭
        self.logger.info(f"[Opacity & Blending] enter value : {value} into text field")
        

class Opacity:
    def __init__(self):
        self.opacity_action = OpacityAction()

    def open_edit_insepctor(self):
        self.opacity_action.click_element("edit_button")
        self.opacity_action.logger.info("[Inspector] open edit inspector")

    def open_opacity_blending_container(self):
        self.opacity_action.click_element("inspector_opacity_&_blending_container_view")
        self.opacity_action.logger.info("[Inspector] open opacity & blending container")

    def opacity_plus_stepper(self):
        self.opacity_action.tap_stepper("opacity_&_blending_opacity_plus_button")

    def opacity_minus_stepper(self):
        self.opacity_action.tap_stepper("opacity_&_blending_opacity_minus_button")

    def opacity_input_text_field(self):
        self.opacity_action.input_textfield("opacity_&_blending_opacity_value_text_field")

    def add_keyframe(self):
        self.opacity_action.click_element(id)  # 키프레임 추가
        self.opacity_action.logger.info("[opacity & Blending] add keyframe")

    def remove_keyframe(self):
        self.opacity_action.click_element(id)  # 키프레임 삭제
        self.opacity_action.logger.info("[opacity & Blending] remove keyframe")

    def open_blend_mode(self):
        self.opacity_action.open_drop_down("timeline_arrow_down_ic")
        self.opacity_action.logger.info("[inspector] open blending mode")


if __name__ == "__main__":
    opacity = Opacity()
    opacity.open_edit_insepctor()
    opacity.open_opacity_blending_container()
    opacity.opacity_input_text_field()



