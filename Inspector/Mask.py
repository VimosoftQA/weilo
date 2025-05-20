from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class MaskAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # ID로 값 찾아서 탭하기
    def tap_element(self,id):
        self.driver.find_element(By.ID, id).click()

    # 스텝퍼 탭하기
    def tap_stepper(self, id, n = 10):
        for _ in range(n):
            self.driver.find_element(By.ID, id).click()
        replace_id = id.replace("_button", " stepper")  # 로그의 가독성을 위해 ID 변경
        self.logger.info(f"[Mask] {replace_id} : {n}")

    # 인풋 텍스트 입력
    def input_textfield(self,id,value):
        text_field = self.driver.find_element(By.ID, id)

        text_field.clear()
        text_field.send_keys(value)
        time.sleep(0.5)

        self.tap_element("Return")
        self.logger.info(f"[Mask] Return value : {value} into text field")


class Mask:
    def __init__(self):
        self.mask_action = MaskAction()

    # 마스크 인스펙터 열기
    def open_mask_inspector(self):
        self.mask_action.tap_element("inspector_mask_container_view")
        self.mask_action.logger.info("[Mask] Opening Mask Inspector")

    # 마스크 인스펙터 밖으로 나가는 버튼에 접근성 ID 없음

    # 마스크 원본 보기 토글 ON
    def show_original_toggle_on(self):
        self.mask_action.tap_element("add_mask_view_mode_toggle_switch")
        self.mask_action.logger.info("[Mask] Show Original Toggle ON")

    # 마스크 원본 보기 토글 OFF
    def show_original_toggle_off(self):
        self.mask_action.tap_element("add_mask_view_mode_toggle_switch")
        self.mask_action.logger.info("[Mask] Show Original Toggle OFF")

    # 마스크 추가 (기본 : rectangle)
    def add_mask(self, mask_shape = "rectangle"):
        self.mask_action.tap_element(f"mask_{mask_shape}_img")
        self.mask_action.logger.info(f"[Mask] Added Mask Shape: {mask_shape}")

    # 마스크 개체 인스펙터 열기
    def open_mask_fold_inspector(self):
        self.mask_action.tap_element("inspector_mask_1_is_folded_button")
        self.mask_action.logger.info(f"[Mask] Open Mask Inspector")

    # 마스크 개체 인스펙터 닫기
    def close_mask_fold_inspector(self):
        self.mask_action.tap_element("inspector_mask_1_is_folded_button")
        self.mask_action.logger.info("[Mask] Close Mask Inspector")

    # 마스크 반전 토글 ON
    def invert_mask_toggle_on(self):
        self.mask_action.tap_element("mask_1_invert_toggle_switch")
        self.mask_action.logger.info(f"[Mask] Invert Mask Toggle ON")

    # 마스크 반전 토글 OFF
    def invert_mask_toggle_off(self):
        self.mask_action.tap_element("mask_1_invert_toggle_switch")
        self.mask_action.logger.info("[Mask] Invert Mask Toggle OFF")

    # 마스크 변형 키프레임 추가
    def transform_mask_add_keyframe(self):
        self.mask_action.tap_element("mask_1_shape_transform_key_frame_iobutton")
        self.mask_action.logger.info("[Mask] Add Transform Keyframe")

    # 마스크 변형 키프레임 제거
    def transform_mask_remove_keyframe(self):
        self.mask_action.tap_element("mask_1_shape_transform_key_frame_iobutton")
        self.mask_action.logger.info("[Mask] Remove Transform Keyframe")

    # 마스크 위치 X의 리셋 탭
    def transform_mask_location_X_reset_default(self):
        self.mask_action.tap_element("mask_1_shape_transform_position_x_default_button")
        self.mask_action.logger.info("[Mask] Reset Transform Mask Location X")

    # 마스크 위치 Y의 리셋 탭
    def transform_mask_location_Y_reset_default(self):
        self.mask_action.tap_element("mask_1_shape_transform_position_y_default_button")
        self.mask_action.logger.info("[Mask] Reset Transform Mask Location Y")

    # 마스크 위치 X의 마이너스 스텝퍼 탭하기
    def transform_mask_location_X_minus_stepper(self):
        self.mask_action.tap_stepper("mask_1_shape_transform_position_x_minus_button")

    # 마스크 위치 X의 플러스 스텝퍼 탭하기
    def transform_mask_location_X_plus_stepper(self):
        self.mask_action.tap_stepper("mask_1_shape_transform_position_x_plus_button")

    # 마스크 위치 Y의 마이너스 스텝퍼 탭하기
    def transform_mask_location_Y_minus_stepper(self):
        self.mask_action.tap_stepper("mask_1_shape_transform_position_y_minus_button")

    # 마스크 위치 Y의 플러스 스텝퍼 탭화기
    def transform_mask_location_Y_plus_stepper(self):
        self.mask_action.tap_stepper("mask_1_shape_transform_position_y_plus_button")

    # 마스크 위치 X의 텍스트 입력
    def transform_mask_location_X_input_textfield(self):
        value = 100
        self.mask_action.input_textfield("mask_1_shape_transform_position_x_value_text_field",value)
        value = -100
        self.mask_action.input_textfield("mask_1_shape_transform_position_x_value_text_field",value)

    # 마스크 위치 Y의 텍스트 입력
    def transform_mask_location_Y_input_textfield(self):
        value = 100
        self.mask_action.input_textfield("mask_1_shape_transform_position_y_value_text_field", value)
        value = -100
        self.mask_action.input_textfield("mask_1_shape_transform_position_y_value_text_field", value)

    # 마스크 크기 링크 ON
    def scale_mask_link_on_width_height(self):
        self.mask_action.tap_element("mask_1_shape_transform_width;height_link_button")
        self.mask_action.logger.info("[Mask] Scale Mask Link ON width and height")

    # 마스크 크기 링크 OFF
    def scale_mask_link_off_width_height(self):
        self.mask_action.tap_element("mask_1_shape_transform_width;height_link_button")
        self.mask_action.logger.info("[Mask] Scale Mask Link OFF width and height")

    # plus stepper 랑 minus stepper 와 같은 ID를 사용 중임 -> 값을 구별해서 넣기 어려운 상황
    # def scale_mask_width_minus_stepper(self):
    #     self.mask_action.tap_stepper("mask_1_shape_transform_width;height_minus_button")
    #
    # def scale_mask_width_plus_stepper(self):
    #     self.mask_action.tap_stepper("mask_1_shape_transform_width;height_plus_button")
    #
    # def scale_mask_height_minus_stepper(self):
    #     self.mask_action.tap_stepper("mask_1_shape_transform_width;height_minus_button")
    #
    # def scale_mask_height_plus_stepper(self):
    #     self.mask_action.tap_stepper("mask_1_shape_transform_width;height_plus_button")
    # def scale_mask_width_input_textfield(self):
    #     value = 10
    #     self.mask_action.input_textfield("mask_1_shape_transform_width;height_value_text_field", value)
    #
    # def scale_mask_height_input_textfield(self):
    #     value = 10
    #     self.mask_action.input_textfield("mask_1_shape_transform_width;height_value_text_field", value)

    # 마스크 오른쪽으로 회전 (기본 n = 5)
    def rotation_mask_right(self, n = 5):
        for _ in range(n):
            self.mask_action.tap_element("mask_1_shape_transform_rotation_button_list_button_2")
        self.mask_action.logger.info(f"[Mask] Rotate Mask Right : {n}")

    # 마스크 왼쪽으로 회전 (기본 n = 5)
    def rotation_mask_left(self, n = 5):
        for _ in range(n):
            self.mask_action.tap_element("mask_1_shape_transform_rotation_button_list_button_1")
        self.mask_action.logger.info(f"[Mask] Rotate Mask Left : {n}")

    # 마스크 확장 키프레임 추가
    def expansion_add_keyframe(self):
        self.mask_action.tap_element("mask_1_expansion_key_frame_iobutton")
        self.mask_action.logger.info("[Mask] Add Expansion Keyframe")

    # 마스크 확장 키프레임 제거
    def expansion_remove_keyframe(self):
        self.mask_action.tap_element("mask_1_expansion_key_frame_iobutton")
        self.mask_action.logger.info("[Mask] Remove Expansion Keyframe")

    # 마스크 확장 기본으로 리셋
    def expansion_reset_default(self):
        self.mask_action.tap_element("mask_1_expansion_default_button")
        self.mask_action.logger.info("[Mask] Reset Expansion Default")

    # 마스크 확장 마이너스 스텝퍼
    def expansion_minus_stepper(self):
        self.mask_action.tap_element("mask_1_expansion_minus_button")
        self.mask_action.logger.info("[Mask] Minus Expansion Button")

    # 마스크 확장 플러스 스텝퍼
    def expansion_plus_stepper(self):
        self.mask_action.tap_element("mask_1_expansion_plus_button")
        self.mask_action.logger.info("[Mask] Plus Expansion Button")

    # 마스크 확장 인풋 텍스트 입력
    def expansion_input_textfield(self):
        value = 10
        self.mask_action.input_textfield("mask_1_expansion_value_text_field",value)


    # 슬라이더 구현하기 (노션 페이지 접근성 아이디와 위 기능을 복사해서 사용할 수 있습니다)
    def expansion_scroll(self):
        pass

    def feather_add_keyframe(self):
        pass

    def feather_remove_keyframe(self):
        pass

    def feather_reset_default(self):
        pass

    def feather_minus_stepper(self):
        pass

    def feather_plus_stepper(self):
        pass

    def feather_input_textfield(self):
        pass

    def feather_scroll(self):
        pass

    def roundness_add_keyframe(self):
        pass

    def roundness_remove_keyframe(self):
        pass

    def roundness_reset_default(self):
        pass

    def roundness_minus_stepper(self):
        pass

    def roundness_plus_stepper(self):
        pass

    def roundness_input_textfield(self):
        pass

    def roundness_scroll(self):
        pass

    def delete_mask_inspector(self):
        self.mask_action.tap_element("inspector_mask_1_right_button")



if __name__ == "__main__":
    mask = Mask()
    mask.open_mask_inspector()
    mask.add_mask()

    mask.invert_mask_toggle_on()
    mask.invert_mask_toggle_off()
    mask.scale_mask_link_off_width_height()
    mask.scale_mask_height_plus_stepper()
    mask.scale_mask_width_plus_stepper()





