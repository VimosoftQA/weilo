from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from Inspector import driver, logger


class OpacityAction:
    def __init__(self):
        self.driver = driver()
        self.action = ActionChains(self.driver)
        # 인스펙터에서 '편집' 을 연다
        self.driver.find_element("edit_button").click()
        logger.info("[inspector] open edit inspector")

        # 편집 창에서 '불투명도 & 혼합' 을 연다
        self.driver.find_element("inspector_opacity_&_blending_container_view")
        logger.info("[inspector] open opacity & blending container")

    def tap_keyframe(self, id):
        self.driver.find_element(id).click()
        logger.info("[opacity & Blending] tap keyframe")

    def tap_stepper(self, id, n = 3):
        for _ in range(n):
            self.driver.find_element(id).click()
            replace_id = id.replace("opacity_&_blending", "").replace("button", "stepper")
            logger.info(f"[opacity & Blending] {replace_id}")

    def move_slider(self, id, horizontal_offset = 0.5):
        # 좌표를 쓰지 않고 비율로 조정해보기
        slider = self.driver.find_element(id)
        self.action.click_and_hold(slider).move_by_offset(horizontal_offset, 0).release().perform()
        logger.info("[opacity & Blending] move slider")

    def tap_blend_mode(self, id):
        # 드롭 다운 열기
        self.driver.find_element("id").click()
        logger.info("[opacity & Blending] open dropbox blend mode")

        
        

class Opacity:
    def __init__(self):
        self.driver = driver()
        self.opacity_action = OpacityAction()

    def open_opacity_view(self):
        driver.find_element("inspector_opacity_&_blending_container_view").click()
        logger.info("Opened Opacity & Blending view")

    def opacity_stepper(self, id):
        self.opacity_action.action(id)

    def opacity_input_text_field(self):
        pass

    def opacity_key_frame(self, id):
        self.opacity_action.tap_keyframe(id)

    def open_blend_mode(self,id):
        self.opacity_action.tap_blend_mode(id)



if __name__ == "__main__":
    oa = OpacityAction()

    move_slider_id = "opacity_&_blending_opacity_slider_handle"
    oa.move_slider(move_slider_id)
    oa.move_slider(move_slider_id, n = -30)

    blendmode_view = "opacity_&_blending_blend_mode_selected_container_view"
    oa.tap_blend_mode(blendmode_view)

    



