import random
from Action import *
from automation import logger, error_handler_class
import time

def choice_random(item : dict , n = 1):
    sampling = random.choice(list(item.keys()))
    logger.info(f"Choice Random Category : {item.get(sampling)}")
    return item.get(sampling), sampling #카테고리 명, 카테고리 오리지날이름


def find_category(category_original_name):
    action = Action()

    # 초기 위치로 이동 TODO 초기 위치로 이동을 안한다... 어떻게 해야하지
    # 페이지에 찾으려는 값이 있으면 발견해서 넘어가기
    # 페이지에 찾으려는 값이 없으면 new 로 돌아가기

    while True:
        try: # 서브 카테고리명 발견 시 클릭하기
            if action.find(category_original_name):
                action.click(category_original_name)
                break

        except: # 서브 카테고리명이 보이지 않는 경우
            action.swipe(200, 134, 469, 134) #일단 맨 처음 NEW 로 이동

            if action.find("browser_new_ic"): # NEW를 찾으면
                action.click("browser_new_ic")
                logger.info(f"[Audio > SFX] 현재 서브 카테고리 목록에서 찾을 수 없어 NEW 카테고리로 돌아감")
                break


            # TODO 다시 랜덤으로 선택된 서브 카테고리로 넘어가는 작업은 추후 진행 (굉장히 복잡해짐)
                # action.swipe(469, 134, 200, 134)

            #     while True: # 다시 새로운
            #         try:
            #             if action.find(category_original_name):
            #                 action.click(category_original_name)
            #                 break
            #         except:
            #             action.swipe(469, 134, 200, 134)
            #     break
            # else:
            #     action.swipe(200, 134, 469, 134)



if __name__ == '__main__':
    lis =["일상", "Vlog", "카페","키즈 & 동물", "여행", "사랑", "웨딩 & 프로포즈", "예능","광고", "영화","게임", "시즌", "뷰티 & 패션", "파티 & 클럽"]

    pick = choice_random(lis)
    print(pick)
    find_category(pick)