from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class TextFormatAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def tap_element(self,id):
        self.driver.find_element(by = By.ID,value = id).click()

    def capture_screenshot(self,route):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"screenshot_{route}_{timestamp}"
        self.driver.save_screenshot(f'screenshot/{screenshot_name}.png')

    def input_textfield(self, id, value):
        text_field = self.driver.find_element(By.ID, id)
        text_field.clear()
        text_field.send_keys(value)
        time.sleep(1)
        self.tap_element(id="Return")

    def tap_stepper(self, id, n=3):
        for _ in range(n):
            self.tap_element(id)
        replace_id = id.replace("button", "stepper")  # 로그의 가독성을 위해 ID 변경
        self.logger.info(f"[Text Format] {replace_id} : {n}")

    def move_slider(self, id, horizontal_offset=-10):
        slider = self.driver.find_element(by=By.ID, value=id)  # 슬라이더 ID가 있는지 확인
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform()  # 슬라이더의 위치 변경
        self.logger.info("[Text Format] move slider")

    # TODO 스크롤 내리는 동작도 구현해야함

class TextFormat:
    def __init__(self):
        self.text_format_action = TextFormatAction()

    def open_text_format_inspector(self):
        self.text_format_action.tap_element("inspector_text_format")
        self.text_format_action.logger.info("[Text Format] Open Text Format Inspector")

    def turn_on_toggle_individual_character_styling(self):
        self.text_format_action.tap_element("text_format_multi_switch")
        self.text_format_action.logger.info("[Text Format] Turn on Individual Character Styling")

    def turn_off_toggle_individual_character_styling(self):
        self.text_format_action.tap_element("text_format_multi_switch")
        self.text_format_action.logger.info("[Text Format] Turn on Individual Character Styling")

    def tap_select_all_button(self):
        self.text_format_action.tap_element("text_format_select_all_button")
        self.text_format_action.logger.info("[Text Format] Tap Select All Individual Character")

    def tap_first_word_in_text(self):
        self.text_format_action.tap_element("character_select_item_2")
        self.text_format_action.logger.info("[Text Format] Tap First Word in Text")

    def tap_text_preset_dropdown(self):
        self.text_format_action.tap_element("text_format_text_preset_dropdown")
        self.text_format_action.logger.info("[Text Format] Tap Text Preset Dropdown")

    def save_text_preset(self):
        self.text_format_action.tap_element("text_format_text_preset_button")
        self.text_format_action.logger.info("[Text Format] Save Text Preset")

    # 폰트 선택 및 폰트 브라우저 탐색은 따로 빼서 작업함

    def add_keyframe_font_size(self):
        self.text_format_action.tap_element("text_format_font_size_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Font Size")

    def remove_keyframe_font_size(self):
        self.text_format_action.tap_element("text_format_font_size_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Font Size")

    def reset_default_font_size(self):
        self.text_format_action.tap_element("text_format_font_size_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Font Size")

    def font_size_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_font_size_minus_button")
        self.text_format_action.logger.info("[Text Format] Font Size Minus Stepper")

    def font_size_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_font_size_plus_button")
        self.text_format_action.logger.info("[Text Format] Font Size Plus Stepper")

    def font_size_input_text_field(self,value):
        self.text_format_action.input_textfield("text_format_font_size_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Font Size Input TextField : {value}")

    def font_size_infinite_roller(self):
        pass


    def tap_alignment(self):
        alignment = {
            1 : "horizontal_left_alignment",
            2 : "horizontal_center_alignment",
            3 : "horizontal_right_alignment",
            4 : "vertical_left_alignment",
            5 : "vertical_center_alignment",
            6 : "vertical_right_alignment"
        }
        for key, value in alignment.items():
            self.text_format_action.tap_element(f"text_format_alignment_segment_{key}")
            self.text_format_action.logger.info(f"[Text Format] Tap Alignment : {value}")

    def tap_emphasis(self):
        emphasis = {
            1 : "italic",
            2 : "bold",
            3 : "underline",
            4 : "strike"
        }
        for key, value in emphasis.items():
            self.text_format_action.tap_element(f"text_format_emphasis_button_list_button_{key}")
            self.text_format_action.logger.info(f"[Text Format] Tap Emphasis : {value}")

    def add_keyframe_character_spacing(self):
        self.text_format_action.tap_element("text_format_character_spacing_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Character Spacing")

    def remove_keyframe_character_spacing(self):
        self.text_format_action.tap_element("text_format_character_spacing_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Character Spacing")

    def reset_default_character_spacing(self):
        self.text_format_action.tap_element("text_format_character_spacing_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Character Spacing")

    def character_spacing_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_character_spacing_minus_button")
        self.text_format_action.logger.info("[Text Format] Minus Stepper Character Spacing")

    def character_spacing_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_character_spacing_plus_button")
        self.text_format_action.logger.info("[Text Format] Plus Stepper Character Spacing")

    def character_spacing_input_text_field(self,value):
        self.text_format_action.input_textfield("text_format_character_spacing_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Character Spacing Input TextField : {value}")

    def character_spacing_move_slider(self):
        self.text_format_action.move_slider("text_format_character_spacing_slider_handle")
        self.text_format_action.logger.info("[Text Format] Character Spacing Move Slider Handle")

    def add_keyframe_line_spacing(self):
        self.text_format_action.tap_element("text_format_line_spacing_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Line Spacing")

    def remove_keyframe_line_spacing(self):
        self.text_format_action.tap_element("text_format_line_spacing_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Line Spacing")

    def reset_default_line_spacing(self):
        self.text_format_action.tap_element("text_format_line_spacing_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Line Spacing")

    def line_spacing_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_line_spacing_minus_button")
        self.text_format_action.logger.info("[Text Format] Line Spacing Minus Stepper")

    def line_spacing_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_line_spacing_plus_button")
        self.text_format_action.logger.info("[Text Format] Line Spacing Plus Stepper")

    def line_spacing_input_text_field(self,value):
        self.text_format_action.input_textfield("text_format_line_spacing_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Line Spacing Input TextField : {value}")

    def line_spacing_move_slider(self):
        self.text_format_action.move_slider("text_format_line_spacing_slider_handle")
        self.text_format_action.logger.info("[Text Format] Line Spacing Move Slider Handle")

    def activate_color_fill_checkbox(self):
        self.text_format_action.tap_element("text_format_fill_checkbox")
        self.text_format_action.logger.info("[Text Format] Activate Color Fill Checkbox")

    def deactivate_color_fill_checkbox(self):
        self.text_format_action.tap_element("text_format_fill_checkbox")
        self.text_format_action.logger.info("[Text Format] Deactivate Color Fill Checkbox")

    def add_keyframe_color_fill(self):
        self.text_format_action.tap_element("text_format_fill_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Color Fill Keyframe")

    def remove_keyframe_color_fill(self):
        self.text_format_action.tap_element("text_format_fill_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Color Fill Keyframe")

    def tap_color_fill_preview(self):
        self.text_format_action.tap_element("text_format_fill_color_preview")
        self.text_format_action.logger.info("[Text Format] Tap Color Fill Preview")

    def tap_color_fill_spoid_button(self):
        self.text_format_action.tap_element("text_format_fill_spoid_button")
        self.text_format_action.logger.info("[Text Format] Tap Color Fill Spoid Button")

    def activate_text_background_checkbox(self):
        self.text_format_action.tap_element("text_format_text_background_checkbox")
        self.text_format_action.logger.info("[Text Format] Activate Text Background Checkbox")

    def deactivate_text_background_checkbox(self):
        self.text_format_action.tap_element("text_format_text_background_checkbox")
        self.text_format_action.logger.info("[Text Format] Deactivate Text Background Checkbox")

    def add_keyframe_text_background_color(self):
        self.text_format_action.tap_element("text_format_text_background_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Text Background Keyframe")

    def remove_keyframe_text_background_color(self):
        self.text_format_action.tap_element("text_format_text_background_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Text Background Keyframe")

    def tap_text_background_color_preview(self):
        self.text_format_action.tap_element("text_format_text_background_color_preview")
        self.text_format_action.logger.info("[Text Format] Tap Text Background Color Preview")

    def tap_text_background_spoid_button(self):
        self.text_format_action.tap_element("text_format_text_background_spoid_button")
        self.text_format_action.logger.info("[Text Format] Tap Text Background Spoid Button")

    def add_keyframe_text_background_width(self):
        self.text_format_action.tap_element("text_format_text_background_width_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Text Background Width Keyframe")

    def remove_keyframe_text_background_width(self):
        self.text_format_action.tap_element("text_format_text_background_width_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Text Background Width Keyframe")

    def reset_default_text_background_width(self):
        self.text_format_action.tap_element("text_format_text_background_width_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Text Background Width")

    def text_background_width_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_text_background_width_minus_button")
        self.text_format_action.logger.info("[Text Format] Text Background Width Minus Stepper")

    def text_background_width_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_text_background_width_plus_button")
        self.text_format_action.logger.info("[Text Format] Text Background Width Plus Stepper")

    def text_background_width_input_textfield(self,value):
        self.text_format_action.input_textfield("text_format_text_background_width_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Text Background Width Input TextField : {value}")

    def text_background_width_slider(self):
        self.text_format_action.move_slider("text_format_text_background_width_slider_handle")
        self.text_format_action.logger.info("[Text Format] Text Background Width Move Slider Handle")

    def add_keyframe_text_background_height(self):
        self.text_format_action.tap_element("text_format_text_background_height_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Text Background Height Keyframe")

    def remove_keyframe_text_background_height(self):
        self.text_format_action.tap_element("text_format_text_background_height_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Text Background Height Keyframe")

    def reset_default_text_background_height(self):
        self.text_format_action.tap_element("text_format_text_background_height_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Text Background Height")

    def text_background_height_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_text_background_height_minus_button")
        self.text_format_action.logger.info("[Text Format] Text Background Height Minus Stepper")

    def text_background_height_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_text_background_height_plus_button")
        self.text_format_action.logger.info("[Text Format] Text Background Height Plus Stepper")

    def text_background_height_input_textfield(self,value):
        self.text_format_action.input_textfield("text_format_text_background_height_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Text Background Height Input TextField : {value}")

    def text_background_height_slider(self):
        self.text_format_action.move_slider("text_format_text_background_height_slider_handle")
        self.text_format_action.logger.info("[Text Format] Text Background Height Move Slider Handle")

    def add_keyframe_text_background_roundness(self):
        self.text_format_action.tap_element("text_format_text_background_roundness_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Text Background Roundness Keyframe")

    def remove_keyframe_text_background_roundness(self):
        self.text_format_action.tap_element("text_format_text_background_roundness_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Text Background Roundness Keyframe")

    def reset_default_text_background_roundness(self):
        self.text_format_action.tap_element("text_format_text_background_roundness_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Text Background Roundness")

    def text_background_roundness_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_text_background_roundness_minus_button")
        self.text_format_action.logger.info("[Text Format] Text Background Roundness Minus Stepper")

    def text_background_roundness_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_text_background_roundness_plus_button")
        self.text_format_action.logger.info("[Text Format] Text Background Roundness Plus Stepper")

    def text_background_roundness_input_textfield(self,value):
        self.text_format_action.input_textfield("text_format_text_background_roundness_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Text Background Roundness Input TextField : {value}")

    def text_background_roundness_slider(self):
        self.text_format_action.move_slider("text_format_text_background_roundness_slider_handle")
        self.text_format_action.logger.info("[Text Format] Text Background Roundness Move Slider Handle")

    def activate_text_stroke(self):
        self.text_format_action.tap_element("text_format_stroke_1_checkbox")
        self.text_format_action.logger.info("[Text Format] Activate Text Stroke")

    def deactivate_text_stroke(self):
        self.text_format_action.tap_element("text_format_stroke_1_checkbox")
        self.text_format_action.logger.info("[Text Format] Deactivate Text Stroke")

    def delete_text_stroke(self):
        self.text_format_action.tap_element("text_format_stroke_1_delete_button")
        self.text_format_action.logger.info("[Text Format] Delete Text Stroke")

    def add_keyframe_text_stroke(self):
        self.text_format_action.tap_element("text_format_stroke_1_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Text Stroke")

    def remove_keyframe_text_stroke(self):
        self.text_format_action.tap_element("text_format_stroke_1_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Text Stroke")

    def tap_text_stroke_color_preview(self):
        self.text_format_action.tap_element("text_format_stroke_1_color_preview")
        self.text_format_action.logger.info("[Text Format] Tap Text Stroke Color Preview")

    def tap_text_stroke_color_spoid_button(self):
        self.text_format_action.tap_element("text_format_stroke_1_spoid_button")
        self.text_format_action.logger.info("[Text Format] Tap Text Stroke Color Spoid")

    def add_keyframe_text_stroke_width(self):
        self.text_format_action.tap_element("text_format_stroke_1_stroke_outline_width_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Text Stroke Outline Width")

    def remove_keyframe_text_stroke_width(self):
        self.text_format_action.tap_element("text_format_stroke_1_stroke_outline_width_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Text Stroke Outline Width")

    def reset_default_text_stroke_width(self):
        self.text_format_action.tap_element("text_format_stroke_1_stroke_outline_width_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Text Stroke Width")

    def text_stroke_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_stroke_1_stroke_outline_width_plus_button")
        self.text_format_action.logger("[Text Format] Text Stroke Plus Stepper")

    def text_stroke_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_stroke_1_stroke_outline_width_minus_button")
        self.text_format_action.logger("[Text Format] Text Stroke Minus Stepper")

    def text_stroke_input_textfield(self,value):
        self.text_format_action.input_textfield("text_format_stroke_1_stroke_outline_width_value_text_field", value)
        self.text_format_action.logger.info(f"[Text Format] Text Stroke Input TextField : {value}")

    def add_new_text_stroke(self):
        self.text_format_action.tap_element("text_format_add_new_stroke_button")
        self.text_format_action.logger("[Text Format] Add New Text Stroke")

    def activate_text_shadow_checkbox(self):
        self.text_format_action.tap_element("text_format_shadow_1_checkbox")
        self.text_format_action.logger.info("[Text Format] Activate Text Shadow Checkbox")

    def deactivate_text_shadow_checkbox(self):
        self.text_format_action.tap_element("text_format_shadow_1_checkbox")
        self.text_format_action.logger.info("[Text Format] Deactivate Text Shadow Checkbox")

    def deleted_text_shadow(self):
        self.text_format_action.tap_element("text_format_shadow_1_delete_button")
        self.text_format_action.logger.info("[Text Format] Deleted Text Shadow")

    def add_keyframe_text_shadow(self):
        self.text_format_action.tap_element("text_format_shadow_1_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Text Shadow Button")

    def remove_keyframe_text_shadow(self):
        self.text_format_action.tap_element("text_format_shadow_1_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Text Shadow Button")

    def tap_color_text_shadow_preview(self):
        self.text_format_action.tap_element("text_format_shadow_1_color_preview")
        self.text_format_action.logger.info("[Text Format] Tap Text Shadow Color Preview")

    def tap_color_text_shadow_spoid_button(self):
        self.text_format_action.tap_element("text_format_shadow_1_spoid_button")
        self.text_format_action.logger.info("[Text Format] Tap Text Shadow Spoid Button")

    def add_keyframe_text_blur_radius(self):
        self.text_format_action.tap_element("text_format_shadow_1_blur_radius_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Text Blur Radius")

    def remove_keyframe_text_blur_radius(self):
        self.text_format_action.tap_element("text_format_shadow_1_blur_radius_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Text Blur Radius")

    def reset_default_text_blur_radius(self):
        self.text_format_action.tap_element("text_format_shadow_1_blur_radius_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Text Blur Radius")

    def text_shadow_blur_radius_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_shadow_1_blur_radius_plus_button")
        self.text_format_action.logger.info("[Text Format] Text Shadow Blur Radius Plus Stepper")

    def text_shadow_blur_radius_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_shadow_1_blur_radius_minus_button")
        self.text_format_action.logger.info("[Text Format] Text Shadow Blur Radius Minus Stepper")

    def text_shadow_blur_radius_input_textfield(self,value):
        self.text_format_action.input_textfield("text_format_shadow_1_blur_radius_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Text Shadow Blur Radius Input TextField : {value}")

    def text_shadow_blur_radius_slider(self):
        self.text_format_action.move_slider("text_format_shadow_1_blur_radius_slider_handle")

    def add_keyframe_text_shadow_angle(self):
        self.text_format_action.tap_element("text_format_shadow_1_angle_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Text Shadow Angle")

    def remove_keyframe_text_shadow_angle(self):
        self.text_format_action.tap_element("text_format_shadow_1_angle_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Text Shadow Angle")

    def reset_default_text_shadow_angle(self):
        self.text_format_action.tap_element("text_format_shadow_1_angle_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Text Shadow Angle")

    def text_shadow_angle_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_shadow_1_angle_plus_button")
        self.text_format_action.logger.info("[Text Format] Text Shadow Angle Plus Stepper")

    def text_shadow_angle_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_shadow_1_angle_minus_button")
        self.text_format_action.logger.info("[Text Format] Text Shadow Angle Minus Stepper")

    def text_shadow_angle_input_textfield(self,value):
        self.text_format_action.input_textfield("text_format_shadow_1_angle_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Text Shadow Angle Input TextField : {value}")

    # angle stepper 와 중복된 ID 사용
    # def text_shadow_angle_15_plus_button(self):
    #     self.text_format_action.tap_element("text_format_shadow_1_angle_minus_button")
    #
    # def text_shadow_angle_15_minus_button(self):
    #     pass

    def add_keyframe_text_shadow_distance(self):
        self.text_format_action.tap_element("text_format_shadow_1_distance_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Add Keyframe Text Shadow Distance")

    def remove_keyframe_text_shadow_distance(self):
        self.text_format_action.tap_element("text_format_shadow_1_distance_key_frame_iobutton")
        self.text_format_action.logger.info("[Text Format] Remove Keyframe Text Shadow Distance")

    def reset_default_text_shadow_distance(self):
        self.text_format_action.tap_element("text_format_shadow_1_distance_default_button")
        self.text_format_action.logger.info("[Text Format] Reset Default Text Shadow Distance")

    def text_shadow_distance_plus_stepper(self):
        self.text_format_action.tap_stepper("text_format_shadow_1_distance_plus_button")
        self.text_format_action.logger.info("[Text Format] Text Shadow Distance Plus Stepper")

    def text_shadow_distance_minus_stepper(self):
        self.text_format_action.tap_stepper("text_format_shadow_1_distance_minus_button")
        self.text_format_action.logger.info("[Text Format] Text Shadow Distance Minus Stepper")

    def text_shadow_distance_input_textfield(self,value):
        self.text_format_action.input_textfield("text_format_shadow_1_distance_value_text_field",value)
        self.text_format_action.logger.info(f"[Text Format] Text Shadow Distance Input TextField : {value}")

    def add_new_text_shadow(self):
        self.text_format_action.tap_element("text_format_add_new_shadow_button")
        self.text_format_action.logger.info("[Text Format] Add New Text Shadow")














if __name__ == '__main__':
    text_format = TextFormat()
    text_format.open_text_format_inspector()
