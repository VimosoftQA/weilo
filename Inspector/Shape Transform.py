from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time



class ShapeTransformAction:
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
            self.logger.info(f"[Shape Transform] {replace_id}")

    def input_textfield(self,id, value):
        text_field = self.driver.find_element(by=By.ID, value=id)  # 화면에서 텍스트 필드 찾기
        text_field.clear()  # 디폴트로 입력되어있던 값을 전부 지우기
        text_field.send_keys(value)  # 파라미터로 입력된 value 값을 입력함
        time.sleep(0.5)
        self.tap_element("Return")  # 가상 키보드에서 return 을 탭
        self.logger.info(f"[Shape Transform] enter value : {value} into text field")




    class ShapeTransform:
        def __init__(self):
            self.shape_transform_action = ShapeTransformAction()

        def open_shape_transform_container(self):
            self.shape_transform_action.tap_element("inspector_shape_transform_container_view")
            self.shape_transform_action.logger.info("[Shape Transform] open shape transform container")

        def close_shape_transform_container(self):
            self.shape_transform_action.tap_element("inspector_shape_transform_container_view")
            self.shape_transform_action.logger.info("[Shape Transform] close shape transform container")

        def add_keyframe_shape_transform(self):
            self.shape_transform_action.tap_element("shape_transform_shape_transform_key_frame_iobutton")
            self.shape_transform_action.logger.info("[Shape Transform] add keyframe shape transform")

        def remove_keyframe_shape_transform(self):
            self.shape_transform_action.tap_element("shape_transform_shape_transform_key_frame_iobutton")
            self.shape_transform_action.logger.info("[Shape Transform] remove keyframe shape transform")

        def turn_on_edit_path_point(self):
            self.shape_transform_action.tap_element("shape_transform_shape_transform_path_point_button_list_button_1")
            self.shape_transform_action.logger.info("[Shape Transform] turn on edit path point")

        def turn_off_edit_path_point(self):
            self.shape_transform_action.tap_element("shape_transform_shape_transform_path_point_button_list_button_1")
            self.shape_transform_action.logger.info("[Shape Transform] turn on edit path point")

        def transform_position_X_plus_stepper(self):
            self.shape_transform_action.tap_stepper("shape_transform_shape_transform_position_x_plus_button")
            self.shape_transform_action.logger.info("[Shape Transform] transform position X plus stepper")

        def transform_position_X_minus_stepper(self):
            self.shape_transform_action.tap_stepper("shape_transform_shape_transform_position_x_minus_button")
            self.shape_transform_action.logger.info("[Shape Transform] transform position X minus stepper")

        def transform_position_X_input_textfield(self,value):
            self.shape_transform_action.input_textfield("shape_transform_shape_transform_position_x_value_text_field",value)
            self.shape_transform_action.logger.info(f"[Shape Transform] transform position X input textfield : {value}")

        def transform_position_Y_plus_stepper(self):
            self.shape_transform_action.tap_stepper("shape_transform_shape_transform_position_y_plus_button")
            self.shape_transform_action.logger.info("[Shape Transform] transform position Y plus stepper")

        def transform_position_Y_minus_stepper(self):
            self.shape_transform_action.tap_stepper("shape_transform_shape_transform_position_y_minus_button")
            self.shape_transform_action.logger.info("[Shape Transform] transform position Y minus stepper")

        def transform_position_Y_input_textfield(self, value):
            self.shape_transform_action.input_textfield("shape_transform_shape_transform_position_y_value_text_field",value)
            self.shape_transform_action.logger.info(f"[Shape Transform] transform position Y input textfield : {value}")

        def transform_rotation_plus_1(self):
            self.shape_transform_action.tap_element("shape_transform_rotation_button_list_button_2")
            self.shape_transform_action.logger.info("[Shape Transform] transform rotation plus 1")

        def transform_rotation_minus_1(self):
            self.shape_transform_action.tap_element("shape_transform_rotation_button_list_button_1")
            self.shape_transform_action.logger.info("[Shape Transform] transform rotation minus 1")

        def transform_flip_horizontal(self):
            self.shape_transform_action.tap_element("shape_transform_flip_button_list_button_2")
            self.shape_transform_action.logger.info("[Shape Transform] transform horizontal flip")

        def transform_flip_vertical(self):
            self.shape_transform_action.tap_element("shape_transform_flip_button_list_button_1")
            self.shape_transform_action.logger.info("[Shape Transform] transform vertical flip")