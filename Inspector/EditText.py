from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import Inspector
import time

class EditTextAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # 아이템 ID로 탭하기
    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

    # 텍스트 필드에 값 입력하기
    def input_textfield(self,id,value):
        text_field = self.driver.find_element(By.ID, id)
        text_field.clear()
        text_field.send_keys(value)
        time.sleep(1)
        self.tap_element(id = "Hide keyboard")

class EditText:
    def __init__(self):
        self.edit_text_action = EditTextAction()

    # 텍스트 편집 인스펙터 열기
    def open_edit_text_inspector(self):
        self.edit_text_action.tap_element("inspector_text_edit")

    # 텍스트 필드 값 입력
    def edit_text_input_textfield(self,value):
        self.edit_text_action.input_textfield("text_edit_edit_text_text_view", value)
        self.edit_text_action.logger.info(f"[Edit Text] Edit Text Input Textfield : {value}")

    # 텍스트 편집 인스펙터 닫기
    def close_edit_text_inspector(self):
        self.edit_text_action.tap_element("inspector_text_edit")



if __name__ == '__main__':
    edit_text = EditText()
    edit_text.open_edit_text_inspector()
    edit_text.edit_text_input_textfield("안녕하세요 \n 반갑습니다")
    edit_text.close_edit_text_inspector()
