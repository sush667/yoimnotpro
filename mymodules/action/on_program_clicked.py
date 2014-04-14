import os
from mymodules.buttons_images import Img
from mymodules.action.dial import dial
from mymodules.categories.menu6_button import Menu6
from mymodules.categories.menu2_button import Menu2
from mymodules.categories.menu1_button import Menu1
from mymodules.action.dial import SetToolTip, action

class OPC:

    @staticmethod
    def on_sevenzip_clicked(self):
        if os.path.isfile("/usr/bin/7zFM"):
            os.system('pacman -Rdd p7zip --noconfirm')
            if not os.path.isfile("/usr/bin/7zFM"):
                Img.sevenzip_img.set_from_file(action.gtk_no)
                dial('7zip', action.remove_it)
                Menu6.sevenzip.set_tooltip_text(format(SetToolTip('7-zip', action.not_here, action.install_it)))
        else:
            os.system('pacman -S p7zip --noconfirm')
            if os.path.isfile("/usr/bin/7zFM"):
                Img.sevenzip_img.set_from_file(action.gtk_yes)
                dial('7zip', action.installed)
                Menu6.sevenzip.set_tooltip_text(format(SetToolTip('7-zip', action.installed, action.remove_it)))

    @staticmethod
    def on_imagemagick_clicked(self):
        if os.path.isfile("/usr/bin/convert"):
            os.system('pacman -Rdd imagemagick --noconfirm')
            if not os.path.isfile("/usr/bin/convert"):
                Img.imagemagick_img.set_from_file(action.gtk_no)
                dial('ImageMagick', action.remove_it)
                Menu2.imagemagick.set_tooltip_text(format(SetToolTip('imageMagick', action.not_here, action.install_it)))
        else:
            os.system('pacman -S imagemagick --noconfirm')
            if os.path.isfile("/usr/bin/convert"):
                Img.imagemagick_img.set_from_file(action.gtk_yes)
                dial('ImageMagick', action.installed)
                Menu2.imagemagick.set_tooltip_text(format(SetToolTip('imageMagick', action.installed, action.remove_it)))
 
    @staticmethod
    def on_openjdk_clicked(self):
        if os.path.exists("/etc/java-7-openjdk/"):
            os.system('pacman -R jre7-openjdk --noconfirm')
            if not os.path.exists("/etc/java-7-openjdk/"):
                Img.openjdk_img.set_from_file(action.gtk_no)
                dial('OpenJDK', action.remove_it)
                Menu1.openjdk.set_tooltip_text(format(SetToolTip('openJDK', action.not_here, action.install_it)))
        else:
            os.system('pacman -S jre7-openjdk --noconfirm')
            if os.path.exists("/etc/java-7-openjdk/"):
                Img.openjdk_img.set_from_file(action.gtk_yes)
                dial('OpenJDK', action.installed)
                Menu1.openjdk.set_tooltip_text(format(SetToolTip('openJDK', action.installed, action.remove_it)))