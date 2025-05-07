from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time


class TransformAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    def tap_stepper(self,id,n = 5):
        for _ in range(n):
            self.tap_element(id)
            replace_id = id.replace("_button", " stepper")  # 로그의 가독성을 위해 ID 변경
            self.logger.info(f"[Transform] {replace_id}")

    # TODO circle offset 값을 어떻게 조정해야할지 모르겠다
    # def move_circle_slider(self,id circle_offset):
    #     pass

    def move_roller(self,id,horizontal_offset = 30):
        slider = self.driver.find_element(by=By.ID, value=id)
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform()
        self.logger.info(f"[Transform] move infinite roller : {horizontal_offset}")

    def input_textfield(self, id, value):
        text_field = self.driver.find_element(by=By.ID, value=id)  # 화면에서 텍스트 필드 찾기

        text_field.clear()  # 디폴트로 입력되어있던 값을 전부 지우기
        text_field.send_keys(value)  # 파라미터로 입력된 value 값을 입력함
        time.sleep(0.5)
        self.tap_element("Return")  # 가상 키보드에서 return 을 탭
        self.logger.info(f"[Transform] enter value : {value} into text field")


    def vertical_scroll(self, id, vertical_offset=-100):
        scroller = self.driver.find_element(by=By.ID, value=id)  #
        self.action.click_and_hold(scroller).move_by_offset(0, vertical_offset).release().perform()  # 세로로 스크롤하기
        self.logger.info("[Transform] vertical scroll")



