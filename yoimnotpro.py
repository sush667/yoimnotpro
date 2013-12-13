#!/usr/bin/python2
import os
import cairo
from gi.repository import Gtk, GdkPixbuf

class iod:

    # menu 7 button actions
    def on_geany__clicked(self, widget):
        if os.path.isfile("/usr/bin/geany"):
            os.system('xterm -e "sudo pacman -R geany"')
            if not os.path.isfile("/usr/bin/geany"):
                self.geany__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S geany"')
            if os.path.isfile("/usr/bin/geany"):
                self.geany__img.set_from_file('categories/gtk-yes.png')

    def on_blender__clicked(self, widget):
        if os.path.isfile("/usr/bin/blender"):
            os.system('xterm -e "sudo pacman -R blender"')
            if not os.path.isfile("/usr/bin/audacious"):
                self.blender__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S blender"')
            if os.path.isfile("/usr/bin/blender"):
                self.blender__img.set_from_file('categories/gtk-yes.png')

    def on_ninja_ide__clicked(self, widget):
        if os.path.isfile("/usr/bin/ninja-ide"):
            os.system('xterm -e "sudo pacman -R ninja-ide"')
            if not os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S banshee"')
            if os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide__img.set_from_file('categories/gtk-yes.png')

    def on_glade__clicked(self, widget):
        if os.path.isfile("/usr/bin/glade"):
            os.system('xterm -e "sudo pacman -R glade"')
            if not os.path.isfile("/usr/bin/glade"):
                self.glade__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S glade"')
            if os.path.isfile("/usr/bin/glade"):
                self.glade__img.set_from_file('categories/gtk-yes.png')

    def on_audacious__clicked(self, widget):
        if os.path.isfile("/usr/bin/audacious"):
            os.system('xterm -e "sudo pacman -R audacious"')
            if not os.path.isfile("/usr/bin/audacious"):
                self.audacious__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S audacious"')
            if os.path.isfile("/usr/bin/audacious"):
                self.audacious__img.set_from_file('categories/gtk-yes.png')

    def on_gimp__clicked(self, widget):
        if os.path.isfile("/usr/bin/gimp"):
            os.system('xterm -e "sudo pacman -R gimp"')
            if not os.path.isfile("/usr/bin/gimp"):
                self.gimp__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S gimp"')
            if os.path.isfile("/usr/bin/gimp"):
                self.gimp__img.set_from_file('categories/gtk-yes.png')

    def on_evince__clicked(self, widget):
        if os.path.isfile("/usr/bin/evince"):
            os.system('xterm -e "sudo pacman -R evince"')
            if not os.path.isfile("/usr/bin/evince"):
                self.evince__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S evince"')
            if os.path.isfile("/usr/bin/evince"):
                self.evince__img.set_from_file('categories/gtk-yes.png')

    def on_xfburn__clicked(self, widget):
        if os.path.isfile("/usr/bin/xfburn"):
            os.system('xterm -e "sudo pacman -R xfburn"')
            if not os.path.isfile("/usr/bin/xfburn"):
                self.xfburn__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S xfburn"')
            if os.path.isfile("/usr/bin/xfburn"):
                self.xfburn__img.set_from_file('categories/gtk-yes.png')

    def on_flashplayer__clicked(self, widget):
        if os.path.isfile("/usr/bin/flash-player-properties"):
            os.system('xterm -e "sudo pacman -R flashplugin"')
            if not os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S flashplugin"')
            if os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer__img.set_from_file('categories/gtk-yes.png')

    def on_openshot__clicked(self, widget):
        if os.path.isfile("/usr/bin/openshot"):
            os.system('xterm -e "sudo pacman -R openshot"')
            if not os.path.isfile("/usr/bin/openshot"):
                self.openshot__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S openshot"')
            if os.path.isfile("/usr/bin/openshot"):
                self.openshot__img.set_from_file('categories/gtk-yes.png')

    def on_chromium__clicked(self, widget):
        if os.path.isfile("/usr/bin/chromium"):
            os.system('xterm -e "sudo pacman -R chromium"')
            if not os.path.isfile("/usr/bin/chromium"):
                self.chromium__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S chromium"')
            if os.path.isfile("/usr/bin/chromium"):
                self.chromium__img.set_from_file('categories/gtk-yes.png')

    def on_deluge__clicked(self, widget):
        if os.path.isfile("/usr/bin/deluge"):
            os.system('xterm -e "sudo pacman -R deluge"')
            if not os.path.isfile("/usr/bin/deluge"):
                self.deluge__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S deluge"')
            if os.path.isfile("/usr/bin/deluge"):
                self.deluge__img.set_from_file('categories/gtk-yes.png')

    def on_liferea__clicked(self, widget):
        if os.path.isfile("/usr/bin/liferea"):
            os.system('xterm -e "sudo pacman -R liferea"')
            if not os.path.isfile("/usr/bin/liferea"):
                self.liferea__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S liferea"')
            if os.path.isfile("/usr/bin/liferea"):
                self.liferea__img.set_from_file('categories/gtk-yes.png')

    def on_htop__clicked(self, widget):
        if os.path.isfile("/usr/bin/htop"):
            os.system('xterm -e "sudo pacman -R htop"')
            if not os.path.isfile("/usr/bin/htop"):
                self.htop__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S htop"')
            if os.path.isfile("/usr/bin/htop"):
                self.htop__img.set_from_file('categories/gtk-yes.png')

    def on_skype__clicked(self, widget):
        if os.path.isfile("/usr/bin/skype"):
            os.system('xterm -e "sudo pacman -R skype"')
            if not os.path.isfile("/usr/bin/skype"):
                self.skype__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S skype"')
            if os.path.isfile("/usr/bin/skype"):
                self.skype__img.set_from_file('categories/gtk-yes.png')

    def on_wireshark__clicked(self, widget):
        if os.path.isfile("/usr/bin/wireshark"):
            os.system('xterm -e "sudo pacman -R wireshark-gtk"')
            if not os.path.isfile("/usr/bin/wireshark"):
                self.wireshark__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S wireshark-gtk"')
            if os.path.isfile("/usr/bin/wireshark"):
                self.wireshark__img.set_from_file('categories/gtk-yes.png')

    def on_virtualbox__clicked(self, widget):
        if os.path.isfile("/usr/bin/virtualbox"):
            os.system('xterm -e "sudo pacman -R virtualbox"')
            if not os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S virtualbox"')
            if os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox__img.set_from_file('categories/gtk-yes.png')

    def on_steam__clicked(self, widget):
        if os.path.isfile("/usr/bin/steam"):
            os.system('xterm -e "sudo pacman -R steam"')
            if not os.path.isfile("/usr/bin/steam"):
                self.steam__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S steam"')
            if os.path.isfile("/usr/bin/steam"):
                self.steam__img.set_from_file('categories/gtk-yes.png')

    def on_xchat__clicked(self, widget):
        if os.path.isfile("/usr/bin/xchat"):
            os.system('xterm -e "sudo pacman -R xchat"')
            if not os.path.isfile("/usr/bin/xchat"):
                self.xchat__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S xchat"')
            if os.path.isfile("/usr/bin/xchat"):
                self.xchat__img.set_from_file('categories/gtk-yes.png')

    def on_gedit__clicked(self, widget):
        if os.path.isfile("/usr/bin/gedit"):
            os.system('xterm -e "sudo pacman -R gedit"')
            if not os.path.isfile("/usr/bin/gedit"):
                self.gedit__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S gedit"')
            if os.path.isfile("/usr/bin/gedit"):
                self.gedit__img.set_from_file('categories/gtk-yes.png')

    # menu 6 button actions
    def on_docky_clicked(self, widget):
        if os.path.isfile("/usr/bin/docky"):
            os.system('xterm -e "sudo pacman -R docky"')
            if not os.path.isfile("/usr/bin/docky"):
                self.docky_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S docky"')
            if os.path.isfile("/usr/bin/docky"):
                self.docky_img.set_from_file('categories/gtk-yes.png')

    def on_emacs_clicked(self, widget):
        if os.path.isfile("/usr/bin/emacs"):
            os.system('xterm -e "sudo pacman -R emacs"')
            if not os.path.isfile("/usr/bin/emacs"):
                self.emacs_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S emacs"')
            if os.path.isfile("/usr/bin/emacs"):
                self.emacs_img.set_from_file('categories/gtk-yes.png')

    def on_vim_clicked(self, widget):
        if os.path.isfile("/usr/bin/vim"):
            os.system('xterm -e "sudo pacman -R vim"')
            if not os.path.isfile("/usr/bin/vim"):
                self.vim_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S vim"')
            if os.path.isfile("/usr/bin/vim"):
                self.vim_img.set_from_file('categories/gtk-yes.png')

    def on_galculator_clicked(self, widget):
        if os.path.isfile("/usr/bin/galculator"):
            os.system('xterm -e "sudo pacman -R galculator"')
            if not os.path.isfile("/usr/bin/galculator"):
                self.galculator_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S galculator"')
            if os.path.isfile("/usr/bin/galculator"):
                self.galculator_img.set_from_file('categories/gtk-yes.png')

    def on_gedit_clicked(self, widget):
        if os.path.isfile("/usr/bin/gedit"):
            os.system('xterm -e "sudo pacman -R gedit"')
            if not os.path.isfile("/usr/bin/gedit"):
                self.gedit_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S gedit"')
            if os.path.isfile("/usr/bin/gedit"):
                self.gedit_img.set_from_file('categories/gtk-yes.png')

    def on_gloobus_clicked(self, widget):
        if os.path.isfile("/usr/bin/gloobus-preview"):
            os.system('xterm -e "sudo pacman -R gloobus-preview"')
            if not os.path.isfile("/usr/bin/gloobus-preview"):
                self.gloobus_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S gloobus-preview"')
            if os.path.isfile("/usr/bin/gloobus-preview"):
                self.gloobus_img.set_from_file('categories/gtk-yes.png')

    def on_leafpad_clicked(self, widget):
        if os.path.isfile("/usr/bin/leafpad"):
            os.system('xterm -e "sudo pacman -R leafpad"')
            if not os.path.isfile("/usr/bin/leafpad"):
                self.leafpad_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S leafpad"')
            if os.path.isfile("/usr/bin/leafpad"):
                self.leafpad_img.set_from_file('categories/gtk-yes.png')

    def on_scribes_clicked(self, widget):
        if os.path.isfile("/usr/bin/scribes"):
            os.system('xterm -e "sudo pacman -R scribes"')
            if not os.path.isfile("/usr/bin/scribes"):
                self.scribes_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S scribes"')
            if os.path.isfile("/usr/bin/scribes"):
                self.scribes_img.set_from_file('categories/gtk-yes.png')

    def on_tomboy_clicked(self, widget):
        if os.path.isfile("/usr/bin/tomboy"):
            os.system('xterm -e "sudo pacman -R tomboy"')
            if not os.path.isfile("/usr/bin/tomboy"):
                self.tomboy_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S tomboy"')
            if os.path.isfile("/usr/bin/tomboy"):
                self.tomboy_img.set_from_file('categories/gtk-yes.png')

    def on_tuxcards_clicked(self, widget):
        if os.path.isfile("/usr/bin/tuxcards"):
            os.system('xterm -e "sudo pacman -R tuxcards"')
            if not os.path.isfile("/usr/bin/tuxcards"):
                self.tuxcards_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S tuxcards"')
            if os.path.isfile("/usr/bin/tuxcards"):
                self.tuxcards_img.set_from_file('categories/gtk-yes.png')

    # menu 5 button actions
    def on_gparted_clicked(self, widget):
        if os.path.isfile("/usr/bin/gparted"):
            os.system('xterm -e "sudo pacman -R gparted"')
            if not os.path.isfile("/usr/bin/gparted"):
                self.gparted_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S gparted"')
            if os.path.isfile("/usr/bin/gparted"):
                self.gparted_img.set_from_file('categories/gtk-yes.png')

    def on_guake_clicked(self, widget):
        if os.path.isfile("/usr/bin/guake"):
            os.system('xterm -e "sudo pacman -R guake"')
            if not os.path.isfile("/usr/bin/guake"):
                self.guake_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S guake"')
            if os.path.isfile("/usr/bin/guake"):
                self.guake_img.set_from_file('categories/gtk-yes.png')

    def on_hardinfo_clicked(self, widget):
        if os.path.isfile("/usr/bin/hardinfo"):
            os.system('xterm -e "sudo pacman -R hardinfo"')
            if not os.path.isfile("/usr/bin/hardinfo"):
                self.hardinfo_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S hardinfo"')
            if os.path.isfile("/usr/bin/hardinfo"):
                self.hardinfo_img.set_from_file('categories/gtk-yes.png')

    def on_htop_clicked(self, widget):
        if os.path.isfile("/usr/bin/htop"):
            os.system('xterm -e "sudo pacman -R htop"')
            if not os.path.isfile("/usr/bin/htop"):
                self.htop_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S htop"')
            if os.path.isfile("/usr/bin/htop"):
                self.htop_img.set_from_file('categories/gtk-yes.png')

    def on_keepassx_clicked(self, widget):
        if os.path.isfile("/usr/bin/keepassx"):
            os.system('xterm -e "sudo pacman -R keepassx"')
            if not os.path.isfile("/usr/bin/keepassx"):
                self.keepassx_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S keepassx"')
            if os.path.isfile("/usr/bin/keepassx"):
                self.keepassx_img.set_from_file('categories/gtk-yes.png')

    def on_playonlinux_clicked(self, widget):
        if os.path.isfile("/usr/bin/playonlinux"):
            os.system('xterm -e "sudo pacman -R playonlinux"')
            if not os.path.isfile("/usr/bin/playonlinux"):
                self.playonlinux_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S playonlinux"')
            if os.path.isfile("/usr/bin/playonlinux"):
                self.playonlinux_img.set_from_file('categories/gtk-yes.png')

    def on_terminator_clicked(self, widget):
        if os.path.isfile("/usr/bin/terminator"):
            os.system('xterm -e "sudo pacman -R terminator"')
            if not os.path.isfile("/usr/bin/terminator"):
                self.terminator_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S terminator"')
            if os.path.isfile("/usr/bin/terminator"):
                self.terminator_img.set_from_file('categories/gtk-yes.png')

    def on_thunar_clicked(self, widget):
        if os.path.isfile("/usr/bin/thunar"):
            os.system('xterm -e "sudo pacman -R thunar"')
            if not os.path.isfile("/usr/bin/thunar"):
                self.thunar_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S thunar"')
            if os.path.isfile("/usr/bin/thunar"):
                self.thunar_img.set_from_file('categories/gtk-yes.png')

    def on_truecrypt_clicked(self, widget):
        if os.path.isfile("/usr/bin/truecrypt"):
            os.system('xterm -e "sudo pacman -R truecrypt"')
            if not os.path.isfile("/usr/bin/truecrypt"):
                self.truecrypt_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S truecrypt"')
            if os.path.isfile("/usr/bin/truecrypt"):
                self.truecrypt_img.set_from_file('categories/gtk-yes.png')

    def on_unetbootin_clicked(self, widget):
        if os.path.isfile("/usr/bin/unetbootin"):
            os.system('xterm -e "sudo pacman -R unetbootin"')
            if not os.path.isfile("/usr/bin/unetbootin"):
                self.unetbootin_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S unetbootin"')
            if os.path.isfile("/usr/bin/unetbootin"):
                self.unetbootin_img.set_from_file('categories/gtk-yes.png')

    def on_virtualbox_clicked(self, widget):
        if os.path.isfile("/usr/bin/virtualbox"):
            os.system('xterm -e "sudo pacman -R virtualbox"')
            if not os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S virtualbox"')
            if os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox_img.set_from_file('categories/gtk-yes.png')

    def on_wine_clicked(self, widget):
        if os.path.isfile("/usr/bin/wine"):
            os.system('xterm -e "sudo pacman -R wine"')
            if not os.path.isfile("/usr/bin/wine"):
                self.wine_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S wine"')
            if os.path.isfile("/usr/bin/wine"):
                self.wine_img.set_from_file('categories/gtk-yes.png')

    def on_wireshark_clicked(self, widget):
        if os.path.isfile("/usr/bin/wireshark"):
            os.system('xterm -e "sudo pacman -R wireshark-gtk"')
            if not os.path.isfile("/usr/bin/wireshark"):
                self.wireshark_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S wireshark-gtk"')
            if os.path.isfile("/usr/bin/wireshark"):
                self.wireshark_img.set_from_file('categories/gtk-yes.png')

    def on_xbmc_clicked(self, widget):
        if os.path.isfile("/usr/bin/xbmc"):
            os.system('xterm -e "sudo pacman -R xbmc"')
            if not os.path.isfile("/usr/bin/xbmc"):
                self.xbmc_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S xbmc"')
            if os.path.isfile("/usr/bin/xbmc"):
                self.xbmc_img.set_from_file('categories/gtk-yes.png')

    # menu 4 button actions
    def on_amarok_clicked(self, widget):
        if os.path.isfile("/usr/bin/amarok"):
            os.system('xterm -e "sudo pacman -R amarok"')
            if not os.path.isfile("/usr/bin/amarok"):
                self.amarok_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S amarok"')
            if os.path.isfile("/usr/bin/amarok"):
                self.amarok_img.set_from_file('categories/gtk-yes.png')

    def on_audacious_clicked(self, widget):
        if os.path.isfile("/usr/bin/audacious"):
            os.system('xterm -e "sudo pacman -R audacious"')
            if not os.path.isfile("/usr/bin/audacious"):
                self.audacious_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S audacious"')
            if os.path.isfile("/usr/bin/audacious"):
                self.audacious_img.set_from_file('categories/gtk-yes.png')

    def on_banshee_clicked(self, widget):
        if os.path.isfile("/usr/bin/banshee"):
            os.system('xterm -e "sudo pacman -R banshee"')
            if not os.path.isfile("/usr/bin/banshee"):
                self.banshee_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S banshee"')
            if os.path.isfile("/usr/bin/banshee"):
                self.banshee_img.set_from_file('categories/gtk-yes.png')

    def on_cheese_clicked(self, widget):
        if os.path.isfile("/usr/bin/cheese"):
            os.system('xterm -e "sudo pacman -R cheese"')
            if not os.path.isfile("/usr/bin/cheese"):
                self.cheese_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S cheese"')
            if os.path.isfile("/usr/bin/cheese"):
                self.cheese_img.set_from_file('categories/gtk-yes.png')

    def on_clementine_clicked(self, widget):
        if os.path.isfile("/usr/bin/clementine"):
            os.system('xterm -e "sudo pacman -R clementine"')
            if not os.path.isfile("/usr/bin/clementine"):
                self.clementine_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S clementine"')
            if os.path.isfile("/usr/bin/clementine"):
                self.clementine_img.set_from_file('categories/gtk-yes.png')

    def on_flashplayer_clicked(self, widget):
        if os.path.isfile("/usr/bin/flash-player-properties"):
            os.system('xterm -e "sudo pacman -R flashplugin"')
            if not os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S flashplugin"')
            if os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer_img.set_from_file('categories/gtk-yes.png')

    def on_recordmydesktop_clicked(self, widget):
        if os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
            os.system('xterm -e "sudo pacman -R gtk-recordmydesktop"')
            if not os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
                self.recordmydesktop_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S gtk-recordmydesktop"')
            if os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
                self.recordmydesktop_img.set_from_file('categories/gtk-yes.png')

    def on_guayadeque_clicked(self, widget):
        if os.path.isfile("/usr/bin/guayadeque"):
            os.system('xterm -e "sudo pacman -R guayadeque"')
            if not os.path.isfile("/usr/bin/guayadeque"):
                self.guayadeque_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S guayadeque"')
            if os.path.isfile("/usr/bin/guayadeque"):
                self.guayadeque_img.set_from_file('categories/gtk-yes.png')

    def on_mplayer_clicked(self, widget):
        if os.path.isfile("/usr/bin/mplayer"):
            os.system('xterm -e "sudo pacman -R mplayer"')
            if not os.path.isfile("/usr/bin/mplayer"):
                self.mplayer_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S mplayer"')
            if os.path.isfile("/usr/bin/mplayer"):
                self.mplayer_img.set_from_file('categories/gtk-yes.png')

    def on_openshot_clicked(self, widget):
        if os.path.isfile("/usr/bin/openshot"):
            os.system('xterm -e "sudo pacman -R openshot"')
            if not os.path.isfile("/usr/bin/openshot"):
                self.openshot_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S openshot"')
            if os.path.isfile("/usr/bin/openshot"):
                self.openshot_img.set_from_file('categories/gtk-yes.png')

    def on_pitivi_clicked(self, widget):
        if os.path.isfile("/usr/bin/pitivi"):
            os.system('xterm -e "sudo pacman -R pitivi"')
            if not os.path.isfile("/usr/bin/pitivi"):
                self.pitivi_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S pitivi"')
            if os.path.isfile("/usr/bin/pitivi"):
                self.pitivi_img.set_from_file('categories/gtk-yes.png')

    def on_rhythmbox_clicked(self, widget):
        if os.path.isfile("/usr/bin/rhythmbox"):
            os.system('xterm -e "sudo pacman -R rhythmbox"')
            if not os.path.isfile("/usr/bin/rhythmbox"):
                self.rhythmbox_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S rhythmbox"')
            if os.path.isfile("/usr/bin/rhythmbox"):
                self.rhythmbox_img.set_from_file('categories/gtk-yes.png')

    def on_soundconverter_clicked(self, widget):
        if os.path.isfile("/usr/bin/soundconverter"):
            os.system('xterm -e "sudo pacman -R soundconverter"')
            if not os.path.isfile("/usr/bin/soundconverter"):
                self.soundconverter_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S soundconverter"')
            if os.path.isfile("/usr/bin/soundconverter"):
                self.soundconverter_img.set_from_file('categories/gtk-yes.png')

    def on_totem_clicked(self, widget):
        if os.path.isfile("/usr/bin/totem"):
            os.system('xterm -e "sudo pacman -R totem"')
            if not os.path.isfile("/usr/bin/totem"):
                self.totem_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S totem"')
            if os.path.isfile("/usr/bin/totem"):
                self.totem_img.set_from_file('categories/gtk-yes.png')

    def on_vlc_clicked(self, widget):
        if os.path.isfile("/usr/bin/vlc"):
            os.system('xterm -e "sudo pacman -R vlc"')
            if not os.path.isfile("/usr/bin/vlc"):
                self.vlc_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S vlc"')
            if os.path.isfile("/usr/bin/vlc"):
                self.vlc_img.set_from_file('categories/gtk-yes.png')

    def on_winff_clicked(self, widget):
        if os.path.isfile("/usr/bin/winff"):
            os.system('xterm -e "sudo pacman -R winff"')
            if not os.path.isfile("/usr/bin/winff"):
                self.winff_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S winff"')
            if os.path.isfile("/usr/bin/winff"):
                self.winff_img.set_from_file('categories/gtk-yes.png')

    def on_xfburn_clicked(self, widget):
        if os.path.isfile("/usr/bin/xfburn"):
            os.system('xterm -e "sudo pacman -R xfburn"')
            if not os.path.isfile("/usr/bin/xfburn"):
                self.xfburn_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S xfburn"')
            if os.path.isfile("/usr/bin/xfburn"):
                self.xfburn_img.set_from_file('categories/gtk-yes.png')

    # menu 3 button actions
    def on_chromium_clicked(self, widget):
        if os.path.isfile("/usr/bin/chromium"):
            os.system('xterm -e "sudo pacman -R chromium"')
            if not os.path.isfile("/usr/bin/chromium"):
                self.chromium_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S chromium"')
            if os.path.isfile("/usr/bin/chromium"):
                self.chromium_img.set_from_file('categories/gtk-yes.png')

    def on_deluge_clicked(self, widget):
        if os.path.isfile("/usr/bin/deluge"):
            os.system('xterm -e "sudo pacman -R deluge"')
            if not os.path.isfile("/usr/bin/deluge"):
                self.deluge_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S deluge"')
            if os.path.isfile("/usr/bin/deluge"):
                self.deluge_img.set_from_file('categories/gtk-yes.png')

    def on_evolution_clicked(self, widget):
        if os.path.isfile("/usr/bin/evolution"):
            os.system('xterm -e "sudo pacman -R evolution"')
            if not os.path.isfile("/usr/bin/evolution"):
                self.evolution_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S evolution"')
            if os.path.isfile("/usr/bin/evolution"):
                self.evolution_img.set_from_file('categories/gtk-yes.png')

    def on_filezilla_clicked(self, widget):
        if os.path.isfile("/usr/bin/filezilla"):
            os.system('xterm -e "sudo pacman -R filezilla"')
            if not os.path.isfile("/usr/bin/filezilla"):
                self.filezilla_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S filezilla"')
            if os.path.isfile("/usr/bin/filezilla"):
                self.filezilla_img.set_from_file('categories/gtk-yes.png')

    def on_firefox_clicked(self, widget):
        if os.path.isfile("/usr/bin/firefox"):
            os.system('xterm -e "sudo pacman -R firefox"')
            if not os.path.isfile("/usr/bin/firefox"):
                self.firefox_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S firefox"')
            if os.path.isfile("/usr/bin/firefox"):
                self.firefox_img.set_from_file('categories/gtk-yes.png')

    def on_chrome_clicked(self, widget):
        if os.path.isfile("/usr/bin/google-chrome-stable"):
            os.system('xterm -e "yaourt -R google-chrome"')
            if not os.path.isfile("/usr/bin/google-chrome-stable"):
                self.chrome_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "yaourt -S google-chrome"')
            if os.path.isfile("/usr/bin/google-chrome-stable"):
                self.chrome_img.set_from_file('categories/gtk-yes.png')

    def on_xchat_clicked(self, widget):
        if os.path.isfile("/usr/bin/xchat"):
            os.system('xterm -e "sudo pacman -R xchat"')
            if not os.path.isfile("/usr/bin/xchat"):
                self.xchat_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S xchat"')
            if os.path.isfile("/usr/bin/xchat"):
                self.xchat_img.set_from_file('categories/gtk-yes.png')

    def on_liferea_clicked(self, widget):
        if os.path.isfile("/usr/bin/liferea"):
            os.system('xterm -e "sudo pacman -R liferea"')
            if not os.path.isfile("/usr/bin/liferea"):
                self.liferea_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S liferea"')
            if os.path.isfile("/usr/bin/liferea"):
                self.liferea_img.set_from_file('categories/gtk-yes.png')

    def on_midori_clicked(self, widget):
        if os.path.isfile("/usr/bin/midori"):
            os.system('xterm -e "sudo pacman -R midori"')
            if not os.path.isfile("/usr/bin/midori"):
                self.midori_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S midori"')
            if os.path.isfile("/usr/bin/midori"):
                self.midori_img.set_from_file('categories/gtk-yes.png')

    def on_minitube_clicked(self, widget):
        if os.path.isfile("/usr/bin/minitube"):
            os.system('xterm -e "sudo pacman -R minitube"')
            if not os.path.isfile("/usr/bin/minitube"):
                self.minitube_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S minitube"')
            if os.path.isfile("/usr/bin/minitube"):
                self.minitube_img.set_from_file('categories/gtk-yes.png')

    def on_opera_clicked(self, widget):
        if os.path.isfile("/usr/bin/opera"):
            os.system('xterm -e "sudo pacman -R opera"')
            if not os.path.isfile("/usr/bin/opera"):
                self.opera_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S opera"')
            if os.path.isfile("/usr/bin/opera"):
                self.opera_img.set_from_file('categories/gtk-yes.png')

    def on_pidgin_clicked(self, widget):
        if os.path.isfile("/usr/bin/pidgin"):
            os.system('xterm -e "sudo pacman -R pidgin"')
            if not os.path.isfile("/usr/bin/pidgin"):
                self.pidgin_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S pidgin"')
            if os.path.isfile("/usr/bin/pidgin"):
                self.pidgin_img.set_from_file('categories/gtk-yes.png')

    def on_skyp_clicked(self, widget):
        if os.path.isfile("/usr/bin/skype"):
            os.system('xterm -e "sudo pacman -R skype"')
            if not os.path.isfile("/usr/bin/skype"):
                self.skype_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S skype"')
            if os.path.isfile("/usr/bin/skype"):
                self.skype_img.set_from_file('categories/gtk-yes.png')

    def on_steam_clicked(self, widget):
        if os.path.isfile("/usr/bin/steam"):
            os.system('xterm -e "sudo pacman -R steam"')
            if not os.path.isfile("/usr/bin/steam"):
                self.steam_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S steam"')
            if os.path.isfile("/usr/bin/steam"):
                self.steam_img.set_from_file('categories/gtk-yes.png')

    def on_thunderbird_clicked(self, widget):
        if os.path.isfile("/usr/bin/thunderbird"):
            os.system('xterm -e "sudo pacman -R thunderbird"')
            if not os.path.isfile("/usr/bin/thunderbird"):
                self.thunderbird_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S thunderbird"')
            if os.path.isfile("/usr/bin/thunderbird"):
                self.thunderbird_img.set_from_file('categories/gtk-yes.png')

    def on_transmission_clicked(self, widget):
        if os.path.isfile("/usr/bin/transmission-gtk"):
            os.system('xterm -e "sudo pacman -R transmission-gtk"')
            if not os.path.isfile("/usr/bin/transmission-gtk"):
                self.transmission_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S transmission-gtk"')
            if os.path.isfile("/usr/bin/transmission-gtk"):
                self.transmission_img.set_from_file('categories/gtk-yes.png')

    # menu 2 button actions
    def on_evince_clicked(self, widget):
        if os.path.isfile("/usr/bin/evince"):
            os.system('xterm -e "sudo pacman -R evince"')
            if not os.path.isfile("/usr/bin/evince"):
                self.evince_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S evince"')
            if os.path.isfile("/usr/bin/evince"):
                self.evince_img.set_from_file('categories/gtk-yes.png')

    def on_f_spot_clicked(self, widget):
        if os.path.isfile("/usr/bin/f-spot"):
            os.system('xterm -e "sudo pacman -R f-spot"')
            if not os.path.isfile("/usr/bin/f-spot"):
                self.f_spot_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S f-spot"')
            if os.path.isfile("/usr/bin/f-spot"):
                self.f_spot_img.set_from_file('categories/gtk-yes.png')

    def on_gimp_clicked(self, widget):
        if os.path.isfile("/usr/bin/gimp"):
            os.system('xterm -e "sudo pacman -R gimp"')
            if not os.path.isfile("/usr/bin/gimp"):
                self.gimp_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S gimp"')
            if os.path.isfile("/usr/bin/gimp"):
                self.gimp_img.set_from_file('categories/gtk-yes.png')

    def on_gwenview_clicked(self, widget):
        if os.path.isfile("/usr/bin/gwenview"):
            os.system('xterm -e "sudo pacman -R gwenview"')
            if not os.path.isfile("/usr/bin/gwenview"):
                self.gwenview_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S gwenview"')
            if os.path.isfile("/usr/bin/gwenview"):
                self.gwenview_img.set_from_file('categories/gtk-yes.png')

    def on_imagemagick_clicked(self, widget):
        if os.path.exists("/usr/share/licenses/imagemagick/"):
            os.system('xterm -e "sudo pacman -R imagemagick"')
            if not os.path.exists("/usr/share/licenses/imagemagick/"):
                self.imagemagick_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S imagemagick"')
            if os.path.exists("/usr/share/licenses/imagemagick/"):
                self.imagemagick_img.set_from_file('categories/gtk-yes.png')

    def on_inkscape_clicked(self, widget):
        if os.path.isfile("/usr/bin/inkscape"):
            os.system('xterm -e "sudo pacman -R inkscape"')
            if not os.path.isfile("/usr/bin/inkscape"):
                self.inkscape_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S inkscape"')
            if os.path.isfile("/usr/bin/inkscape"):
                self.inkscape_img.set_from_file('categories/gtk-yes.png')

    def on_mypaint_clicked(self, widget):
        if os.path.isfile("/usr/bin/mypaint"):
            os.system('xterm -e "sudo pacman -R mypaint"')
            if not os.path.isfile("/usr/bin/mypaint"):
                self.mypaint_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S mypaint"')
            if os.path.isfile("/usr/bin/mypaint"):
                self.mypaint_img.set_from_file('categories/gtk-yes.png')

    def on_pinta_clicked(self, widget):
        if os.path.isfile("/usr/bin/pinta"):
            os.system('xterm -e "sudo pacman -R pinta"')
            if not os.path.isfile("/usr/bin/pinta"):
                self.pinta_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S pinta"')
            if os.path.isfile("/usr/bin/pinta"):
                self.pinta_img.set_from_file('categories/gtk-yes.png')

    def on_shotwell_clicked(self, widget):
        if os.path.isfile("/usr/bin/shotwell"):
            os.system('xterm -e "sudo pacman -R shotwell"')
            if not os.path.isfile("/usr/bin/shotwell"):
                self.shotwell_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S shotwell"')
            if os.path.isfile("/usr/bin/shotwell"):
                self.shotwell_img.set_from_file('categories/gtk-yes.png')

    def on_stellarium_clicked(self, widget):
        if os.path.isfile("/usr/bin/stellarium"):
            os.system('xterm -e "sudo pacman -R stellarium"')
            if not os.path.isfile("/usr/bin/stellarium"):
                self.stellarium_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S stellarium"')
            if os.path.isfile("/usr/bin/stellarium"):
                self.stellarium_img.set_from_file('categories/gtk-yes.png')

    # menu 1 button actions
    def on_anjuta_clicked(self, widget):
        if os.path.isfile("/usr/bin/anjuta"):
            os.system('xterm -e "sudo pacman -R anjuta"')
            if not os.path.isfile("/usr/bin/anjuta"):
                self.anjuta_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S anjuta"')
            if os.path.isfile("/usr/bin/anjuta"):
                self.anjuta_img.set_from_file('categories/gtk-yes.png')

    def on_blender_clicked(self, widget):
        if os.path.isfile("/usr/bin/anjuta"):
            os.system('xterm -e "sudo pacman -R blender"')
            if not os.path.isfile("/usr/bin/anjuta"):
                self.blender_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S blender"')
            if os.path.isfile("/usr/bin/anjuta"):
                self.blender_img.set_from_file('categories/gtk-yes.png')

    def on_bluefish_clicked(self, widget):
        if os.path.isfile("/usr/bin/bluefish"):
            os.system('xterm -e "sudo pacman -R bluefish"')
            if not os.path.isfile("/usr/bin/bluefish"):
                self.bluefish_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S bluefish"')
            if os.path.isfile("/usr/bin/bluefish"):
                self.bluefish_img.set_from_file('categories/gtk-yes.png')

    def on_eclipse_clicked(self, widget):
        if os.path.isfile("/usr/bin/eclipse"):
            os.system('xterm -e "sudo pacman -R eclipse"')
            if not os.path.isfile("/usr/bin/eclipse"):
                self.eclipse_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S eclipse"')
            if os.path.isfile("/usr/bin/eclipse"):
                self.eclipse_img.set_from_file('categories/gtk-yes.png')

    def on_geany_clicked(self, widget):
        if os.path.isfile("/usr/bin/geany"):
            os.system('xterm -e "sudo pacman -R geany"')
            if not os.path.isfile("/usr/bin/geany"):
                self.geany_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S geany"')
            if os.path.isfile("/usr/bin/geany"):
                self.geany_img.set_from_file('categories/gtk-yes.png')

    def on_glade_clicked(self, widget):
        if os.path.isfile("/usr/bin/glade"):
            os.system('xterm -e "sudo pacman -R glade"')
            if not os.path.isfile("/usr/bin/glade"):
                self.glade_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S glade"')
            if os.path.isfile("/usr/bin/glade"):
                self.glade_img.set_from_file('categories/gtk-yes.png')

    def on_openjdk_clicked(self, widget):
        if os.path.exists("/etc/java-7-openjdk/"):
            os.system('xterm -e "sudo pacman -R jre7-openjdk"')
            if not os.path.exists("/etc/java-7-openjdk/"):
                self.openjdk_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S jre7-openjdk"')
            if os.path.exists("/etc/java-7-openjdk/"):
                self.openjdk_img.set_from_file('categories/gtk-yes.png')

    def on_meld_clicked(self, widget):
        if os.path.isfile("/usr/bin/meld"):
            os.system('xterm -e "sudo pacman -R meld"')
            if not os.path.isfile("/usr/bin/meld"):
                self.meld_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S meld"')
            if os.path.isfile("/usr/bin/meld"):
                self.meld_img.set_from_file('categories/gtk-yes.png')

    def on_netbeans_clicked(self, widget):
        if os.path.isfile("/usr/bin/netbeans"):
            os.system('xterm -e "sudo pacman -R netbeans"')
            if not os.path.isfile("/usr/bin/netbeans"):
                self.netbeans_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S netbeans"')
            if os.path.isfile("/usr/bin/netbeans"):
                self.netbeans_img.set_from_file('categories/gtk-yes.png')

    def on_qt4_clicked(self, widget):
        if os.path.exists("/usr/share/qt4/"):
            os.system('xterm -e "sudo pacman -R qt4"')
            if not os.path.exists("/usr/share/qt4/"):
                self.qt4_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S qt4"')
            if os.path.exists("/usr/share/qt4/"):
                self.qt4_img.set_from_file('categories/gtk-yes.png')

    def on_qt5_clicked(self, widget):
        if os.path.exists("/usr/share/licenses/qt5/"):
            os.system('xterm -e "sudo pacman -R qt5-base"')
            if not os.path.exists("/usr/share/licenses/qt5/"):
                self.qt5_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S qt5-base"')
            if os.path.exists("/usr/share/licenses/qt5/"):
                self.qt5_img.set_from_file('categories/gtk-yes.png')

    def on_qtcreator_clicked(self, widget):
        if os.path.isfile("/usr/bin/netbeans"):
            os.system('xterm -e "sudo pacman -R qtcreator"')
            if not os.path.isfile("/usr/bin/netbeans"):
                self.qtcreator_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S qtcreator"')
            if os.path.isfile("/usr/bin/netbeans"):
                self.qtcreator_img.set_from_file('categories/gtk-yes.png')

    def on_ninja_ide_clicked(self, widget):
        if os.path.isfile("/usr/bin/ninja-ide"):
            os.system('xterm -e "sudo pacman -R ninja-ide"')
            if not os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xterm -e "sudo pacman -S ninja-ide"')
            if os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide_img.set_from_file('categories/gtk-yes.png')


    def on_button1_clicked(self, widget):
        self.image1.set_from_file('categories/menu11.png')
        self.image2.set_from_file('categories/menu2.png')
        self.image3.set_from_file('categories/menu3.png')
        self.image4.set_from_file('categories/menu4.png')
        self.image5.set_from_file('categories/menu5.xpm')
        self.image6.set_from_file('categories/menu6.png')
        self.vbox.remove(self.grid_graphics)
        self.vbox.remove(self.grid_internet)
        self.vbox.remove(self.grid_multimedia)
        self.vbox.remove(self.grid_system)
        self.vbox.remove(self.grid_utilities)
        self.vbox.remove(self.grid_custom)
        # check if those programs are installed and set appropriate sign
        self.anjuta_img = self.builder2.get_object("anjuta_img")
        if os.path.isfile("/usr/bin/anjuta"):
            self.anjuta_img.set_from_file('categories/gtk-yes.png')
        else:
            self.anjuta_img.set_from_file('categories/gtk-no.png')

        self.blender_img = self.builder2.get_object("blender_img")
        if os.path.isfile("/usr/bin/blender"):
            self.blender_img.set_from_file('categories/gtk-yes.png')
        else:
            self.blender_img.set_from_file('categories/gtk-no.png')

        self.bluefish_img = self.builder2.get_object("bluefish_img")
        if os.path.isfile("/usr/bin/bluefish"):
            self.bluefish_img.set_from_file('categories/gtk-yes.png')
        else:
            self.bluefish_img.set_from_file('categories/gtk-no.png')

        self.eclipse_img = self.builder2.get_object("eclipse_img")
        if os.path.isfile("/usr/bin/eclipse"):
            self.eclipse_img.set_from_file('categories/gtk-yes.png')
        else:
            self.eclipse_img.set_from_file('categories/gtk-no.png')

        self.geany_img = self.builder2.get_object("geany_img")
        if os.path.isfile("/usr/bin/geany"):
            self.geany_img.set_from_file('categories/gtk-yes.png')
        else:
            self.geany_img.set_from_file('categories/gtk-no.png')

        self.glade_img = self.builder2.get_object("glade_img")
        if os.path.isfile("/usr/bin/glade"):
            self.glade_img.set_from_file('categories/gtk-yes.png')
        else:
            self.glade_img.set_from_file('categories/gtk-no.png')

        self.openjdk_img = self.builder2.get_object("openjdk_img")
        if os.path.exists("/etc/java-7-openjdk/"):
            self.openjdk_img.set_from_file('categories/gtk-yes.png')
        else:
            self.openjdk_img.set_from_file('categories/gtk-no.png')

        self.meld_img = self.builder2.get_object("meld_img")
        if os.path.isfile("/usr/bin/meld"):
            self.meld_img.set_from_file('categories/gtk-yes.png')
        else:
            self.meld_img.set_from_file('categories/gtk-no.png')

        self.netbeans_img = self.builder2.get_object("netbeans_img")
        if os.path.isfile("/usr/bin/netbeans"):
            self.netbeans_img.set_from_file('categories/gtk-yes.png')
        else:
            self.netbeans_img.set_from_file('categories/gtk-no.png')

        self.qt4_img = self.builder2.get_object("qt4_img")
        if os.path.exists("/usr/share/qt4/"):
            self.qt4_img.set_from_file('categories/gtk-yes.png')
        else:
            self.qt4_img.set_from_file('categories/gtk-no.png')

        self.qt5_img = self.builder2.get_object("qt5_img")
        if os.path.exists("/usr/share/licenses/qt5/"):
            self.qt5_img.set_from_file('categories/gtk-yes.png')
        else:
            self.qt5_img.set_from_file('categories/gtk-no.png')

        self.qtcreator_img = self.builder2.get_object("qtcreator_img")
        if os.path.isfile("/usr/bin/qtcreator"):
            self.qtcreator_img.set_from_file('categories/gtk-yes.png')
        else:
            self.qtcreator_img.set_from_file('categories/gtk-no.png')

        self.ninja_ide_img = self.builder2.get_object("ninja_ide_img")
        if os.path.isfile("/usr/bin/ninja-ide"):
            self.ninja_ide_img.set_from_file('categories/gtk-yes.png')
        else:
            self.ninja_ide_img.set_from_file('categories/gtk-no.png')
        self.vbox.add(self.grid_development)

    def on_button2_clicked(self, widget):
        self.image1.set_from_file('categories/menu1.png')
        self.image2.set_from_file('categories/menu22.png')
        self.image3.set_from_file('categories/menu3.png')
        self.image4.set_from_file('categories/menu4.png')
        self.image5.set_from_file('categories/menu5.xpm')
        self.image6.set_from_file('categories/menu6.png')
        self.vbox.remove(self.grid_development)
        self.vbox.remove(self.grid_internet)
        self.vbox.remove(self.grid_multimedia)
        self.vbox.remove(self.grid_system)
        self.vbox.remove(self.grid_utilities)
        self.vbox.remove(self.grid_custom)
        # check if those programs are installed and set appropriate sign
        self.evince_img = self.builder3.get_object("evince_img")
        if os.path.isfile("/usr/bin/evince"):
            self.evince_img.set_from_file('categories/gtk-yes.png')
        else:
            self.evince_img.set_from_file('categories/gtk-no.png')

        self.f_spot_img = self.builder3.get_object("f_spot_img")
        if os.path.isfile("/usr/bin/f-spot"):
            self.f_spot_img.set_from_file('categories/gtk-yes.png')
        else:
            self.f_spot_img.set_from_file('categories/gtk-no.png')

        self.gimp_img = self.builder3.get_object("gimp_img")
        if os.path.isfile("/usr/bin/gimp"):
            self.gimp_img.set_from_file('categories/gtk-yes.png')
        else:
            self.gimp_img.set_from_file('categories/gtk-no.png')

        self.gwenview_img = self.builder3.get_object("gwenview_img")
        if os.path.isfile("/usr/bin/gwenview"):
            self.gwenview_img.set_from_file('categories/gtk-yes.png')
        else:
            self.gwenview_img.set_from_file('categories/gtk-no.png')

        self.imagemagick_img = self.builder3.get_object("imagemagick_img")
        if os.path.exists("/usr/share/licenses/imagemagick/"):
            self.imagemagick_img.set_from_file('categories/gtk-yes.png')
        else:
            self.imagemagick_img.set_from_file('categories/gtk-no.png')

        self.inkscape_img = self.builder3.get_object("inkscape_img")
        if os.path.isfile("/usr/bin/inkscape"):
            self.inkscape_img.set_from_file('categories/gtk-yes.png')
        else:
            self.inkscape_img.set_from_file('categories/gtk-no.png')

        self.mypaint_img = self.builder3.get_object("mypaint_img")
        if os.path.isfile("/usr/bin/mypaint"):
            self.mypaint_img.set_from_file('categories/gtk-yes.png')
        else:
            self.mypaint_img.set_from_file('categories/gtk-no.png')

        self.pinta_img = self.builder3.get_object("pinta_img")
        if os.path.isfile("/usr/bin/pinta"):
            self.pinta_img.set_from_file('categories/gtk-yes.png')
        else:
            self.pinta_img.set_from_file('categories/gtk-no.png')

        self.shotwell_img = self.builder3.get_object("shotwell_img")
        if os.path.isfile("/usr/bin/shotwell"):
            self.shotwell_img.set_from_file('categories/gtk-yes.png')
        else:
            self.shotwell_img.set_from_file('categories/gtk-no.png')

        self.stellarium_img = self.builder3.get_object("stellarium_img")
        if os.path.isfile("/usr/bin/stellarium"):
            self.stellarium_img.set_from_file('categories/gtk-yes.png')
        else:
            self.stellarium_img.set_from_file('categories/gtk-no.png')
        self.vbox.add(self.grid_graphics)

    def on_button3_clicked(self, widget):
        self.image1.set_from_file('categories/menu1.png')
        self.image2.set_from_file('categories/menu2.png')
        self.image3.set_from_file('categories/menu33.png')
        self.image4.set_from_file('categories/menu4.png')
        self.image5.set_from_file('categories/menu5.xpm')
        self.image6.set_from_file('categories/menu6.png')
        self.vbox.remove(self.grid_graphics)
        self.vbox.remove(self.grid_development)
        self.vbox.remove(self.grid_multimedia)
        self.vbox.remove(self.grid_system)
        self.vbox.remove(self.grid_utilities)
        self.vbox.remove(self.grid_custom)
        # check if those programs are installed and set appropriate sign
        self.chromium_img = self.builder4.get_object("chromium_img")
        if os.path.isfile("/usr/bin/chromium"):
            self.chromium_img.set_from_file('categories/gtk-yes.png')
        else:
            self.chromium_img.set_from_file('categories/gtk-no.png')

        self.deluge_img = self.builder4.get_object("deluge_img")
        if os.path.isfile("/usr/bin/deluge"):
            self.deluge_img.set_from_file('categories/gtk-yes.png')
        else:
            self.deluge_img.set_from_file('categories/gtk-no.png')

        self.evolution_img = self.builder4.get_object("evolution_img")
        if os.path.isfile("/usr/bin/evolution"):
            self.evolution_img.set_from_file('categories/gtk-yes.png')
        else:
            self.evolution_img.set_from_file('categories/gtk-no.png')

        self.filezilla_img = self.builder4.get_object("filezilla_img")
        if os.path.isfile("/usr/bin/filezilla"):
            self.filezilla_img.set_from_file('categories/gtk-yes.png')
        else:
            self.filezilla_img.set_from_file('categories/gtk-no.png')

        self.firefox_img = self.builder4.get_object("firefox_img")
        if os.path.isfile("/usr/bin/firefox"):
            self.firefox_img.set_from_file('categories/gtk-yes.png')
        else:
            self.firefox_img.set_from_file('categories/gtk-no.png')

        self.chrome_img = self.builder4.get_object("chrome_img")
        if os.path.isfile("/usr/bin/google-chrome-stable"):
            self.chrome_img.set_from_file('categories/gtk-yes.png')
        else:
            self.chrome_img.set_from_file('categories/gtk-no.png')

        self.xchat_img = self.builder4.get_object("xchat_img")
        if os.path.isfile("/usr/bin/xchat"):
            self.xchat_img.set_from_file('categories/gtk-yes.png')
        else:
            self.xchat_img.set_from_file('categories/gtk-no.png')

        self.liferea_img = self.builder4.get_object("liferea_img")
        if os.path.isfile("/usr/bin/liferea"):
            self.liferea_img.set_from_file('categories/gtk-yes.png')
        else:
            self.liferea_img.set_from_file('categories/gtk-no.png')

        self.midori_img = self.builder4.get_object("midori_img")
        if os.path.isfile("/usr/bin/midori"):
            self.midori_img.set_from_file('categories/gtk-yes.png')
        else:
            self.midori_img.set_from_file('categories/gtk-no.png')

        self.minitube_img = self.builder4.get_object("minitube_img")
        if os.path.isfile("/usr/bin/minitube"):
            self.minitube_img.set_from_file('categories/gtk-yes.png')
        else:
            self.minitube_img.set_from_file('categories/gtk-no.png')

        self.opera_img = self.builder4.get_object("opera_img")
        if os.path.isfile("/usr/bin/opera"):
            self.opera_img.set_from_file('categories/gtk-yes.png')
        else:
            self.opera_img.set_from_file('categories/gtk-no.png')

        self.pidgin_img = self.builder4.get_object("pidgin_img")
        if os.path.isfile("/usr/bin/pidgin"):
            self.pidgin_img.set_from_file('categories/gtk-yes.png')
        else:
            self.pidgin_img.set_from_file('categories/gtk-no.png')

        self.skype_img = self.builder4.get_object("skype_img")
        if os.path.isfile("/usr/bin/skype"):
            self.skype_img.set_from_file('categories/gtk-yes.png')
        else:
            self.skype_img.set_from_file('categories/gtk-no.png')

        self.steam_img = self.builder4.get_object("steam_img")
        if os.path.isfile("/usr/bin/steam"):
            self.steam_img.set_from_file('categories/gtk-yes.png')
        else:
            self.steam_img.set_from_file('categories/gtk-no.png')

        self.thunderbird_img = self.builder4.get_object("thunderbird_img")
        if os.path.isfile("/usr/bin/thunderbird"):
            self.thunderbird_img.set_from_file('categories/gtk-yes.png')
        else:
            self.thunderbird_img.set_from_file('categories/gtk-no.png')

        self.transmission_img = self.builder4.get_object("transmission_img")
        if os.path.isfile("/usr/bin/transmission-gtk"):
            self.transmission_img.set_from_file('categories/gtk-yes.png')
        else:
            self.transmission_img.set_from_file('categories/gtk-no.png')
        self.vbox.add(self.grid_internet)

    def on_button4_clicked(self, widget):
        self.image1.set_from_file('categories/menu1.png')
        self.image2.set_from_file('categories/menu2.png')
        self.image3.set_from_file('categories/menu3.png')
        self.image4.set_from_file('categories/menu44.png')
        self.image5.set_from_file('categories/menu5.xpm')
        self.image6.set_from_file('categories/menu6.png')
        self.vbox.remove(self.grid_graphics)
        self.vbox.remove(self.grid_development)
        self.vbox.remove(self.grid_internet)
        self.vbox.remove(self.grid_system)
        self.vbox.remove(self.grid_utilities)
        self.vbox.remove(self.grid_custom)
        # check if those programs are installed and set appropriate sign
        self.amarok_img = self.builder5.get_object("amarok_img")
        if os.path.isfile("/usr/bin/amarok"):
            self.amarok_img.set_from_file('categories/gtk-yes.png')
        else:
            self.amarok_img.set_from_file('categories/gtk-no.png')

        self.audacious_img = self.builder5.get_object("audacious_img")
        if os.path.isfile("/usr/bin/audacious"):
            self.audacious_img.set_from_file('categories/gtk-yes.png')
        else:
            self.audacious_img.set_from_file('categories/gtk-no.png')

        self.banshee_img = self.builder5.get_object("banshee_img")
        if os.path.isfile("/usr/bin/banshee"):
            self.banshee_img.set_from_file('categories/gtk-yes.png')
        else:
            self.banshee_img.set_from_file('categories/gtk-no.png')

        self.cheese_img = self.builder5.get_object("cheese_img")
        if os.path.isfile("/usr/bin/cheese"):
            self.cheese_img.set_from_file('categories/gtk-yes.png')
        else:
            self.cheese_img.set_from_file('categories/gtk-no.png')

        self.clementine_img = self.builder5.get_object("clementine_img")
        if os.path.isfile("/usr/bin/clementine"):
            self.clementine_img.set_from_file('categories/gtk-yes.png')
        else:
            self.clementine_img.set_from_file('categories/gtk-no.png')

        self.flashplayer_img = self.builder5.get_object("flashplayer_img")
        if os.path.isfile("/usr/bin/flash-player-properties"):
            self.flashplayer_img.set_from_file('categories/gtk-yes.png')
        else:
            self.flashplayer_img.set_from_file('categories/gtk-no.png')

        self.recordmydesktop_img = self.builder5.get_object("recordmydesktop_img")
        if os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
            self.recordmydesktop_img.set_from_file('categories/gtk-yes.png')
        else:
            self.recordmydesktop_img.set_from_file('categories/gtk-no.png')

        self.guayadeque_img = self.builder5.get_object("guayadeque_img")
        if os.path.isfile("/usr/bin/guayadeque"):
            self.guayadeque_img.set_from_file('categories/gtk-yes.png')
        else:
            self.guayadeque_img.set_from_file('categories/gtk-no.png')

        self.mplayer_img = self.builder5.get_object("mplayer_img")
        if os.path.isfile("/usr/bin/mplayer"):
            self.mplayer_img.set_from_file('categories/gtk-yes.png')
        else:
            self.mplayer_img.set_from_file('categories/gtk-no.png')

        self.openshot_img = self.builder5.get_object("openshot_img")
        if os.path.isfile("/usr/bin/openshot"):
            self.openshot_img.set_from_file('categories/gtk-yes.png')
        else:
            self.openshot_img.set_from_file('categories/gtk-no.png')

        self.pitivi_img = self.builder5.get_object("pitivi_img")
        if os.path.isfile("/usr/bin/pitivi"):
            self.pitivi_img.set_from_file('categories/gtk-yes.png')
        else:
            self.pitivi_img.set_from_file('categories/gtk-no.png')

        self.rhythmbox = self.builder5.get_object("rhythmbox_img")
        if os.path.isfile("/usr/bin/rhythmbox"):
            self.rhythmbox.set_from_file('categories/gtk-yes.png')
        else:
            self.rhythmbox.set_from_file('categories/gtk-no.png')

        self.soundconverter_img = self.builder5.get_object("soundconverter_img")
        if os.path.isfile("/usr/bin/soundconverter"):
            self.soundconverter_img.set_from_file('categories/gtk-yes.png')
        else:
            self.soundconverter_img.set_from_file('categories/gtk-no.png')

        self.totem_img = self.builder5.get_object("totem_img")
        if os.path.isfile("/usr/bin/totem"):
            self.totem_img.set_from_file('categories/gtk-yes.png')
        else:
            self.totem_img.set_from_file('categories/gtk-no.png')

        self.vlc_img = self.builder5.get_object("vlc_img")
        if os.path.isfile("/usr/bin/vlc"):
            self.vlc_img.set_from_file('categories/gtk-yes.png')
        else:
            self.vlc_img.set_from_file('categories/gtk-no.png')

        self.winff_img = self.builder5.get_object("winff_img")
        if os.path.isfile("/usr/bin/winff"):
            self.winff_img.set_from_file('categories/gtk-yes.png')
        else:
            self.winff_img.set_from_file('categories/gtk-no.png')

        self.xfburn_img = self.builder5.get_object("xfburn_img")
        if os.path.isfile("/usr/bin/xfburn"):
            self.xfburn_img.set_from_file('categories/gtk-yes.png')
        else:
            self.xfburn_img.set_from_file('categories/gtk-no.png')
        self.vbox.add(self.grid_multimedia)

    def on_button5_clicked(self, widget):
        self.image1.set_from_file('categories/menu1.png')
        self.image2.set_from_file('categories/menu2.png')
        self.image3.set_from_file('categories/menu3.png')
        self.image4.set_from_file('categories/menu4.png')
        self.image5.set_from_file('categories/menu55.xpm')
        self.image6.set_from_file('categories/menu6.png')
        self.vbox.remove(self.grid_graphics)
        self.vbox.remove(self.grid_development)
        self.vbox.remove(self.grid_internet)
        self.vbox.remove(self.grid_multimedia)
        self.vbox.remove(self.grid_utilities)
        self.vbox.remove(self.grid_custom)
        # check if those programs are installed and set appropriate sign
        self.gparted_img = self.builder6.get_object("gparted_img")
        if os.path.isfile("/usr/bin/gparted"):
            self.gparted_img.set_from_file('categories/gtk-yes.png')
        else:
            self.gparted_img.set_from_file('categories/gtk-no.png')

        self.guake_img = self.builder6.get_object("guake_img")
        if os.path.isfile("/usr/bin/guake"):
            self.guake_img.set_from_file('categories/gtk-yes.png')
        else:
            self.guake_img.set_from_file('categories/gtk-no.png')

        self.hardinfo_img = self.builder6.get_object("hardinfo_img")
        if os.path.isfile("/usr/bin/hardinfo"):
            self.hardinfo_img.set_from_file('categories/gtk-yes.png')
        else:
            self.hardinfo_img.set_from_file('categories/gtk-no.png')

        self.htop_img = self.builder6.get_object("htop_img")
        if os.path.isfile("/usr/bin/htop"):
            self.htop_img.set_from_file('categories/gtk-yes.png')
        else:
            self.htop_img.set_from_file('categories/gtk-no.png')

        self.keepassx_img = self.builder6.get_object("keepassx_img")
        if os.path.isfile("/usr/bin/keepassx"):
            self.keepassx_img.set_from_file('categories/gtk-yes.png')
        else:
            self.keepassx_img.set_from_file('categories/gtk-no.png')

        self.playonlinux_img = self.builder6.get_object("playonlinux_img")
        if os.path.isfile("/usr/bin/playonlinux"):
            self.playonlinux_img.set_from_file('categories/gtk-yes.png')
        else:
            self.playonlinux_img.set_from_file('categories/gtk-no.png')

        self.terminator_img = self.builder6.get_object("terminator_img")
        if os.path.isfile("/usr/bin/terminator"):
            self.terminator_img.set_from_file('categories/gtk-yes.png')
        else:
            self.terminator_img.set_from_file('categories/gtk-no.png')

        self.thunar_img = self.builder6.get_object("thunar_img")
        if os.path.isfile("/usr/bin/thunar"):
            self.thunar_img.set_from_file('categories/gtk-yes.png')
        else:
            self.thunar_img.set_from_file('categories/gtk-no.png')

        self.truecrypt_img = self.builder6.get_object("truecrypt_img")
        if os.path.isfile("/usr/bin/truecrypt"):
            self.truecrypt_img.set_from_file('categories/gtk-yes.png')
        else:
            self.truecrypt_img.set_from_file('categories/gtk-no.png')

        self.unetbootin_img = self.builder6.get_object("unetbootin_img")
        if os.path.isfile("/usr/bin/unetbootin"):
            self.unetbootin_img.set_from_file('categories/gtk-yes.png')
        else:
            self.unetbootin_img.set_from_file('categories/gtk-no.png')

        self.virtualbox_img = self.builder6.get_object("virtualbox_img")
        if os.path.isfile("/usr/bin/virtualbox"):
            self.virtualbox_img.set_from_file('categories/gtk-yes.png')
        else:
            self.virtualbox_img.set_from_file('categories/gtk-no.png')

        self.wine_img = self.builder6.get_object("wine_img")
        if os.path.isfile("/usr/bin/wine"):
            self.wine_img.set_from_file('categories/gtk-yes.png')
        else:
            self.wine_img.set_from_file('categories/gtk-no.png')

        self.wireshark_img = self.builder6.get_object("wireshark_img")
        if os.path.isfile("/usr/bin/wireshark"):
            self.wireshark_img.set_from_file('categories/gtk-yes.png')
        else:
            self.wireshark_img.set_from_file('categories/gtk-no.png')

        self.xbmc_img = self.builder6.get_object("xbmc_img")
        if os.path.isfile("/usr/bin/xbmc"):
            self.xbmc_img.set_from_file('categories/gtk-yes.png')
        else:
            self.xbmc_img.set_from_file('categories/gtk-no.png')
        self.vbox.add(self.grid_system)

    def on_button6_clicked(self, widget):
        self.image1.set_from_file('categories/menu1.png')
        self.image2.set_from_file('categories/menu2.png')
        self.image3.set_from_file('categories/menu3.png')
        self.image4.set_from_file('categories/menu4.png')
        self.image5.set_from_file('categories/menu5.xpm')
        self.image6.set_from_file('categories/menu66.png')
        self.vbox.remove(self.grid_graphics)
        self.vbox.remove(self.grid_development)
        self.vbox.remove(self.grid_internet)
        self.vbox.remove(self.grid_multimedia)
        self.vbox.remove(self.grid_system)
        self.vbox.remove(self.grid_custom)
        # check if those programs are installed and set appropriate sign
        self.docky_img = self.builder7.get_object("docky_img")
        if os.path.isfile("/usr/bin/docky"):
            self.docky_img.set_from_file('categories/gtk-yes.png')
        else:
            self.docky_img.set_from_file('categories/gtk-no.png')

        self.emacs_img = self.builder7.get_object("emacs_img")
        if os.path.isfile("/usr/bin/emacs"):
            self.emacs_img.set_from_file('categories/gtk-yes.png')
        else:
            self.emacs_img.set_from_file('categories/gtk-no.png')

        self.vim_img = self.builder7.get_object("vim_img")
        if os.path.isfile("/usr/bin/vim"):
            self.vim_img.set_from_file('categories/gtk-yes.png')
        else:
            self.vim_img.set_from_file('categories/gtk-no.png')

        self.galculator_img = self.builder7.get_object("galculator_img")
        if os.path.isfile("/usr/bin/galculator"):
            self.galculator_img.set_from_file('categories/gtk-yes.png')
        else:
            self.galculator_img.set_from_file('categories/gtk-no.png')

        self.gedit_img = self.builder7.get_object("gedit_img")
        if os.path.isfile("/usr/bin/gedit"):
            self.gedit_img.set_from_file('categories/gtk-yes.png')
        else:
            self.gedit_img.set_from_file('categories/gtk-no.png')

        self.gloobus_img = self.builder7.get_object("gloobus_img")
        if os.path.isfile("/usr/bin/gloobus-preview"):
            self.gloobus_img.set_from_file('categories/gtk-yes.png')
        else:
            self.gloobus_img.set_from_file('categories/gtk-no.png')

        self.leafpad_img = self.builder7.get_object("leafpad_img")
        if os.path.isfile("/usr/bin/leafpad"):
            self.leafpad_img.set_from_file('categories/gtk-yes.png')
        else:
            self.leafpad_img.set_from_file('categories/gtk-no.png')

        self.scribes_img = self.builder7.get_object("scribes_img")
        if os.path.isfile("/usr/bin/scribes"):
            self.scribes_img.set_from_file('categories/gtk-yes.png')
        else:
            self.scribes_img.set_from_file('categories/gtk-no.png')

        self.tomboy_img = self.builder7.get_object("tomboy_img")
        if os.path.isfile("/usr/bin/tomboy"):
            self.tomboy_img.set_from_file('categories/gtk-yes.png')
        else:
            self.tomboy_img.set_from_file('categories/gtk-no.png')

        self.tuxcards_img = self.builder7.get_object("tuxcards_img")
        if os.path.isfile("/usr/bin/tuxcards"):
            self.tuxcards_img.set_from_file('categories/gtk-yes.png')
        else:
            self.tuxcards_img.set_from_file('categories/gtk-no.png')
        self.vbox.add(self.grid_utilities)

    def on_button7_clicked(self, widget):
        aboutdialog = Gtk.AboutDialog()
        aboutdialog.set_program_name("Yo I\'m not pro")
        aboutdialog.set_logo(GdkPixbuf.Pixbuf.new_from_file("ui/yoimnotpro_icon.png"))
        aboutdialog.set_comments("Small app center\n")
        aboutdialog.set_website("http://linux.sytes.net/")
        aboutdialog.set_website_label("Developer Website")
        aboutdialog.set_authors(["Aaron\nhttp://linux.sytes.net/"])
        aboutdialog.set_license('GPLv3 - http://www.gnu.org/licenses/gpl.html\nor read the COPYING file')
        aboutdialog.run()
        aboutdialog.destroy()

    def draw_transparency(self, widget, cr):
        cr.set_source_rgba(.1, .1, .1, 0.8)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('ui/main.ui')

        self.builder2 = Gtk.Builder()
        self.builder2.add_from_file('ui/menu1.ui')
        self.grid_development = self.builder2.get_object("grid1")

        self.builder3 = Gtk.Builder()
        self.builder3.add_from_file('ui/menu2.ui')
        self.grid_graphics = self.builder3.get_object("grid1")

        self.builder4 = Gtk.Builder()
        self.builder4.add_from_file('ui/menu3.ui')
        self.grid_internet = self.builder4.get_object("grid1")

        self.builder5 = Gtk.Builder()
        self.builder5.add_from_file('ui/menu4.ui')
        self.grid_multimedia = self.builder5.get_object("grid1")

        self.builder6 = Gtk.Builder()
        self.builder6.add_from_file('ui/menu5.ui')
        self.grid_system = self.builder6.get_object("grid1")

        self.builder7 = Gtk.Builder()
        self.builder7.add_from_file('ui/menu6.ui')
        self.grid_utilities = self.builder7.get_object("grid1")

        self.builder8 = Gtk.Builder()
        self.builder8.add_from_file('ui/menu7.ui')
        self.grid_custom = self.builder8.get_object("grid1")

        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window1")

        # it's horizontal box, separating the menu buttons from the ui files
        self.vbox = self.builder.get_object("box1")
        self.vbox.add(self.grid_custom)

        # transparancy
        self.window.screen = self.window.get_screen()
        self.window.visual = self.window.screen.get_rgba_visual()
        if self.window.visual is not None and self.window.screen.is_composited():
            self.window.set_visual(self.window.visual)
        self.window.set_app_paintable(True)
        self.window.connect("draw", self.draw_transparency)

        # get the categories images, will be used once you click on some the categories to change those images with active or inactive
        self.image1 = self.builder.get_object("image1")
        self.image2 = self.builder.get_object("image2")
        self.image3 = self.builder.get_object("image3")
        self.image4 = self.builder.get_object("image4")
        self.image5 = self.builder.get_object("image5")
        self.image6 = self.builder.get_object("image6")

        # get menu 7 application buttons
        self.geany_ = self.builder8.get_object("geany_")
        self.geany_.set_tooltip_text("Geany is a small and lightweight integrated development environment.")
        self.blender_ = self.builder8.get_object("blender_")
        self.blender_.set_tooltip_text("Blender is the open source, cross platform suite of tools for 3D creation.")
        self.ninja_ide_ = self.builder8.get_object("ninja_ide_")
        self.ninja_ide_.set_tooltip_text("Ninja-IDE is a cross-platform integrated development environment designed to build Python applications.")
        self.glade_ = self.builder8.get_object("glade_")
        self.glade_.set_tooltip_text("Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment.")
        self.audacious_ = self.builder8.get_object("audacious_")
        self.audacious_.set_tooltip_text("Audio player with support for many formats, and it has support for third-party plugins. ")
        self.gimp_ = self.builder8.get_object("gimp_")
        self.gimp_.set_tooltip_text("GIMP is an image retouching and editing tool, similar to Photoshop.")
        self.evince_ = self.builder8.get_object("evince_")
        self.evince_.set_tooltip_text("Evince is a document viewer for multiple document formats.")
        self.xfburn_ = self.builder8.get_object("xfburn_")
        self.xfburn_.set_tooltip_text("Xfburn is a simple CD/DVD burning tool")
        self.flashplayer_ = self.builder8.get_object("flashplayer_")
        self.flashplayer_.set_tooltip_text("Cross-platform plugin plays animations, videos and sound files.")
        self.openshot_ = self.builder8.get_object("openshot_")
        self.openshot_.set_tooltip_text("A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style")
        self.chromium_ = self.builder8.get_object("chromium_")
        self.chromium_.set_tooltip_text("Chromium is the open source web browser project from which Google Chrome draws its source code.")
        self.deluge_ = self.builder8.get_object("deluge_")
        self.deluge_.set_tooltip_text("Open source, cross-platform BitTorrent client.")
        self.liferea_ = self.builder8.get_object("liferea_")
        self.liferea_.set_tooltip_text("Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds.")
        self.htop_ = self.builder8.get_object("htop_")
        self.htop_.set_tooltip_text("Htop is an interactive system-monitor process-viewer.")
        self.skype_ = self.builder8.get_object("skype_")
        self.skype_.set_tooltip_text("Skype is a freemium voice-over-IP service and instant messaging client")
        self.wireshark_ = self.builder8.get_object("wireshark_")
        self.wireshark_.set_tooltip_text("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development.")
        self.virtualbox_ = self.builder8.get_object("virtualbox_")
        self.virtualbox_.set_tooltip_text("VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC.")
        self.steam_ = self.builder8.get_object("steam_")
        self.steam_.set_tooltip_text("Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses.")
        self.xchat_ = self.builder8.get_object("xchat_")
        self.xchat_.set_tooltip_text("XChat is a popular Internet Relay Chat (IRC) client.")
        self.gedit_ = self.builder8.get_object("gedit_")
        self.gedit_.set_tooltip_text("gedit is lightweight text editor.")
        # connect "clicked" signal to those buttons
        self.geany_.connect("clicked", self.on_geany__clicked)
        self.blender_.connect("clicked", self.on_blender__clicked)
        self.ninja_ide_.connect("clicked", self.on_ninja_ide__clicked)
        self.glade_.connect("clicked", self.on_glade__clicked)
        self.audacious_.connect("clicked", self.on_audacious__clicked)
        self.gimp_.connect("clicked", self.on_gimp__clicked)
        self.evince_.connect("clicked", self.on_evince__clicked)
        self.xfburn_.connect("clicked", self.on_xfburn__clicked)
        self.flashplayer_.connect("clicked", self.on_flashplayer__clicked)
        self.openshot_.connect("clicked", self.on_openshot__clicked)
        self.chromium_.connect("clicked", self.on_chromium__clicked)
        self.deluge_.connect("clicked", self.on_deluge__clicked)
        self.liferea_.connect("clicked", self.on_liferea__clicked)
        self.htop_.connect("clicked", self.on_htop__clicked)
        self.skype_.connect("clicked", self.on_skype__clicked)
        self.wireshark_.connect("clicked", self.on_wireshark__clicked)
        self.virtualbox_.connect("clicked", self.on_virtualbox__clicked)
        self.steam_.connect("clicked", self.on_steam__clicked)
        self.xchat_.connect("clicked", self.on_xchat__clicked)
        self.gedit_.connect("clicked", self.on_gedit__clicked)
        # check if those programs are installed and set appropriate sign
        self.geany__img = self.builder8.get_object("geany_img_")
        if os.path.isfile("/usr/bin/geany"):
            self.geany__img.set_from_file('categories/gtk-yes.png')
        else:
            self.geany__img.set_from_file('categories/gtk-no.png')

        self.blender__img = self.builder8.get_object("blender_img_")
        if os.path.isfile("/usr/bin/blender"):
            self.blender__img.set_from_file('categories/gtk-yes.png')
        else:
            self.blender__img.set_from_file('categories/gtk-no.png')

        self.ninja_ide__img = self.builder8.get_object("ninja_ide_img_")
        if os.path.isfile("/usr/bin/ninja-ide"):
            self.ninja_ide__img.set_from_file('categories/gtk-yes.png')
        else:
            self.ninja_ide__img.set_from_file('categories/gtk-no.png')

        self.glade__img = self.builder8.get_object("glade_img_")
        if os.path.isfile("/usr/bin/glade"):
            self.glade__img.set_from_file('categories/gtk-yes.png')
        else:
            self.glade__img.set_from_file('categories/gtk-no.png')

        self.audacious__img = self.builder8.get_object("audacious_img_")
        if os.path.isfile("/usr/bin/audacious"):
            self.audacious__img.set_from_file('categories/gtk-yes.png')
        else:
            self.audacious__img.set_from_file('categories/gtk-no.png')

        self.gimp__img = self.builder8.get_object("gimp_img_")
        if os.path.isfile("/usr/bin/gimp"):
            self.gimp__img.set_from_file('categories/gtk-yes.png')
        else:
            self.gimp__img.set_from_file('categories/gtk-no.png')

        self.evince__img = self.builder8.get_object("evince_img_")
        if os.path.isfile("/usr/bin/evince"):
            self.evince__img.set_from_file('categories/gtk-yes.png')
        else:
            self.evince__img.set_from_file('categories/gtk-no.png')

        self.xfburn__img = self.builder8.get_object("xfburn_img_")
        if os.path.isfile("/usr/bin/xfburn"):
            self.xfburn__img.set_from_file('categories/gtk-yes.png')
        else:
            self.xfburn__img.set_from_file('categories/gtk-no.png')

        self.flashplayer__img = self.builder8.get_object("flashplayer_img_")
        if os.path.isfile("/usr/bin/flash-player-properties"):
            self.flashplayer__img.set_from_file('categories/gtk-yes.png')
        else:
            self.flashplayer__img.set_from_file('categories/gtk-no.png')

        self.openshot__img = self.builder8.get_object("openshot_img_")
        if os.path.isfile("/usr/bin/openshot"):
            self.openshot__img.set_from_file('categories/gtk-yes.png')
        else:
            self.openshot__img.set_from_file('categories/gtk-no.png')

        self.chromium__img = self.builder8.get_object("chromium_img_")
        if os.path.isfile("/usr/bin/chromium"):
            self.chromium__img.set_from_file('categories/gtk-yes.png')
        else:
            self.chromium__img.set_from_file('categories/gtk-no.png')

        self.deluge__img = self.builder8.get_object("deluge_img_")
        if os.path.isfile("/usr/bin/deluge"):
            self.deluge__img.set_from_file('categories/gtk-yes.png')
        else:
            self.deluge__img.set_from_file('categories/gtk-no.png')

        self.liferea__img = self.builder8.get_object("liferea_img_")
        if os.path.isfile("/usr/bin/liferea"):
            self.liferea__img.set_from_file('categories/gtk-yes.png')
        else:
            self.liferea__img.set_from_file('categories/gtk-no.png')

        self.htop__img = self.builder8.get_object("htop_img_")
        if os.path.isfile("/usr/bin/htop"):
            self.htop__img.set_from_file('categories/gtk-yes.png')
        else:
            self.htop__img.set_from_file('categories/gtk-no.png')

        self.skype__img = self.builder8.get_object("skype_img_")
        if os.path.isfile("/usr/bin/skype"):
            self.skype__img.set_from_file('categories/gtk-yes.png')
        else:
            self.skype__img.set_from_file('categories/gtk-no.png')

        self.wireshark__img = self.builder8.get_object("wireshark_img_")
        if os.path.isfile("/usr/bin/wireshark"):
            self.wireshark__img.set_from_file('categories/gtk-yes.png')
        else:
            self.wireshark__img.set_from_file('categories/gtk-no.png')

        self.virtualbox__img = self.builder8.get_object("virtualbox_img_")
        if os.path.isfile("/usr/bin/virtualbox"):
            self.virtualbox__img.set_from_file('categories/gtk-yes.png')
        else:
            self.virtualbox__img.set_from_file('categories/gtk-no.png')

        self.steam__img = self.builder8.get_object("steam_img_")
        if os.path.isfile("/usr/bin/steam"):
            self.steam__img.set_from_file('categories/gtk-yes.png')
        else:
            self.steam__img.set_from_file('categories/gtk-no.png')

        self.xchat__img = self.builder8.get_object("xchat_img_")
        if os.path.isfile("/usr/bin/xchat"):
            self.xchat__img.set_from_file('categories/gtk-yes.png')
        else:
            self.xchat__img.set_from_file('categories/gtk-no.png')

        self.gedit__img = self.builder8.get_object("gedit_img_")
        if os.path.isfile("/usr/bin/gedit"):
            self.gedit__img.set_from_file('categories/gtk-yes.png')
        else:
            self.gedit__img.set_from_file('categories/gtk-no.png')

        # get menu 6 application buttons
        self.docky = self.builder7.get_object("docky")
        self.docky.set_tooltip_text("Docky is an advanced shortcut bar that sits at the edges of your screen.")
        self.emacs = self.builder7.get_object("emacs")
        self.emacs.set_tooltip_text("Emacs is a text editor.")
        self.vim = self.builder7.get_object("vim")
        self.vim.set_tooltip_text("Vim is a text editor")
        self.galculator = self.builder7.get_object("galculator")
        self.galculator.set_tooltip_text("galculator is an open source scientific calculator with a modern GUI.")
        self.gedit = self.builder7.get_object("gedit")
        self.gedit.set_tooltip_text("gedit is lightweight text editor.")
        self.gloobus = self.builder7.get_object("gloobus")
        self.gloobus.set_tooltip_text(" Gloobus Preview is a program designed to preview the contents of a file or folder on Linux OS")
        self.leafpad = self.builder7.get_object("leafpad")
        self.leafpad.set_tooltip_text("Leafpad is a text editor")
        self.scribes = self.builder7.get_object("scribes")
        self.scribes.set_tooltip_text("Simple, slim and sleek, yet powerful text editor.")
        self.tomboy = self.builder7.get_object("tomboy")
        self.tomboy.set_tooltip_text("Tomboy is a desktop note-taking application")
        self.tuxcards = self.builder7.get_object("tuxcards")
        self.tuxcards.set_tooltip_text("TuxCards is a hierarical notebook.")
        # connect "clicked" signal to those buttons
        self.docky.connect("clicked", self.on_docky_clicked)
        self.emacs.connect("clicked", self.on_emacs_clicked)
        self.vim.connect("clicked", self.on_vim_clicked)
        self.galculator.connect("clicked", self.on_galculator_clicked)
        self.gedit.connect("clicked", self.on_gedit_clicked)
        self.gloobus.connect("clicked", self.on_gloobus_clicked)
        self.leafpad.connect("clicked", self.on_leafpad_clicked)
        self.scribes.connect("clicked", self.on_scribes_clicked)
        self.tomboy.connect("clicked", self.on_tomboy_clicked)
        self.tuxcards.connect("clicked", self.on_tuxcards_clicked)

        # get menu 5 application buttons
        self.gparted = self.builder6.get_object("gparted")
        self.gparted.set_tooltip_text("GParted is a free partition editor for graphically managing your disk partitions. ")
        self.guake = self.builder6.get_object("guake")
        self.guake.set_tooltip_text("Guake is a drop-down terminal.")
        self.hardinfo = self.builder6.get_object("hardinfo")
        self.hardinfo.set_tooltip_text("Hardinfo provides comprehensive details of your PC's software and hardware and allows you to benchmark its performance.")
        self.htop = self.builder6.get_object("htop")
        self.htop.set_tooltip_text("Htop is an interactive process viewer.")
        self.keepassx = self.builder6.get_object("keepassx")
        self.keepassx.set_tooltip_text("KeePassX is an application for people with extremly high demands on secure personal data management.")
        self.playonlinux = self.builder6.get_object("playonlinux")
        self.playonlinux.set_tooltip_text("PlayOnLinux will allow you to play your favorite games on Linux easily.")
        self.terminator = self.builder6.get_object("terminator")
        self.terminator.set_tooltip_text(" Terminator is a cross-platform GPL terminal emulator with advanced features not yet found elsewhere.")
        self.thunar = self.builder6.get_object("thunar")
        self.thunar.set_tooltip_text("Thunar is a file manager.")
        self.truecrypt = self.builder6.get_object("truecrypt")
        self.truecrypt.set_tooltip_text("TrueCrypt is free open-source disk encryption software.")
        self.unetbootin = self.builder6.get_object("unetbootin")
        self.unetbootin.set_tooltip_text("UNetbootin allows you to create bootable Live USB drives for GNU/Linux distributions without burning a CD")
        self.virtualbox = self.builder6.get_object("virtualbox")
        self.virtualbox.set_tooltip_text("VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC.")
        self.wine = self.builder6.get_object("wine")
        self.wine.set_tooltip_text("Wine is a compatibility layer for running windows applications on GNU/Linux.")
        self.wireshark = self.builder6.get_object("wireshark")
        self.wireshark.set_tooltip_text("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development.")
        self.xbmc = self.builder6.get_object("xbmc")
        self.xbmc.set_tooltip_text("XBMC Media Center is a free cross-platform media player software and entertainment system application framework.")
        # connect "clicked" signal to those buttons
        self.gparted.connect("clicked", self.on_gparted_clicked)
        self.guake.connect("clicked", self.on_guake_clicked)
        self.hardinfo.connect("clicked", self.on_hardinfo_clicked)
        self.htop.connect("clicked", self.on_htop_clicked)
        self.keepassx.connect("clicked", self.on_keepassx_clicked)
        self.playonlinux.connect("clicked", self.on_playonlinux_clicked)
        self.terminator.connect("clicked", self.on_terminator_clicked)
        self.thunar.connect("clicked", self.on_thunar_clicked)
        self.truecrypt.connect("clicked", self.on_truecrypt_clicked)
        self.unetbootin.connect("clicked", self.on_unetbootin_clicked)
        self.virtualbox.connect("clicked", self.on_virtualbox_clicked)
        self.wine.connect("clicked", self.on_wine_clicked)
        self.wireshark.connect("clicked", self.on_wireshark_clicked)
        self.xbmc.connect("clicked", self.on_xbmc_clicked)

        # get menu 4 application buttons
        self.amarok = self.builder5.get_object("amarok")
        self.amarok.set_tooltip_text("Amarok is a cross-platform free and open source music player.")
        self.audacious = self.builder5.get_object("audacious")
        self.audacious.set_tooltip_text("Audacious is a free and open source audio player.")
        self.banshee = self.builder5.get_object("banshee")
        self.banshee.set_tooltip_text("Banshee is a cross-platform open-source media player.")
        self.cheese = self.builder5.get_object("cheese")
        self.cheese.set_tooltip_text("Cheese uses your webcam to take photos and videos, applies fancy special effects, and lets you share the fun with others.")
        self.clementine = self.builder5.get_object("clementine")
        self.clementine.set_tooltip_text("Clementine is a cross-platform free and open source music player and library organizer. ")
        self.flashplayer = self.builder5.get_object("flashplayer")
        self.flashplayer.set_tooltip_text("Cross-platform plugin plays animations, videos and sound files.")
        self.recordmydesktop = self.builder5.get_object("recordmydesktop")
        self.recordmydesktop.set_tooltip_text("recordMyDesktop is a desktop session recorder.")
        self.guayadeque = self.builder5.get_object("guayadeque")
        self.guayadeque.set_tooltip_text("Guayadeque is a music management program designed for all music enthusiasts.")
        self.mplayer = self.builder5.get_object("mplayer")
        self.mplayer.set_tooltip_text("MPlayer is a free software and open source media player.")
        self.openshot = self.builder5.get_object("openshot")
        self.openshot.set_tooltip_text("A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style.")
        self.pitivi = self.builder5.get_object("pitivi")
        self.pitivi.set_tooltip_text("Pitivi is an open source, non-linear video editor.")
        self.rhythmbox = self.builder5.get_object("rhythmbox")
        self.rhythmbox.set_tooltip_text("Rhythmbox is an integrated music management application, originally inspired by Apple's iTunes.")
        self.soundconverter = self.builder5.get_object("soundconverter")
        self.soundconverter.set_tooltip_text("SoundConverter is the leading audio file converter.")
        self.totem = self.builder5.get_object("totem")
        self.totem.set_tooltip_text("Totem is a media player.")
        self.vlc = self.builder5.get_object("vlc")
        self.vlc.set_tooltip_text("VLC is a multimedia player for various audio and video formats.")
        self.winff = self.builder5.get_object("winff")
        self.winff.set_tooltip_text("WinFF is a video converter.")
        self.xfburn = self.builder5.get_object("xfburn")
        self.xfburn.set_tooltip_text("Xfburn is a simple CD/DVD burning tool.")
        # connect "clicked" signal to those buttons
        self.amarok.connect("clicked", self.on_amarok_clicked)
        self.audacious.connect("clicked", self.on_audacious_clicked)
        self.banshee.connect("clicked", self.on_banshee_clicked)
        self.cheese.connect("clicked", self.on_cheese_clicked)
        self.clementine.connect("clicked", self.on_clementine_clicked)
        self.flashplayer.connect("clicked", self.on_flashplayer_clicked)
        self.recordmydesktop.connect("clicked", self.on_recordmydesktop_clicked)
        self.guayadeque.connect("clicked", self.on_guayadeque_clicked)
        self.mplayer.connect("clicked", self.on_mplayer_clicked)
        self.openshot.connect("clicked", self.on_openshot_clicked)
        self.pitivi.connect("clicked", self.on_pitivi_clicked)
        self.rhythmbox.connect("clicked", self.on_rhythmbox_clicked)
        self.soundconverter.connect("clicked", self.on_soundconverter_clicked)
        self.totem.connect("clicked", self.on_totem_clicked)
        self.vlc.connect("clicked", self.on_vlc_clicked)
        self.winff.connect("clicked", self.on_winff_clicked)
        self.xfburn.connect("clicked", self.on_xfburn_clicked)

        # get menu 3 application buttons
        self.chromium = self.builder4.get_object("chromium")
        self.chromium.set_tooltip_text("Chromium is the open source web browser project from which Google Chrome draws its source code.")
        self.deluge = self.builder4.get_object("deluge")
        self.deluge.set_tooltip_text("Open source, cross-platform BitTorrent client.")
        self.evolution = self.builder4.get_object("evolution")
        self.evolution.set_tooltip_text("Evolution is a fully featured open source powerful, flexible and generally great email client.")
        self.filezilla = self.builder4.get_object("filezilla")
        self.filezilla.set_tooltip_text("Open-source FTP client.")
        self.firefox = self.builder4.get_object("firefox")
        self.firefox.set_tooltip_text("Firefox is a free and open-source web browser")
        self.chrome = self.builder4.get_object("chrome")
        self.chrome.set_tooltip_text("Google Chrome is a browser that combines a minimal design with sophisticated technology to make the web faster, safer and easier.")
        self.xchat = self.builder4.get_object("xchat")
        self.xchat.set_tooltip_text("XChat is a popular Internet Relay Chat (IRC) client.")
        self.liferea = self.builder4.get_object("liferea")
        self.liferea.set_tooltip_text("Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds.")
        self.midori = self.builder4.get_object("midori")
        self.midori.set_tooltip_text("Midori is a lightweight Webkit-based web browser.")
        self.minitube = self.builder4.get_object("minitube")
        self.minitube.set_tooltip_text("Minitube is a native YouTube client. With it you can watch YouTube videos in a new way.")
        self.opera = self.builder4.get_object("opera")
        self.opera.set_tooltip_text("Opera is a web browser.")
        self.pidgin = self.builder4.get_object("pidgin")
        self.pidgin.set_tooltip_text("Pidgin is universal chat client.")
        self.skyp = self.builder4.get_object("skyp")
        self.skyp.set_tooltip_text("Skype is a freemium voice-over-IP service and instant messaging client.")
        self.steam = self.builder4.get_object("steam")
        self.steam.set_tooltip_text("Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses.")
        self.thunderbird = self.builder4.get_object("thunderbird")
        self.thunderbird.set_tooltip_text("Thunderbird is an email program.")
        self.transmission = self.builder4.get_object("transmission")
        self.transmission.set_tooltip_text("Transmission is a BitTorrent client.")
        # connect "clicked" signal to those buttons
        self.chromium.connect("clicked", self.on_chromium_clicked)
        self.deluge.connect("clicked", self.on_deluge_clicked)
        self.evolution.connect("clicked", self.on_evolution_clicked)
        self.filezilla.connect("clicked", self.on_filezilla_clicked)
        self.firefox.connect("clicked", self.on_firefox_clicked)
        self.chrome.connect("clicked", self.on_chrome_clicked)
        self.xchat.connect("clicked", self.on_xchat_clicked)
        self.liferea.connect("clicked", self.on_liferea_clicked)
        self.midori.connect("clicked", self.on_midori_clicked)
        self.minitube.connect("clicked", self.on_minitube_clicked)
        self.opera.connect("clicked", self.on_opera_clicked)
        self.pidgin.connect("clicked", self.on_pidgin_clicked)
        self.skyp.connect("clicked", self.on_skyp_clicked)
        self.steam.connect("clicked", self.on_steam_clicked)
        self.thunderbird.connect("clicked", self.on_thunderbird_clicked)
        self.transmission.connect("clicked", self.on_transmission_clicked)

        # get menu 2 application buttons
        self.evince = self.builder3.get_object("evince")
        self.evince.set_tooltip_text("Evince is a document viewer for multiple document formats.")
        self.f_spot = self.builder3.get_object("f_spot")
        self.f_spot.set_tooltip_text("F-Spot is a full-featured personal photo management application.")
        self.gimp = self.builder3.get_object("gimp")
        self.gimp.set_tooltip_text("GIMP is an image retouching and editing tool, similar to Photoshop.")
        self.gwenview = self.builder3.get_object("gwenview")
        self.gwenview.set_tooltip_text("Gwenview is an image viewer.")
        self.imagemagick = self.builder3.get_object("imagemagick")
        self.imagemagick.set_tooltip_text("Use ImageMagick to convert, edit, or compose bitmap images in a variety of formats.")
        self.inkscape = self.builder3.get_object("inkscape")
        self.inkscape.set_tooltip_text("Inkscape is an open source vector graphics editor.")
        self.mypaint = self.builder3.get_object("mypaint")
        self.mypaint.set_tooltip_text("MyPaint is a fast and easy open-source graphics application for digital painters.")
        self.pinta = self.builder3.get_object("pinta")
        self.pinta.set_tooltip_text("Pinta is an open-source, cross-platform bitmap image drawing and editing program inspired by Paint.NET")
        self.shotwell = self.builder3.get_object("shotwell")
        self.shotwell.set_tooltip_text("Shotwell is an image organizer.")
        self.stellarium = self.builder3.get_object("stellarium")
        self.stellarium.set_tooltip_text("Stellarium is a planetarium software that shows exactly what you see when you look up at the stars.")
        # connect "clicked" signal to those buttons
        self.evince.connect("clicked", self.on_evince_clicked)
        self.f_spot.connect("clicked", self.on_f_spot_clicked)
        self.gimp.connect("clicked", self.on_gimp_clicked)
        self.gwenview.connect("clicked", self.on_gwenview_clicked)
        self.imagemagick.connect("clicked", self.on_imagemagick_clicked)
        self.inkscape.connect("clicked", self.on_inkscape_clicked)
        self.mypaint.connect("clicked", self.on_mypaint_clicked)
        self.pinta.connect("clicked", self.on_pinta_clicked)
        self.shotwell.connect("clicked", self.on_shotwell_clicked)
        self.stellarium.connect("clicked", self.on_stellarium_clicked)

        # get menu 1 application buttons
        self.anjuta = self.builder2.get_object("anjuta")
        self.anjuta.set_tooltip_text("Anjuta is an integrated development environment.")
        self.blender = self.builder2.get_object("blender")
        self.blender.set_tooltip_text("Blender is a free and open-source 3D computer graphics software product used for creating animated films, \nvisual effects, art, 3D printed models and so on.")
        self.bluefish = self.builder2.get_object("bluefish")
        self.bluefish.set_tooltip_text("Bluefish is a free and open source advanced text editor with a variety of tools for programming in general\nand the development of dynamic websites")
        self.eclipse = self.builder2.get_object("eclipse")
        self.eclipse.set_tooltip_text("Eclipse is IDE.")
        self.geany = self.builder2.get_object("geany")
        self.geany.set_tooltip_text("Geany is a small and lightweight integrated development environment.")
        self.glade = self.builder2.get_object("glade")
        self.glade.set_tooltip_text("Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment.")
        self.openjdk = self.builder2.get_object("openjdk")
        self.openjdk.set_tooltip_text("OpenJDK (Open Java Development Kit) is a free and open source implementation of the Java Platform, Standard Edition (Java SE).")
        self.meld = self.builder2.get_object("meld")
        self.meld.set_tooltip_text("Meld is a visual diff and merge tool targeted at developers.")
        self.netbeans = self.builder2.get_object("netbeans")
        self.netbeans.set_tooltip_text("Fully-featured Java IDE written completely in Java, with many modules available.")
        self.qt4 = self.builder2.get_object("qt4")
        self.qt4.set_tooltip_text("Qt4 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface.")
        self.qt5 = self.builder2.get_object("qt5")
        self.qt5.set_tooltip_text("Qt5 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface.")
        self.qtcreator = self.builder2.get_object("qtcreator")
        self.qtcreator.set_tooltip_text("Qt Creator is a cross-platform C++ IDE")
        self.ninja_ide = self.builder2.get_object("ninja_ide")
        self.ninja_ide.set_tooltip_text("Ninja-IDE is a cross-platform integrated development environment designed to build Python applications.")
        # connect "clicked" signal to those buttons
        self.anjuta.connect("clicked", self.on_anjuta_clicked)
        self.blender.connect("clicked", self.on_blender_clicked)
        self.bluefish.connect("clicked", self.on_bluefish_clicked)
        self.eclipse.connect("clicked", self.on_eclipse_clicked)
        self.geany.connect("clicked", self.on_geany_clicked)
        self.glade.connect("clicked", self.on_glade_clicked)
        self.openjdk.connect("clicked", self.on_openjdk_clicked)
        self.meld.connect("clicked", self.on_meld_clicked)
        self.netbeans.connect("clicked", self.on_netbeans_clicked)
        self.qt4.connect("clicked", self.on_qt4_clicked)
        self.qt5.connect("clicked", self.on_qt5_clicked)
        self.qtcreator.connect("clicked", self.on_qtcreator_clicked)
        self.ninja_ide.connect("clicked", self.on_ninja_ide_clicked)

        # display text for each category while hovering it with your mouse
        self.button1 = self.builder.get_object("button1")
        self.button1.set_tooltip_text("Development")
        self.button2 = self.builder.get_object("button2")
        self.button2.set_tooltip_text("Graphics")
        self.button3 = self.builder.get_object("button3")
        self.button3.set_tooltip_text("Internet")
        self.button4 = self.builder.get_object("button4")
        self.button4.set_tooltip_text("Multimedia")
        self.button5 = self.builder.get_object("button5")
        self.button5.set_tooltip_text("System")
        self.button6 = self.builder.get_object("button6")
        self.button6.set_tooltip_text("Utilities")
        self.button7 = self.builder.get_object("button7")
        self.button7.set_tooltip_text("About")

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

if __name__ == '__main__':
    iod()
    Gtk.main()