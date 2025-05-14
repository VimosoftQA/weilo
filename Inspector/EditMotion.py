from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class EditMotionAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

class EditMotion:
    def __init__(self):
        self.edit_motion_action = EditMotionAction()

    def open_edit_motion_inspector(self):
        self.edit_motion_action.tap_element("inspector_edit_motion")
        self.edit_motion_action.logger.info("[Edit Motion] Open Edit Motion Inspector")

    def turn_on_reverse_toggle(self):
        self.edit_motion_action.tap_element("edit_motion_reverse_toggle_switch")
        self.edit_motion_action.logger.info("[Edit Motion] Turn on Reverse Toggle")

    def turn_off_reverse_toggle(self):
        self.edit_motion_action.tap_element("edit_motion_reverse_toggle_switch")
        self.edit_motion_action.logger.info("[Edit Motion] Turn off Reverse Toggle")

    def turn_on_stop_motion_toggle(self):
        self.edit_motion_action.tap_element("edit_motion_stop_motion_toggle_switch")
        self.edit_motion_action.logger.info("[Edit Motion] Turn on Stop Motion Toggle")

    def turn_off_stop_motion_toggle(self):
        self.edit_motion_action.tap_element("edit_motion_stop_motion_toggle_switch")
        self.edit_motion_action.logger.info("[Edit Motion] Turn off Stop Motion Toggle")

    def close_edit_motion_inspector(self):
        self.edit_motion_action.tap_element("inspector_edit_motion")
        self.edit_motion_action.logger.info("[Edit Motion] Close Edit Motion Inspector")

if __name__ == '__main__':
    edit_motion = EditMotion()
    edit_motion.open_edit_motion_inspector()
    edit_motion.turn_on_reverse_toggle()
    edit_motion.turn_off_reverse_toggle()
    edit_motion.turn_on_stop_motion_toggle()
    edit_motion.turn_off_stop_motion_toggle()
    edit_motion.close_edit_motion_inspector()
