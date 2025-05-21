from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time


class FillStrokeAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    def tap_stepper(self, id, n = 5):
        for _ in range(n):
            self.tap_element(id)
            replace_id = id.replace("_button", " stepper")  # 로그의 가독성을 위해 ID 변경
            self.logger.info(f"[Shape Transform] {replace_id}")

    def input_textfield(self,id, value):
        text_field = self.driver.find_element(by=By.ID, value=id)  # 화면에서 텍스트 필드 찾기
        text_field.clear()  # 디폴트로 입력되어있던 값을 전부 지우기
        text_field.send_keys(value)  # 파라미터로 입력된 value 값을 입력함
        time.sleep(0.5)
        self.tap_element("Return")  # 가상 키보드에서 return 을 탭
        self.logger.info(f"[Shape Transform] enter value : {value} into text field")

    def move_slider(self, id, horizontal_offset=-10):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform()  # 슬라이더의 위치 변경
        self.logger.info("[Text Format] move slider")

class FillStroke:
    def __init__(self):
        self.fill_stroke_action = FillStrokeAction()

    def open_fill_stroke_container(self):
        self.fill_stroke_action.tap_element("inspector_fill_&_stroke_container_view")
        self.fill_stroke_action.logger.info("[Fill & Stroke] open Fill & Stroke container")

    def close_fill_stroke_container(self):
        self.fill_stroke_action.tap_element("inspector_fill_&_stroke_container_view")
        self.fill_stroke_action.logger.info("[Fill & Stroke] close Fill & Stroke container")

    def turn_on_fill_checkbox(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_fill_checkbox")
        self.fill_stroke_action.logger.info("[Fill & Stroke] turn on fill checkbox")

    def turn_off_fill_checkbox(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_fill_checkbox")
        self.fill_stroke_action.logger.info("[Fill & Stroke] turn off fill checkbox")

    def add_keyframe_fill(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_fill_key_frame_iobutton")
        self.fill_stroke_action.logger.info("[Fill & Stroke] add keyframe fill")

    def remove_keyframe_fill(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_fill_key_frame_iobutton")
        self.fill_stroke_action.logger.info("[Fill & Stroke] remove keyframe fill")

    def tap_fill_color_preview(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_fill_color_preview")
        self.fill_stroke_action.logger.info("[Fill & Stroke] tap fill color preview")

    def tap_fill_spoid_button(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_fill_spoid_button")
        self.fill_stroke_action.logger.info("[Fill & Stroke] tap fill spoid button")

    def turn_on_stroke_checkbox(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_checkbox")
        self.fill_stroke_action.logger.info("[Fill & Stroke] turn on stroke checkbox")

    def turn_off_stroke_checkbox(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_checkbox")
        self.fill_stroke_action.logger.info("[Fill & Stroke] turn off stroke checkbox")

    def add_keyframe_stroke(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_key_frame_iobutton")
        self.fill_stroke_action.logger.info("[Fill & Stroke] add stroke keyframe")

    def remove_keyframe_stroke(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_key_frame_iobutton")
        self.fill_stroke_action.logger.info("[Fill & Stroke] remove stroke keyframe")

    def tap_stroke_color_preview(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_color_preview")
        self.fill_stroke_action.logger.info("[Fill & Stroke] tap stroke color preview")

    def tap_stroke_spoid_button(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_spoid_button")
        self.fill_stroke_action.logger.info("[Fill & Stroke] tap stroke spoid button")

    def add_keyframe_stroke_width(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_stroke_outline_width_key_frame_iobutton")
        self.fill_stroke_action.logger.info("[Fill & Stroke] add stroke width keyframe")

    def remove_keyframe_stroke_width(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_stroke_outline_width_key_frame_iobutton")
        self.fill_stroke_action.logger.info("[Fill & Stroke] remove stroke width keyframe")

    def reset_default_stroke_width(self):
        self.fill_stroke_action.tap_element("fill_&_stroke_stroke_stroke_outline_width_default_button")
        self.fill_stroke_action.logger.info("[Fill & Stroke] reset default stroke width")

    def tap_stroke_width_minus_stepper(self):
        self.fill_stroke_action.tap_stepper("fill_&_stroke_stroke_stroke_outline_width_minus_button")
        self.fill_stroke_action.logger.info("[Fill & Stroke] tap stroke width minus stepper")

    def tap_stroke_width_plus_stepper(self):
        self.fill_stroke_action.tap_stepper("fill_&_stroke_stroke_stroke_outline_width_plus_button")
        self.fill_stroke_action.logger.info("[Fill & Stroke] tap stroke width plus stepper")

    def tap_stroke_width_input_textfield(self,value):
        self.fill_stroke_action.input_textfield("fill_&_stroke_stroke_stroke_outline_width_value_text_field",value)
        self.fill_stroke_action.logger.info(f"[Fill & Stroke] stroke width input textfield : {value}")

    def move_stroke_width_slider(self):
        self.fill_stroke_action.move_slider("fill_&_stroke_stroke_stroke_outline_width_slider_handle")
        self.fill_stroke_action.logger.info("[Fill & Stroke] move stroke width slider")

    def tap_align(self):
        aligns = ["inspector shape border center", "inspector shape border inside", "inspector shape border outside"]
        for ali in aligns:
            self.fill_stroke_action.tap_element(ali)
            self.fill_stroke_action.logger.info(f"[Fill & Stroke] align : {ali}")

    def tap_edge(self):
        edges = ["inspector shape edge angular i", "inspector shape edge  round ic", "inspector shape edge  flat ic"]
        for edge in edges:
            self.fill_stroke_action.tap_element(edge)
            self.fill_stroke_action.logger.info(f"[Fill & Stroke] edge : {edge}")
