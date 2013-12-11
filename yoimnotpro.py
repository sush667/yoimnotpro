#!/usr/bin/python2
import os
import cairo
from gi.repository import Gtk, GdkPixbuf

class iod:

    # menu 7 button actions
    def on_geany__clicked(self, widget):
        if os.path.isfile("/usr/bin/geany"):
            os.system('xfce4-terminal -H -x sudo pacman -R geany')
            if not os.path.isfile("/usr/bin/geany"):
                self.geany__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S geany')
            if os.path.isfile("/usr/bin/geany"):
                self.geany__img.set_from_file('categories/gtk-yes.png')

    def on_blender__clicked(self, widget):
        if os.path.isfile("/usr/bin/blender"):
            os.system('xfce4-terminal -H -x sudo pacman -R blender')
            if not os.path.isfile("/usr/bin/audacious"):
                self.blender__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S blender')
            if os.path.isfile("/usr/bin/blender"):
                self.blender__img.set_from_file('categories/gtk-yes.png')

    def on_ninja_ide__clicked(self, widget):
        if os.path.isfile("/usr/bin/ninja-ide"):
            os.system('xfce4-terminal -H -x sudo pacman -R ninja-ide')
            if not os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S banshee')
            if os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide__img.set_from_file('categories/gtk-yes.png')

    def on_glade__clicked(self, widget):
        if os.path.isfile("/usr/bin/glade"):
            os.system('xfce4-terminal -H -x sudo pacman -R glade')
            if not os.path.isfile("/usr/bin/glade"):
                self.glade__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S glade')
            if os.path.isfile("/usr/bin/glade"):
                self.glade__img.set_from_file('categories/gtk-yes.png')

    def on_audacious__clicked(self, widget):
        if os.path.isfile("/usr/bin/audacious"):
            os.system('xfce4-terminal -H -x sudo pacman -R audacious')
            if not os.path.isfile("/usr/bin/audacious"):
                self.audacious__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S audacious')
            if os.path.isfile("/usr/bin/audacious"):
                self.audacious__img.set_from_file('categories/gtk-yes.png')

    def on_gimp__clicked(self, widget):
        if os.path.isfile("/usr/bin/gimp"):
            os.system('xfce4-terminal -H -x sudo pacman -R gimp')
            if not os.path.isfile("/usr/bin/gimp"):
                self.gimp__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S gimp')
            if os.path.isfile("/usr/bin/gimp"):
                self.gimp__img.set_from_file('categories/gtk-yes.png')

    def on_evince__clicked(self, widget):
        if os.path.isfile("/usr/bin/evince"):
            os.system('xfce4-terminal -H -x sudo pacman -R evince')
            if not os.path.isfile("/usr/bin/evince"):
                self.evince__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S evince')
            if os.path.isfile("/usr/bin/evince"):
                self.evince__img.set_from_file('categories/gtk-yes.png')

    def on_xfburn__clicked(self, widget):
        if os.path.isfile("/usr/bin/xfburn"):
            os.system('xfce4-terminal -H -x sudo pacman -R xfburn')
            if not os.path.isfile("/usr/bin/xfburn"):
                self.xfburn__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S xfburn')
            if os.path.isfile("/usr/bin/xfburn"):
                self.xfburn__img.set_from_file('categories/gtk-yes.png')

    def on_flashplayer__clicked(self, widget):
        if os.path.isfile("/usr/bin/flash-player-properties"):
            os.system('xfce4-terminal -H -x sudo pacman -R flashplugin')
            if not os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S flashplugin')
            if os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer__img.set_from_file('categories/gtk-yes.png')

    def on_openshot__clicked(self, widget):
        if os.path.isfile("/usr/bin/openshot"):
            os.system('xfce4-terminal -H -x sudo pacman -R openshot')
            if not os.path.isfile("/usr/bin/openshot"):
                self.openshot__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S openshot')
            if os.path.isfile("/usr/bin/openshot"):
                self.openshot__img.set_from_file('categories/gtk-yes.png')

    def on_chromium__clicked(self, widget):
        if os.path.isfile("/usr/bin/chromium"):
            os.system('xfce4-terminal -H -x sudo pacman -R chromium')
            if not os.path.isfile("/usr/bin/chromium"):
                self.chromium__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S chromium')
            if os.path.isfile("/usr/bin/chromium"):
                self.chromium__img.set_from_file('categories/gtk-yes.png')

    def on_deluge__clicked(self, widget):
        if os.path.isfile("/usr/bin/deluge"):
            os.system('xfce4-terminal -H -x sudo pacman -R deluge')
            if not os.path.isfile("/usr/bin/deluge"):
                self.deluge__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S deluge')
            if os.path.isfile("/usr/bin/deluge"):
                self.deluge__img.set_from_file('categories/gtk-yes.png')

    def on_liferea__clicked(self, widget):
        if os.path.isfile("/usr/bin/liferea"):
            os.system('xfce4-terminal -H -x sudo pacman -R liferea')
            if not os.path.isfile("/usr/bin/liferea"):
                self.liferea__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S liferea')
            if os.path.isfile("/usr/bin/liferea"):
                self.liferea__img.set_from_file('categories/gtk-yes.png')

    def on_htop__clicked(self, widget):
        if os.path.isfile("/usr/bin/htop"):
            os.system('xfce4-terminal -H -x sudo pacman -R htop')
            if not os.path.isfile("/usr/bin/htop"):
                self.htop__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S htop')
            if os.path.isfile("/usr/bin/htop"):
                self.htop__img.set_from_file('categories/gtk-yes.png')

    def on_skype__clicked(self, widget):
        if os.path.isfile("/usr/bin/skype"):
            os.system('xfce4-terminal -H -x sudo pacman -R skype')
            if not os.path.isfile("/usr/bin/skype"):
                self.skype__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S skype')
            if os.path.isfile("/usr/bin/skype"):
                self.skype__img.set_from_file('categories/gtk-yes.png')

    def on_wireshark__clicked(self, widget):
        if os.path.isfile("/usr/bin/wireshark"):
            os.system('xfce4-terminal -H -x sudo pacman -R wireshark-gtk')
            if not os.path.isfile("/usr/bin/wireshark"):
                self.wireshark__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S wireshark-gtk')
            if os.path.isfile("/usr/bin/wireshark"):
                self.wireshark__img.set_from_file('categories/gtk-yes.png')

    def on_virtualbox__clicked(self, widget):
        if os.path.isfile("/usr/bin/virtualbox"):
            os.system('xfce4-terminal -H -x sudo pacman -R virtualbox')
            if not os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S virtualbox')
            if os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox__img.set_from_file('categories/gtk-yes.png')

    def on_steam__clicked(self, widget):
        if os.path.isfile("/usr/bin/steam"):
            os.system('xfce4-terminal -H -x sudo pacman -R steam')
            if not os.path.isfile("/usr/bin/steam"):
                self.steam__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S steam')
            if os.path.isfile("/usr/bin/steam"):
                self.steam__img.set_from_file('categories/gtk-yes.png')

    def on_xchat__clicked(self, widget):
        if os.path.isfile("/usr/bin/xchat"):
            os.system('xfce4-terminal -H -x sudo pacman -R xchat')
            if not os.path.isfile("/usr/bin/xchat"):
                self.xchat__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S xchat')
            if os.path.isfile("/usr/bin/xchat"):
                self.xchat__img.set_from_file('categories/gtk-yes.png')

    def on_gedit__clicked(self, widget):
        if os.path.isfile("/usr/bin/gedit"):
            os.system('xfce4-terminal -H -x sudo pacman -R gedit')
            if not os.path.isfile("/usr/bin/gedit"):
                self.gedit__img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S gedit')
            if os.path.isfile("/usr/bin/gedit"):
                self.gedit__img.set_from_file('categories/gtk-yes.png')

    # menu 6 button actions
    def on_docky_clicked(self, widget):
        if os.path.isfile("/usr/bin/docky"):
            os.system('xfce4-terminal -H -x sudo pacman -R docky')
            if not os.path.isfile("/usr/bin/docky"):
                self.docky_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S docky')
            if os.path.isfile("/usr/bin/docky"):
                self.docky_img.set_from_file('categories/gtk-yes.png')

    def on_emacs_clicked(self, widget):
        if os.path.isfile("/usr/bin/emacs"):
            os.system('xfce4-terminal -H -x sudo pacman -R emacs')
            if not os.path.isfile("/usr/bin/emacs"):
                self.emacs_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S emacs')
            if os.path.isfile("/usr/bin/emacs"):
                self.emacs_img.set_from_file('categories/gtk-yes.png')

    def on_vim_clicked(self, widget):
        if os.path.isfile("/usr/bin/vim"):
            os.system('xfce4-terminal -H -x sudo pacman -R vim')
            if not os.path.isfile("/usr/bin/vim"):
                self.vim_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S vim')
            if os.path.isfile("/usr/bin/vim"):
                self.vim_img.set_from_file('categories/gtk-yes.png')

    def on_galculator_clicked(self, widget):
        if os.path.isfile("/usr/bin/galculator"):
            os.system('xfce4-terminal -H -x sudo pacman -R galculator')
            if not os.path.isfile("/usr/bin/galculator"):
                self.galculator_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S galculator')
            if os.path.isfile("/usr/bin/galculator"):
                self.galculator_img.set_from_file('categories/gtk-yes.png')

    def on_gedit_clicked(self, widget):
        if os.path.isfile("/usr/bin/gedit"):
            os.system('xfce4-terminal -H -x sudo pacman -R gedit')
            if not os.path.isfile("/usr/bin/gedit"):
                self.gedit_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S gedit')
            if os.path.isfile("/usr/bin/gedit"):
                self.gedit_img.set_from_file('categories/gtk-yes.png')

    def on_gloobus_clicked(self, widget):
        if os.path.isfile("/usr/bin/gloobus-preview"):
            os.system('xfce4-terminal -H -x sudo pacman -R gloobus-preview')
            if not os.path.isfile("/usr/bin/gloobus-preview"):
                self.gloobus_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S gloobus-preview')
            if os.path.isfile("/usr/bin/gloobus-preview"):
                self.gloobus_img.set_from_file('categories/gtk-yes.png')

    def on_leafpad_clicked(self, widget):
        if os.path.isfile("/usr/bin/leafpad"):
            os.system('xfce4-terminal -H -x sudo pacman -R leafpad')
            if not os.path.isfile("/usr/bin/leafpad"):
                self.leafpad_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S leafpad')
            if os.path.isfile("/usr/bin/leafpad"):
                self.leafpad_img.set_from_file('categories/gtk-yes.png')

    def on_scribes_clicked(self, widget):
        if os.path.isfile("/usr/bin/scribes"):
            os.system('xfce4-terminal -H -x sudo pacman -R scribes')
            if not os.path.isfile("/usr/bin/scribes"):
                self.scribes_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S scribes')
            if os.path.isfile("/usr/bin/scribes"):
                self.scribes_img.set_from_file('categories/gtk-yes.png')

    def on_tomboy_clicked(self, widget):
        if os.path.isfile("/usr/bin/tomboy"):
            os.system('xfce4-terminal -H -x sudo pacman -R tomboy')
            if not os.path.isfile("/usr/bin/tomboy"):
                self.tomboy_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S tomboy')
            if os.path.isfile("/usr/bin/tomboy"):
                self.tomboy_img.set_from_file('categories/gtk-yes.png')

    def on_tuxcards_clicked(self, widget):
        if os.path.isfile("/usr/bin/tuxcards"):
            os.system('xfce4-terminal -H -x sudo pacman -R tuxcards')
            if not os.path.isfile("/usr/bin/tuxcards"):
                self.tuxcards_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S tuxcards')
            if os.path.isfile("/usr/bin/tuxcards"):
                self.tuxcards_img.set_from_file('categories/gtk-yes.png')

    # menu 5 button actions
    def on_gparted_clicked(self, widget):
        if os.path.isfile("/usr/bin/gparted"):
            os.system('xfce4-terminal -H -x sudo pacman -R gparted')
            if not os.path.isfile("/usr/bin/gparted"):
                self.gparted_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S gparted')
            if os.path.isfile("/usr/bin/gparted"):
                self.gparted_img.set_from_file('categories/gtk-yes.png')

    def on_guake_clicked(self, widget):
        if os.path.isfile("/usr/bin/guake"):
            os.system('xfce4-terminal -H -x sudo pacman -R guake')
            if not os.path.isfile("/usr/bin/guake"):
                self.guake_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S guake')
            if os.path.isfile("/usr/bin/guake"):
                self.guake_img.set_from_file('categories/gtk-yes.png')

    def on_hardinfo_clicked(self, widget):
        if os.path.isfile("/usr/bin/hardinfo"):
            os.system('xfce4-terminal -H -x sudo pacman -R hardinfo')
            if not os.path.isfile("/usr/bin/hardinfo"):
                self.hardinfo_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S hardinfo')
            if os.path.isfile("/usr/bin/hardinfo"):
                self.hardinfo_img.set_from_file('categories/gtk-yes.png')

    def on_htop_clicked(self, widget):
        if os.path.isfile("/usr/bin/htop"):
            os.system('xfce4-terminal -H -x sudo pacman -R htop')
            if not os.path.isfile("/usr/bin/htop"):
                self.htop_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S htop')
            if os.path.isfile("/usr/bin/htop"):
                self.htop_img.set_from_file('categories/gtk-yes.png')

    def on_keepassx_clicked(self, widget):
        if os.path.isfile("/usr/bin/keepassx"):
            os.system('xfce4-terminal -H -x sudo pacman -R keepassx')
            if not os.path.isfile("/usr/bin/keepassx"):
                self.keepassx_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S keepassx')
            if os.path.isfile("/usr/bin/keepassx"):
                self.keepassx_img.set_from_file('categories/gtk-yes.png')

    def on_playonlinux_clicked(self, widget):
        if os.path.isfile("/usr/bin/playonlinux"):
            os.system('xfce4-terminal -H -x sudo pacman -R playonlinux')
            if not os.path.isfile("/usr/bin/playonlinux"):
                self.playonlinux_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S playonlinux')
            if os.path.isfile("/usr/bin/playonlinux"):
                self.playonlinux_img.set_from_file('categories/gtk-yes.png')

    def on_terminator_clicked(self, widget):
        if os.path.isfile("/usr/bin/terminator"):
            os.system('xfce4-terminal -H -x sudo pacman -R terminator')
            if not os.path.isfile("/usr/bin/terminator"):
                self.terminator_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S terminator')
            if os.path.isfile("/usr/bin/terminator"):
                self.terminator_img.set_from_file('categories/gtk-yes.png')

    def on_thunar_clicked(self, widget):
        if os.path.isfile("/usr/bin/thunar"):
            os.system('xfce4-terminal -H -x sudo pacman -R thunar')
            if not os.path.isfile("/usr/bin/thunar"):
                self.thunar_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S thunar')
            if os.path.isfile("/usr/bin/thunar"):
                self.thunar_img.set_from_file('categories/gtk-yes.png')

    def on_truecrypt_clicked(self, widget):
        if os.path.isfile("/usr/bin/truecrypt"):
            os.system('xfce4-terminal -H -x sudo pacman -R truecrypt')
            if not os.path.isfile("/usr/bin/truecrypt"):
                self.truecrypt_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S truecrypt')
            if os.path.isfile("/usr/bin/truecrypt"):
                self.truecrypt_img.set_from_file('categories/gtk-yes.png')

    def on_unetbootin_clicked(self, widget):
        if os.path.isfile("/usr/bin/unetbootin"):
            os.system('xfce4-terminal -H -x sudo pacman -R unetbootin')
            if not os.path.isfile("/usr/bin/unetbootin"):
                self.unetbootin_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S unetbootin')
            if os.path.isfile("/usr/bin/unetbootin"):
                self.unetbootin_img.set_from_file('categories/gtk-yes.png')

    def on_virtualbox_clicked(self, widget):
        if os.path.isfile("/usr/bin/virtualbox"):
            os.system('xfce4-terminal -H -x sudo pacman -R virtualbox')
            if not os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S virtualbox')
            if os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox_img.set_from_file('categories/gtk-yes.png')

    def on_wine_clicked(self, widget):
        if os.path.isfile("/usr/bin/wine"):
            os.system('xfce4-terminal -H -x sudo pacman -R wine')
            if not os.path.isfile("/usr/bin/wine"):
                self.wine_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S wine')
            if os.path.isfile("/usr/bin/wine"):
                self.wine_img.set_from_file('categories/gtk-yes.png')

    def on_wireshark_clicked(self, widget):
        if os.path.isfile("/usr/bin/wireshark"):
            os.system('xfce4-terminal -H -x sudo pacman -R wireshark-gtk')
            if not os.path.isfile("/usr/bin/wireshark"):
                self.wireshark_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S wireshark-gtk')
            if os.path.isfile("/usr/bin/wireshark"):
                self.wireshark_img.set_from_file('categories/gtk-yes.png')

    def on_xbmc_clicked(self, widget):
        if os.path.isfile("/usr/bin/xbmc"):
            os.system('xfce4-terminal -H -x sudo pacman -R xbmc')
            if not os.path.isfile("/usr/bin/xbmc"):
                self.xbmc_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S xbmc')
            if os.path.isfile("/usr/bin/xbmc"):
                self.xbmc_img.set_from_file('categories/gtk-yes.png')

    # menu 4 button actions
    def on_amarok_clicked(self, widget):
        if os.path.isfile("/usr/bin/amarok"):
            os.system('xfce4-terminal -H -x sudo pacman -R amarok')
            if not os.path.isfile("/usr/bin/amarok"):
                self.amarok_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S amarok')
            if os.path.isfile("/usr/bin/amarok"):
                self.amarok_img.set_from_file('categories/gtk-yes.png')

    def on_audacious_clicked(self, widget):
        if os.path.isfile("/usr/bin/audacious"):
            os.system('xfce4-terminal -H -x sudo pacman -R audacious')
            if not os.path.isfile("/usr/bin/audacious"):
                self.audacious_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S audacious')
            if os.path.isfile("/usr/bin/audacious"):
                self.audacious_img.set_from_file('categories/gtk-yes.png')

    def on_banshee_clicked(self, widget):
        if os.path.isfile("/usr/bin/banshee"):
            os.system('xfce4-terminal -H -x sudo pacman -R banshee')
            if not os.path.isfile("/usr/bin/banshee"):
                self.banshee_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S banshee')
            if os.path.isfile("/usr/bin/banshee"):
                self.banshee_img.set_from_file('categories/gtk-yes.png')

    def on_cheese_clicked(self, widget):
        if os.path.isfile("/usr/bin/cheese"):
            os.system('xfce4-terminal -H -x sudo pacman -R cheese')
            if not os.path.isfile("/usr/bin/cheese"):
                self.cheese_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S cheese')
            if os.path.isfile("/usr/bin/cheese"):
                self.cheese_img.set_from_file('categories/gtk-yes.png')

    def on_clementine_clicked(self, widget):
        if os.path.isfile("/usr/bin/clementine"):
            os.system('xfce4-terminal -H -x sudo pacman -R clementine')
            if not os.path.isfile("/usr/bin/clementine"):
                self.clementine_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S clementine')
            if os.path.isfile("/usr/bin/clementine"):
                self.clementine_img.set_from_file('categories/gtk-yes.png')

    def on_flashplayer_clicked(self, widget):
        if os.path.isfile("/usr/bin/flash-player-properties"):
            os.system('xfce4-terminal -H -x sudo pacman -R flashplugin')
            if not os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S flashplugin')
            if os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer_img.set_from_file('categories/gtk-yes.png')

    def on_recordmydesktop_clicked(self, widget):
        if os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
            os.system('xfce4-terminal -H -x sudo pacman -R gtk-recordmydesktop')
            if not os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
                self.recordmydesktop_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S gtk-recordmydesktop')
            if os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
                self.recordmydesktop_img.set_from_file('categories/gtk-yes.png')

    def on_guayadeque_clicked(self, widget):
        if os.path.isfile("/usr/bin/guayadeque"):
            os.system('xfce4-terminal -H -x sudo pacman -R guayadeque')
            if not os.path.isfile("/usr/bin/guayadeque"):
                self.guayadeque_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S guayadeque')
            if os.path.isfile("/usr/bin/guayadeque"):
                self.guayadeque_img.set_from_file('categories/gtk-yes.png')

    def on_mplayer_clicked(self, widget):
        if os.path.isfile("/usr/bin/mplayer"):
            os.system('xfce4-terminal -H -x sudo pacman -R mplayer')
            if not os.path.isfile("/usr/bin/mplayer"):
                self.mplayer_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S mplayer')
            if os.path.isfile("/usr/bin/mplayer"):
                self.mplayer_img.set_from_file('categories/gtk-yes.png')

    def on_openshot_clicked(self, widget):
        if os.path.isfile("/usr/bin/openshot"):
            os.system('xfce4-terminal -H -x sudo pacman -R openshot')
            if not os.path.isfile("/usr/bin/openshot"):
                self.openshot_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S openshot')
            if os.path.isfile("/usr/bin/openshot"):
                self.openshot_img.set_from_file('categories/gtk-yes.png')

    def on_pitivi_clicked(self, widget):
        if os.path.isfile("/usr/bin/pitivi"):
            os.system('xfce4-terminal -H -x sudo pacman -R pitivi')
            if not os.path.isfile("/usr/bin/pitivi"):
                self.pitivi_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S pitivi')
            if os.path.isfile("/usr/bin/pitivi"):
                self.pitivi_img.set_from_file('categories/gtk-yes.png')

    def on_rhythmbox_clicked(self, widget):
        if os.path.isfile("/usr/bin/rhythmbox"):
            os.system('xfce4-terminal -H -x sudo pacman -R rhythmbox')
            if not os.path.isfile("/usr/bin/rhythmbox"):
                self.rhythmbox_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S rhythmbox')
            if os.path.isfile("/usr/bin/rhythmbox"):
                self.rhythmbox_img.set_from_file('categories/gtk-yes.png')

    def on_soundconverter_clicked(self, widget):
        if os.path.isfile("/usr/bin/soundconverter"):
            os.system('xfce4-terminal -H -x sudo pacman -R soundconverter')
            if not os.path.isfile("/usr/bin/soundconverter"):
                self.soundconverter_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S soundconverter')
            if os.path.isfile("/usr/bin/soundconverter"):
                self.soundconverter_img.set_from_file('categories/gtk-yes.png')

    def on_totem_clicked(self, widget):
        if os.path.isfile("/usr/bin/totem"):
            os.system('xfce4-terminal -H -x sudo pacman -R totem')
            if not os.path.isfile("/usr/bin/totem"):
                self.totem_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S totem')
            if os.path.isfile("/usr/bin/totem"):
                self.totem_img.set_from_file('categories/gtk-yes.png')

    def on_vlc_clicked(self, widget):
        if os.path.isfile("/usr/bin/vlc"):
            os.system('xfce4-terminal -H -x sudo pacman -R vlc')
            if not os.path.isfile("/usr/bin/vlc"):
                self.vlc_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S vlc')
            if os.path.isfile("/usr/bin/vlc"):
                self.vlc_img.set_from_file('categories/gtk-yes.png')

    def on_winff_clicked(self, widget):
        if os.path.isfile("/usr/bin/winff"):
            os.system('xfce4-terminal -H -x sudo pacman -R winff')
            if not os.path.isfile("/usr/bin/winff"):
                self.winff_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S winff')
            if os.path.isfile("/usr/bin/winff"):
                self.winff_img.set_from_file('categories/gtk-yes.png')

    def on_xfburn_clicked(self, widget):
        if os.path.isfile("/usr/bin/xfburn"):
            os.system('xfce4-terminal -H -x sudo pacman -R xfburn')
            if not os.path.isfile("/usr/bin/xfburn"):
                self.xfburn_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S xfburn')
            if os.path.isfile("/usr/bin/xfburn"):
                self.xfburn_img.set_from_file('categories/gtk-yes.png')

    # menu 3 button actions
    def on_chromium_clicked(self, widget):
        if os.path.isfile("/usr/bin/chromium"):
            os.system('xfce4-terminal -H -x sudo pacman -R chromium')
            if not os.path.isfile("/usr/bin/chromium"):
                self.chromium_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S chromium')
            if os.path.isfile("/usr/bin/chromium"):
                self.chromium_img.set_from_file('categories/gtk-yes.png')

    def on_deluge_clicked(self, widget):
        if os.path.isfile("/usr/bin/deluge"):
            os.system('xfce4-terminal -H -x sudo pacman -R deluge')
            if not os.path.isfile("/usr/bin/deluge"):
                self.deluge_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S deluge')
            if os.path.isfile("/usr/bin/deluge"):
                self.deluge_img.set_from_file('categories/gtk-yes.png')

    def on_evolution_clicked(self, widget):
        if os.path.isfile("/usr/bin/evolution"):
            os.system('xfce4-terminal -H -x sudo pacman -R evolution')
            if not os.path.isfile("/usr/bin/evolution"):
                self.evolution_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S evolution')
            if os.path.isfile("/usr/bin/evolution"):
                self.evolution_img.set_from_file('categories/gtk-yes.png')

    def on_filezilla_clicked(self, widget):
        if os.path.isfile("/usr/bin/filezilla"):
            os.system('xfce4-terminal -H -x sudo pacman -R filezilla')
            if not os.path.isfile("/usr/bin/filezilla"):
                self.filezilla_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S filezilla')
            if os.path.isfile("/usr/bin/filezilla"):
                self.filezilla_img.set_from_file('categories/gtk-yes.png')

    def on_firefox_clicked(self, widget):
        if os.path.isfile("/usr/bin/firefox"):
            os.system('xfce4-terminal -H -x sudo pacman -R firefox')
            if not os.path.isfile("/usr/bin/firefox"):
                self.firefox_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S firefox')
            if os.path.isfile("/usr/bin/firefox"):
                self.firefox_img.set_from_file('categories/gtk-yes.png')

    def on_chrome_clicked(self, widget):
        if os.path.isfile("/usr/bin/google-chrome-stable"):
            os.system('xfce4-terminal -H -x yaourt -R google-chrome')
            if not os.path.isfile("/usr/bin/google-chrome-stable"):
                self.chrome_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x yaourt -S google-chrome')
            if os.path.isfile("/usr/bin/google-chrome-stable"):
                self.chrome_img.set_from_file('categories/gtk-yes.png')

    def on_xchat_clicked(self, widget):
        if os.path.isfile("/usr/bin/xchat"):
            os.system('xfce4-terminal -H -x sudo pacman -R xchat')
            if not os.path.isfile("/usr/bin/xchat"):
                self.xchat_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S xchat')
            if os.path.isfile("/usr/bin/xchat"):
                self.xchat_img.set_from_file('categories/gtk-yes.png')

    def on_liferea_clicked(self, widget):
        if os.path.isfile("/usr/bin/liferea"):
            os.system('xfce4-terminal -H -x sudo pacman -R liferea')
            if not os.path.isfile("/usr/bin/liferea"):
                self.liferea_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S liferea')
            if os.path.isfile("/usr/bin/liferea"):
                self.liferea_img.set_from_file('categories/gtk-yes.png')

    def on_midori_clicked(self, widget):
        if os.path.isfile("/usr/bin/midori"):
            os.system('xfce4-terminal -H -x sudo pacman -R midori')
            if not os.path.isfile("/usr/bin/midori"):
                self.midori_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S midori')
            if os.path.isfile("/usr/bin/midori"):
                self.midori_img.set_from_file('categories/gtk-yes.png')

    def on_minitube_clicked(self, widget):
        if os.path.isfile("/usr/bin/minitube"):
            os.system('xfce4-terminal -H -x sudo pacman -R minitube')
            if not os.path.isfile("/usr/bin/minitube"):
                self.minitube_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S minitube')
            if os.path.isfile("/usr/bin/minitube"):
                self.minitube_img.set_from_file('categories/gtk-yes.png')

    def on_opera_clicked(self, widget):
        if os.path.isfile("/usr/bin/opera"):
            os.system('xfce4-terminal -H -x sudo pacman -R opera')
            if not os.path.isfile("/usr/bin/opera"):
                self.opera_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S opera')
            if os.path.isfile("/usr/bin/opera"):
                self.opera_img.set_from_file('categories/gtk-yes.png')

    def on_pidgin_clicked(self, widget):
        if os.path.isfile("/usr/bin/pidgin"):
            os.system('xfce4-terminal -H -x sudo pacman -R pidgin')
            if not os.path.isfile("/usr/bin/pidgin"):
                self.pidgin_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S pidgin')
            if os.path.isfile("/usr/bin/pidgin"):
                self.pidgin_img.set_from_file('categories/gtk-yes.png')

    def on_skyp_clicked(self, widget):
        if os.path.isfile("/usr/bin/skype"):
            os.system('xfce4-terminal -H -x sudo pacman -R skype')
            if not os.path.isfile("/usr/bin/skype"):
                self.skype_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S skype')
            if os.path.isfile("/usr/bin/skype"):
                self.skype_img.set_from_file('categories/gtk-yes.png')

    def on_steam_clicked(self, widget):
        if os.path.isfile("/usr/bin/steam"):
            os.system('xfce4-terminal -H -x sudo pacman -R steam')
            if not os.path.isfile("/usr/bin/steam"):
                self.steam_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S steam')
            if os.path.isfile("/usr/bin/steam"):
                self.steam_img.set_from_file('categories/gtk-yes.png')

    def on_thunderbird_clicked(self, widget):
        if os.path.isfile("/usr/bin/thunderbird"):
            os.system('xfce4-terminal -H -x sudo pacman -R thunderbird')
            if not os.path.isfile("/usr/bin/thunderbird"):
                self.thunderbird_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S thunderbird')
            if os.path.isfile("/usr/bin/thunderbird"):
                self.thunderbird_img.set_from_file('categories/gtk-yes.png')

    def on_transmission_clicked(self, widget):
        if os.path.isfile("/usr/bin/transmission-gtk"):
            os.system('xfce4-terminal -H -x sudo pacman -R transmission-gtk')
            if not os.path.isfile("/usr/bin/transmission-gtk"):
                self.transmission_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S transmission-gtk')
            if os.path.isfile("/usr/bin/transmission-gtk"):
                self.transmission_img.set_from_file('categories/gtk-yes.png')

    # menu 2 button actions
    def on_evince_clicked(self, widget):
        if os.path.isfile("/usr/bin/evince"):
            os.system('xfce4-terminal -H -x sudo pacman -R evince')
            if not os.path.isfile("/usr/bin/evince"):
                self.evince_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S evince')
            if os.path.isfile("/usr/bin/evince"):
                self.evince_img.set_from_file('categories/gtk-yes.png')

    def on_f_spot_clicked(self, widget):
        if os.path.isfile("/usr/bin/f-spot"):
            os.system('xfce4-terminal -H -x sudo pacman -R f-spot')
            if not os.path.isfile("/usr/bin/f-spot"):
                self.f_spot_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S f-spot')
            if os.path.isfile("/usr/bin/f-spot"):
                self.f_spot_img.set_from_file('categories/gtk-yes.png')

    def on_gimp_clicked(self, widget):
        if os.path.isfile("/usr/bin/gimp"):
            os.system('xfce4-terminal -H -x sudo pacman -R gimp')
            if not os.path.isfile("/usr/bin/gimp"):
                self.gimp_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S gimp')
            if os.path.isfile("/usr/bin/gimp"):
                self.gimp_img.set_from_file('categories/gtk-yes.png')

    def on_gwenview_clicked(self, widget):
        if os.path.isfile("/usr/bin/gwenview"):
            os.system('xfce4-terminal -H -x sudo pacman -R gwenview')
            if not os.path.isfile("/usr/bin/gwenview"):
                self.gwenview_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S gwenview')
            if os.path.isfile("/usr/bin/gwenview"):
                self.gwenview_img.set_from_file('categories/gtk-yes.png')

    def on_imagemagick_clicked(self, widget):
        if os.path.exists("/usr/share/licenses/imagemagick/"):
            os.system('xfce4-terminal -H -x sudo pacman -R imagemagick')
            if not os.path.exists("/usr/share/licenses/imagemagick/"):
                self.imagemagick_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S imagemagick')
            if os.path.exists("/usr/share/licenses/imagemagick/"):
                self.imagemagick_img.set_from_file('categories/gtk-yes.png')

    def on_inkscape_clicked(self, widget):
        if os.path.isfile("/usr/bin/inkscape"):
            os.system('xfce4-terminal -H -x sudo pacman -R inkscape')
            if not os.path.isfile("/usr/bin/inkscape"):
                self.inkscape_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S inkscape')
            if os.path.isfile("/usr/bin/inkscape"):
                self.inkscape_img.set_from_file('categories/gtk-yes.png')

    def on_mypaint_clicked(self, widget):
        if os.path.isfile("/usr/bin/mypaint"):
            os.system('xfce4-terminal -H -x sudo pacman -R mypaint')
            if not os.path.isfile("/usr/bin/mypaint"):
                self.mypaint_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S mypaint')
            if os.path.isfile("/usr/bin/mypaint"):
                self.mypaint_img.set_from_file('categories/gtk-yes.png')

    def on_pinta_clicked(self, widget):
        if os.path.isfile("/usr/bin/pinta"):
            os.system('xfce4-terminal -H -x sudo pacman -R pinta')
            if not os.path.isfile("/usr/bin/pinta"):
                self.pinta_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S pinta')
            if os.path.isfile("/usr/bin/pinta"):
                self.pinta_img.set_from_file('categories/gtk-yes.png')

    def on_shotwell_clicked(self, widget):
        if os.path.isfile("/usr/bin/shotwell"):
            os.system('xfce4-terminal -H -x sudo pacman -R shotwell')
            if not os.path.isfile("/usr/bin/shotwell"):
                self.shotwell_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S shotwell')
            if os.path.isfile("/usr/bin/shotwell"):
                self.shotwell_img.set_from_file('categories/gtk-yes.png')

    def on_stellarium_clicked(self, widget):
        if os.path.isfile("/usr/bin/stellarium"):
            os.system('xfce4-terminal -H -x sudo pacman -R stellarium')
            if not os.path.isfile("/usr/bin/stellarium"):
                self.stellarium_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S stellarium')
            if os.path.isfile("/usr/bin/stellarium"):
                self.stellarium_img.set_from_file('categories/gtk-yes.png')

    # menu 1 button actions
    def on_anjuta_clicked(self, widget):
        if os.path.isfile("/usr/bin/anjuta"):
            os.system('xfce4-terminal -H -x sudo pacman -R anjuta')
            if not os.path.isfile("/usr/bin/anjuta"):
                self.anjuta_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S anjuta')
            if os.path.isfile("/usr/bin/anjuta"):
                self.anjuta_img.set_from_file('categories/gtk-yes.png')

    def on_blender_clicked(self, widget):
        if os.path.isfile("/usr/bin/anjuta"):
            os.system('xfce4-terminal -H -x sudo pacman -R blender')
            if not os.path.isfile("/usr/bin/anjuta"):
                self.blender_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S blender')
            if os.path.isfile("/usr/bin/anjuta"):
                self.blender_img.set_from_file('categories/gtk-yes.png')

    def on_bluefish_clicked(self, widget):
        if os.path.isfile("/usr/bin/bluefish"):
            os.system('xfce4-terminal -H -x sudo pacman -R bluefish')
            if not os.path.isfile("/usr/bin/bluefish"):
                self.bluefish_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S bluefish')
            if os.path.isfile("/usr/bin/bluefish"):
                self.bluefish_img.set_from_file('categories/gtk-yes.png')

    def on_eclipse_clicked(self, widget):
        if os.path.isfile("/usr/bin/eclipse"):
            os.system('xfce4-terminal -H -x sudo pacman -R eclipse')
            if not os.path.isfile("/usr/bin/eclipse"):
                self.eclipse_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S eclipse')
            if os.path.isfile("/usr/bin/eclipse"):
                self.eclipse_img.set_from_file('categories/gtk-yes.png')

    def on_geany_clicked(self, widget):
        if os.path.isfile("/usr/bin/geany"):
            os.system('xfce4-terminal -H -x sudo pacman -R geany')
            if not os.path.isfile("/usr/bin/geany"):
                self.geany_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S geany')
            if os.path.isfile("/usr/bin/geany"):
                self.geany_img.set_from_file('categories/gtk-yes.png')

    def on_glade_clicked(self, widget):
        if os.path.isfile("/usr/bin/glade"):
            os.system('xfce4-terminal -H -x sudo pacman -R glade')
            if not os.path.isfile("/usr/bin/glade"):
                self.glade_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S glade')
            if os.path.isfile("/usr/bin/glade"):
                self.glade_img.set_from_file('categories/gtk-yes.png')

    def on_openjdk_clicked(self, widget):
        if os.path.exists("/etc/java-7-openjdk/"):
            os.system('xfce4-terminal -H -x sudo pacman -R jre7-openjdk')
            if not os.path.exists("/etc/java-7-openjdk/"):
                self.openjdk_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S jre7-openjdk')
            if os.path.exists("/etc/java-7-openjdk/"):
                self.openjdk_img.set_from_file('categories/gtk-yes.png')

    def on_meld_clicked(self, widget):
        if os.path.isfile("/usr/bin/meld"):
            os.system('xfce4-terminal -H -x sudo pacman -R meld')
            if not os.path.isfile("/usr/bin/meld"):
                self.meld_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S meld')
            if os.path.isfile("/usr/bin/meld"):
                self.meld_img.set_from_file('categories/gtk-yes.png')

    def on_netbeans_clicked(self, widget):
        if os.path.isfile("/usr/bin/netbeans"):
            os.system('xfce4-terminal -H -x sudo pacman -R netbeans')
            if not os.path.isfile("/usr/bin/netbeans"):
                self.netbeans_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S netbeans')
            if os.path.isfile("/usr/bin/netbeans"):
                self.netbeans_img.set_from_file('categories/gtk-yes.png')

    def on_qt4_clicked(self, widget):
        if os.path.exists("/usr/share/qt4/"):
            os.system('xfce4-terminal -H -x sudo pacman -R qt4')
            if not os.path.exists("/usr/share/qt4/"):
                self.qt4_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S qt4')
            if os.path.exists("/usr/share/qt4/"):
                self.qt4_img.set_from_file('categories/gtk-yes.png')

    def on_qt5_clicked(self, widget):
        if os.path.exists("/usr/share/licenses/qt5/"):
            os.system('xfce4-terminal -H -x sudo pacman -R qt5-base')
            if not os.path.exists("/usr/share/licenses/qt5/"):
                self.qt5_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S qt5-base')
            if os.path.exists("/usr/share/licenses/qt5/"):
                self.qt5_img.set_from_file('categories/gtk-yes.png')

    def on_qtcreator_clicked(self, widget):
        if os.path.isfile("/usr/bin/netbeans"):
            os.system('xfce4-terminal -H -x sudo pacman -R qtcreator')
            if not os.path.isfile("/usr/bin/netbeans"):
                self.qtcreator_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S qtcreator')
            if os.path.isfile("/usr/bin/netbeans"):
                self.qtcreator_img.set_from_file('categories/gtk-yes.png')

    def on_ninja_ide_clicked(self, widget):
        if os.path.isfile("/usr/bin/ninja-ide"):
            os.system('xfce4-terminal -H -x sudo pacman -R ninja-ide')
            if not os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide_img.set_from_file('categories/gtk-no.png')
        else:
            os.system('xfce4-terminal -H -x sudo pacman -S ninja-ide')
            if os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide_img.set_from_file('categories/gtk-yes.png')


    def on_button1_clicked(self, widget):
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

        # get menu 7 application buttons
        self.geany_ = self.builder8.get_object("geany_")
        self.blender_ = self.builder8.get_object("blender_")
        self.ninja_ide_ = self.builder8.get_object("ninja_ide_")
        self.glade_ = self.builder8.get_object("glade_")
        self.audacious_ = self.builder8.get_object("audacious_")
        self.gimp_ = self.builder8.get_object("gimp_")
        self.evince_ = self.builder8.get_object("evince_")
        self.xfburn_ = self.builder8.get_object("xfburn_")
        self.flashplayer_ = self.builder8.get_object("flashplayer_")
        self.openshot_ = self.builder8.get_object("openshot_")
        self.chromium_ = self.builder8.get_object("chromium_")
        self.deluge_ = self.builder8.get_object("deluge_")
        self.liferea_ = self.builder8.get_object("liferea_")
        self.htop_ = self.builder8.get_object("htop_")
        self.skype_ = self.builder8.get_object("skype_")
        self.wireshark_ = self.builder8.get_object("wireshark_")
        self.virtualbox_ = self.builder8.get_object("virtualbox_")
        self.steam_ = self.builder8.get_object("steam_")
        self.xchat_ = self.builder8.get_object("xchat_")
        self.gedit_ = self.builder8.get_object("gedit_")
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
        self.emacs = self.builder7.get_object("emacs")
        self.vim = self.builder7.get_object("vim")
        self.galculator = self.builder7.get_object("galculator")
        self.gedit = self.builder7.get_object("gedit")
        self.gloobus = self.builder7.get_object("gloobus")
        self.leafpad = self.builder7.get_object("leafpad")
        self.scribes = self.builder7.get_object("scribes")
        self.tomboy = self.builder7.get_object("tomboy")
        self.tuxcards = self.builder7.get_object("tuxcards")
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
        self.guake = self.builder6.get_object("guake")
        self.hardinfo = self.builder6.get_object("hardinfo")
        self.htop = self.builder6.get_object("htop")
        self.keepassx = self.builder6.get_object("keepassx")
        self.playonlinux = self.builder6.get_object("playonlinux")
        self.terminator = self.builder6.get_object("terminator")
        self.thunar = self.builder6.get_object("thunar")
        self.truecrypt = self.builder6.get_object("truecrypt")
        self.unetbootin = self.builder6.get_object("unetbootin")
        self.virtualbox = self.builder6.get_object("virtualbox")
        self.wine = self.builder6.get_object("wine")
        self.wireshark = self.builder6.get_object("wireshark")
        self.xbmc = self.builder6.get_object("xbmc")
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
        self.audacious = self.builder5.get_object("audacious")
        self.banshee = self.builder5.get_object("banshee")
        self.cheese = self.builder5.get_object("cheese")
        self.clementine = self.builder5.get_object("clementine")
        self.flashplayer = self.builder5.get_object("flashplayer")
        self.recordmydesktop = self.builder5.get_object("recordmydesktop")
        self.guayadeque = self.builder5.get_object("guayadeque")
        self.mplayer = self.builder5.get_object("mplayer")
        self.openshot = self.builder5.get_object("openshot")
        self.pitivi = self.builder5.get_object("pitivi")
        self.rhythmbox = self.builder5.get_object("rhythmbox")
        self.soundconverter = self.builder5.get_object("soundconverter")
        self.totem = self.builder5.get_object("totem")
        self.vlc = self.builder5.get_object("vlc")
        self.winff = self.builder5.get_object("winff")
        self.xfburn = self.builder5.get_object("xfburn")
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
        self.deluge = self.builder4.get_object("deluge")
        self.evolution = self.builder4.get_object("evolution")
        self.filezilla = self.builder4.get_object("filezilla")
        self.firefox = self.builder4.get_object("firefox")
        self.chrome = self.builder4.get_object("chrome")
        self.xchat = self.builder4.get_object("xchat")
        self.liferea = self.builder4.get_object("liferea")
        self.midori = self.builder4.get_object("midori")
        self.minitube = self.builder4.get_object("minitube")
        self.opera = self.builder4.get_object("opera")
        self.pidgin = self.builder4.get_object("pidgin")
        self.skyp = self.builder4.get_object("skyp")
        self.steam = self.builder4.get_object("steam")
        self.thunderbird = self.builder4.get_object("thunderbird")
        self.transmission = self.builder4.get_object("transmission")
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
        self.f_spot = self.builder3.get_object("f_spot")
        self.gimp = self.builder3.get_object("gimp")
        self.gwenview = self.builder3.get_object("gwenview")
        self.imagemagick = self.builder3.get_object("imagemagick")
        self.inkscape = self.builder3.get_object("inkscape")
        self.mypaint = self.builder3.get_object("mypaint")
        self.pinta = self.builder3.get_object("pinta")
        self.shotwell = self.builder3.get_object("shotwell")
        self.stellarium = self.builder3.get_object("stellarium")
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
        self.blender = self.builder2.get_object("blender")
        self.bluefish = self.builder2.get_object("bluefish")
        self.eclipse = self.builder2.get_object("eclipse")
        self.geany = self.builder2.get_object("geany")
        self.glade = self.builder2.get_object("glade")
        self.openjdk = self.builder2.get_object("openjdk")
        self.meld = self.builder2.get_object("meld")
        self.netbeans = self.builder2.get_object("netbeans")
        self.qt4 = self.builder2.get_object("qt4")
        self.qt5 = self.builder2.get_object("qt5")
        self.qtcreator = self.builder2.get_object("qtcreator")
        self.ninja_ide = self.builder2.get_object("ninja_ide")
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