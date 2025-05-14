from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class TrackingAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def tap_element(self, id):
        self.driver.find_element(by=By.ID, value=id).click()

    def open_drop_down(self, id):
        self.driver.find_element(by=By.ID, value=id).click()

class Tracking:
    def __init__(self):
        self.tracking_action = TrackingAction()

    def open_tracking_inspector(self):
        self.tracking_action.tap_element("inspector_tracking")
        self.tracking_action.logger.info("[Tracking] Open Tracking Inspector")

    def select_tracker_dropdown(self):
        self.tracking_action.tap_element("tracking_select_tracker_dropdown")
        self.tracking_action.tap_element("tracking_select_tracker_table_view")  # 트래커의 드롭다운에서 트래커 선택
        self.tracking_action.logger.info("[Tracking] Select Tracker Dropdown")

    def tracking_option_position(self):
        self.tracking_action.tap_element("tracking_select_tracker_position;position_&_scale_radio1")
        self.tracking_action.logger.info("[Tracking] Select Tracker Position")

    def tracking_option_position_scale(self):
        self.tracking_action.tap_element("tracking_select_tracker_position;position_&_scale_radio2")
        self.tracking_action.logger.info("[Tracking] Select Tracker Position & Scale")

    # 트래커로 이동 후 되돌아오는 동작은 구현되어있지 않음
    def move_to_tracker_inspector(self):
        self.tracking_action.tap_element("tracking_select_tracker_button")
        self.tracking_action.logger.info("[Tracking] Move to Tracker Inspector")

    def close_tracking_inspector(self):
        self.tracking_action.tap_element("inspector_tracking")
        self.tracking_action.logger.info("[Tracking] Close Tracking Inspector")


if __name__ == "__main__":
    tracking = Tracking()
    tracking.move_to_tracker_inspector()




