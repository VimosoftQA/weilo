from automation import logger, error_handler_class
from Action import Action
import time

@error_handler_class
class SourcePlayer:
    def __init__(self):
        self.action = Action()

    def tap_prev_frame_button(self , n = 5):
        for _ in range(n):
            self.action.click("source_player_prev_frame_button")
            logger.info(f"[Source Player] Tap Prev Frame Button")

    def tap_next_frame_button(self , n = 5):
        for _ in range(n):
            self.action.click("source_player_next_frame_button")
            logger.info(f"[Source Player] Tap Next Frame Button")

    def tap_add_button(self):
        self.action.click("source_player_add_button")
        logger.info(f"[Source Player] Tap Add Button")

    def tap_play_button(self):
        self.action.click("source_player_play_button")
        time.sleep(5)
        logger.info(f"[Source Player] Tap Play Button")

    def tap_reset_button(self):
        self.action.click("source_player_time_reset_button")

    def tap_screenshot(self):
        self.action.screenshot("Source Player")

if __name__ == "__main__":
    source_player = SourcePlayer()
    source_player.tap_next_frame_button()
    source_player.tap_prev_frame_button()
    source_player.tap_play_button()
    source_player.tap_reset_button()
    source_player.tap_add_button()

