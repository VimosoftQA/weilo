from Action import *
from bottombar import logger, error_handler_class
# from browser.NewFolder import *
# from browser.Sort import *


@error_handler_class
class BottomBar:
    def __init__(self):
        self.action = Action()
    #
    # def screenshot(self):
    #     pass

@error_handler_class
class Copy(BottomBar):
    def __init__(self):
        super().__init__()
    def copy_clip(self):
        self.action.click("copy_button")
        logger.info("tap copy button")
        element = self.action.find("클립 복사")
        if element:
            self.action.screenshot("Copy Clip")
            logger.info("completed copy clip")


class Paste(BottomBar):
    def __init__(self):
        super().__init__()

    def paste_clip(self):
        self.action.click("paste_button")
        self.action.screenshot("Paste Clip")
        logger.info("tap paste button")


class Dupliate(BottomBar):
    def __init__(self):
        super().__init__()

    def duplicate_clip(self):
        self.action.click("duplicate_button")
        self.action.screenshot("Duplicate Clip")
        logger.info("tap duplicate button")


class Link(BottomBar):
    def __init__(self):
        super().__init__()

    def link_clip(self):
        self.action.click("link_button")
        self.action.screenshot("Link Clip")
        logger.info("tap link button")


class FromNow(BottomBar):
    def __init__(self):
        super().__init__()

    def fromnow_clip(self):
        self.action.click("from_here_button")
        self.action.screenshot("From Now Clip")
        logger.info("tap from now button")


class UntilNow(BottomBar):
    def __init__(self):
        super().__init__()

    def until_now(self):
        self.action.click("until_here_button")
        self.action.screenshot("Until Now Clip")
        logger.info("tap until now button")


class Split(BottomBar):
    def __init__(self):
        super().__init__()

    def split_clip(self):
        self.action.click("split_button")
        self.action.screenshot("Split Clip")
        logger.info("tap split button")


class MoveHere(BottomBar):
    def __init__(self):
        super().__init__()

    def move_here_clip(self):
        self.action.click("move_here_button")
        self.action.screenshot("Move Here Clip")
        logger.info("tap move here button")


class Delete(BottomBar):
    def __init__(self):
        super().__init__()
    def delete_clip(self):
        self.action.click("delete_button")
        self.action.screenshot("Delete Clip")
        logger.info("tap delete button")


class Compound(BottomBar):
    def __init__(self):
        super().__init__()

    def compound_clip(self):
        self.action.click("compound_button")
        self.action.screenshot("Compound Clip")
        logger.info("tap compound button")

    def save_compound(self):
        self.action.click("완료")
        self.action.screenshot("Save Compound")
        logger.info("tap save compound button")

    def cancel_compound(self):
        self.action.click("취소")
        logger.info("tap cancel compound button")


class SaveClip(BottomBar):
    def __init__(self):
        super().__init__()

    # def create_new_folder(self):
    #     newfolder = CurrentNewFolder()
    #     newfolder.create_new_folder() #TODO 로그 내용 변경하기
    #
    # def sorting(self):
    #     sort = Sort()
    #     sort.sort_by_create_time()
    #     sort.sort_by_edit_time()
    #     sort.sort_by_name()


    def save_clip(self):
        self.action.click("save_clip_button")
        logger.info("tap save clip button")
        self.action.click("키보드 가리기")

    def save(self):
        self.action.click("저장")
        logger.info("tap save clip")


    def cancel(self):
        self.action.click("취소")
        logger.info("tap cancel save clip")


if __name__ == '__main__':

    bottombar = BottomBar()
    copy = Copy()
    copy.copy_clip()
    paste = Paste()
    paste.paste_clip()
    dupli = Dupliate()
    dupli.duplicate_clip()
    link = Link()
    link.link_clip()
    from_now = FromNow()
    from_now.fromnow_clip()
    until_now = UntilNow()
    until_now.until_now()
    split = Split()
    split.split_clip()
    move_here = MoveHere()
    move_here.move_here_clip()
    compound = Compound()
    compound.compound_clip()
    compound.save_compound()
    save_clip = SaveClip()
    # save_clip.create_new_folder()
    # save_clip.sorting()
    save_clip.save_clip()
    save_clip.save()
    delete_compound = Delete()
    delete_compound.delete_clip()





