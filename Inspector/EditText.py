from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class EditTextAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    def input_textfield(self,id,value):
        text_field = self.driver.find_element(By.ID, id)
        text_field.clear()
        text_field.send_keys(value)
        time.sleep(1)
        self.tap_element(id = "Hide keyboard")

class EditText:
    def __init__(self):
        self.edit_text_action = EditTextAction()

    def open_edit_text_inspector(self):
        self.edit_text_action.tap_element("inspector_text_edit")

    def edit_text_input_textfield(self,value):
        self.edit_text_action.input_textfield("text_edit_edit_text_text_view", value)
        self.edit_text_action.logger.info(f"[Edit Text] Edit Text Input Textfield : {value}")

    def close_edit_text_inspector(self):
        self.edit_text_action.tap_element("inspector_text_edit")



if __name__ == '__main__':
    edit_text = EditText()
    edit_text.open_edit_text_inspector()
    edit_text.edit_text_input_textfield("안녕하세요 \n 반갑습니다")
    edit_text.close_edit_text_inspector()
