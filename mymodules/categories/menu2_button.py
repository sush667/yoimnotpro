from mymodules.buttons_images import Img
from mymodules.action.dial import action

class Menu2(object):
    pass
    @staticmethod
    def on_button2_clicked():
        Img.image1.set_from_file(action.menu_img_1)
        Img.image2.set_from_file(action.menu_img_22)
        Img.image3.set_from_file(action.menu_img_3)
        Img.image4.set_from_file(action.menu_img_4)
        Img.image5.set_from_file(action.menu_img_5)
        Img.image6.set_from_file(action.menu_img_6)

        from mymodules.categories.somesome import menu2
        menu2.load()