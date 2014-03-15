import os
from mymodules.action.find_program import Find as find
from mymodules.buttons_images import Img
from mymodules.action.dial import dial
from mymodules.categories.menu7_button import Menu7
from mymodules.categories.menu6_button import Menu6
from mymodules.categories.menu5_button import Menu5
from mymodules.categories.menu4_button import Menu4
from mymodules.categories.menu3_button import Menu3
from mymodules.categories.menu2_button import Menu2
from mymodules.categories.menu1_button import Menu1

class OPC:
    # menu 7 button actions
    @staticmethod
    def on_geany__clicked(self):
        if os.path.isfile(find.program['geany']):
            os.system('pacman -R geany --noconfirm')
            if not os.path.isfile(find.program['geany']):
                Img.geany__img.set_from_file('./categories/gtk-no.png')
                dial('Geany','2')
                Menu7.geany_.set_tooltip_text("Geany is not installed.\nClick to install it.")
        else:
            os.system('pacman -S geany --noconfirm')
            if os.path.isfile(find.program['geany']):
                Img.geany__img.set_from_file('./categories/gtk-yes.png')
                dial('Geany','1')
                Menu7.geany_.set_tooltip_text("Geany is installed.\nClick to remove it.")

    @staticmethod
    def on_blender__clicked(self):
        if os.path.isfile(find.program['blender']):
            os.system('pacman -R blender --noconfirm')
            if not os.path.isfile(find.program['blender']):
                Img.blender__img.set_from_file('./categories/gtk-no.png')
                dial('Blender','2')
                Menu7.blender_.set_tooltip_text("Blender is not installed.\nClick to install it.")
        else:
            os.system('pacman -S blender --noconfirm')
            if os.path.isfile(find.program['blender']):
                Img.blender__img.set_from_file('./categories/gtk-yes.png')
                dial('Blender','1')
                Menu7.blender_.set_tooltip_text("Blender is installed.\nClick to remove it.")

    @staticmethod
    def on_ninja_ide__clicked(self):
        if os.path.isfile(find.program['ninja-ide']):
            os.system('pacman -R ninja-ide --noconfirm')
            if not os.path.isfile(find.program['ninja-ide']):
                Img.ninja_ide__img.set_from_file('./categories/gtk-no.png')
                dial('Ninja-IDE','2')
                Menu7.ninja_ide_.set_tooltip_text("Ninja-IDE is not installed.\nClick to install it.")

        else:
            os.system('pacman -S ninja-ide --noconfirm')
            if os.path.isfile(find.program['ninja-ide']):
                Img.ninja_ide__img.set_from_file('./categories/gtk-yes.png')
                dial('Ninja-IDE','1')
                Menu7.ninja_ide_.set_tooltip_text("Ninja-IDE is installed.\nClick to remove it.")

    @staticmethod
    def on_glade__clicked(self):
        if os.path.isfile(find.program['glade']):
            os.system('pacman -R glade --noconfirm')
            if not os.path.isfile(find.program['glade']):
                Img.glade__img.set_from_file('./categories/gtk-no.png')
                dial('Glade','2')
                Menu7.glade_.set_tooltip_text("Glade is not installed.\nClick to install it.")
        else:
            os.system('pacman -S glade --noconfirm')
            if os.path.isfile(find.program['glade']):
                Img.glade__img.set_from_file('./categories/gtk-yes.png')
                dial('Glade','1')
                Menu7.glade_.set_tooltip_text("Glade is installed.\nClick to remove it.")

    @staticmethod
    def on_audacious__clicked(self):
        if os.path.isfile(find.program['audacious']):
            os.system('pacman -R audacious --noconfirm')
            if not os.path.isfile(find.program['audacious']):
                Img.audacious__img.set_from_file('./categories/gtk-no.png')
                dial('Audacious','2')
                Menu7.audacious_.set_tooltip_text("Audacious is not installed.\nClick to install it.")

        else:
            os.system('pacman -S audacious --noconfirm')
            if os.path.isfile(find.program['audacious']):
                Img.audacious__img.set_from_file('./categories/gtk-yes.png')
                dial('Audacious','1')
                Menu7.audacious_.set_tooltip_text("Audacious is installed.\nClick to remove it.")

    @staticmethod
    def on_gimp__clicked(self):
        if os.path.isfile(find.program['gimp']):
            os.system('pacman -R gimp --noconfirm')
            if not os.path.isfile(find.program['gimp']):
                Img.gimp__img.set_from_file('./categories/gtk-no.png')
                dial('Gimp','2')
                Menu7.gimp_.set_tooltip_text("Gimp is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gimp --noconfirm')
            if os.path.isfile(find.program['gimp']):
                Img.gimp__img.set_from_file('./categories/gtk-yes.png')
                dial('Gimp','1')
                Menu7.gimp_.set_tooltip_text("GIMP is installed.\nClick to remove it.")

    @staticmethod
    def on_evince__clicked(self):
        if os.path.isfile(find.program['evince']):
            os.system('pacman -R evince --noconfirm')
            if not os.path.isfile(find.program['evince']):
                Img.evince__img.set_from_file('./categories/gtk-no.png')
                dial('Evince','2')
                Menu7.evince_.set_tooltip_text("Evince is not installed.\nClick to install it.")
        else:
            os.system('pacman -S evince --noconfirm')
            if os.path.isfile(find.program['evince']):
                Img.evince__img.set_from_file('./categories/gtk-yes.png')
                dial('Evince','1')
                Menu7.evince_.set_tooltip_text("Evince is installed.\nClick to remove it.")

    @staticmethod
    def on_xfburn__clicked(self):
        if os.path.isfile(find.program['xfburn']):
            os.system('pacman -R xfburn --noconfirm')
            if not os.path.isfile(find.program['xfburn']):
                Img.xfburn__img.set_from_file('./categories/gtk-no.png')
                dial('Xfburn','2')
                Menu7.xfburn_.set_tooltip_text("Xfburn is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xfburn --noconfirm')
            if os.path.isfile(find.program['xfburn']):
                Img.xfburn__img.set_from_file('./categories/gtk-yes.png')
                dial('Xfburn','1')
                Menu7.xfburn_.set_tooltip_text("Xfburn is installed.\nClick to remove it.")

    @staticmethod
    def on_flashplayer__clicked(self):
        if os.path.isfile(find.program['flash-player']):
            os.system('pacman -R flashplugin --noconfirm')
            if not os.path.isfile(find.program['flash-player']):
                Img.flashplayer__img.set_from_file('./categories/gtk-no.png')
                dial('Adobe Flashplayer','2')
                Menu7.flashplayer_.set_tooltip_text("Flashplayer is not installed.\nClick to install it.")
        else:
            os.system('pacman -S flashplugin --noconfirm')
            if os.path.isfile(find.program['flash-player']):
                Img.flashplayer__img.set_from_file('./categories/gtk-yes.png')
                dial('Adobe Flashplayer','1')
                Menu7.flashplayer_.set_tooltip_text("Flashplayer is installed.\nClick to remove it.")

    @staticmethod
    def on_openshot__clicked(self):
        if os.path.isfile(find.program['openshot']):
            os.system('pacman -R openshot --noconfirm')
            if not os.path.isfile(find.program['openshot']):
                Img.openshot__img.set_from_file('./categories/gtk-no.png')
                dial('OpenShot','2')
                Menu7.openshot_.set_tooltip_text("Openshot is not installed.\nClick to install it.")
        else:
            os.system('pacman -S openshot --noconfirm')
            if os.path.isfile(find.program['openshot']):
                Img.openshot__img.set_from_file('./categories/gtk-yes.png')
                dial('OpenShot','1')
                Menu7.openshot_.set_tooltip_text("Openshot is installed.\nClick to remove it.")

    @staticmethod
    def on_chromium__clicked(self):
        if os.path.isfile(find.program['chromium']):
            os.system('pacman -R chromium --noconfirm')
            if not os.path.isfile(find.program['chromium']):
                Img.chromium__img.set_from_file('./categories/gtk-no.png')
                dial('Chromium','2')
                Menu7.chromium_.set_tooltip_text("Chromium is not installed.\nClick to install it.")
        else:
            os.system('pacman -S chromium --noconfirm')
            if os.path.isfile(find.program['chromium']):
                Img.chromium__img.set_from_file('./categories/gtk-yes.png')
                dial('Chromium','1')
                Menu7.chromium_.set_tooltip_text("Chromium is installed.\nClick to remove it.")

    @staticmethod
    def on_deluge__clicked(self):
        if os.path.isfile(find.program['deluge']):
            os.system('pacman -R deluge --noconfirm')
            if not os.path.isfile(find.program['deluge']):
                Img.deluge__img.set_from_file('./categories/gtk-no.png')
                dial('Deluge','2')
                Menu7.deluge_.set_tooltip_text("Deluge is not installed.\nClick to install it.")
        else:
            os.system('pacman -S deluge --noconfirm')
            if os.path.isfile(find.program['deluge']):
                Img.deluge__img.set_from_file('./categories/gtk-yes.png')
                dial('Deluge','1')
                Menu7.deluge_.set_tooltip_text("Deluge is installed.\nClick to remove it.")

    @staticmethod
    def on_liferea__clicked(self):
        if os.path.isfile(find.program['liferea']):
            os.system('pacman -R liferea --noconfirm')
            if not os.path.isfile(find.program['liferea']):
                Img.liferea__img.set_from_file('./categories/gtk-no.png')
                dial('Liferea','2')
                Menu7.liferea_.set_tooltip_text("Liferea is not installed.\nClick to install it.")
        else:
            os.system('pacman -S liferea --noconfirm')
            if os.path.isfile(find.program['liferea']):
                Img.liferea__img.set_from_file('./categories/gtk-yes.png')
                dial('Liferea','1')
                Menu7.liferea_.set_tooltip_text("Liferea is installed.\nClick to remove it.")

    @staticmethod
    def on_htop__clicked(self):
        if os.path.isfile(find.program['htop']):
            os.system('pacman -R htop --noconfirm')
            if not os.path.isfile(find.program['htop']):
                Img.htop__img.set_from_file('./categories/gtk-no.png')
                dial('Htop','2')
                Menu7.htop_.set_tooltip_text("Htop is not installed.\nClick to install it.")
        else:
            os.system('pacman -S htop --noconfirm')
            if os.path.isfile(find.program['htop']):
                Img.htop__img.set_from_file('./categories/gtk-yes.png')
                dial('Htop','1')
                Menu7.htop_.set_tooltip_text("Htop is installed.\nClick to remove it.")

    @staticmethod
    def on_skype__clicked(self):
        if os.path.isfile(find.program['skype']):
            os.system('pacman -R skype --noconfirm')
            if not os.path.isfile(find.program['skype']):
                Img.skype__img.set_from_file('./categories/gtk-no.png')
                dial('Skype','2')
                Menu7.skype_.set_tooltip_text("Skype is not installed.\nClick to install it.")
        else:
            os.system('pacman -S skype --noconfirm')
            if os.path.isfile(find.program['skype']):
                Img.skype__img.set_from_file('./categories/gtk-yes.png')
                dial('Skype','1')
                Menu7.skype_.set_tooltip_text("Skype is installed.\nClick to remove it.")

    @staticmethod
    def on_wireshark__clicked(self):
        if os.path.isfile(find.program['wireshark']):
            os.system('pacman -R wireshark-gtk --noconfirm')
            if not os.path.isfile(find.program['wireshark']):
                Img.wireshark__img.set_from_file('./categories/gtk-no.png')
                dial('Wireshark','2')
                Menu7.wireshark_.set_tooltip_text("Wireshark is not installed.\nClick to install it.")

        else:
            os.system('pacman -S wireshark-gtk --noconfirm')
            if os.path.isfile(find.program['wireshark']):
                Img.wireshark__img.set_from_file('./categories/gtk-yes.png')
                dial('Wireshark','1')
                Menu7.wireshark_.set_tooltip_text("Wireshark is installed.\nClick to remove it.")

    @staticmethod
    def on_virtualbox__clicked(self):
        if os.path.isfile(find.program['virtualbox']):
            os.system('pacman -R virtualbox --noconfirm')
            if not os.path.isfile(find.program['virtualbox']):
                Img.virtualbox__img.set_from_file('./categories/gtk-no.png')
                dial('Virtualbox','2')
                Menu7.virtualbox_.set_tooltip_text("Virtualbox is not installed.\nClick to install it.")
        else:
            os.system('pacman -S virtualbox --noconfirm')
            if os.path.isfile(find.program['virtualbox']):
                Img.virtualbox__img.set_from_file('./categories/gtk-yes.png')
                dial('Virtualbox','1')
                Menu7.virtualbox_.set_tooltip_text("Virtualbox is installed.\nClick to remove it.")

    @staticmethod
    def on_steam__clicked(self):
        if os.path.isfile(find.program['steam']):
            os.system('pacman -R steam --noconfirm')
            if not os.path.isfile(find.program['steam']):
                Img.steam__img.set_from_file('./categories/gtk-no.png')
                dial('Steam','2')
                Menu7.steam_.set_tooltip_text("Steam is not installed.\nClick to install it.")
        else:
            os.system('pacman -S steam --noconfirm')
            if os.path.isfile(find.program['steam']):
                Img.steam__img.set_from_file('./categories/gtk-yes.png')
                dial('Steam','1')
                Menu7.steam_.set_tooltip_text("Steam is installed.\nClick to remove it.")

    @staticmethod
    def on_xchat__clicked(self):
        if os.path.isfile(find.program['xchat']):
            os.system('pacman -R xchat --noconfirm')
            if not os.path.isfile(find.program['xchat']):
                Img.xchat__img.set_from_file('./categories/gtk-no.png')
                dial('Xchat','2')
                Menu7.xchat_.set_tooltip_text("Xchat is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xchat --noconfirm')
            if os.path.isfile(find.program['xchat']):
                Img.xchat__img.set_from_file('./categories/gtk-yes.png')
                dial('Xchat','1')
                Menu7.xchat_.set_tooltip_text("Xchat is installed.\nClick to remove it.")

    @staticmethod
    def on_gedit__clicked(self):
        if os.path.isfile(find.program['gedit']):
            os.system('pacman -R gedit --noconfirm')
            if not os.path.isfile(find.program['gedit']):
                Img.gedit__img.set_from_file('./categories/gtk-no.png')
                dial('Gedit','2')
                Menu7.gedit_.set_tooltip_text("gedit is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gedit --noconfirm')
            if os.path.isfile(find.program['gedit']):
                Img.gedit__img.set_from_file('./categories/gtk-yes.png')
                dial('Gedit','1')
                Menu7.gedit_.set_tooltip_text("Gedit is installed.\nClick to remove it.")

    @staticmethod
    # menu 6 button actions
    def on_docky_clicked(self):
        if os.path.isfile(find.program['docky']):
            os.system('pacman -R docky --noconfirm')
            if not os.path.isfile(find.program['docky']):
                Img.docky_img.set_from_file('./categories/gtk-no.png')
                dial('Docky','2')
                Menu6.docky.set_tooltip_text("Docky is not installed.\nClick to install it.")
        else:
            os.system('pacman -S docky --noconfirm')
            if os.path.isfile(find.program['docky']):
                Img.docky_img.set_from_file('./categories/gtk-yes.png')
                dial('Docky','1')
                Menu6.docky.set_tooltip_text("Docky is installed.\nClick to remove it.")

    @staticmethod
    def on_emacs_clicked(self):
        if os.path.isfile(find.program['emacs']):
            os.system('pacman -R emacs --noconfirm')
            if not os.path.isfile(find.program['emacs']):
                Img.emacs_img.set_from_file('./categories/gtk-no.png')
                dial('Emacs','2')
                Menu6.emacs.set_tooltip_text("Emacs is not installed.\nClick to install it.")
        else:
            os.system('pacman -S emacs --noconfirm')
            if os.path.isfile(find.program['emacs']):
                Img.emacs_img.set_from_file('./categories/gtk-yes.png')
                dial('Emacs','1')
                Menu6.emacs.set_tooltip_text("Emacs is installed.\nClick to remove it.")

    @staticmethod
    def on_vim_clicked(self):
        if os.path.isfile(find.program['vim']):
            os.system('pacman -R vim --noconfirm')
            if not os.path.isfile(find.program['vim']):
                Img.vim_img.set_from_file('./categories/gtk-no.png')
                dial('Vim','2')
                Menu6.vim.set_tooltip_text("Vim is not installed.\nClick to install it.")
        else:
            os.system('pacman -S vim --noconfirm')
            if os.path.isfile(find.program['vim']):
                Img.vim_img.set_from_file('./categories/gtk-yes.png')
                dial('Vim','1')
                Menu6.vim.set_tooltip_text("Vim is installed.\nClick to remove it.")

    @staticmethod
    def on_galculator_clicked(self):
        if os.path.isfile(find.program['galculator']):
            os.system('pacman -R galculator --noconfirm')
            if not os.path.isfile(find.program['galculator']):
                Img.galculator_img.set_from_file('./categories/gtk-no.png')
                dial('Galculator','2')
                Menu6.galculator.set_tooltip_text("Galculator is not installed.\nClick to install it.")
        else:
            os.system('pacman -S galculator --noconfirm')
            if os.path.isfile(find.program['galculator']):
                Img.galculator_img.set_from_file('./categories/gtk-yes.png')
                dial('Galculator','1')
                Menu6.galculator.set_tooltip_text("Galculator is installed.\nClick to remove it.")

    @staticmethod
    def on_gedit_clicked(self):
        if os.path.isfile(find.program['gedit']):
            os.system('pacman -R gedit --noconfirm')
            if not os.path.isfile(find.program['gedit']):
                Img.gedit_img.set_from_file('./categories/gtk-no.png')
                dial('Gedit','2')
                Menu6.gedit.set_tooltip_text("gedit is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gedit --noconfirm')
            if os.path.isfile(find.program['gedit']):
                Img.gedit_img.set_from_file('./categories/gtk-yes.png')
                dial('Gedit','1')
                Menu6.gedit.set_tooltip_text("gedit is installed.\nClick to remove it.")

    @staticmethod
    def on_gloobus_clicked(self):
        if os.path.isfile(find.program['gloobus']):
            os.system('pacman -R gloobus-preview --noconfirm')
            if not os.path.isfile(find.program['gloobus']):
                Img.gloobus_img.set_from_file('./categories/gtk-no.png')
                dial('Gloobus','2')
                Menu6.gloobus.set_tooltip_text("Gloobus is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gloobus-preview --noconfirm')
            if os.path.isfile(find.program['gloobus']):
                Img.gloobus_img.set_from_file('./categories/gtk-yes.png')
                dial('Gloobus','1')
                Menu6.gloobus.set_tooltip_text("Gloobus is installed.\nClick to remove it.")

    @staticmethod
    def on_leafpad_clicked(self):
        if os.path.isfile(find.program['leafpad']):
            os.system('pacman -R leafpad --noconfirm')
            if not os.path.isfile(find.program['leafpad']):
                Img.leafpad_img.set_from_file('./categories/gtk-no.png')
                dial('Leafpad','2')
                Menu6.leafpad.set_tooltip_text("Leafpad is not installed.\nClick to install it.")
        else:
            os.system('pacman -S leafpad --noconfirm')
            if os.path.isfile(find.program['leafpad']):
                Img.leafpad_img.set_from_file('./categories/gtk-yes.png')
                dial('Leafpad','1')
                Menu6.leafpad.set_tooltip_text("Leafpad is installed.\nClick to remove it.")

    @staticmethod
    def on_scribes_clicked(self):
        if os.path.isfile(find.program['scribes']):
            os.system('pacman -R scribes --noconfirm')
            if not os.path.isfile(find.program['scribes']):
                Img.scribes_img.set_from_file('./categories/gtk-no.png')
                dial('Scribes','2')
                Menu6.scribes.set_tooltip_text("Scribes is not installed.\nClick to install it.")
        else:
            os.system('pacman -S scribes --noconfirm')
            if os.path.isfile(find.program['scribes']):
                Img.scribes_img.set_from_file('./categories/gtk-yes.png')
                dial('Scribes','1')
                Menu6.scribes.set_tooltip_text("Scribes is installed.\nClick to remove it.")

    @staticmethod
    def on_tomboy_clicked(self):
        if os.path.isfile(find.program['tomboy']):
            os.system('pacman -R tomboy --noconfirm')
            if not os.path.isfile(find.program['tomboy']):
                Img.tomboy_img.set_from_file('./categories/gtk-no.png')
                dial('Tomboy','2')
                Menu6.tomboy.set_tooltip_text("Tomboy is not installed.\nClick to install it.")
        else:
            os.system('pacman -S tomboy --noconfirm')
            if os.path.isfile(find.program['tomboy']):
                Img.tomboy_img.set_from_file('./categories/gtk-yes.png')
                dial('Tomboy','1')
                Menu6.tomboy.set_tooltip_text("Tomboy is installed.\nClick to remove it.")

    @staticmethod
    def on_tuxcards_clicked(self):
        if os.path.isfile(find.program['tuxcards']):
            os.system('pacman -R tuxcards --noconfirm')
            if not os.path.isfile(find.program['tuxcards']):
                Img.tuxcards_img.set_from_file('./categories/gtk-no.png')
                dial('TuxCards','2')
                Menu6.tuxcards.set_tooltip_text("Tuxcards is not installed.\nClick to install it.")
        else:
            os.system('pacman -S tuxcards --noconfirm')
            if os.path.isfile(find.program['tuxcards']):
                Img.tuxcards_img.set_from_file('./categories/gtk-yes.png')
                dial('TuxCards','1')
                Menu6.tuxcards.set_tooltip_text("Tuxcards is installed.\nClick to remove it.")

    @staticmethod
    def on_imagewriter_clicked(self):
        if os.path.isfile(find.program['tuxcards']):
            os.system('pacman -R imagewriter --noconfirm')
            if not os.path.isfile(find.program['tuxcards']):
                Img.imagewriter_img.set_from_file('./categories/gtk-no.png')
                dial('Imagewriter','2')
                Menu6.imagewriter.set_tooltip_text("Imagewriter is not installed.\nClick to install it.")
        else:
            os.system('pacman -S imagewriter --noconfirm')
            if os.path.isfile(find.program['tuxcards']):
                Img.imagewriter_img.set_from_file('./categories/gtk-yes.png')
                dial('Imagewriter','1')
                Menu6.imagewriter.set_tooltip_text("Imagewriter is installed.\nClick to remove it.")

    @staticmethod
    def on_sevenzip_clicked(self):
        if os.path.isfile(find.program['7zip']):
            os.system('pacman -Rdd p7zip --noconfirm')
            if not os.path.isfile(find.program['7zip']):
                Img.sevenzip_img.set_from_file('./categories/gtk-no.png')
                dial('p7zip','2')
                Menu6.sevenzip.set_tooltip_text("7-zip is not installed.\nClick to install it.")
        else:
            os.system('pacman -S p7zip --noconfirm')
            if os.path.isfile(find.program['7zip']):
                Img.sevenzip_img.set_from_file('./categories/gtk-yes.png')
                dial('p7zip','1')
                Menu6.sevenzip.set_tooltip_text("7-zip is installed.\nClick to remove it.")

    @staticmethod
    # menu 5 button actions
    def on_gparted_clicked(self):
        if os.path.isfile(find.program['gparted']):
            os.system('pacman -R gparted --noconfirm')
            if not os.path.isfile(find.program['gparted']):
                Img.gparted_img.set_from_file('./categories/gtk-no.png')
                dial('Gparted','2')
                Menu5.gparted.set_tooltip_text("Gparted is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gparted --noconfirm')
            if os.path.isfile(find.program['gparted']):
                Img.gparted_img.set_from_file('./categories/gtk-yes.png')
                dial('Gparted','1')
                Menu5.gparted.set_tooltip_text("Gparted is installed.\nClick to remove it.")

    @staticmethod
    def on_guake_clicked(self):
        if os.path.isfile(find.program['guake']):
            os.system('pacman -R guake --noconfirm')
            if not os.path.isfile(find.program['guake']):
                Img.guake_img.set_from_file('./categories/gtk-no.png')
                dial('Guake','2')
                Menu5.guake.set_tooltip_text("Guake is not installed.\nClick to install it.")
        else:
            os.system('pacman -S guake --noconfirm')
            if os.path.isfile(find.program['guake']):
                Img.guake_img.set_from_file('./categories/gtk-yes.png')
                dial('Guake','1')
                Menu5.guake.set_tooltip_text("Guake is installed.\nClick to remove it.")

    @staticmethod
    def on_hardinfo_clicked(self):
        if os.path.isfile(find.program['hardinfo']):
            os.system('pacman -R hardinfo --noconfirm')
            if not os.path.isfile(find.program['hardinfo']):
                Img.hardinfo_img.set_from_file('./categories/gtk-no.png')
                dial('HardInfo','2')
                Menu5.hardinfo.set_tooltip_text("Hardinfo is not installed.\nClick to install it.")
        else:
            os.system('pacman -S hardinfo --noconfirm')
            if os.path.isfile(find.program['hardinfo']):
                Img.hardinfo_img.set_from_file('./categories/gtk-yes.png')
                dial('HardInfo','1')
                Menu5.hardinfo.set_tooltip_text("Hardinfo is installed.\nClick to remove it.")

    @staticmethod
    def on_htop_clicked(self):
        if os.path.isfile(find.program['htop']):
            os.system('pacman -R htop --noconfirm')
            if not os.path.isfile(find.program['htop']):
                Img.htop_img.set_from_file('./categories/gtk-no.png')
                dial('Htop','2')
                Menu5.htop.set_tooltip_text("Htop is not installed.\nClick to install it.")
        else:
            os.system('pacman -S htop --noconfirm')
            if os.path.isfile(find.program['htop']):
                Img.htop_img.set_from_file('./categories/gtk-yes.png')
                dial('Htop','1')
                Menu5.htop.set_tooltip_text("Htop is installed.\nClick to remove it.")

    @staticmethod
    def on_keepassx_clicked(self):
        if os.path.isfile(find.program['keepassx']):
            os.system('pacman -R keepassx --noconfirm')
            if not os.path.isfile(find.program['keepassx']):
                Img.keepassx_img.set_from_file('./categories/gtk-no.png')
                dial('KeePassX','2')
                Menu5.keepassx.set_tooltip_text("Keepassx is not installed.\nClick to install it.")
        else:
            os.system('pacman -S keepassx --noconfirm')
            if os.path.isfile(find.program['keepassx']):
                Img.keepassx_img.set_from_file('./categories/gtk-yes.png')
                dial('KeePassX','1')
                Menu5.keepassx.set_tooltip_text("Keepassx is installed.\nClick to remove it.")

    @staticmethod
    def on_playonlinux_clicked(self):
        if os.path.isfile(find.program['playonlinux']):
            os.system('pacman -R playonlinux --noconfirm')
            if not os.path.isfile(find.program['playonlinux']):
                Img.playonlinux_img.set_from_file('./categories/gtk-no.png')
                dial('PlayOnLinux','2')
                Menu5.playonlinux.set_tooltip_text("Playonlinux is not installed.\nClick to install it.")
        else:
            os.system('pacman -S playonlinux --noconfirm')
            if os.path.isfile(find.program['playonlinux']):
                Img.playonlinux_img.set_from_file('./categories/gtk-yes.png')
                dial('PlayOnLinux','1')
                Menu5.playonlinux.set_tooltip_text("Playonlinux is installed.\nClick to remove it.")

    @staticmethod
    def on_terminator_clicked(self):
        if os.path.isfile(find.program['terminator']):
            os.system('pacman -R terminator --noconfirm')
            if not os.path.isfile(find.program['terminator']):
                Img.terminator_img.set_from_file('./categories/gtk-no.png')
                dial('Terminator','2')
                Menu5.terminator.set_tooltip_text("Terminato is not installed.\nClick to install it.")
        else:
            os.system('pacman -S terminator --noconfirm')
            if os.path.isfile(find.program['terminator']):
                Img.terminator_img.set_from_file('./categories/gtk-yes.png')
                dial('Terminator','1')
                Menu5.terminator.set_tooltip_text("Terminator is installed.\nClick to remove it.")

    @staticmethod
    def on_thunar_clicked(self):
        if os.path.isfile(find.program['thunar']):
            os.system('pacman -R thunar --noconfirm')
            if not os.path.isfile(find.program['thunar']):
                Img.thunar_img.set_from_file('./categories/gtk-no.png')
                dial('Thunar','2')
                Menu5.thunar.set_tooltip_text("Thunar is not installed.\nClick to install it.")
        else:
            os.system('pacman -S thunar --noconfirm')
            if os.path.isfile(find.program['thunar']):
                Img.thunar_img.set_from_file('./categories/gtk-yes.png')
                dial('Thunar','1')
                Menu5.thunar.set_tooltip_text("Thunar is installed.\nClick to remove it.")

    @staticmethod
    def on_truecrypt_clicked(self):
        if os.path.isfile(find.program['truecrypt']):
            os.system('pacman -R truecrypt --noconfirm')
            if not os.path.isfile(find.program['truecrypt']):
                Img.truecrypt_img.set_from_file('./categories/gtk-no.png')
                dial('TrueCrypt','2')
                Menu5.truecrypt.set_tooltip_text("Truecrypt is not installed.\nClick to install it.")
        else:
            os.system('pacman -S truecrypt --noconfirm')
            if os.path.isfile(find.program['truecrypt']):
                Img.truecrypt_img.set_from_file('./categories/gtk-yes.png')
                dial('TrueCrypt','1')
                Menu5.truecrypt.set_tooltip_text("Truecrypt is installed.\nClick to remove it.")

    @staticmethod
    def on_unetbootin_clicked(self):
        if os.path.isfile(find.program['unetbootin']):
            os.system('pacman -R unetbootin --noconfirm')
            if not os.path.isfile(find.program['unetbootin']):
                Img.unetbootin_img.set_from_file('./categories/gtk-no.png')
                dial('Unetbootin','2')
                Menu5.unetbootin.set_tooltip_text("Unetbootin is not installed.\nClick to install it.")
        else:
            os.system('pacman -S unetbootin --noconfirm')
            if os.path.isfile(find.program['unetbootin']):
                Img.unetbootin_img.set_from_file('./categories/gtk-yes.png')
                dial('Unetbootin','1')
                Menu5.unetbootin.set_tooltip_text("Unetoobin is installed.\nClick to remove it.")

    @staticmethod
    def on_virtualbox_clicked(self):
        if os.path.isfile(find.program['virtualbox']):
            os.system('pacman -R virtualbox --noconfirm')
            if not os.path.isfile(find.program['virtualbox']):
                Img.virtualbox_img.set_from_file('./categories/gtk-no.png')
                dial('Virtualbox','2')
                Menu5.virtualbox.set_tooltip_text("Virtualbox is not installed.\nClick to install it.")
        else:
            os.system('pacman -S virtualbox --noconfirm')
            if os.path.isfile(find.program['virtualbox']):
                Img.virtualbox_img.set_from_file('./categories/gtk-yes.png')
                dial('Virtualbox','1')
                Menu5.virtualbox.set_tooltip_text("Virtualbox is installed.\nClick to remove it.")

    @staticmethod
    def on_wine_clicked(self):
        if os.path.isfile(find.program['wine']):
            os.system('pacman -R wine --noconfirm')
            if not os.path.isfile(find.program['wine']):
                Img.wine_img.set_from_file('./categories/gtk-no.png')
                dial('Wine','2')
                Menu5.wine.set_tooltip_text("Wine is not installed.\nClick to install it.")
        else:
            os.system('pacman -S wine --noconfirm')
            if os.path.isfile(find.program['wine']):
                Img.wine_img.set_from_file('./categories/gtk-yes.png')
                dial('Wine','1')
                Menu5.wine.set_tooltip_text("Wine is installed.\nClick to remove it.")

    @staticmethod
    def on_wireshark_clicked(self):
        if os.path.isfile(find.program['wireshark']):
            os.system('pacman -R wireshark-gtk --noconfirm')
            if not os.path.isfile(find.program['wireshark']):
                Img.wireshark_img.set_from_file('./categories/gtk-no.png')
                dial('Wireshark','2')
                Menu5.wireshark.set_tooltip_text("Wireshark is not installed.\nClick to install it.")
        else:
            os.system('pacman -S wireshark-gtk --noconfirm')
            if os.path.isfile(find.program['wireshark']):
                Img.wireshark_img.set_from_file('./categories/gtk-yes.png')
                dial('Wireshark','1')
                Menu5.wireshark.set_tooltip_text("Wireshark is installed.\nClick to remove it.")

    @staticmethod
    def on_xbmc_clicked(self):
        if os.path.isfile(find.program['xbmc']):
            os.system('pacman -R xbmc --noconfirm')
            if not os.path.isfile(find.program['xbmc']):
                Img.xbmc_img.set_from_file('./categories/gtk-no.png')
                dial('XBMC','2')
                Menu5.xbmc.set_tooltip_text("XBMC is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xbmc --noconfirm')
            if os.path.isfile(find.program['xbmc']):
                Img.xbmc_img.set_from_file('./categories/gtk-yes.png')
                dial('XBMC','1')
                Menu5.xbmc.set_tooltip_text("XBMC is installed.\nClick to remove it.")

    @staticmethod
    def on_gufw_clicked(self):
        if os.path.isfile(find.program['gufw']):
            os.system('pacman -R gufw --noconfirm')
            if not os.path.isfile(find.program['gufw']):
                Img.gufw_img.set_from_file('./categories/gtk-no.png')
                dial('Gufw','2')
                Menu5.gufw.set_tooltip_text("Gufw is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gufw --noconfirm')
            if os.path.isfile(find.program['gufw']):
                Img.gufw_img.set_from_file('./categories/gtk-yes.png')
                dial('Gufw','1')
                Menu5.gufw.set_tooltip_text("Gufw is installed.\nClick to remove it.")

    @staticmethod
    def on_octopi_clicked(self):
        if os.path.isfile(find.program['octopi']):
            os.system('pacman -R octopi --noconfirm')
            if not os.path.isfile(find.program['octopi']):
                Img.octopi_img.set_from_file('./categories/gtk-no.png')
                dial('Octopi','2')
                Menu5.octopi.set_tooltip_text("Octopi is not installed.\nClick to install it.")
        else:
            os.system('pacman -S octopi --noconfirm')
            if os.path.isfile(find.program['octopi']):
                Img.octopi_img.set_from_file('./categories/gtk-yes.png')
                dial('Octopi','1')
                Menu5.octopi.set_tooltip_text("Octopi is installed.\nClick to remove it.")

    @staticmethod
    def on_pamac_clicked(self):
        if os.path.isfile(find.program['pamac']):
            os.system('pacman -R pamac --noconfirm')
            if not os.path.isfile(find.program['pamac']):
                Img.pamac_img.set_from_file('./categories/gtk-no.png')
                dial('Pamac','2')
                Menu5.pamac.set_tooltip_text("Pamac is not installed.\nClick to install it.")
        else:
            os.system('pacman -S pamac --noconfirm')
            if os.path.isfile(find.program['pamac']):
                Img.pamac_img.set_from_file('./categories/gtk-yes.png')
                dial('Pamac','1')
                Menu5.pamac.set_tooltip_text("Pamac is installed.\nClick to remove it.")

    @staticmethod
    def on_gnome_system_monitor_clicked(self):
        if os.path.isfile(find.program['gnome-system-monitor']):
            os.system('pacman -R gnome-system-monitor --noconfirm')
            if not os.path.isfile(find.program['gnome-system-monitor']):
                Img.gnome_system_monitor_img.set_from_file('./categories/gtk-no.png')
                dial('Gnome System Monitor','2')
                Menu5.gnome_system_monitor.set_tooltip_text("Gnome system monitor is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gnome-system-monitor --noconfirm')
            if os.path.isfile(find.program['gnome-system-monitor']):
                Img.gnome_system_monitor_img.set_from_file('./categories/gtk-yes.png')
                dial('Gnome System Monitor','1')
                Menu5.gnome_system_monitor.set_tooltip_text("Gnome system monitor is installed.\nClick to remove it.")

    @staticmethod
    # menu 4 button actions
    def on_amarok_clicked(self):
        if os.path.isfile(find.program['amarok']):
            os.system('pacman -R amarok --noconfirm')
            if not os.path.isfile(find.program['amarok']):
                Img.amarok_img.set_from_file('./categories/gtk-no.png')
                dial('Amarok','2')
                Menu4.amarok.set_tooltip_text("Amarok is not installed.\nClick to install it.")
        else:
            os.system('pacman -S amarok --noconfirm')
            if os.path.isfile(find.program['amarok']):
                Img.amarok_img.set_from_file('./categories/gtk-yes.png')
                dial('Amarok','1')
                Menu4.amarok.set_tooltip_text("Amarok is installed.\nClick to remove it.")

    @staticmethod
    def on_audacious_clicked(self):
        if os.path.isfile(find.program['audacious']):
            os.system('pacman -R audacious --noconfirm')
            if not os.path.isfile(find.program['audacious']):
                Img.audacious_img.set_from_file('./categories/gtk-no.png')
                dial('Audacious','2')
                Menu4.audacious.set_tooltip_text("Audacious is not installed.\nClick to install it.")
        else:
            os.system('pacman -S audacious --noconfirm')
            if os.path.isfile(find.program['audacious']):
                Img.audacious_img.set_from_file('./categories/gtk-yes.png')
                dial('Audacious','1')
                Menu4.audacious.set_tooltip_text("Audacious is installed.\nClick to remove it.")

    @staticmethod
    def on_banshee_clicked(self):
        if os.path.isfile(find.program['banshee']):
            os.system('pacman -R banshee --noconfirm')
            if not os.path.isfile(find.program['banshee']):
                Img.banshee_img.set_from_file('./categories/gtk-no.png')
                dial('Banshee','2')
                Menu4.banshee.set_tooltip_text("Banshee is not installed.\nClick to install it.")
        else:
            os.system('pacman -S banshee --noconfirm')
            if os.path.isfile(find.program['banshee']):
                Img.banshee_img.set_from_file('./categories/gtk-yes.png')
                dial('Banshee','1')
                Menu4.banshee.set_tooltip_text("Banshee is installed.\nClick to remove it.")

    @staticmethod
    def on_cheese_clicked(self):
        if os.path.isfile(find.program['cheese']):
            os.system('pacman -R cheese --noconfirm')
            if not os.path.isfile(find.program['cheese']):
                Img.cheese_img.set_from_file('./categories/gtk-no.png')
                dial('Cheese','2')
                Menu4.cheese.set_tooltip_text("Cheese is not installed.\nClick to install it.")
        else:
            os.system('pacman -S cheese --noconfirm')
            if os.path.isfile(find.program['cheese']):
                Img.cheese_img.set_from_file('./categories/gtk-yes.png')
                dial('Cheese','1')
                Menu4.cheese.set_tooltip_text("Cheese is installed.\nClick to remove it.")

    @staticmethod
    def on_clementine_clicked(self):
        if os.path.isfile(find.program['clementine']):
            os.system('pacman -R clementine --noconfirm')
            if not os.path.isfile(find.program['clementine']):
                Img.clementine_img.set_from_file('./categories/gtk-no.png')
                dial('Clementine','2')
                Menu4.clementine.set_tooltip_text("Clementine is not installed.\nClick to install it.")
        else:
            os.system('pacman -S clementine --noconfirm')
            if os.path.isfile(find.program['clementine']):
                Img.clementine_img.set_from_file('./categories/gtk-yes.png')
                dial('Clementine','1')
                Menu4.clementine.set_tooltip_text("Clementine is installed.\nClick to remove it.")

    @staticmethod
    def on_flashplayer_clicked(self):
        if os.path.isfile(find.program['flash-player']):
            os.system('pacman -R flashplugin --noconfirm')
            if not os.path.isfile(find.program['flash-player']):
                Img.flashplayer_img.set_from_file('./categories/gtk-no.png')
                dial('Adobe Flashplayer','2')
                Menu4.flashplayer.set_tooltip_text("Flashplayer is not installed.\nClick to install it.")
        else:
            os.system('pacman -S flashplugin --noconfirm')
            if os.path.isfile(find.program['flash-player']):
                Img.flashplayer_img.set_from_file('./categories/gtk-yes.png')
                dial('Adobe Flashplayer','1')
                Menu4.flashplayer.set_tooltip_text("Flashpleyer is installed.\nClick to remove it.")

    @staticmethod
    def on_recordmydesktop_clicked(self):
        if os.path.isfile(find.program['recordmydesktop']):
            os.system('pacman -R gtk-recordmydesktop --noconfirm')
            if not os.path.isfile(find.program['recordmydesktop']):
                Img.recordmydesktop_img.set_from_file('./categories/gtk-no.png')
                dial('RecordMyDesktop','2')
                Menu4.recordmydesktop.set_tooltip_text("RecordMyDesktop is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gtk-recordmydesktop --noconfirm')
            if os.path.isfile(find.program['recordmydesktop']):
                Img.recordmydesktop_img.set_from_file('./categories/gtk-yes.png')
                dial('RecordMyDesktop','1')
                Menu4.recordmydesktop.set_tooltip_text("RecordMyDesktop is installed.\nClick to remove it.")

    @staticmethod
    def on_guayadeque_clicked(self):
        if os.path.isfile(find.program['guayadeque']):
            os.system('pacman -R guayadeque --noconfirm')
            if not os.path.isfile(find.program['guayadeque']):
                Img.guayadeque_img.set_from_file('./categories/gtk-no.png')
                dial('Guayadeque','2')
                Menu4.guayadeque.set_tooltip_text("Guayadeque is not installed.\nClick to install it.")
        else:
            os.system('pacman -S guayadeque --noconfirm')
            if os.path.isfile(find.program['guayadeque']):
                Img.guayadeque_img.set_from_file('./categories/gtk-yes.png')
                dial('Guayadeque','1')
                Menu4.guayadeque.set_tooltip_text("Guayadeque is installed.\nClick to remove it.")

    @staticmethod
    def on_mplayer_clicked(self):
        if os.path.isfile(find.program['mplayer']):
            os.system('pacman -R mplayer --noconfirm')
            if not os.path.isfile(find.program['mplayer']):
                Img.mplayer_img.set_from_file('./categories/gtk-no.png')
                dial('MPlayer','2')
                Menu4.mplayer.set_tooltip_text("Mplayer is not installed.\nClick to install it.")
        else:
            os.system('pacman -S mplayer --noconfirm')
            if os.path.isfile(find.program['mplayer']):
                Img.mplayer_img.set_from_file('./categories/gtk-yes.png')
                dial('MPlayer','1')
                Menu4.mplayer.set_tooltip_text("Mplayer is installed.\nClick to remove it.")

    @staticmethod
    def on_openshot_clicked(self):
        if os.path.isfile(find.program['openshot']):
            os.system('pacman -R openshot --noconfirm')
            if not os.path.isfile(find.program['openshot']):
                Img.openshot_img.set_from_file('./categories/gtk-no.png')
                dial('OpenShot','2')
                Menu4.openshot.set_tooltip_text("Openshot is not installed.\nClick to install it.")
        else:
            os.system('pacman -S openshot --noconfirm')
            if os.path.isfile(find.program['openshot']):
                Img.openshot_img.set_from_file('./categories/gtk-yes.png')
                dial('OpenShot','1')
                Menu4.openshot.set_tooltip_text("Openshot is installed.\nClick to remove it.")

    @staticmethod
    def on_pitivi_clicked(self):
        if os.path.isfile(find.program['pitivi']):
            os.system('pacman -R pitivi --noconfirm')
            if not os.path.isfile(find.program['pitivi']):
                Img.pitivi_img.set_from_file('./categories/gtk-no.png')
                dial('PiTiVi','2')
                Menu4.pitivi.set_tooltip_text("PiTiVi is not installed.\nClick to install it.")
        else:
            os.system('pacman -S pitivi --noconfirm')
            if os.path.isfile(find.program['pitivi']):
                Img.pitivi_img.set_from_file('./categories/gtk-yes.png')
                dial('PiTiVi','1')
                Menu4.pitivi.set_tooltip_text("PiTiVi is installed.\nClick to remove it.")

    @staticmethod
    def on_rhythmbox_clicked(self):
        if os.path.isfile(find.program['rhythmobx']):
            os.system('pacman -R rhythmbox --noconfirm')
            if not os.path.isfile(find.program['rhythmbox']):
                Img.rhythmbox_img.set_from_file('./categories/gtk-no.png')
                dial('Rhythmbox','2')
                Menu4.rhythmbox.set_tooltip_text("Rhythmbox is not installed.\nClick to install it.")
        else:
            os.system('pacman -S rhythmbox --noconfirm')
            if os.path.isfile(find.program['rhythmbox']):
                Img.rhythmbox_img.set_from_file('./categories/gtk-yes.png')
                dial('Rhythmbox','1')
                Menu4.rhythmbox.set_tooltip_text("Rhythmbox is installed.\nClick to remove it.")

    @staticmethod
    def on_soundconverter_clicked(self):
        if os.path.isfile(find.program['soundconverter']):
            os.system('pacman -R soundconverter --noconfirm')
            if not os.path.isfile(find.program['soundconverter']):
                Img.soundconverter_img.set_from_file('./categories/gtk-no.png')
                dial('SoundConverter','2')
                Menu4.soundconverter.set_tooltip_text("Soundconverter is not installed.\nClick to install it.")
        else:
            os.system('pacman -S soundconverter --noconfirm')
            if os.path.isfile(find.program['soundconverter']):
                Img.soundconverter_img.set_from_file('./categories/gtk-yes.png')
                dial('SoundConverter','1')
                Menu4.soundconverter.set_tooltip_text("Soundconverter is installed.\nClick to remove it.")

    @staticmethod
    def on_totem_clicked(self):
        if os.path.isfile(find.program['totem']):
            os.system('pacman -R totem --noconfirm')
            if not os.path.isfile(find.program['totem']):
                Img.totem_img.set_from_file('./categories/gtk-no.png')
                dial('Totem','2')
                Menu4.totem.set_tooltip_text("Totem is not installed.\nClick to install it.")
        else:
            os.system('pacman -S totem --noconfirm')
            if os.path.isfile(find.program['totem']):
                Img.totem_img.set_from_file('./categories/gtk-yes.png')
                dial('Totem','1')
                Menu4.totem.set_tooltip_text("Totem is installed.\nClick to remove it.")

    @staticmethod
    def on_vlc_clicked(self):
        if os.path.isfile(find.program['vlc']):
            os.system('pacman -R vlc --noconfirm')
            if not os.path.isfile(find.program['vlc']):
                Img.vlc_img.set_from_file('./categories/gtk-no.png')
                dial('Vlc','2')
                Menu4.vlc.set_tooltip_text("Vlc is not installed.\nClick to install it.")
        else:
            os.system('pacman -S vlc --noconfirm')
            if os.path.isfile(find.program['vlc']):
                Img.vlc_img.set_from_file('./categories/gtk-yes.png')
                dial('Vlc','1')
                Menu4.vlc.set_tooltip_text("Vlc is installed.\nClick to remove it.")

    @staticmethod
    def on_winff_clicked(self):
        if os.path.isfile(find.program['winff']):
            os.system('pacman -R winff --noconfirm')
            if not os.path.isfile(find.program['winff']):
                Img.winff_img.set_from_file('./categories/gtk-no.png')
                dial('Winff','2')
                Menu4.winff.set_tooltip_text("Winff is not installed.\nClick to install it.")
        else:
            os.system('pacman -S winff --noconfirm')
            if os.path.isfile(find.program['winff']):
                Img.winff_img.set_from_file('./categories/gtk-yes.png')
                dial('Winff','1')
                Menu4.winff.set_tooltip_text("Winff is installed.\nClick to remove it.")

    @staticmethod
    def on_xfburn_clicked(self):
        if os.path.isfile(find.program['xfburn']):
            os.system('pacman -R xfburn --noconfirm')
            if not os.path.isfile(find.program['xfburn']):
                Img.xfburn_img.set_from_file('./categories/gtk-no.png')
                dial('Xfburn','2')
                Menu4.xfburn.set_tooltip_text("Xfburn is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xfburn --noconfirm')
            if os.path.isfile(find.program['xfburn']):
                Img.xfburn_img.set_from_file('./categories/gtk-yes.png')
                dial('Xfburn','1')
                Menu4.xfburn.set_tooltip_text("Xfburn is installed.\nClick to remove it.")

    @staticmethod
    def on_kdenlive_clicked(self):
        if os.path.isfile(find.program['kdenlive']):
            os.system('pacman -R kdenlive --noconfirm')
            if not os.path.isfile(find.program['kdenlive']):
                Img.kdenlive_img.set_from_file('./categories/gtk-no.png')
                dial('Kdenlive','2')
                Menu4.kdenlive.set_tooltip_text("Kdenlive is not installed.\nClick to install it.")
        else:
            os.system('pacman -S kdenlive --noconfirm')
            if os.path.isfile(find.program['kdenlive']):
                Img.kdenlive_img.set_from_file('./categories/gtk-yes.png')
                dial('Kdenlive','1')
                Menu4.kdenlive.set_tooltip_text("Kdenlive is installed.\nClick to remove it.")

    @staticmethod
    def on_simplescreenrecorder_clicked(self):
        if os.path.isfile(find.program['simplescreenrecorder']):
            os.system('pacman -R simplescreenrecorder --noconfirm')
            if not os.path.isfile(find.program['simplescreenrecorder']):
                Img.simplescreenrecorder_img.set_from_file('./categories/gtk-no.png')
                dial('SimpleScreenRecorder','2')
                Menu4.simplescreenrecorder.set_tooltip_text("Simple screen recorder is not installed.\nClick to install it.")
        else:
            os.system('yaourt -S simplescreenrecorder --noconfirm')
            if os.path.isfile(find.program['simplescreenrecorder']):
                Img.simplescreenrecorder_img.set_from_file('./categories/gtk-yes.png')
                dial('SimpleScreenRecorder','1')
                Menu4.simplescreenrecorder.set_tooltip_text("Simple screen recorder is installed.\nClick to remove it.")

    @staticmethod
    def on_vokoscreen_clicked(self):
        if os.path.isfile(find.program['vokoscreen']):
            os.system('pacman -R vokoscreen --noconfirm')
            if not os.path.isfile(find.program['vokoscreen']):
                Img.vokoscreen_img.set_from_file('./categories/gtk-no.png')
                dial('Vokoscreen','2')
                Menu4.vokoscreen.set_tooltip_text("Vokoscreen is not installed.\nClick to install it.")
        else:
            os.system('yaourt -S vokoscreen --noconfirm')
            if os.path.isfile(find.program['vokoscreen']):
                Img.vokoscreen_img.set_from_file('./categories/gtk-yes.png')
                dial('Vokoscreen','1')
                Menu4.vokoscreen.set_tooltip_text("Vokoscreen is installed.\nClick to remove it.")

    @staticmethod
    # menu 3 button actions
    def on_linuxdcpp_clicked(self):
        if os.path.isfile(find.program['linuxdcpp']):
            os.system('pacman -R linuxdcpp --noconfirm')
            if not os.path.isfile(find.program['linuxdcpp']):
                Img.linuxdcpp_img.set_from_file('./categories/gtk-no.png')
                dial('Linuxdcpp','2')
                Menu3.linuxdcpp.set_tooltip_text("Linuxdcpp is not installed.\nClick to install it.")
        else:
            os.system('pacman -S linuxdcpp --noconfirm')
            if os.path.isfile(find.program['linuxdcpp']):
                Img.linuxdcpp_img.set_from_file('./categories/gtk-yes.png')
                dial('Linuxdcpp','1')
                Menu3.linuxdcpp.set_tooltip_text("Linuxdcpp is installed.\nClick to remove it.")

    @staticmethod
    def on_chromium_clicked(self):
        if os.path.isfile(find.program['chromium']):
            os.system('pacman -R chromium --noconfirm')
            if not os.path.isfile(find.program['chromium']):
                Img.chromium_img.set_from_file('./categories/gtk-no.png')
                dial('Chromium','2')
                Menu3.chromium.set_tooltip_text("Chromium is not installed.\nClick to install it.")
        else:
            os.system('pacman -S chromium --noconfirm')
            if os.path.isfile(find.program['chromium']):
                Img.chromium_img.set_from_file('./categories/gtk-yes.png')
                dial('Chromium','1')
                Menu3.chromium.set_tooltip_text("Chromium is installed.\nClick to remove it.")

    @staticmethod
    def on_deluge_clicked(self):
        if os.path.isfile(find.program['deluge']):
            os.system('pacman -R deluge --noconfirm')
            if not os.path.isfile(find.program['deluge']):
                Img.deluge_img.set_from_file('./categories/gtk-no.png')
                dial('Deluge','2')
                Menu3.deluge.set_tooltip_text("Deluge is not installed.\nClick to install it.")
        else:
            os.system('pacman -S deluge --noconfirm')
            if os.path.isfile(find.program['deluge']):
                Img.deluge_img.set_from_file('./categories/gtk-yes.png')
                dial('Deluge','1')
                Menu3.deluge.set_tooltip_text("Deluge is installed.\nClick to remove it.")

    @staticmethod
    def on_evolution_clicked(self):
        if os.path.isfile(find.program['evolution']):
            os.system('pacman -R evolution --noconfirm')
            if not os.path.isfile(find.program['evolution']):
                Img.evolution_img.set_from_file('./categories/gtk-no.png')
                dial('Evolution','2')
                Menu3.evolution.set_tooltip_text("Evolution is not installed.\nClick to install it.")
        else:
            os.system('pacman -S evolution --noconfirm')
            if os.path.isfile(find.program['evolution']):
                Img.evolution_img.set_from_file('./categories/gtk-yes.png')
                dial('Evolution','1')
                Menu3.evolution.set_tooltip_text("Evolution is installed.\nClick to remove it.")

    @staticmethod
    def on_filezilla_clicked(self):
        if os.path.isfile(find.program['filezilla']):
            os.system('pacman -R filezilla --noconfirm')
            if not os.path.isfile(find.program['filezilla']):
                Img.filezilla_img.set_from_file('./categories/gtk-no.png')
                dial('Filezilla','2')
                Menu3.filezilla.set_tooltip_text("Filezilla is not installed.\nClick to install it.")
        else:
            os.system('pacman -S filezilla --noconfirm')
            if os.path.isfile(find.program['filezilla']):
                Img.filezilla_img.set_from_file('./categories/gtk-yes.png')
                dial('Filezilla','1')
                Menu3.filezilla.set_tooltip_text("Filezilla is installed.\nClick to remove it.")

    @staticmethod
    def on_firefox_clicked(self):
        if os.path.isfile(find.program['firefox']):
            os.system('pacman -R firefox --noconfirm')
            if not os.path.isfile(find.program['firefox']):
                Img.firefox_img.set_from_file('./categories/gtk-no.png')
                dial('Firefox','2')
                Menu3.firefox.set_tooltip_text("Firefox is not installed.\nClick to install it.")
        else:
            os.system('pacman -S firefox --noconfirm')
            if os.path.isfile(find.program['firefox']):
                Img.firefox_img.set_from_file('./categories/gtk-yes.png')
                dial('Firefox','1')
                Menu3.firefox.set_tooltip_text("Firefox is installed.\nClick to remove it.")

    @staticmethod
    def on_chrome_clicked(self):
        if os.path.isfile(find.program['chrome']):
            os.system('pacman -R google-chrome --noconfirm')
            if not os.path.isfile(find.program['chrome']):
                Img.chrome_img.set_from_file('./categories/gtk-no.png')
                dial('Google Chrome','2')
                Menu3.chrome.set_tooltip_text("Google Chrome is not installed.\nClick to install it.")
        else:
            os.system('yaourt -S google-chrome --noconfirm')
            if os.path.isfile(find.program['chrome']):
                Img.chrome_img.set_from_file('./categories/gtk-yes.png')
                dial('Google Chrome','1')
                Menu3.chrome.set_tooltip_text("Google Chrome is installed.\nClick to remove it.")

    @staticmethod
    def on_xchat_clicked(self):
        if os.path.isfile(find.program['xchat']):
            os.system('pacman -R xchat --noconfirm')
            if not os.path.isfile(find.program['xchat']):
                Img.xchat_img.set_from_file('./categories/gtk-no.png')
                dial('Xchat','2')
                Menu3.xchat.set_tooltip_text("Xchat is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xchat --noconfirm')
            if os.path.isfile(find.program['xchat']):
                Img.xchat_img.set_from_file('./categories/gtk-yes.png')
                dial('Xchat','1')
                Menu3.xchat.set_tooltip_text("Xchat is installed.\nClick to remove it.")

    @staticmethod
    def on_liferea_clicked(self):
        if os.path.isfile(find.program['liferea']):
            os.system('pacman -R liferea --noconfirm')
            if not os.path.isfile(find.program['liferea']):
                Img.liferea_img.set_from_file('./categories/gtk-no.png')
                dial('Liferea','2')
                Menu3.liferea.set_tooltip_text("Liferea is not installed.\nClick to install it.")
        else:
            os.system('pacman -S liferea --noconfirm')
            if os.path.isfile(find.program['liferea']):
                Img.liferea_img.set_from_file('./categories/gtk-yes.png')
                dial('Liferea','1')
                Menu3.liferea.set_tooltip_text("Liferea is installed.\nClick to remove it.")

    @staticmethod
    def on_midori_clicked(self):
        if os.path.isfile(find.program['midori']):
            os.system('pacman -R midori --noconfirm')
            if not os.path.isfile(find.program['midori']):
                Img.midori_img.set_from_file('./categories/gtk-no.png')
                dial('Midori','2')
                Menu3.midori.set_tooltip_text("Midori is not installed.\nClick to install it.")
        else:
            os.system('pacman -S midori --noconfirm')
            if os.path.isfile(find.program['midori']):
                Img.midori_img.set_from_file('./categories/gtk-yes.png')
                dial('Midori','1')
                Menu3.midori.set_tooltip_text("Midori is installed.\nClick to remove it.")

    @staticmethod
    def on_minitube_clicked(self):
        if os.path.isfile(find.program['minitube']):
            os.system('pacman -R minitube --noconfirm')
            if not os.path.isfile(find.program['minitube']):
                Img.minitube_img.set_from_file('./categories/gtk-no.png')
                dial('MiniTube','2')
                Menu3.minitube.set_tooltip_text("MiniTube is not installed.\nClick to install it.")
        else:
            os.system('pacman -S minitube --noconfirm')
            if os.path.isfile(find.program['minitube']):
                Img.minitube_img.set_from_file('./categories/gtk-yes.png')
                dial('MiniTube','1')
                Menu3.minitube.set_tooltip_text("MiniTube is installed.\nClick to remove it.")

    @staticmethod
    def on_opera_clicked(self):
        if os.path.isfile(find.program['opera']):
            os.system('pacman -R opera --noconfirm')
            if not os.path.isfile(find.program['opera']):
                Img.opera_img.set_from_file('./categories/gtk-no.png')
                dial('Opera','2')
                Menu3.opera.set_tooltip_text("Opera is not installed.\nClick to install it.")
        else:
            os.system('pacman -S opera --noconfirm')
            if os.path.isfile(find.program['opera']):
                Img.opera_img.set_from_file('./categories/gtk-yes.png')
                dial('Opera','1')
                Menu3.opera.set_tooltip_text("Opera is installed.\nClick to remove it.")

    @staticmethod
    def on_pidgin_clicked(self):
        if os.path.isfile(find.program['pidgin']):
            os.system('pacman -R pidgin --noconfirm')
            if not os.path.isfile(find.program['pidgin']):
                Img.pidgin_img.set_from_file('./categories/gtk-no.png')
                dial('Pidgin','2')
                Menu3.pidgin.set_tooltip_text("Pidgin is not installed.\nClick to install it.")
        else:
            os.system('pacman -S pidgin --noconfirm')
            if os.path.isfile(find.program['pidgin']):
                Img.pidgin_img.set_from_file('./categories/gtk-yes.png')
                dial('Pidgin','1')
                Menu3.pidgin.set_tooltip_text("Pidgin is installed.\nClick to remove it.")

    @staticmethod
    def on_skyp_clicked(self):
        if os.path.isfile(find.program['skype']):
            os.system('pacman -R skype --noconfirm')
            if not os.path.isfile(find.program['skype']):
                Img.skype_img.set_from_file('./categories/gtk-no.png')
                dial('Skype','2')
                Menu3.skyp.set_tooltip_text("Skype is not installed.\nClick to install it.")
        else:
            os.system('pacman -S skype --noconfirm')
            if os.path.isfile(find.program['skype']):
                Img.skype_img.set_from_file('./categories/gtk-yes.png')
                dial('Skype','1')
                Menu3.skyp.set_tooltip_text("Skype is installed.\nClick to remove it.")

    @staticmethod
    def on_steam_clicked(self):
        if os.path.isfile(find.program['steam']):
            os.system('pacman -R steam --noconfirm')
            if not os.path.isfile(find.program['steam']):
                Img.steam_img.set_from_file('./categories/gtk-no.png')
                dial('Steam','2')
                Menu3.steam.set_tooltip_text("Steam is not installed.\nClick to install it.")
        else:
            os.system('pacman -S steam --noconfirm')
            if os.path.isfile(find.program['steam']):
                Img.steam_img.set_from_file('./categories/gtk-yes.png')
                dial('Steam','1')
                Menu3.steam.set_tooltip_text("Steam is installed.\nClick to remove it.")

    @staticmethod
    def on_thunderbird_clicked(self):
        if os.path.isfile(find.program['thunderbird']):
            os.system('pacman -R thunderbird --noconfirm')
            if not os.path.isfile(find.program['thunderbird']):
                Img.thunderbird_img.set_from_file('./categories/gtk-no.png')
                dial('Thunderbird','2')
                Menu3.thunderbird.set_tooltip_text("Thunderbird is not installed.\nClick to install it.")
        else:
            os.system('pacman -S thunderbird --noconfirm')
            if os.path.isfile(find.program['thunderbird']):
                Img.thunderbird_img.set_from_file('./categories/gtk-yes.png')
                dial('Thunderbird','1')
                Menu3.thunderbird.set_tooltip_text("Thunderbird is not installed.\nClick to install it.")

    @staticmethod
    def on_transmission_clicked(self):
        if os.path.isfile(find.program['transmission']):
            os.system('pacman -R transmission-gtk --noconfirm')
            if not os.path.isfile(find.program['transmission']):
                Img.transmission_img.set_from_file('./categories/gtk-no.png')
                dial('Transmission','2')
                Menu3.transmission.set_tooltip_text("Transmission is not installed.\nClick to install it.")
        else:
            os.system('pacman -S transmission-gtk --noconfirm')
            if os.path.isfile(find.program['transmission']):
                Img.transmission_img.set_from_file('./categories/gtk-yes.png')
                dial('Transmission','1')
                Menu3.transmission.set_tooltip_text("Transmission is installed.\nClick to remove it.")

    @staticmethod
    # menu 2 button actions
    def on_evince_clicked(self):
        if os.path.isfile(find.program['evince']):
            os.system('pacman -R evince --noconfirm')
            if not os.path.isfile(find.program['evince']):
                Img.evince_img.set_from_file('./categories/gtk-no.png')
                dial('Evince','2')
                Menu2.evince.set_tooltip_text("Evince is not installed.\nClick to install it.")
        else:
            os.system('pacman -S evince --noconfirm')
            if os.path.isfile(find.program['evince']):
                Img.evince_img.set_from_file('./categories/gtk-yes.png')
                dial('Evince','1')
                Menu2.evince.set_tooltip_text("Evince is installed.\nClick to remove it.")

    @staticmethod
    def on_f_spot_clicked(self):
        if os.path.isfile(find.program['f-spot']):
            os.system('pacman -R f-spot --noconfirm')
            if not os.path.isfile(find.program['f-spot']):
                Img.f_spot_img.set_from_file('./categories/gtk-no.png')
                dial('F-spot','2')
                Menu2.f_spot.set_tooltip_text("F-spot is not installed.\nClick to install it.")
        else:
            os.system('pacman -S f-spot --noconfirm')
            if os.path.isfile(find.program['f-spot']):
                Img.f_spot_img.set_from_file('./categories/gtk-yes.png')
                dial('F-spot','1')
                Menu2.f_spot.set_tooltip_text("F-spot is installed.\nClick to remove it.")

    @staticmethod
    def on_gimp_clicked(self):
        if os.path.isfile(find.program['gimp']):
            os.system('pacman -R gimp --noconfirm')
            if not os.path.isfile(find.program['gimp']):
                Img.gimp_img.set_from_file('./categories/gtk-no.png')
                dial('Gimp','2')
                Menu2.gimp.set_tooltip_text("GIMP is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gimp --noconfirm')
            if os.path.isfile(find.program['gimp']):
                Img.gimp_img.set_from_file('./categories/gtk-yes.png')
                dial('Gimp','1')
                Menu2.gimp.set_tooltip_text("GIMP is installed.\nClick to remove it.")

    @staticmethod
    def on_gwenview_clicked(self):
        if os.path.isfile(find.program['gwenview']):
            os.system('pacman -R gwenview --noconfirm')
            if not os.path.isfile(find.program['gwenview']):
                Img.gwenview_img.set_from_file('./categories/gtk-no.png')
                dial('Gwenview','2')
                Menu2.gwenview.set_tooltip_text("Gwenview is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gwenview --noconfirm')
            if os.path.isfile(find.program['gwenview']):
                Img.gwenview_img.set_from_file('./categories/gtk-yes.png')
                dial('Gwenview','1')
                Menu2.gwenview.set_tooltip_text("Gwenview is installed.\nClick to remove it.")

    @staticmethod
    def on_imagemagick_clicked(self):
        if os.path.isfile(find.program['imagemagick']):
            os.system('pacman -Rdd imagemagick --noconfirm')
            if not os.path.isfile(find.program['imagemagick']):
                Img.imagemagick_img.set_from_file('./categories/gtk-no.png')
                dial('ImageMagick','2')
                Menu2.imagemagick.set_tooltip_text("ImageMagick is not installed.\nClick to install it.")
        else:
            os.system('pacman -S imagemagick --noconfirm')
            if os.path.isfile(find.program['imagemagick']):
                Img.imagemagick_img.set_from_file('./categories/gtk-yes.png')
                dial('ImageMagick','1')
                Menu2.imagemagick.set_tooltip_text("ImageMagick is installed.\nClick to remove it.")

    @staticmethod
    def on_inkscape_clicked(self):
        if os.path.isfile(find.program['inkscape']):
            os.system('pacman -R inkscape --noconfirm')
            if not os.path.isfile(find.program['inkscape']):
                Img.inkscape_img.set_from_file('./categories/gtk-no.png')
                dial('Inkscape','2')
                Menu2.inkscape.set_tooltip_text("Inkscape is not installed.\nClick to install it.")
        else:
            os.system('pacman -S inkscape --noconfirm')
            if os.path.isfile(find.program['inkscape']):
                Img.inkscape_img.set_from_file('./categories/gtk-yes.png')
                dial('Inkscape','1')
                Menu2.inkscape.set_tooltip_text("Inkscape is installed.\nClick to remove it.")

    @staticmethod
    def on_mypaint_clicked(self):
        if os.path.isfile(find.program['mypaint']):
            os.system('pacman -R mypaint --noconfirm')
            if not os.path.isfile(find.program['mypaint']):
                Img.mypaint_img.set_from_file('./categories/gtk-no.png')
                dial('MyPaint','2')
                Menu2.mypaint.set_tooltip_text("MyPaint is not installed.\nClick to install it.")
        else:
            os.system('pacman -S mypaint --noconfirm')
            if os.path.isfile(find.program['mypaint']):
                Img.mypaint_img.set_from_file('./categories/gtk-yes.png')
                dial('MyPaint','1')
                Menu2.mypaint.set_tooltip_text("MyPaint is installed.\nClick to remove it.")

    @staticmethod
    def on_pinta_clicked(self):
        if os.path.isfile(find.program['pinta']):
            os.system('pacman -R pinta --noconfirm')
            if not os.path.isfile(find.program['pinta']):
                Img.pinta_img.set_from_file('./categories/gtk-no.png')
                dial('Pinta','2')
                Menu2.pinta.set_tooltip_text("Pinta is not installed.\nClick to install it.")
        else:
            os.system('pacman -S pinta --noconfirm')
            if os.path.isfile(find.program['pinta']):
                Img.pinta_img.set_from_file('./categories/gtk-yes.png')
                dial('Pinta','1')
                Menu2.pinta.set_tooltip_text("Pinta is installed.\nClick to remove it.")

    @staticmethod
    def on_shotwell_clicked(self):
        if os.path.isfile(find.program['shotwell']):
            os.system('pacman -R shotwell --noconfirm')
            if not os.path.isfile(find.program['shotwell']):
                Img.shotwell_img.set_from_file('./categories/gtk-no.png')
                dial('Shotwell','2')
                Menu2.shotwell.set_tooltip_text("Shotwell is not installed.\nClick to install it.")
        else:
            os.system('pacman -S shotwell --noconfirm')
            if os.path.isfile(find.program['shotwell']):
                Img.shotwell_img.set_from_file('./categories/gtk-yes.png')
                dial('Shotwell','1')
                Menu2.shotwell.set_tooltip_text("Shotwell is installed.\nClick to remove it.")

    def on_stellarium_clicked(self):
        if os.path.isfile(find.program['stellarium']):
            os.system('pacman -R stellarium --noconfirm')
            if not os.path.isfile(find.program['stellarium']):
                Img.stellarium_img.set_from_file('./categories/gtk-no.png')
                dial('Stellarium','2')
                Menu2.stellarium.set_tooltip_text("Stellarium is not installed.\nClick to install it.")
        else:
            os.system('pacman -S stellarium --noconfirm')
            if os.path.isfile(find.program['stellarium']):
                Img.stellarium_img.set_from_file('./categories/gtk-yes.png')
                dial('Stellarium','1')
                Menu2.stellarium.set_tooltip_text("Stellarium is installed.\nClick to remove it.")

    @staticmethod
    # menu 1 button actions
    def on_anjuta_clicked(self):
        if os.path.isfile(find.program['anjuta']):
            os.system('pacman -R anjuta --noconfirm')
            if not os.path.isfile(find.program['anjuta']):
                Img.anjuta_img.set_from_file('./categories/gtk-no.png')
                dial('Anjuta','2')
                Menu1.anjuta.set_tooltip_text("Anjuta is not installed.\nClick to install it.")
        else:
            os.system('pacman -S anjuta --noconfirm')
            if os.path.isfile(find.program['anjuta']):
                Img.anjuta_img.set_from_file('./categories/gtk-yes.png')
                dial('Anjuta','1')
                Menu1.anjuta.set_tooltip_text("Anjuta is installed.\nClick to remove it.")

    @staticmethod
    def on_blender_clicked(self):
        if os.path.isfile(find.program['blender']):
            os.system('pacman -R blender --noconfirm')
            if not os.path.isfile(find.program['blender']):
                Img.blender_img.set_from_file('./categories/gtk-no.png')
                dial('Blender','2')
                Menu1.blender.set_tooltip_text("Blender is not installed.\nClick to install it.")
        else:
            os.system('pacman -S blender --noconfirm')
            if os.path.isfile(find.program['blender']):
                Img.blender_img.set_from_file('./categories/gtk-yes.png')
                dial('Blender','1')
                Menu1.blender.set_tooltip_text("Blender is installed.\nClick to remove it.")

    @staticmethod
    def on_bluefish_clicked(self):
        if os.path.isfile(find.program['bluefish']):
            os.system('pacman -R bluefish --noconfirm')
            if not os.path.isfile(find.program['bluefish']):
                Img.bluefish_img.set_from_file('./categories/gtk-no.png')
                dial('Bluefish','2')
                Menu1.bluefish.set_tooltip_text("Bluefish is not installed.\nClick to install it.")
        else:
            os.system('pacman -S bluefish --noconfirm')
            if os.path.isfile(find.program['bluefish']):
                Img.bluefish_img.set_from_file('./categories/gtk-yes.png')
                dial('Bluefish','1')
                Menu1.bluefish.set_tooltip_text("Bluefish is installed.\nClick to remove it.")

    @staticmethod
    def on_eclipse_clicked(self):
        if os.path.isfile(find.program['eclipse']):
            os.system('pacman -R eclipse --noconfirm')
            if not os.path.isfile(find.program['eclipse']):
                Img.eclipse_img.set_from_file('./categories/gtk-no.png')
                dial('Eclipse','2')
                Menu1.eclipse.set_tooltip_text("Eclipse is not installed.\nClick to install it.")
        else:
            os.system('pacman -S eclipse --noconfirm')
            if os.path.isfile(find.program['eclipse']):
                Img.eclipse_img.set_from_file('./categories/gtk-yes.png')
                dial('Eclipse','1')
                Menu1.eclipse.set_tooltip_text("Eclipse is installed.\nClick to remove it.")

    @staticmethod
    def on_geany_clicked(self):
        if os.path.isfile(find.program['geany']):
            os.system('pacman -R geany --noconfirm')
            if not os.path.isfile(find.program['geany']):
                Img.geany_img.set_from_file('./categories/gtk-no.png')
                dial('Geany','2')
                Menu1.geany.set_tooltip_text("Geany is not installed.\nClick to install it.")
        else:
            os.system('pacman -S geany --noconfirm')
            if os.path.isfile(find.program['geany']):
                Img.geany_img.set_from_file('./categories/gtk-yes.png')
                dial('Geany','1')
                Menu1.geany.set_tooltip_text("Geany is installed.\nClick to remove it.")

    @staticmethod
    def on_glade_clicked(self):
        if os.path.isfile(find.program['glade']):
            os.system('pacman -R glade --noconfirm')
            if not os.path.isfile(find.program['glade']):
                Img.glade_img.set_from_file('./categories/gtk-no.png')
                dial('Glade','2')
                Menu1.glade.set_tooltip_text("Glade is not installed.\nClick to install it.")
        else:
            os.system('pacman -S glade --noconfirm')
            if os.path.isfile(find.program['glade']):
                Img.glade_img.set_from_file('./categories/gtk-yes.png')
                dial('Glade','1')
                Menu1.glade.set_tooltip_text("Glade is installed.\nClick to remove it.")

    @staticmethod
    def on_openjdk_clicked(self):
        if os.path.exists(find.program['openjdk']):
            os.system('pacman -R jre7-openjdk --noconfirm')
            if not os.path.exists(find.program['openjdk']):
                Img.openjdk_img.set_from_file('./categories/gtk-no.png')
                dial('OpenJDK','2')
                Menu1.openjdk.set_tooltip_text("OpenJDK is not installed.\nClick to install it.")
        else:
            os.system('pacman -S jre7-openjdk --noconfirm')
            if os.path.exists(find.program['openjdk']):
                Img.openjdk_img.set_from_file('./categories/gtk-yes.png')
                dial('OpenJDK','1')
                Menu1.openjdk.set_tooltip_text("OpenJDK is installed.\nClick to remove it.")

    @staticmethod
    def on_meld_clicked(self):
        if os.path.isfile(find.program['meld']):
            os.system('pacman -R meld --noconfirm')
            if not os.path.isfile(find.program['meld']):
                Img.meld_img.set_from_file('./categories/gtk-no.png')
                dial('Meld','2')
                Menu1.meld.set_tooltip_text("Meld is not installed.\nClick to install it.")
        else:
            os.system('pacman -S meld --noconfirm')
            if os.path.isfile(find.program['meld']):
                Img.meld_img.set_from_file('./categories/gtk-yes.png')
                dial('Meld','1')
                Menu1.meld.set_tooltip_text("Meld is installed.\nClick to remove it.")

    @staticmethod
    def on_netbeans_clicked(self):
        if os.path.isfile(find.program['netbeans']):
            os.system('pacman -R netbeans --noconfirm')
            if not os.path.isfile(find.program['netbeans']):
                Img.netbeans_img.set_from_file('./categories/gtk-no.png')
                dial('NetBeans','2')
                Menu1.netbeans.set_tooltip_text("NetBeans is not installed.\nClick to install it.")
        else:
            os.system('pacman -S netbeans --noconfirm')
            if os.path.isfile(find.program['netbeans']):
                Img.netbeans_img.set_from_file('./categories/gtk-yes.png')
                dial('NetBeans','1')
                Menu1.netbeans.set_tooltip_text("NetBeans is installed.\nClick to remove it.")

    @staticmethod
    def on_qt4_clicked(self):
        if os.path.isfile(find.program['qt4']):
            os.system('pacman -R qt4 --noconfirm')
            if not os.path.isfile(find.program['qt4']):
                Img.qt4_img.set_from_file('./categories/gtk-no.png')
                dial('Qt4','2')
                Menu1.qt4.set_tooltip_text("Qt4 is not installed.\nClick to install it.")
        else:
            os.system('pacman -S qt4 --noconfirm')
            if os.path.isfile(find.program['qt4']):
                Img.qt4_img.set_from_file('./categories/gtk-yes.png')
                dial('Qt4','1')
                Menu1.qt4.set_tooltip_text("Qt4 is installed.\nClick to remove it.")

    @staticmethod
    def on_qt5_clicked(self):
        if os.path.isfile(find.program['qt5']):
            os.system('pacman -R qt5-base --noconfirm')
            if not os.path.isfile(find.program['qt5']):
                Img.qt5_img.set_from_file('./categories/gtk-no.png')
                dial('Qt5','2')
                Menu1.qt5.set_tooltip_text("Qt5 is not installed.\nClick to install it.")
        else:
            os.system('pacman -S qt5-base --noconfirm')
            if os.path.isfile(find.program['qt5']):
                Img.qt5_img.set_from_file('./categories/gtk-yes.png')
                dial('Qt5','1')
                Menu1.qt5.set_tooltip_text("Qt5 is installed.\nClick to remove it.")

    @staticmethod
    def on_qtcreator_clicked(self):
        if os.path.isfile(find.program['qtcreator']):
            os.system('pacman -R qtcreator --noconfirm')
            if not os.path.isfile(find.program['qtcreator']):
                Img.qtcreator_img.set_from_file('./categories/gtk-no.png')
                dial('QtCreator','2')
                Menu1.qtcreator.set_tooltip_text("QtCreator is not installed.\nClick to install it.")
        else:
            os.system('pacman -S qtcreator --noconfirm')
            if os.path.isfile(find.program['qtcreator']):
                Img.qtcreator_img.set_from_file('./categories/gtk-yes.png')
                dial('QtCreator','1')
                Menu1.qtcreator.set_tooltip_text("QtCreator is installed.\nClick to remove it.")

    @staticmethod
    def on_ninja_ide_clicked(self):
        if os.path.isfile(find.program['ninja-ide']):
            os.system('pacman -R ninja-ide --noconfirm')
            if not os.path.isfile(find.program['ninja-ide']):
                Img.ninja_ide_img.set_from_file('./categories/gtk-no.png')
                dial('Ninja-IDE','2')
                Menu1.ninja_ide.set_tooltip_text("Ninja-IDE is not installed.\nClick to install it.")
        else:
            os.system('pacman -S ninja-ide --noconfirm')
            if os.path.isfile(find.program['ninja-ide']):
                Img.ninja_ide_img.set_from_file('./categories/gtk-yes.png')
                dial('Ninja-IDE','1')
                Menu1.ninja_ide.set_tooltip_text("Ninja-IDE is installed.\nClick to remove it.")