class Transform:
    def __init__(self):
        self.transform_action = TransformAction()

    def open_edit_insepctor(self):
        self.transform_action.tap_element("edit_button")
        self.transform_action.logger.info("[Inspector] open edit inspector")

    def open_transform_container(self):
        self.transform_action.tap_element("inspector_transform_container_view")
        self.transform_action.logger.info("[Inspector] open transform container")

    def close_transform_container(self):
        self.transform_action.tap_element("inspector_transform_container_view")
        self.transform_action.logger.info("[Inspector] close transform container")

    def transform_location_add_keyframe(self):
        self.transform_action.tap_element("transform_position_key_frame_iobutton")
        self.transform_action.logger.info("[Transform] location : add keyframe")

    def transform_location_remove_keyframe(self):
        self.transform_action.tap_element("transform_position_key_frame_iobutton")
        self.transform_action.logger.info("[Transform] location : remove keyframe")

    # TODO 겹치는 함수들은 정리해두자
    def transform_location_X_reset_default(self):
        self.transform_action.tap_element("transform_position_x_default_button")
        self.transform_action.logger.info("[Transform] location : reset default X")

    def transform_location_Y_reset_default(self):
        self.transform_action.tap_element("transform_position_y_default_button")
        self.transform_action.logger.info("[Transform] location : reset default Y")

    # TODO roller 가 제대로 동작하는지 확인 필요함
    def transform_location_X_infinite_roller(self):
        value = -100
        self.transform_action.move_roller("transform_position_x_infinite_roller",value)
        value = 100
        self.transform_action.move_roller("transform_position_x_infinite_roller",value)

    def transform_location_Y_infinite_roller(self):
        value = -100
        self.transform_action.move_roller("transform_position_y_infinite_roller",value)
        value = 100
        self.transform_action.move_roller("transform_position_y_infinite_roller",value)

    def transform_location_X_plus_stepper(self):
        self.transform_action.tap_element("transform_position_x_plus_button")

    def transform_location_X_minus_stepper(self):
        self.transform_action.tap_element("transform_position_x_minus_button")

    def transform_location_Y_plus_stepper(self):
        self.transform_action.tap_element("transform_position_y_plus_button")

    def transform_location_Y_minus_stepper(self):
        self.transform_action.tap_element("transform_position_y_minus_button")

    def transform_location_X_input_textfield(self):
        value = 50
        self.transform_action.input_textfield("transform_position_x_value_text_field",value)
        value = -50
        self.transform_action.input_textfield("transform_position_x_value_text_field",value)

    def transform_location_Y_input_textfield(self):
        value = 50
        self.transform_action.input_textfield("transform_position_y_value_text_field",value)
        value = -50
        self.transform_action.input_textfield("transform_position_y_value_text_field",value)


    # scale 값 조정
    def transform_scale_add_keyframe(self):
        self.transform_action.tap_element("transform_scale_key_frame_iobutton")
        self.transform_action.logger.info("[Transform] scale : add keyframe")

    def transform_scale_remove_keyframe(self):
        self.transform_action.tap_element("transform_scale_key_frame_iobutton")
        self.transform_action.logger.info("[Transform] scale : remove keyframe")

    def transform_scale_X_Y_turn_off_link(self):
        self.transform_action.tap_element("transform_scale_x;y_link_button")
        self.transform_action.logger.info("[Transform] scale : turn off link")

    def transform_scale_X_Y_turn_on_link(self):
        self.transform_action.tap_element("transform_scale_x;y_link_button")
        self.transform_action.logger.info("[Transform] scale : turn on link")

    def transform_scale_x_reset_default(self):
        self.transform_action.tap_element("transform_scale_x;y_default_button")
        self.transform_action.logger.info("[Transform] scale : reset default X")

    def transform_scale_y_reset_default(self):
        self.transform_action.tap_element("transform_scale_x;y_linked_default_button")
        self.transform_action.logger.info("[Transform] scale : reset default Y")

    # TODO roller 가 제대로 동작하는지 확인 필요함
    def transform_scale_X_infinite_roller(self):
        value = -100
        self.transform_action.move_roller("transform_scale_x;y_infinite_roller",value)
        value = 100
        self.transform_action.move_roller("transform_scale_x_infinite_roller",value)

    # Y값 롤러는 없는지 inspector 창에서 확인 필요
    def transform_scale_Y_infinite_roller(self):
        pass

    def transform_scale_X_plus_stepper(self):
        self.transform_action.tap_stepper("transform_scale_x;y_plus_button")

    def transform_scale_X_minus_stepper(self):
        self.transform_action.tap_stepper("transform_scale_x;y_minus_button")

    # x랑 y값의 iD가 동일한데 어떻게 구별할 수 있지?
    def transform_scale_Y_plus_stepper(self):
        self.transform_action.tap_stepper("transform_scale_x;y_plus_button")

    def transform_scale_Y_minus_stepper(self):
        self.transform_action.tap_stepper("transform_scale_x;y_minus_button")

    def transform_scale_X_input_textfield(self):
        value = 50
        self.transform_action.input_textfield("transform_scale_x;y_value_text_field",value)
        value = -50
        self.transform_action.input_textfield("transform_scale_x;y_value_text_field",value)

    def transform_scale_Y_input_textfield(self):
        value = 50
        self.transform_action.input_textfield("transform_scale_x;y_value_text_field",value)
        value = -50
        self.transform_action.input_textfield("transform_scale_x;y_value_text_field",value)

    # 로테이션 값 지정
    def transform_rotation_add_keyframe(self):
        self.transform_action.tap_element("transform_rotation_key_frame_iobutton")
        self.transform_action.logger.info("[Transform] rotation : add keyframe")

    def transform_rotation_remove_keyframe(self):
        self.transform_action.tap_element("transform_rotation_key_frame_iobutton")
        self.transform_action.logger.info("[Transform] rotation : remove keyframe")

    def transform_rotation_reset_default(self):
        self.transform_action.tap_element("transform_rotation_default_button")
        self.transform_action.logger.info("[Transform] rotation : reset default")


    def transform_rotation_plus_15_button(self,n = 4):
        for _ in range(n):
            self.transform_action.tap_element("transform_rotation_plus_button") # 스텝퍼랑 이름이 겹침
        self.transform_action.logger.info(f"[Transform] rotation : tap {n} times +15 button")

    def transform_rotation_minus_15_button(self,n = 4):
        for _ in range(n):
            self.transform_action.tap_element("transform_rotation_minus_button")
        self.transform_action.logger.info(f"[Transform] rotation : tap {n} times -15 button")

    def transform_rotation_plus_stepper(self):
        self.transform_action.tap_stepper("transform_rotation_plus_button")

    def transform_rotation_minus_stepper(self):
        self.transform_action.tap_stepper("transform_rotation_minus_button")

    def transform_rotation_input_textfield(self):
        value = 90
        self.transform_action.input_textfield("transform_rotation_value_text_field",value)
        value = -90
        self.transform_action.input_textfield("transform_rotation_value_text_field",value)

    # 앵커 포인트
    def transform_anchor_point_x_reset_default(self):
        self.transform_action.tap_element("transform_anchor_point_x_default_button")
        self.transform_action.logger.info("[Transform] anchor : reset default X")

    def transform_anchor_point_y_reset_default(self):
        self.transform_action.tap_element("transform_anchor_point_y_default_button")
        self.transform_action.logger.info("[Transform] anchor : reset default Y")

    def transform_anchor_point_x_plus_stepper(self):
        self.transform_action.tap_element("transform_anchor_point_x_plus_button")

    def transform_anchor_point_x_minus_stepper(self):
        self.transform_action.tap_element("transform_anchor_point_x_minus_button")

    def transform_anchor_point_y_plus_stepper(self):
        self.transform_action.tap_element("transform_anchor_point_y_plus_button")

    def transform_anchor_point_y_minus_stepper(self):
        self.transform_action.tap_element("transform_anchor_point_y_minus_button")

    def transform_anchor_point_X_input_textfield(self):
        value = 50
        self.transform_action.input_textfield("transform_anchor_point_x_value_text_field",value)
        value = -50
        self.transform_action.input_textfield("transform_anchor_point_x_value_text_field",value)

    def transform_anchor_point_Y_input_textfield(self):
        value = 50
        self.transform_action.input_textfield("transform_anchor_point_y_value_text_field",value)
        value = -50
        self.transform_action.input_textfield("transform_anchor_point_y_value_text_field",value)

    # TODO roller 가 제대로 동작하는지 확인 필요함
    def transform_anchor_point_X_infinite_roller(self):
        value = -100
        self.transform_action.move_roller("transform_anchor_point_x_infinite_roller",value)
        value = 100
        self.transform_action.move_roller("transform_anchor_point_x_infinite_roller",value)

    def transform_anchor_point_Y_infinite_roller(self):
        value = -100
        self.transform_action.move_roller("transform_anchor_point_y_infinite_roller",value)
        value = 100
        self.transform_action.move_roller("transform_anchor_point_y_infinite_roller",value)






    def transform_flip_vertical(self):
        self.transform_action.tap_element("transform_flip_button_list_button_1")
        self.tranform_action.logger.info("[Transform] flip vertical")

    def transform_flip_horizontal(self):
        self.transform_action.tap_element("transform_flip_button_list_button_2")
        self.transform_action.logger.info("[Transform] flip horizontal")