from mymodules.buttons_images import Img
from mymodules.action.dial import action

class Menu1(object):
    pass
    @staticmethod
    def on_button1_clicked():
        Img.image1.set_from_file(action.menu_img_11)
        Img.image2.set_from_file(action.menu_img_2)
        Img.image3.set_from_file(action.menu_img_3)
        Img.image4.set_from_file(action.menu_img_4)
        Img.image5.set_from_file(action.menu_img_5)
        Img.image6.set_from_file(action.menu_img_6)

        from mymodules.categories.somesome import menu1
        menu1.load()