import random
from Action import Action
from automation import logger, error_handler_class

def choice_random(lis , n = 1):
    sampling = random.sample(lis,n)[0]
    logger.info(f"Choice Random Category : {sampling}")
    return sampling


def find_category(category):  # 랜덤으로 선택된 카테고리를 선택한다.
    # 원하는 카테고리가 있을 때까지 계속 찾는다.
    action = Action()
    while True:
        try:
            if action.find(category):
                action.click(category)
                break
        except:
            action.swipe(120, 134, 58, 134)


if __name__ == '__main__':
    lis =["일상", "Vlog", "카페","키즈 & 동물", "여행", "사랑", "웨딩 & 프로포즈", "예능","광고", "영화","게임", "시즌", "뷰티 & 패션", "파티 & 클럽"]

    pick = choice_random(lis)
    print(pick)
    find_category(pick)