from appium import webdriver
from appium.options.ios import XCUITestOptions
import json
import logging
from datetime import datetime
from functools import wraps
import os

def setup_logger(log_dir = 'logs'): # 로거 셋업
    logger = logging.getLogger()
    logger.setLevel(logging.INFO) #INFO 로 로그 레벨 설정

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        today = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        log_path = os.path.join(log_dir, f"{today}.logs")
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

def initialize_driver(): # 자동화에 필요한 driver를 초기화
    with open('capabilities.json', 'r', encoding='utf-8') as f:
        capabilities = json.load(f)

    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

    logger.info("initialize appium driver settings")
    return driver


def error_handler_class(cls):
    for name, method in cls.__dict__.items(): # 클래스의 모든 메소드를 순회
        if callable(method) and not name.startswith('__'): # 일반 메소드만 처리 (매직 메소드 제외)
            setattr(cls, name, error_handler(method)) # 각 메소드에 에러 핸들링 래퍼 적용
    return cls

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #TODO 에러 메세지 조금 더 상세하게 변경해보기
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper




logger = setup_logger()
driver = initialize_driver()
__all__ = ['driver']
