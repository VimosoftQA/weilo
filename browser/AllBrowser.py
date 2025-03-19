from Audio import *
from Text import *
from Graphic import *
from Effect import *
from Transition import *
from Voiceover import *


def AudioBrowser():

    audio = Audio()
    audio.open_audio_browser()

    bgm = BGM()
    bgm.tap_BGM_category()
    bgm.tap_BGM_sub_category()
    bgm.random_find_category()
    bgm.download_BGM_items()
    bgm.play_source_player()
    bgm.set_bookmark()

    sfx = SFX()
    sfx.tap_SFX_category()
    audio.close_audio_guide()
    sfx.tap_SFX_sub_category()
    sfx.random_find_category()
    sfx.download_SFX_items()
    sfx.set_bookmark()
    sfx.play_source_player()
    audio.close_audio_browser()


def TextBrowser():

    text = Text()
    text.open_Text_browser()
    text.tap_Text_category()
    text.random_find_category_asset()
    text.play_source_player()
    # text.text_double_tap() # 더블탭할 값이 있어야함
    text.close_Text_browser()


def GraphicBrowser():

    graphic = Graphic()
    graphic.open_graphic_browser()

    drawing = Drawing()
    drawing.open_drawing_popup()
    drawing.select_marker()
    drawing.test_drawing()

    pen = Pen()
    pen.open_pen_popup()
    pen.test_pen()

    sticker = Sticker()
    sticker.open_sticker_popup()
    sticker.tap_sticker_category()
    sticker.random_find_category()
    sticker.set_bookmark()
    sticker.play_source_player()

    frame = Frame()
    frame.open_frame_popup()
    frame.tap_frame_category()
    frame.random_find_category()
    frame.set_bookmark()
    frame.play_source_player()

    particle = Particle()
    particle.open_particle_popup()
    particle.tap_particle_category()
    particle.random_find_category()
    particle.set_bookmark()
    particle.play_source_player()

    stock = Stock()
    stock.open_stock_popup()
    stock.tap_stock_category()
    stock.random_find_category()
    stock.set_bookmark()
    stock.play_source_player()

    graphic.close_graphic_browser()


def EffectBrowser():
    effect = Effect()

    effect.open_effect_browser()

    video_effect = VideoEffect()
    video_effect.open_effect_browser()
    video_effect.tap_video_effect_sub_category()
    video_effect.random_find_category_asset()
    video_effect.video_effect_double_tap()
    video_effect.play_source_player()

    audio_effect = AudioEffect()
    audio_effect.tap_audio_effect_sub_category()
    audio_effect.random_find_category_asset()
    audio_effect.audio_effect_double_tap()
    audio_effect.play_source_player()

    effect.close_effect_browser()


def TransitionBrowser():
    transition = Transition()

    transition.open_transition_browser()
    transition.tap_Transition_category()
    transition.random_find_category_asset()
    transition.transition_double_tap()
    transition.play_source_player()
    transition.close_transition_browser()


def VoiceoverBrowser():
    voiceover = Voiceover()
    voiceover.tap_voiceover_button()
    voiceover.setting_voiceover()
    voiceover.back_setting_voiceover()
    voiceover.start_voiceover()
    voiceover.close_voiceover()


if __name__ == '__main__':
    AudioBrowser()
    TextBrowser()
    GraphicBrowser()
    EffectBrowser()
    TransitionBrowser()
    VoiceoverBrowser()



















