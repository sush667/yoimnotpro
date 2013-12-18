#!/usr/bin/python2
import os
import sys
import cairo
from gi.repository import Gtk, GdkPixbuf

class iod:

    # check if the program is started as root, else start it with gksudo
    if os.geteuid() != 0:
        arguments = ['', sys.executable] + sys.argv + [os.environ]
        os.execlpe('gksudo', *arguments)

    # menu 7 button actions
    def on_geany__clicked(self, widget):
        if os.path.isfile("/usr/bin/geany"):
            os.system('pacman -R geany --noconfirm')
            if not os.path.isfile("/usr/bin/geany"):
                self.geany__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Geany was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.geany_.set_tooltip_text("Geany is not installed.\nClick to install it.")
        else:
            os.system('pacman -S geany --noconfirm')
            if os.path.isfile("/usr/bin/geany"):
                self.geany__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Geany was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.geany_.set_tooltip_text("Geany is installed.\nClick to remove it.")

    def on_blender__clicked(self, widget):
        if os.path.isfile("/usr/bin/blender"):
            os.system('pacman -R blender --noconfirm')
            if not os.path.isfile("/usr/bin/blender"):
                self.blender__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Blender was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.blender_.set_tooltip_text("Blender is not installed.\nClick to install it.")
        else:
            os.system('pacman -S blender --noconfirm')
            if os.path.isfile("/usr/bin/blender"):
                self.blender__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Blender was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.blender_.set_tooltip_text("Blender is installed.\nClick to remove it.")

    def on_ninja_ide__clicked(self, widget):
        if os.path.isfile("/usr/bin/ninja-ide"):
            os.system('pacman -R ninja-ide --noconfirm')
            if not os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Ninja-IDE was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.ninja_ide_.set_tooltip_text("Ninja-IDE is not installed.\nClick to install it.")
        else:
            os.system('pacman -S ninja-ide --noconfirm')
            if os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Ninja-IDE was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.ninja_ide_.set_tooltip_text("Ninja-IDE is installed.\nClick to remove it.")

    def on_glade__clicked(self, widget):
        if os.path.isfile("/usr/bin/glade"):
            os.system('pacman -R glade --noconfirm')
            if not os.path.isfile("/usr/bin/glade"):
                self.glade__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Glade was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.glade_.set_tooltip_text("Glade is not installed.\nClick to install it.")
        else:
            os.system('pacman -S glade --noconfirm')
            if os.path.isfile("/usr/bin/glade"):
                self.glade__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Glade was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.glade_.set_tooltip_text("Glade is installed.\nClick to remove it.")

    def on_audacious__clicked(self, widget):
        if os.path.isfile("/usr/bin/audacious"):
            os.system('pacman -R audacious --noconfirm')
            if not os.path.isfile("/usr/bin/audacious"):
                self.audacious__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Audacious was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.audacious_.set_tooltip_text("Audacious is not installed.\nClick to install it.")
        else:
            os.system('pacman -S audacious --noconfirm')
            if os.path.isfile("/usr/bin/audacious"):
                self.audacious__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Audacious was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.audacious_.set_tooltip_text("Audacious is installed.\nClick to remove it.")

    def on_gimp__clicked(self, widget):
        if os.path.isfile("/usr/bin/gimp"):
            os.system('pacman -R gimp --noconfirm')
            if not os.path.isfile("/usr/bin/gimp"):
                self.gimp__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "GIMP was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gimp_.set_tooltip_text("Gimp is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gimp --noconfirm')
            if os.path.isfile("/usr/bin/gimp"):
                self.gimp__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "GIMP was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gimp_.set_tooltip_text("GIMP is installed.\nClick to remove it.")

    def on_evince__clicked(self, widget):
        if os.path.isfile("/usr/bin/evince"):
            os.system('pacman -R evince --noconfirm')
            if not os.path.isfile("/usr/bin/evince"):
                self.evince__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Evince was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.evince_.set_tooltip_text("Evince is not installed.\nClick to install it.")
        else:
            os.system('pacman -S evince --noconfirm')
            if os.path.isfile("/usr/bin/evince"):
                self.evince__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Evince was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.evince_.set_tooltip_text("Evince is installed.\nClick to remove it.")

    def on_xfburn__clicked(self, widget):
        if os.path.isfile("/usr/bin/xfburn"):
            os.system('pacman -R xfburn --noconfirm')
            if not os.path.isfile("/usr/bin/xfburn"):
                self.xfburn__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Xfburn was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.xfburn_.set_tooltip_text("Xfburn is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xfburn --noconfirm')
            if os.path.isfile("/usr/bin/xfburn"):
                self.xfburn__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Xfburn was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.xfburn_.set_tooltip_text("Xfburn is installed.\nClick to remove it.")

    def on_flashplayer__clicked(self, widget):
        if os.path.isfile("/usr/bin/flash-player-properties"):
            os.system('pacman -R flashplugin --noconfirm')
            if not os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Flashplayer was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.flashplayer_.set_tooltip_text("Flashplayer is not installed.\nClick to install it.")
        else:
            os.system('pacman -S flashplugin --noconfirm')
            if os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Flashplayer was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.flashplayer_.set_tooltip_text("Flashplayer is installed.\nClick to remove it.")

    def on_openshot__clicked(self, widget):
        if os.path.isfile("/usr/bin/openshot"):
            os.system('pacman -R openshot --noconfirm')
            if not os.path.isfile("/usr/bin/openshot"):
                self.openshot__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Openshot was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.openshot_.set_tooltip_text("Openshot is not installed.\nClick to install it.")
        else:
            os.system('pacman -S openshot --noconfirm')
            if os.path.isfile("/usr/bin/openshot"):
                self.openshot__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Openshot was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.openshot_.set_tooltip_text("Openshot is installed.\nClick to remove it.")

    def on_chromium__clicked(self, widget):
        if os.path.isfile("/usr/bin/chromium"):
            os.system('pacman -R chromium --noconfirm')
            if not os.path.isfile("/usr/bin/chromium"):
                self.chromium__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Chromium was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.chromium_.set_tooltip_text("Chromium is not installed.\nClick to install it.")
        else:
            os.system('pacman -S chromium --noconfirm')
            if os.path.isfile("/usr/bin/chromium"):
                self.chromium__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Chromium was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.chromium_.set_tooltip_text("Chromium is installed.\nClick to remove it.")

    def on_deluge__clicked(self, widget):
        if os.path.isfile("/usr/bin/deluge"):
            os.system('pacman -R deluge --noconfirm')
            if not os.path.isfile("/usr/bin/deluge"):
                self.deluge__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Deluge was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.deluge_.set_tooltip_text("Deluge is not installed.\nClick to install it.")
        else:
            os.system('pacman -S deluge --noconfirm')
            if os.path.isfile("/usr/bin/deluge"):
                self.deluge__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Deluge was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.deluge_.set_tooltip_text("Deluge is installed.\nClick to remove it.")

    def on_liferea__clicked(self, widget):
        if os.path.isfile("/usr/bin/liferea"):
            os.system('pacman -R liferea --noconfirm')
            if not os.path.isfile("/usr/bin/liferea"):
                self.liferea__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Liferea was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.liferea_.set_tooltip_text("Liferea is not installed.\nClick to install it.")
        else:
            os.system('pacman -S liferea --noconfirm')
            if os.path.isfile("/usr/bin/liferea"):
                self.liferea__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Liferea was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.liferea_.set_tooltip_text("Liferea is installed.\nClick to remove it.")

    def on_htop__clicked(self, widget):
        if os.path.isfile("/usr/bin/htop"):
            os.system('pacman -R htop --noconfirm')
            if not os.path.isfile("/usr/bin/htop"):
                self.htop__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Htop was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.htop_.set_tooltip_text("Htop is not installed.\nClick to install it.")
        else:
            os.system('pacman -S htop --noconfirm')
            if os.path.isfile("/usr/bin/htop"):
                self.htop__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Liferea was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.htop_.set_tooltip_text("Htop is installed.\nClick to remove it.")

    def on_skype__clicked(self, widget):
        if os.path.isfile("/usr/bin/skype"):
            os.system('pacman -R skype --noconfirm')
            if not os.path.isfile("/usr/bin/skype"):
                self.skype__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Skype was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.skype_.set_tooltip_text("Skype is not installed.\nClick to install it.")
        else:
            os.system('pacman -S skype --noconfirm')
            if os.path.isfile("/usr/bin/skype"):
                self.skype__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Skype was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.skype_.set_tooltip_text("Skype is installed.\nClick to remove it.")

    def on_wireshark__clicked(self, widget):
        if os.path.isfile("/usr/bin/wireshark"):
            os.system('pacman -R wireshark-gtk --noconfirm')
            if not os.path.isfile("/usr/bin/wireshark"):
                self.wireshark__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Wireshark was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.wireshark_.set_tooltip_text("Wireshark is not installed.\nClick to install it.")
        else:
            os.system('pacman -S wireshark-gtk --noconfirm')
            if os.path.isfile("/usr/bin/wireshark"):
                self.wireshark__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Wireshark was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.wireshark_.set_tooltip_text("Wireshark is installed.\nClick to remove it.")

    def on_virtualbox__clicked(self, widget):
        if os.path.isfile("/usr/bin/virtualbox"):
            os.system('pacman -R virtualbox --noconfirm')
            if not os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Virtualbox was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.virtualbox_.set_tooltip_text("Virtualbox is not installed.\nClick to install it.")
        else:
            os.system('pacman -S virtualbox --noconfirm')
            if os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Virtualbox was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.virtualbox_.set_tooltip_text("Virtualbox is installed.\nClick to remove it.")

    def on_steam__clicked(self, widget):
        if os.path.isfile("/usr/bin/steam"):
            os.system('pacman -R steam --noconfirm')
            if not os.path.isfile("/usr/bin/steam"):
                self.steam__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Steam was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.steam_.set_tooltip_text("Steam is not installed.\nClick to install it.")
        else:
            os.system('pacman -S steam --noconfirm')
            if os.path.isfile("/usr/bin/steam"):
                self.steam__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Steam was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.steam_.set_tooltip_text("Steam is installed.\nClick to remove it.")

    def on_xchat__clicked(self, widget):
        if os.path.isfile("/usr/bin/xchat"):
            os.system('pacman -R xchat --noconfirm')
            if not os.path.isfile("/usr/bin/xchat"):
                self.xchat__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Xchat was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.xchat_.set_tooltip_text("Xchat is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xchat --noconfirm')
            if os.path.isfile("/usr/bin/xchat"):
                self.xchat__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Xchat was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.xchat_.set_tooltip_text("Xchat is installed.\nClick to remove it.")

    def on_gedit__clicked(self, widget):
        if os.path.isfile("/usr/bin/gedit"):
            os.system('pacman -R gedit --noconfirm')
            if not os.path.isfile("/usr/bin/gedit"):
                self.gedit__img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gedit was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gedit_.set_tooltip_text("gedit is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gedit --noconfirm')
            if os.path.isfile("/usr/bin/gedit"):
                self.gedit__img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gedit was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gedit_.set_tooltip_text("Gedit is installed.\nClick to remove it.")

    # menu 6 button actions
    def on_docky_clicked(self, widget):
        if os.path.isfile("/usr/bin/docky"):
            os.system('pacman -R docky --noconfirm')
            if not os.path.isfile("/usr/bin/docky"):
                self.docky_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Docky was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.docky.set_tooltip_text("Docky is not installed.\nClick to install it.")
        else:
            os.system('pacman -S docky --noconfirm')
            if os.path.isfile("/usr/bin/docky"):
                self.docky_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Docky was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.docky.set_tooltip_text("Docky is installed.\nClick to remove it.")

    def on_emacs_clicked(self, widget):
        if os.path.isfile("/usr/bin/emacs"):
            os.system('pacman -R emacs --noconfirm')
            if not os.path.isfile("/usr/bin/emacs"):
                self.emacs_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Emacs was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.emacs.set_tooltip_text("Emacs is not installed.\nClick to install it.")
        else:
            os.system('pacman -S emacs --noconfirm')
            if os.path.isfile("/usr/bin/emacs"):
                self.emacs_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Emacs was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.emacs.set_tooltip_text("Emacs is installed.\nClick to remove it.")

    def on_vim_clicked(self, widget):
        if os.path.isfile("/usr/bin/vim"):
            os.system('pacman -R vim --noconfirm')
            if not os.path.isfile("/usr/bin/vim"):
                self.vim_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Vim was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.vim.set_tooltip_text("Vim is not installed.\nClick to install it.")
        else:
            os.system('pacman -S vim --noconfirm')
            if os.path.isfile("/usr/bin/vim"):
                self.vim_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Vim was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.vim.set_tooltip_text("Vim is installed.\nClick to remove it.")

    def on_galculator_clicked(self, widget):
        if os.path.isfile("/usr/bin/galculator"):
            os.system('pacman -R galculator --noconfirm')
            if not os.path.isfile("/usr/bin/galculator"):
                self.galculator_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Galculator was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.galculator.set_tooltip_text("Galculator is not installed.\nClick to install it.")
        else:
            os.system('pacman -S galculator --noconfirm')
            if os.path.isfile("/usr/bin/galculator"):
                self.galculator_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Galculator was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.galculator.set_tooltip_text("Galculator is installed.\nClick to remove it.")

    def on_gedit_clicked(self, widget):
        if os.path.isfile("/usr/bin/gedit"):
            os.system('pacman -R gedit --noconfirm')
            if not os.path.isfile("/usr/bin/gedit"):
                self.gedit_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gedit was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gedit.set_tooltip_text("gedit is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gedit --noconfirm')
            if os.path.isfile("/usr/bin/gedit"):
                self.gedit_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gedit was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gedit.set_tooltip_text("gedit is installed.\nClick to remove it.")

    def on_gloobus_clicked(self, widget):
        if os.path.isfile("/usr/bin/gloobus-preview"):
            os.system('pacman -R gloobus-preview --noconfirm')
            if not os.path.isfile("/usr/bin/gloobus-preview"):
                self.gloobus_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gloobus was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gloobus.set_tooltip_text("Gloobus is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gloobus-preview --noconfirm')
            if os.path.isfile("/usr/bin/gloobus-preview"):
                self.gloobus_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gloobus was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gloobus.set_tooltip_text("Gloobus is installed.\nClick to remove it.")

    def on_leafpad_clicked(self, widget):
        if os.path.isfile("/usr/bin/leafpad"):
            os.system('pacman -R leafpad --noconfirm')
            if not os.path.isfile("/usr/bin/leafpad"):
                self.leafpad_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Leafpad was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.leafpad.set_tooltip_text("Leafpad is not installed.\nClick to install it.")
        else:
            os.system('pacman -S leafpad --noconfirm')
            if os.path.isfile("/usr/bin/leafpad"):
                self.leafpad_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Leafpad was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.leafpad.set_tooltip_text("Leafpad is installed.\nClick to remove it.")

    def on_scribes_clicked(self, widget):
        if os.path.isfile("/usr/bin/scribes"):
            os.system('pacman -R scribes --noconfirm')
            if not os.path.isfile("/usr/bin/scribes"):
                self.scribes_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Scribes was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.scribes.set_tooltip_text("Scribes is not installed.\nClick to install it.")
        else:
            os.system('pacman -S scribes --noconfirm')
            if os.path.isfile("/usr/bin/scribes"):
                self.scribes_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Scribes was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.scribes.set_tooltip_text("Scribes is installed.\nClick to remove it.")

    def on_tomboy_clicked(self, widget):
        if os.path.isfile("/usr/bin/tomboy"):
            os.system('pacman -R tomboy --noconfirm')
            if not os.path.isfile("/usr/bin/tomboy"):
                self.tomboy_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Tomboy was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.tomboy.set_tooltip_text("Tomboy is not installed.\nClick to install it.")
        else:
            os.system('pacman -S tomboy --noconfirm')
            if os.path.isfile("/usr/bin/tomboy"):
                self.tomboy_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Tomboy was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.tomboy.set_tooltip_text("Tomboy is installed.\nClick to remove it.")

    def on_tuxcards_clicked(self, widget):
        if os.path.isfile("/usr/bin/tuxcards"):
            os.system('pacman -R tuxcards --noconfirm')
            if not os.path.isfile("/usr/bin/tuxcards"):
                self.tuxcards_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Tuxcards was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.tuxcards.set_tooltip_text("Tuxcards is not installed.\nClick to install it.")
        else:
            os.system('pacman -S tuxcards --noconfirm')
            if os.path.isfile("/usr/bin/tuxcards"):
                self.tuxcards_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Tuxcards was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.tuxcards.set_tooltip_text("Tuxcards is installed.\nClick to remove it.")

    def on_imagewriter_clicked(self, widget):
        if os.path.isfile("/usr/bin/imagewriter"):
            os.system('pacman -R imagewriter --noconfirm')
            if not os.path.isfile("/usr/bin/imagewriter"):
                self.imagewriter_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Imagewriter was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.imagewriter.set_tooltip_text("Imagewriter is not installed.\nClick to install it.")
        else:
            os.system('pacman -S imagewriter --noconfirm')
            if os.path.isfile("/usr/bin/imagewriter"):
                self.imagewriter_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Imagewriter was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.imagewriter.set_tooltip_text("Imagewriter is installed.\nClick to remove it.")

    def on_sevenzip_clicked(self, widget):
        if os.path.isfile("/usr/bin/7zFM"):
            os.system('pacman -R p7zip --noconfirm')
            if not os.path.isfile("/usr/bin/7zFM"):
                self.sevenzip_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "7-zip was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.sevenzip.set_tooltip_text("7-zip is not installed.\nClick to install it.")
        else:
            os.system('pacman -S p7zip --noconfirm')
            if os.path.isfile("/usr/bin/7zFM"):
                self.sevenzip_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "7-zip was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.sevenzip.set_tooltip_text("7-zip is installed.\nClick to remove it.")

    # menu 5 button actions
    def on_gparted_clicked(self, widget):
        if os.path.isfile("/usr/bin/gparted"):
            os.system('pacman -R gparted --noconfirm')
            if not os.path.isfile("/usr/bin/gparted"):
                self.gparted_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gparted was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gparted.set_tooltip_text("Gparted is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gparted --noconfirm')
            if os.path.isfile("/usr/bin/gparted"):
                self.gparted_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gparted was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gparted.set_tooltip_text("Gparted is installed.\nClick to remove it.")

    def on_guake_clicked(self, widget):
        if os.path.isfile("/usr/bin/guake"):
            os.system('pacman -R guake --noconfirm')
            if not os.path.isfile("/usr/bin/guake"):
                self.guake_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Guake was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.guake.set_tooltip_text("Guake is not installed.\nClick to install it.")
        else:
            os.system('pacman -S guake --noconfirm')
            if os.path.isfile("/usr/bin/guake"):
                self.guake_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Guake was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.guake.set_tooltip_text("Guake is installed.\nClick to remove it.")

    def on_hardinfo_clicked(self, widget):
        if os.path.isfile("/usr/bin/hardinfo"):
            os.system('pacman -R hardinfo --noconfirm')
            if not os.path.isfile("/usr/bin/hardinfo"):
                self.hardinfo_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Hardinfo was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.hardinfo.set_tooltip_text("Hardinfo is not installed.\nClick to install it.")
        else:
            os.system('pacman -S hardinfo --noconfirm')
            if os.path.isfile("/usr/bin/hardinfo"):
                self.hardinfo_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Hardinfo was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.hardinfo.set_tooltip_text("Hardinfo is installed.\nClick to remove it.")

    def on_htop_clicked(self, widget):
        if os.path.isfile("/usr/bin/htop"):
            os.system('pacman -R htop --noconfirm')
            if not os.path.isfile("/usr/bin/htop"):
                self.htop_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Htop was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.htop.set_tooltip_text("Htop is not installed.\nClick to install it.")
        else:
            os.system('pacman -S htop --noconfirm')
            if os.path.isfile("/usr/bin/htop"):
                self.htop_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Htop was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.htop.set_tooltip_text("Htop is installed.\nClick to remove it.")

    def on_keepassx_clicked(self, widget):
        if os.path.isfile("/usr/bin/keepassx"):
            os.system('pacman -R keepassx --noconfirm')
            if not os.path.isfile("/usr/bin/keepassx"):
                self.keepassx_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Keepassx was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.keepassx.set_tooltip_text("Keepassx is not installed.\nClick to install it.")
        else:
            os.system('pacman -S keepassx --noconfirm')
            if os.path.isfile("/usr/bin/keepassx"):
                self.keepassx_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Keepassx was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.keepassx.set_tooltip_text("Keepassx is installed.\nClick to remove it.")

    def on_playonlinux_clicked(self, widget):
        if os.path.isfile("/usr/bin/playonlinux"):
            os.system('pacman -R playonlinux --noconfirm')
            if not os.path.isfile("/usr/bin/playonlinux"):
                self.playonlinux_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Playonlinux was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.playonlinux.set_tooltip_text("Playonlinux is not installed.\nClick to install it.")
        else:
            os.system('pacman -S playonlinux --noconfirm')
            if os.path.isfile("/usr/bin/playonlinux"):
                self.playonlinux_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Playonlinux was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.playonlinux.set_tooltip_text("Playonlinux is installed.\nClick to remove it.")

    def on_terminator_clicked(self, widget):
        if os.path.isfile("/usr/bin/terminator"):
            os.system('pacman -R terminator --noconfirm')
            if not os.path.isfile("/usr/bin/terminator"):
                self.terminator_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Terminator was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.terminator.set_tooltip_text("Terminato is not installed.\nClick to install it.")
        else:
            os.system('pacman -S terminator --noconfirm')
            if os.path.isfile("/usr/bin/terminator"):
                self.terminator_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Terminator was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.terminator.set_tooltip_text("Terminator is installed.\nClick to remove it.")

    def on_thunar_clicked(self, widget):
        if os.path.isfile("/usr/bin/thunar"):
            os.system('pacman -R thunar --noconfirm')
            if not os.path.isfile("/usr/bin/thunar"):
                self.thunar_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Thunar was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.thunar.set_tooltip_text("Thunar is not installed.\nClick to install it.")
        else:
            os.system('pacman -S thunar --noconfirm')
            if os.path.isfile("/usr/bin/thunar"):
                self.thunar_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Thunar was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.thunar.set_tooltip_text("Thunar is installed.\nClick to remove it.")

    def on_truecrypt_clicked(self, widget):
        if os.path.isfile("/usr/bin/truecrypt"):
            os.system('pacman -R truecrypt --noconfirm')
            if not os.path.isfile("/usr/bin/truecrypt"):
                self.truecrypt_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Truecrypt was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.truecrypt.set_tooltip_text("Truecrypt is not installed.\nClick to install it.")
        else:
            os.system('pacman -S truecrypt --noconfirm')
            if os.path.isfile("/usr/bin/truecrypt"):
                self.truecrypt_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Truecrypt was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.truecrypt.set_tooltip_text("Truecrypt is installed.\nClick to remove it.")

    def on_unetbootin_clicked(self, widget):
        if os.path.isfile("/usr/bin/unetbootin"):
            os.system('pacman -R unetbootin --noconfirm')
            if not os.path.isfile("/usr/bin/unetbootin"):
                self.unetbootin_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Unetbootin was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.unetbootin.set_tooltip_text("Unetbootin is not installed.\nClick to install it.")
        else:
            os.system('pacman -S unetbootin --noconfirm')
            if os.path.isfile("/usr/bin/unetbootin"):
                self.unetbootin_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Unetbootin was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.unetbootin.set_tooltip_text("Unetoobin is installed.\nClick to remove it.")

    def on_virtualbox_clicked(self, widget):
        if os.path.isfile("/usr/bin/virtualbox"):
            os.system('pacman -R virtualbox --noconfirm')
            if not os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Virtualbox was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.virtualbox.set_tooltip_text("Virtualbox is not installed.\nClick to install it.")
        else:
            os.system('pacman -S virtualbox --noconfirm')
            if os.path.isfile("/usr/bin/virtualbox"):
                self.virtualbox_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Virtualbox was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.virtualbox.set_tooltip_text("Virtualbox is installed.\nClick to remove it.")

    def on_wine_clicked(self, widget):
        if os.path.isfile("/usr/bin/wine"):
            os.system('pacman -R wine --noconfirm')
            if not os.path.isfile("/usr/bin/wine"):
                self.wine_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Wine was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.wine.set_tooltip_text("Wine is not installed.\nClick to install it.")
        else:
            os.system('pacman -S wine --noconfirm')
            if os.path.isfile("/usr/bin/wine"):
                self.wine_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Wine was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.wine.set_tooltip_text("Wine is installed.\nClick to remove it.")

    def on_wireshark_clicked(self, widget):
        if os.path.isfile("/usr/bin/wireshark"):
            os.system('pacman -R wireshark-gtk --noconfirm')
            if not os.path.isfile("/usr/bin/wireshark"):
                self.wireshark_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Wireshark was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.wireshark.set_tooltip_text("Wireshark is not installed.\nClick to install it.")
        else:
            os.system('pacman -S wireshark-gtk --noconfirm')
            if os.path.isfile("/usr/bin/wireshark"):
                self.wireshark_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Wireshark was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.wireshark.set_tooltip_text("Wireshark is installed.\nClick to remove it.")

    def on_xbmc_clicked(self, widget):
        if os.path.isfile("/usr/bin/xbmc"):
            os.system('pacman -R xbmc --noconfirm')
            if not os.path.isfile("/usr/bin/xbmc"):
                self.xbmc_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "XBMC was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.xbmc.set_tooltip_text("XBMC is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xbmc --noconfirm')
            if os.path.isfile("/usr/bin/xbmc"):
                self.xbmc_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "XBMC was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.xbmc.set_tooltip_text("XBMC is installed.\nClick to remove it.")

    def on_gufw_clicked(self, widget):
        if os.path.isfile("/usr/bin/gufw"):
            os.system('pacman -R gufw --noconfirm')
            if not os.path.isfile("/usr/bin/gufw"):
                self.gufw_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gufw was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gufw.set_tooltip_text("Gufw is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gufw --noconfirm')
            if os.path.isfile("/usr/bin/gufw"):
                self.gufw_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gufw was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gufw.set_tooltip_text("Gufw is installed.\nClick to remove it.")

    def on_octopi_clicked(self, widget):
        if os.path.isfile("/usr/bin/octopi"):
            os.system('pacman -R octopi --noconfirm')
            if not os.path.isfile("/usr/bin/octopi"):
                self.octopi_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Octopi was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.octopi.set_tooltip_text("Octopi is not installed.\nClick to install it.")
        else:
            os.system('pacman -S octopi --noconfirm')
            if os.path.isfile("/usr/bin/octopi"):
                self.octopi_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Octopi was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.octopi.set_tooltip_text("Octopi is installed.\nClick to remove it.")

    def on_pamac_clicked(self, widget):
        if os.path.isfile("/usr/bin/pamac-manager"):
            os.system('pacman -R pamac --noconfirm')
            if not os.path.isfile("/usr/bin/pamac-manager"):
                self.pamac_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Pamac was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.pamac.set_tooltip_text("Pamac is not installed.\nClick to install it.")
        else:
            os.system('pacman -S pamac --noconfirm')
            if os.path.isfile("/usr/bin/pamac-manager"):
                self.pamac_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Pamac was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.pamac.set_tooltip_text("Pamac is installed.\nClick to remove it.")

    def on_gnome_system_monitor_clicked(self, widget):
        if os.path.isfile("/usr/bin/gnome-system-monitor"):
            os.system('pacman -R gnome-system-monitor --noconfirm')
            if not os.path.isfile("/usr/bin/gnome-system-monitor"):
                self.gnome_system_monitor_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gnome system monitor was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gnome_system_monitor.set_tooltip_text("Gnome system monitor is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gnome-system-monitor --noconfirm')
            if os.path.isfile("/usr/bin/gnome-system-monitor"):
                self.gnome_system_monitor_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gnome system monitor was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gnome_system_monitor.set_tooltip_text("Gnome system monitor is installed.\nClick to remove it.")

    # menu 4 button actions
    def on_amarok_clicked(self, widget):
        if os.path.isfile("/usr/bin/amarok"):
            os.system('pacman -R amarok --noconfirm')
            if not os.path.isfile("/usr/bin/amarok"):
                self.amarok_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Amarok was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.amarok.set_tooltip_text("Amarok is not installed.\nClick to install it.")
        else:
            os.system('pacman -S amarok --noconfirm')
            if os.path.isfile("/usr/bin/amarok"):
                self.amarok_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Amarok was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.amarok.set_tooltip_text("Amarok is installed.\nClick to remove it.")

    def on_audacious_clicked(self, widget):
        if os.path.isfile("/usr/bin/audacious"):
            os.system('pacman -R audacious --noconfirm')
            if not os.path.isfile("/usr/bin/audacious"):
                self.audacious_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Audacious was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.audacious.set_tooltip_text("Audacious is not installed.\nClick to install it.")
        else:
            os.system('pacman -S audacious --noconfirm')
            if os.path.isfile("/usr/bin/audacious"):
                self.audacious_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Audacious was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.audacious.set_tooltip_text("Audacious is installed.\nClick to remove it.")

    def on_banshee_clicked(self, widget):
        if os.path.isfile("/usr/bin/banshee"):
            os.system('pacman -R banshee --noconfirm')
            if not os.path.isfile("/usr/bin/banshee"):
                self.banshee_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Banshee was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.banshee.set_tooltip_text("Banshee is not installed.\nClick to install it.")
        else:
            os.system('pacman -S banshee --noconfirm')
            if os.path.isfile("/usr/bin/banshee"):
                self.banshee_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Banshee was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.banshee.set_tooltip_text("Banshee is installed.\nClick to remove it.")

    def on_cheese_clicked(self, widget):
        if os.path.isfile("/usr/bin/cheese"):
            os.system('pacman -R cheese --noconfirm')
            if not os.path.isfile("/usr/bin/cheese"):
                self.cheese_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Cheese was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.cheese.set_tooltip_text("Cheese is not installed.\nClick to install it.")
        else:
            os.system('pacman -S cheese --noconfirm')
            if os.path.isfile("/usr/bin/cheese"):
                self.cheese_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Cheese was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.cheese.set_tooltip_text("Cheese is installed.\nClick to remove it.")

    def on_clementine_clicked(self, widget):
        if os.path.isfile("/usr/bin/clementine"):
            os.system('pacman -R clementine --noconfirm')
            if not os.path.isfile("/usr/bin/clementine"):
                self.clementine_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Clementine was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.clementine.set_tooltip_text("Clementine is not installed.\nClick to install it.")
        else:
            os.system('pacman -S clementine --noconfirm')
            if os.path.isfile("/usr/bin/clementine"):
                self.clementine_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Clementine was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.clementine.set_tooltip_text("Clementine is installed.\nClick to remove it.")

    def on_flashplayer_clicked(self, widget):
        if os.path.isfile("/usr/bin/flash-player-properties"):
            os.system('pacman -R flashplugin --noconfirm')
            if not os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Flashplayer was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.flashplayer.set_tooltip_text("Flashplayer is not installed.\nClick to install it.")
        else:
            os.system('pacman -S flashplugin --noconfirm')
            if os.path.isfile("/usr/bin/flash-player-properties"):
                self.flashplayer_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Flashplayer was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.flashplayer.set_tooltip_text("Flashpleyer is installed.\nClick to remove it.")

    def on_recordmydesktop_clicked(self, widget):
        if os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
            os.system('pacman -R gtk-recordmydesktop --noconfirm')
            if not os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
                self.recordmydesktop_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Record My Desktop was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.recordmydesktop.set_tooltip_text("RecordMyDesktop is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gtk-recordmydesktop --noconfirm')
            if os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
                self.recordmydesktop_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Record My Desktop was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.recordmydesktop.set_tooltip_text("RecordMyDesktop is installed.\nClick to remove it.")

    def on_guayadeque_clicked(self, widget):
        if os.path.isfile("/usr/bin/guayadeque"):
            os.system('pacman -R guayadeque --noconfirm')
            if not os.path.isfile("/usr/bin/guayadeque"):
                self.guayadeque_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Guayadeque was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.guayadeque.set_tooltip_text("Guayadeque is not installed.\nClick to install it.")
        else:
            os.system('pacman -S guayadeque --noconfirm')
            if os.path.isfile("/usr/bin/guayadeque"):
                self.guayadeque_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Guayadeque was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.guayadeque.set_tooltip_text("Guayadeque is installed.\nClick to remove it.")

    def on_mplayer_clicked(self, widget):
        if os.path.isfile("/usr/bin/mplayer"):
            os.system('pacman -R mplayer --noconfirm')
            if not os.path.isfile("/usr/bin/mplayer"):
                self.mplayer_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Mplayer was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.mplayer.set_tooltip_text("Mplayer is not installed.\nClick to install it.")
        else:
            os.system('pacman -S mplayer --noconfirm')
            if os.path.isfile("/usr/bin/mplayer"):
                self.mplayer_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Mplayer was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.mplayer.set_tooltip_text("Mplayer is installed.\nClick to remove it.")

    def on_openshot_clicked(self, widget):
        if os.path.isfile("/usr/bin/openshot"):
            os.system('pacman -R openshot --noconfirm')
            if not os.path.isfile("/usr/bin/openshot"):
                self.openshot_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Openshot was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.openshot.set_tooltip_text("Openshot is not installed.\nClick to install it.")
        else:
            os.system('pacman -S openshot --noconfirm')
            if os.path.isfile("/usr/bin/openshot"):
                self.openshot_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Openshot was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.openshot.set_tooltip_text("Openshot is installed.\nClick to remove it.")

    def on_pitivi_clicked(self, widget):
        if os.path.isfile("/usr/bin/pitivi"):
            os.system('pacman -R pitivi --noconfirm')
            if not os.path.isfile("/usr/bin/pitivi"):
                self.pitivi_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "PiTiVi was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.pitivi.set_tooltip_text("PiTiVi is not installed.\nClick to install it.")
        else:
            os.system('pacman -S pitivi --noconfirm')
            if os.path.isfile("/usr/bin/pitivi"):
                self.pitivi_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "PiTiVi was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.pitivi.set_tooltip_text("PiTiVi is installed.\nClick to remove it.")

    def on_rhythmbox_clicked(self, widget):
        if os.path.isfile("/usr/bin/rhythmbox"):
            os.system('pacman -R rhythmbox --noconfirm')
            if not os.path.isfile("/usr/bin/rhythmbox"):
                self.rhythmbox_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Rhythmbox was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.rhythmbox.set_tooltip_text("Rhythmbox is not installed.\nClick to install it.")
        else:
            os.system('pacman -S rhythmbox --noconfirm')
            if os.path.isfile("/usr/bin/rhythmbox"):
                self.rhythmbox_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Rhythmbox was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.rhythmbox.set_tooltip_text("Rhythmbox is installed.\nClick to remove it.")

    def on_soundconverter_clicked(self, widget):
        if os.path.isfile("/usr/bin/soundconverter"):
            os.system('pacman -R soundconverter --noconfirm')
            if not os.path.isfile("/usr/bin/soundconverter"):
                self.soundconverter_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Sound converter was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.soundconverter.set_tooltip_text("Soundconverter is not installed.\nClick to install it.")
        else:
            os.system('pacman -S soundconverter --noconfirm')
            if os.path.isfile("/usr/bin/soundconverter"):
                self.soundconverter_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Sound converter was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.soundconverter.set_tooltip_text("Soundconverter is installed.\nClick to remove it.")

    def on_totem_clicked(self, widget):
        if os.path.isfile("/usr/bin/totem"):
            os.system('pacman -R totem --noconfirm')
            if not os.path.isfile("/usr/bin/totem"):
                self.totem_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Totem was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.totem.set_tooltip_text("Totem is not installed.\nClick to install it.")
        else:
            os.system('pacman -S totem --noconfirm')
            if os.path.isfile("/usr/bin/totem"):
                self.totem_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Totem was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.totem.set_tooltip_text("Totem is installed.\nClick to remove it.")

    def on_vlc_clicked(self, widget):
        if os.path.isfile("/usr/bin/vlc"):
            os.system('pacman -R vlc --noconfirm')
            if not os.path.isfile("/usr/bin/vlc"):
                self.vlc_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "VLC was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.vlc.set_tooltip_text("Vlc is not installed.\nClick to install it.")
        else:
            os.system('pacman -S vlc --noconfirm')
            if os.path.isfile("/usr/bin/vlc"):
                self.vlc_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "VLC was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.vlc.set_tooltip_text("Vlc is installed.\nClick to remove it.")

    def on_winff_clicked(self, widget):
        if os.path.isfile("/usr/bin/winff"):
            os.system('pacman -R winff --noconfirm')
            if not os.path.isfile("/usr/bin/winff"):
                self.winff_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Winff was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.winff.set_tooltip_text("Winff is not installed.\nClick to install it.")
        else:
            os.system('pacman -S winff --noconfirm')
            if os.path.isfile("/usr/bin/winff"):
                self.winff_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Winff was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.winff.set_tooltip_text("Winff is installed.\nClick to remove it.")

    def on_xfburn_clicked(self, widget):
        if os.path.isfile("/usr/bin/xfburn"):
            os.system('pacman -R xfburn --noconfirm')
            if not os.path.isfile("/usr/bin/xfburn"):
                self.xfburn_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Xfburn was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.xfburn.set_tooltip_text("Xfburn is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xfburn --noconfirm')
            if os.path.isfile("/usr/bin/xfburn"):
                self.xfburn_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Xfburn was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.xfburn.set_tooltip_text("Xfburn is installed.\nClick to remove it.")

    def on_kdenlive_clicked(self, widget):
        if os.path.isfile("/usr/bin/kdenlive"):
            os.system('pacman -R kdenlive --noconfirm')
            if not os.path.isfile("/usr/bin/kdenlive"):
                self.kdenlive_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Kdenlive was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.kdenlive.set_tooltip_text("Kdenlive is not installed.\nClick to install it.")
        else:
            os.system('pacman -S kdenlive --noconfirm')
            if os.path.isfile("/usr/bin/kdenlive"):
                self.kdenlive_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Kdenlive was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.kdenlive.set_tooltip_text("Kdenlive is installed.\nClick to remove it.")

    def on_simplescreenrecorder_clicked(self, widget):
        if os.path.isfile("/usr/bin/simplescreenrecorder"):
            os.system('pacman -R simplescreenrecorder --noconfirm')
            if not os.path.isfile("/usr/bin/simplescreenrecorder"):
                self.simplescreenrecorder_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Simple screen recorder was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.simplescreenrecorder.set_tooltip_text("Simple screen recorder is not installed.\nClick to install it.")
        else:
            os.system('yaourt -S simplescreenrecorder --noconfirm')
            if os.path.isfile("/usr/bin/simplescreenrecorder"):
                self.simplescreenrecorder_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Simple screen recorder was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.simplescreenrecorder.set_tooltip_text("Simple screen recorder is installed.\nClick to remove it.")

    def on_vokoscreen_clicked(self, widget):
        if os.path.isfile("/usr/bin/vokoscreen"):
            os.system('pacman -R vokoscreen --noconfirm')
            if not os.path.isfile("/usr/bin/vokoscreen"):
                self.vokoscreen_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Vokoscreen was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.vokoscreen.set_tooltip_text("Vokoscreen is not installed.\nClick to install it.")
        else:
            os.system('yaourt -S vokoscreen --noconfirm')
            if os.path.isfile("/usr/bin/vokoscreen"):
                self.vokoscreen_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Vokoscreen was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.vokoscreen.set_tooltip_text("Vokoscreen is installed.\nClick to remove it.")

    # menu 3 button actions
    def on_linuxdcpp_clicked(self, widget):
        if os.path.isfile("/usr/bin/linuxdcpp"):
            os.system('pacman -R linuxdcpp --noconfirm')
            if not os.path.isfile("/usr/bin/linuxdcpp"):
                self.linuxdcpp_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Linuxdcpp was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.linuxdcpp.set_tooltip_text("Linuxdcpp is not installed.\nClick to install it.")
        else:
            os.system('pacman -S linuxdcpp --noconfirm')
            if os.path.isfile("/usr/bin/linuxdcpp"):
                self.linuxdcpp_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Linuxdcpp was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.linuxdcpp.set_tooltip_text("Linuxdcpp is installed.\nClick to remove it.")

    def on_chromium_clicked(self, widget):
        if os.path.isfile("/usr/bin/chromium"):
            os.system('pacman -R chromium --noconfirm')
            if not os.path.isfile("/usr/bin/chromium"):
                self.chromium_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Chromium was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.chromium.set_tooltip_text("Chromium is not installed.\nClick to install it.")
        else:
            os.system('pacman -S chromium --noconfirm')
            if os.path.isfile("/usr/bin/chromium"):
                self.chromium_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Chromium was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.chromium.set_tooltip_text("Chromium is installed.\nClick to remove it.")

    def on_deluge_clicked(self, widget):
        if os.path.isfile("/usr/bin/deluge"):
            os.system('pacman -R deluge --noconfirm')
            if not os.path.isfile("/usr/bin/deluge"):
                self.deluge_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Deluge was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.deluge.set_tooltip_text("Deluge is not installed.\nClick to install it.")
        else:
            os.system('pacman -S deluge --noconfirm')
            if os.path.isfile("/usr/bin/deluge"):
                self.deluge_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Deluge was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.deluge.set_tooltip_text("Deluge is installed.\nClick to remove it.")

    def on_evolution_clicked(self, widget):
        if os.path.isfile("/usr/bin/evolution"):
            os.system('pacman -R evolution --noconfirm')
            if not os.path.isfile("/usr/bin/evolution"):
                self.evolution_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Evolution was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.evolution.set_tooltip_text("Evolution is not installed.\nClick to install it.")
        else:
            os.system('pacman -S evolution --noconfirm')
            if os.path.isfile("/usr/bin/evolution"):
                self.evolution_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Evolution was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.evolution.set_tooltip_text("Evolution is installed.\nClick to remove it.")

    def on_filezilla_clicked(self, widget):
        if os.path.isfile("/usr/bin/filezilla"):
            os.system('pacman -R filezilla --noconfirm')
            if not os.path.isfile("/usr/bin/filezilla"):
                self.filezilla_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Filezilla was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.filezilla.set_tooltip_text("Filezilla is not installed.\nClick to install it.")
        else:
            os.system('pacman -S filezilla --noconfirm')
            if os.path.isfile("/usr/bin/filezilla"):
                self.filezilla_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Filezilla was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.filezilla.set_tooltip_text("Filezilla is installed.\nClick to remove it.")

    def on_firefox_clicked(self, widget):
        if os.path.isfile("/usr/bin/firefox"):
            os.system('pacman -R firefox --noconfirm')
            if not os.path.isfile("/usr/bin/firefox"):
                self.firefox_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Firefox was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.firefox.set_tooltip_text("Firefox is not installed.\nClick to install it.")
        else:
            os.system('pacman -S firefox --noconfirm')
            if os.path.isfile("/usr/bin/firefox"):
                self.firefox_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Firefox was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.firefox.set_tooltip_text("Firefox is installed.\nClick to remove it.")

    def on_chrome_clicked(self, widget):
        if os.path.isfile("/usr/bin/google-chrome-stable"):
            os.system('pacman -R google-chrome --noconfirm')
            if not os.path.isfile("/usr/bin/google-chrome-stable"):
                self.chrome_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Google Chrome was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.chrome.set_tooltip_text("Google Chrome is not installed.\nClick to install it.")
        else:
            os.system('yaourt -S google-chrome --noconfirm')
            if os.path.isfile("/usr/bin/google-chrome-stable"):
                self.chrome_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Google Chrome was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.chrome.set_tooltip_text("Google Chrome is installed.\nClick to remove it.")

    def on_xchat_clicked(self, widget):
        if os.path.isfile("/usr/bin/xchat"):
            os.system('pacman -R xchat --noconfirm')
            if not os.path.isfile("/usr/bin/xchat"):
                self.xchat_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Xchat was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.xchat.set_tooltip_text("Xchat is not installed.\nClick to install it.")
        else:
            os.system('pacman -S xchat --noconfirm')
            if os.path.isfile("/usr/bin/xchat"):
                self.xchat_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Xchat was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.xchat.set_tooltip_text("Xchat is installed.\nClick to remove it.")

    def on_liferea_clicked(self, widget):
        if os.path.isfile("/usr/bin/liferea"):
            os.system('pacman -R liferea --noconfirm')
            if not os.path.isfile("/usr/bin/liferea"):
                self.liferea_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Liferea was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.liferea.set_tooltip_text("Liferea is not installed.\nClick to install it.")
        else:
            os.system('pacman -S liferea --noconfirm')
            if os.path.isfile("/usr/bin/liferea"):
                self.liferea_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Liferea was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.liferea.set_tooltip_text("Liferea is installed.\nClick to remove it.")

    def on_midori_clicked(self, widget):
        if os.path.isfile("/usr/bin/midori"):
            os.system('pacman -R midori --noconfirm')
            if not os.path.isfile("/usr/bin/midori"):
                self.midori_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Midori was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.midori.set_tooltip_text("Midori is not installed.\nClick to install it.")
        else:
            os.system('pacman -S midori --noconfirm')
            if os.path.isfile("/usr/bin/midori"):
                self.midori_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Midori was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.midori.set_tooltip_text("Midori is installed.\nClick to remove it.")

    def on_minitube_clicked(self, widget):
        if os.path.isfile("/usr/bin/minitube"):
            os.system('pacman -R minitube --noconfirm')
            if not os.path.isfile("/usr/bin/minitube"):
                self.minitube_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "MiniTube was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.minitube.set_tooltip_text("MiniTube is not installed.\nClick to install it.")
        else:
            os.system('pacman -S minitube --noconfirm')
            if os.path.isfile("/usr/bin/minitube"):
                self.minitube_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "MiniTube was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.minitube.set_tooltip_text("MiniTube is installed.\nClick to remove it.")

    def on_opera_clicked(self, widget):
        if os.path.isfile("/usr/bin/opera"):
            os.system('pacman -R opera --noconfirm')
            if not os.path.isfile("/usr/bin/opera"):
                self.opera_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Opera was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.opera.set_tooltip_text("Opera is not installed.\nClick to install it.")
        else:
            os.system('pacman -S opera --noconfirm')
            if os.path.isfile("/usr/bin/opera"):
                self.opera_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Opera was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.opera.set_tooltip_text("Opera is installed.\nClick to remove it.")

    def on_pidgin_clicked(self, widget):
        if os.path.isfile("/usr/bin/pidgin"):
            os.system('pacman -R pidgin --noconfirm')
            if not os.path.isfile("/usr/bin/pidgin"):
                self.pidgin_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Pidgin was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.pidgin.set_tooltip_text("Pidgin is not installed.\nClick to install it.")
        else:
            os.system('pacman -S pidgin --noconfirm')
            if os.path.isfile("/usr/bin/pidgin"):
                self.pidgin_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Pidgin was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.pidgin.set_tooltip_text("Pidgin is installed.\nClick to remove it.")

    def on_skyp_clicked(self, widget):
        if os.path.isfile("/usr/bin/skype"):
            os.system('pacman -R skype --noconfirm')
            if not os.path.isfile("/usr/bin/skype"):
                self.skype_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Skype was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.skyp.set_tooltip_text("Skype is not installed.\nClick to install it.")
        else:
            os.system('pacman -S skype --noconfirm')
            if os.path.isfile("/usr/bin/skype"):
                self.skype_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Skype was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.skyp.set_tooltip_text("Skype is installed.\nClick to remove it.")

    def on_steam_clicked(self, widget):
        if os.path.isfile("/usr/bin/steam"):
            os.system('pacman -R steam --noconfirm')
            if not os.path.isfile("/usr/bin/steam"):
                self.steam_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Steam was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.steam.set_tooltip_text("Steam is not installed.\nClick to install it.")
        else:
            os.system('pacman -S steam --noconfirm')
            if os.path.isfile("/usr/bin/steam"):
                self.steam_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Steam was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.steam.set_tooltip_text("Steam is installed.\nClick to remove it.")

    def on_thunderbird_clicked(self, widget):
        if os.path.isfile("/usr/bin/thunderbird"):
            os.system('pacman -R thunderbird --noconfirm')
            if not os.path.isfile("/usr/bin/thunderbird"):
                self.thunderbird_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Thunderbird was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.thunderbird.set_tooltip_text("Thunderbird is not installed.\nClick to install it.")
        else:
            os.system('pacman -S thunderbird --noconfirm')
            if os.path.isfile("/usr/bin/thunderbird"):
                self.thunderbird_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Thunderbird was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.thunderbird.set_tooltip_text("Thunderbird is not installed.\nClick to install it.")

    def on_transmission_clicked(self, widget):
        if os.path.isfile("/usr/bin/transmission-gtk"):
            os.system('pacman -R transmission-gtk --noconfirm')
            if not os.path.isfile("/usr/bin/transmission-gtk"):
                self.transmission_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Transmission was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.transmission.set_tooltip_text("Transmission is not installed.\nClick to install it.")
        else:
            os.system('pacman -S transmission-gtk --noconfirm')
            if os.path.isfile("/usr/bin/transmission-gtk"):
                self.transmission_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Transmission was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.transmission.set_tooltip_text("Transmission is installed.\nClick to remove it.")

    # menu 2 button actions
    def on_evince_clicked(self, widget):
        if os.path.isfile("/usr/bin/evince"):
            os.system('pacman -R evince --noconfirm')
            if not os.path.isfile("/usr/bin/evince"):
                self.evince_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Evince was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.evince.set_tooltip_text("Evince is not installed.\nClick to install it.")
        else:
            os.system('pacman -S evince --noconfirm')
            if os.path.isfile("/usr/bin/evince"):
                self.evince_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Evince was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.evince.set_tooltip_text("Evince is installed.\nClick to remove it.")

    def on_f_spot_clicked(self, widget):
        if os.path.isfile("/usr/bin/f-spot"):
            os.system('pacman -R f-spot --noconfirm')
            if not os.path.isfile("/usr/bin/f-spot"):
                self.f_spot_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "F-spot was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.f_spot.set_tooltip_text("F-spot is not installed.\nClick to install it.")
        else:
            os.system('pacman -S f-spot --noconfirm')
            if os.path.isfile("/usr/bin/f-spot"):
                self.f_spot_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "F-spot was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.f_spot.set_tooltip_text("F-spot is installed.\nClick to remove it.")

    def on_gimp_clicked(self, widget):
        if os.path.isfile("/usr/bin/gimp"):
            os.system('pacman -R gimp --noconfirm')
            if not os.path.isfile("/usr/bin/gimp"):
                self.gimp_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "GIMP was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gimp.set_tooltip_text("GIMP is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gimp --noconfirm')
            if os.path.isfile("/usr/bin/gimp"):
                self.gimp_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "GIMP was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gimp.set_tooltip_text("GIMP is installed.\nClick to remove it.")

    def on_gwenview_clicked(self, widget):
        if os.path.isfile("/usr/bin/gwenview"):
            os.system('pacman -R gwenview --noconfirm')
            if not os.path.isfile("/usr/bin/gwenview"):
                self.gwenview_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gwenview was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.gwenview.set_tooltip_text("Gwenview is not installed.\nClick to install it.")
        else:
            os.system('pacman -S gwenview --noconfirm')
            if os.path.isfile("/usr/bin/gwenview"):
                self.gwenview_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Gwenview was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.gwenview.set_tooltip_text("Gwenview is installed.\nClick to remove it.")

    def on_imagemagick_clicked(self, widget):
        if os.path.isfile("/usr/bin/convert"):
            os.system('pacman -R imagemagick --noconfirm')
            if not os.path.isfile("/usr/bin/convert"):
                self.imagemagick_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Imagemagick was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.imagemagick.set_tooltip_text("ImageMagick is not installed.\nClick to install it.")
        else:
            os.system('pacman -S imagemagick --noconfirm')
            if os.path.isfile("/usr/bin/convert"):
                self.imagemagick_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Imagemagick was installed successfully\nPlease note that it\'s operated via command line interface.")
                dialog.run()
                dialog.destroy()
                self.imagemagick.set_tooltip_text("ImageMagick is installed.\nClick to remove it.")

    def on_inkscape_clicked(self, widget):
        if os.path.isfile("/usr/bin/inkscape"):
            os.system('pacman -R inkscape --noconfirm')
            if not os.path.isfile("/usr/bin/inkscape"):
                self.inkscape_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Inkscape was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.inkscape.set_tooltip_text("Inkscape is not installed.\nClick to install it.")
        else:
            os.system('pacman -S inkscape --noconfirm')
            if os.path.isfile("/usr/bin/inkscape"):
                self.inkscape_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Inkscape was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.inkscape.set_tooltip_text("Inkscape is installed.\nClick to remove it.")

    def on_mypaint_clicked(self, widget):
        if os.path.isfile("/usr/bin/mypaint"):
            os.system('pacman -R mypaint --noconfirm')
            if not os.path.isfile("/usr/bin/mypaint"):
                self.mypaint_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "MyPaint was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.mypaint.set_tooltip_text("MyPaint is not installed.\nClick to install it.")
        else:
            os.system('pacman -S mypaint --noconfirm')
            if os.path.isfile("/usr/bin/mypaint"):
                self.mypaint_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "MyPaint was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.mypaint.set_tooltip_text("MyPaint is installed.\nClick to remove it.")

    def on_pinta_clicked(self, widget):
        if os.path.isfile("/usr/bin/pinta"):
            os.system('pacman -R pinta --noconfirm')
            if not os.path.isfile("/usr/bin/pinta"):
                self.pinta_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Pinta was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.pinta.set_tooltip_text("Pinta is not installed.\nClick to install it.")
        else:
            os.system('pacman -S pinta --noconfirm')
            if os.path.isfile("/usr/bin/pinta"):
                self.pinta_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Pinta was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.pinta.set_tooltip_text("Pinta is installed.\nClick to remove it.")

    def on_shotwell_clicked(self, widget):
        if os.path.isfile("/usr/bin/shotwell"):
            os.system('pacman -R shotwell --noconfirm')
            if not os.path.isfile("/usr/bin/shotwell"):
                self.shotwell_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Shotwell was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.shotwell.set_tooltip_text("Shotwell is not installed.\nClick to install it.")
        else:
            os.system('pacman -S shotwell --noconfirm')
            if os.path.isfile("/usr/bin/shotwell"):
                self.shotwell_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Shotwell was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.shotwell.set_tooltip_text("Shotwell is installed.\nClick to remove it.")

    def on_stellarium_clicked(self, widget):
        if os.path.isfile("/usr/bin/stellarium"):
            os.system('pacman -R stellarium --noconfirm')
            if not os.path.isfile("/usr/bin/stellarium"):
                self.stellarium_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Stellarium was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.stellarium.set_tooltip_text("Stellarium is not installed.\nClick to install it.")
        else:
            os.system('pacman -S stellarium --noconfirm')
            if os.path.isfile("/usr/bin/stellarium"):
                self.stellarium_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Stellarium was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.stellarium.set_tooltip_text("Stellarium is installed.\nClick to remove it.")

    # menu 1 button actions
    def on_anjuta_clicked(self, widget):
        if os.path.isfile("/usr/bin/anjuta"):
            os.system('pacman -R anjuta --noconfirm')
            if not os.path.isfile("/usr/bin/anjuta"):
                self.anjuta_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Anjuta was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.anjuta.set_tooltip_text("Anjuta is not installed.\nClick to install it.")
        else:
            os.system('pacman -S anjuta --noconfirm')
            if os.path.isfile("/usr/bin/anjuta"):
                self.anjuta_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Anjuta was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.anjuta.set_tooltip_text("Anjuta is installed.\nClick to remove it.")

    def on_blender_clicked(self, widget):
        if os.path.isfile("/usr/bin/blender"):
            os.system('pacman -R blender --noconfirm')
            if not os.path.isfile("/usr/bin/blender"):
                self.blender_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Blender was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.blender.set_tooltip_text("Blender is not installed.\nClick to install it.")
        else:
            os.system('pacman -S blender --noconfirm')
            if os.path.isfile("/usr/bin/blender"):
                self.blender_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Blender was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.blender.set_tooltip_text("Blender is installed.\nClick to remove it.")

    def on_bluefish_clicked(self, widget):
        if os.path.isfile("/usr/bin/bluefish"):
            os.system('pacman -R bluefish --noconfirm')
            if not os.path.isfile("/usr/bin/bluefish"):
                self.bluefish_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Bluefish was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.bluefish.set_tooltip_text("Bluefish is not installed.\nClick to install it.")
        else:
            os.system('pacman -S bluefish --noconfirm')
            if os.path.isfile("/usr/bin/bluefish"):
                self.bluefish_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Bluefish was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.bluefish.set_tooltip_text("Bluefish is installed.\nClick to remove it.")

    def on_eclipse_clicked(self, widget):
        if os.path.isfile("/usr/bin/eclipse"):
            os.system('pacman -R eclipse --noconfirm')
            if not os.path.isfile("/usr/bin/eclipse"):
                self.eclipse_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Eclipse was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.eclipse.set_tooltip_text("Eclipse is not installed.\nClick to install it.")
        else:
            os.system('pacman -S eclipse --noconfirm')
            if os.path.isfile("/usr/bin/eclipse"):
                self.eclipse_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Eclipse was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.eclipse.set_tooltip_text("Eclipse is installed.\nClick to remove it.")

    def on_geany_clicked(self, widget):
        if os.path.isfile("/usr/bin/geany"):
            os.system('pacman -R geany --noconfirm')
            if not os.path.isfile("/usr/bin/geany"):
                self.geany_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Geany was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.geany.set_tooltip_text("Geany is not installed.\nClick to install it.")
        else:
            os.system('pacman -S geany --noconfirm')
            if os.path.isfile("/usr/bin/geany"):
                self.geany_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Geany was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.geany.set_tooltip_text("Geany is installed.\nClick to remove it.")

    def on_glade_clicked(self, widget):
        if os.path.isfile("/usr/bin/glade"):
            os.system('pacman -R glade --noconfirm')
            if not os.path.isfile("/usr/bin/glade"):
                self.glade_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Glade was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.glade.set_tooltip_text("Glade is not installed.\nClick to install it.")
        else:
            os.system('pacman -S glade --noconfirm')
            if os.path.isfile("/usr/bin/glade"):
                self.glade_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Glade was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.glade.set_tooltip_text("Glade is installed.\nClick to remove it.")

    def on_openjdk_clicked(self, widget):
        if os.path.exists("/etc/java-7-openjdk/"):
            os.system('pacman -R jre7-openjdk --noconfirm')
            if not os.path.exists("/etc/java-7-openjdk/"):
                self.openjdk_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "OpenJDK was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.openjdk.set_tooltip_text("OpenJDK is not installed.\nClick to install it.")
        else:
            os.system('pacman -S jre7-openjdk --noconfirm')
            if os.path.exists("/etc/java-7-openjdk/"):
                self.openjdk_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "OpenJDK was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.openjdk.set_tooltip_text("OpenJDK is installed.\nClick to remove it.")

    def on_meld_clicked(self, widget):
        if os.path.isfile("/usr/bin/meld"):
            os.system('pacman -R meld --noconfirm')
            if not os.path.isfile("/usr/bin/meld"):
                self.meld_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Meld was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.meld.set_tooltip_text("Meld is not installed.\nClick to install it.")
        else:
            os.system('pacman -S meld --noconfirm')
            if os.path.isfile("/usr/bin/meld"):
                self.meld_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Meld was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.meld.set_tooltip_text("Meld is installed.\nClick to remove it.")

    def on_netbeans_clicked(self, widget):
        if os.path.isfile("/usr/bin/netbeans"):
            os.system('pacman -R netbeans --noconfirm')
            if not os.path.isfile("/usr/bin/netbeans"):
                self.netbeans_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "NetBeans was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.netbeans.set_tooltip_text("NetBeans is not installed.\nClick to install it.")
        else:
            os.system('pacman -S netbeans --noconfirm')
            if os.path.isfile("/usr/bin/netbeans"):
                self.netbeans_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "NetBeans was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.netbeans.set_tooltip_text("NetBeans is installed.\nClick to remove it.")

    def on_qt4_clicked(self, widget):
        if os.path.isfile("/usr/lib/qt4/bin/designer"):
            os.system('pacman -R qt4 --noconfirm')
            if not os.path.isfile("/usr/lib/qt4/bin/designer"):
                self.qt4_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Qt 4 was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.qt4.set_tooltip_text("Qt4 is not installed.\nClick to install it.")
        else:
            os.system('pacman -S qt4 --noconfirm')
            if os.path.isfile("/usr/lib/qt4/bin/designer"):
                self.qt4_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Qt 4 was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.qt4.set_tooltip_text("Qt4 is installed.\nClick to remove it.")

    def on_qt5_clicked(self, widget):
        if os.path.isfile("/usr/lib/qt/bin/designer"):
            os.system('pacman -R qt5-base --noconfirm')
            if not os.path.isfile("/usr/lib/qt/bin/designer"):
                self.qt5_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Qt 5 was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.qt5.set_tooltip_text("Qt5 is not installed.\nClick to install it.")
        else:
            os.system('pacman -S qt5-base --noconfirm')
            if os.path.isfile("/usr/lib/qt/bin/designer"):
                self.qt5_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Qt 5 was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.qt5.set_tooltip_text("Qt5 is installed.\nClick to remove it.")

    def on_qtcreator_clicked(self, widget):
        if os.path.isfile("/usr/bin/netbeans"):
            os.system('pacman -R qtcreator --noconfirm')
            if not os.path.isfile("/usr/bin/netbeans"):
                self.qtcreator_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Qt Creator was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.qtcreator.set_tooltip_text("QtCreator is not installed.\nClick to install it.")
        else:
            os.system('pacman -S qtcreator --noconfirm')
            if os.path.isfile("/usr/bin/netbeans"):
                self.qtcreator_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Qt Creaator was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.qtcreator.set_tooltip_text("QtCreator is installed.\nClick to remove it.")

    def on_ninja_ide_clicked(self, widget):
        if os.path.isfile("/usr/bin/ninja-ide"):
            os.system('pacman -R ninja-ide --noconfirm')
            if not os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide_img.set_from_file('categories/gtk-no.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Ninja-IDE was removed successfully.")
                dialog.run()
                dialog.destroy()
                self.ninja_ide.set_tooltip_text("Ninja-IDE is not installed.\nClick to install it.")
        else:
            os.system('pacman -S ninja-ide --noconfirm')
            if os.path.isfile("/usr/bin/ninja-ide"):
                self.ninja_ide_img.set_from_file('categories/gtk-yes.png')
                dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                    Gtk.ButtonsType.OK, "Ninja-IDE was installed successfully.")
                dialog.run()
                dialog.destroy()
                self.ninja_ide.set_tooltip_text("Ninja-IDE is installed.\nClick to remove it.")

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
        if os.path.isfile("/usr/bin/anjuta"):
            self.anjuta_img.set_from_file('categories/gtk-yes.png')
            self.anjuta.set_tooltip_text("Anjuta is installed.\nClick to remove it.")
        else:
            self.anjuta_img.set_from_file('categories/gtk-no.png')
            self.anjuta.set_tooltip_text("Anjuta is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/blender"):
            self.blender_img.set_from_file('categories/gtk-yes.png')
            self.blender.set_tooltip_text("Blender is installed.\nClick to remove it.")
        else:
            self.blender_img.set_from_file('categories/gtk-no.png')
            self.blender.set_tooltip_text("Blender is not installed.\nClick to insall it.")

        if os.path.isfile("/usr/bin/bluefish"):
            self.bluefish_img.set_from_file('categories/gtk-yes.png')
            self.bluefish.set_tooltip_text("Bluefish is installed.\nClick to remove it.")
        else:
            self.bluefish_img.set_from_file('categories/gtk-no.png')
            self.bluefish.set_tooltip_text("Bluefish is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/eclipse"):
            self.eclipse_img.set_from_file('categories/gtk-yes.png')
            self.eclipse.set_tooltip_text("Eclipse is installed.\nClick to remove it.")
        else:
            self.eclipse_img.set_from_file('categories/gtk-no.png')
            self.eclipse.set_tooltip_text("Eclipse is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/geany"):
            self.geany_img.set_from_file('categories/gtk-yes.png')
            self.geany.set_tooltip_text("Geany is installed.\nClick to install it.")
        else:
            self.geany_img.set_from_file('categories/gtk-no.png')
            self.geany.set_tooltip_text("Geany is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/glade"):
            self.glade_img.set_from_file('categories/gtk-yes.png')
            self.glade.set_tooltip_text("Glade is installed.\nClick to remove it.")
        else:
            self.glade_img.set_from_file('categories/gtk-no.png')
            self.glade.set_tooltip_text("Glade is not installed.\nClick to install it.")

        if os.path.exists("/etc/java-7-openjdk/"):
            self.openjdk_img.set_from_file('categories/gtk-yes.png')
            self.openjdk.set_tooltip_text("OpenJDK is installed.\nClick to remove it.")
        else:
            self.openjdk_img.set_from_file('categories/gtk-no.png')
            self.openjdk.set_tooltip_text("OpenJDK is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/meld"):
            self.meld_img.set_from_file('categories/gtk-yes.png')
            self.meld.set_tooltip_text("Meld is installed.\nClick to remove it.")
        else:
            self.meld_img.set_from_file('categories/gtk-no.png')
            self.meld.set_tooltip_text("Meld is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/netbeans"):
            self.netbeans_img.set_from_file('categories/gtk-yes.png')
            self.netbeans.set_tooltip_text("NetBeans is installed.\nClick to remove it.")
        else:
            self.netbeans_img.set_from_file('categories/gtk-no.png')
            self.netbeans.set_tooltip_text("NetBeans is not installed.\nClick to install it.")

        if os.path.isfile("/usr/lib/qt4/bin/designer"):
            self.qt4_img.set_from_file('categories/gtk-yes.png')
            self.qt4.set_tooltip_text("Qt4 is installed.\nClick to remove it.")
        else:
            self.qt4_img.set_from_file('categories/gtk-no.png')
            self.qt4.set_tooltip_text("Qt4 is not installed.\nClick to install it.")

        if os.path.isfile("/usr/lib/qt/bin/designer"):
            self.qt5_img.set_from_file('categories/gtk-yes.png')
            self.qt5.set_tooltip_text("Qt5 is installed.\nClick to remove it.")
        else:
            self.qt5_img.set_from_file('categories/gtk-no.png')
            self.qt5.set_tooltip_text("Qt5 is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/qtcreator"):
            self.qtcreator_img.set_from_file('categories/gtk-yes.png')
            self.qtcreator.set_tooltip_text("QtCreator is installed.\nClick to remove it.")
        else:
            self.qtcreator_img.set_from_file('categories/gtk-no.png')
            self.qtcreator.set_tooltip_text("QtCreator is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/ninja-ide"):
            self.ninja_ide_img.set_from_file('categories/gtk-yes.png')
            self.ninja_ide.set_tooltip_text("Ninja-IDE is installed.\nClick to remove it.")
        else:
            self.ninja_ide_img.set_from_file('categories/gtk-no.png')
            self.ninja_ide.set_tooltip_text("Ninja-IDE is not installed.\nClick to install it.")
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
        if os.path.isfile("/usr/bin/evince"):
            self.evince_img.set_from_file('categories/gtk-yes.png')
            self.evince.set_tooltip_text("Evince is installed.\nClick to remove it.")
        else:
            self.evince_img.set_from_file('categories/gtk-no.png')
            self.evince.set_tooltip_text("Evince is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/f-spot"):
            self.f_spot_img.set_from_file('categories/gtk-yes.png')
            self.f_spot.set_tooltip_text("F-spot is installed.\nClick to remove it.")
        else:
            self.f_spot_img.set_from_file('categories/gtk-no.png')
            self.f_spot.set_tooltip_text("F-spot is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/gimp"):
            self.gimp_img.set_from_file('categories/gtk-yes.png')
            self.gimp.set_tooltip_text("Gimp is installed.\nClick to remove it.")
        else:
            self.gimp_img.set_from_file('categories/gtk-no.png')
            self.gimp.set_tooltip_text("Gimp is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/gwenview"):
            self.gwenview_img.set_from_file('categories/gtk-yes.png')
            self.gwenview.set_tooltip_text("Gwenview is installed.\nClick to remove it.")
        else:
            self.gwenview_img.set_from_file('categories/gtk-no.png')
            self.gwenview.set_tooltip_text("Gwenview is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/convert"):
            self.imagemagick_img.set_from_file('categories/gtk-yes.png')
            self.imagemagick.set_tooltip_text("ImageMagick is installed.\nClick to remove it.")
        else:
            self.imagemagick_img.set_from_file('categories/gtk-no.png')
            self.imagemagick.set_tooltip_text("ImageMagick is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/inkscape"):
            self.inkscape_img.set_from_file('categories/gtk-yes.png')
            self.inkscape.set_tooltip_text("Inkscape is installed.\nClick to remove it.")
        else:
            self.inkscape_img.set_from_file('categories/gtk-no.png')
            self.inkscape.set_tooltip_text("Inkscape is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/mypaint"):
            self.mypaint_img.set_from_file('categories/gtk-yes.png')
            self.mypaint.set_tooltip_text("MyPaint is installed.\nClick to remove it.")
        else:
            self.mypaint_img.set_from_file('categories/gtk-no.png')
            self.mypaint.set_tooltip_text("MyPaint is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/pinta"):
            self.pinta_img.set_from_file('categories/gtk-yes.png')
            self.pinta.set_tooltip_text("Pinta is installed.\nClick to remove it.")
        else:
            self.pinta_img.set_from_file('categories/gtk-no.png')
            self.pinta.set_tooltip_text("Pinta is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/shotwell"):
            self.shotwell_img.set_from_file('categories/gtk-yes.png')
            self.shotwell.set_tooltip_text("Shotwell is installed.\nClick to remove it.")
        else:
            self.shotwell_img.set_from_file('categories/gtk-no.png')
            self.shotwell.set_tooltip_text("Shotwell is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/stellarium"):
            self.stellarium_img.set_from_file('categories/gtk-yes.png')
            self.stellarium.set_tooltip_text("Stellarium is installed.\nClick to remove it.")
        else:
            self.stellarium_img.set_from_file('categories/gtk-no.png')
            self.stellarium.set_tooltip_text("Stellarium is not installed.\nClick to install it.")
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
        if os.path.isfile("/usr/bin/chromium"):
            self.chromium_img.set_from_file('categories/gtk-yes.png')
            self.chromium.set_tooltip_text("Chromium is installed.\nClick to remove it.")
        else:
            self.chromium_img.set_from_file('categories/gtk-no.png')
            self.chromium.set_tooltip_text("Chromium is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/deluge"):
            self.deluge_img.set_from_file('categories/gtk-yes.png')
            self.deluge.set_tooltip_text("Deluge is not installed.\nClick to remove it.")
        else:
            self.deluge_img.set_from_file('categories/gtk-no.png')
            self.deluge.set_tooltip_text("Deluge is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/evolution"):
            self.evolution_img.set_from_file('categories/gtk-yes.png')
            self.evolution.set_tooltip_text("Evolution is installed.\nClick to remove it.")
        else:
            self.evolution_img.set_from_file('categories/gtk-no.png')
            self.evolution.set_tooltip_text("Evolution is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/filezilla"):
            self.filezilla_img.set_from_file('categories/gtk-yes.png')
            self.filezilla.set_tooltip_text("Filezilla is installed.\nClick to remove it.")
        else:
            self.filezilla_img.set_from_file('categories/gtk-no.png')
            self.filezilla.set_tooltip_text("Filezilla is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/firefox"):
            self.firefox_img.set_from_file('categories/gtk-yes.png')
            self.firefox.set_tooltip_text("Firefox is installed.\nClick to remove it.")
        else:
            self.firefox_img.set_from_file('categories/gtk-no.png')
            self.firefox.set_tooltip_text("Firefox is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/google-chrome-stable"):
            self.chrome_img.set_from_file('categories/gtk-yes.png')
            self.chrome.set_tooltip_text("Google Chrome is installed.\nClick to remove it.")
        else:
            self.chrome_img.set_from_file('categories/gtk-no.png')
            self.chrome.set_tooltip_text("Google Chrome is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/xchat"):
            self.xchat_img.set_from_file('categories/gtk-yes.png')
            self.xchat.set_tooltip_text("Xchat is installed.\nClick to remove it.")
        else:
            self.xchat_img.set_from_file('categories/gtk-no.png')
            self.xchat.set_tooltip_text("Xchat is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/liferea"):
            self.liferea_img.set_from_file('categories/gtk-yes.png')
            self.liferea.set_tooltip_text("Liferea is installed.\nClick to remove it.")
        else:
            self.liferea_img.set_from_file('categories/gtk-no.png')
            self.liferea.set_tooltip_text("Liferea is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/midori"):
            self.midori_img.set_from_file('categories/gtk-yes.png')
            self.midori.set_tooltip_text("Midori is installed.\nClick to remove it.")
        else:
            self.midori_img.set_from_file('categories/gtk-no.png')
            self.midori.set_tooltip_text("Midori is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/minitube"):
            self.minitube_img.set_from_file('categories/gtk-yes.png')
            self.minitube.set_tooltip_text("Minitube is installed.\nClick to remove it.")
        else:
            self.minitube_img.set_from_file('categories/gtk-no.png')
            self.minitube.set_tooltip_text("Minitube is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/opera"):
            self.opera_img.set_from_file('categories/gtk-yes.png')
            self.opera.set_tooltip_text("Opera is installed.\nClick to remove it.")
        else:
            self.opera_img.set_from_file('categories/gtk-no.png')
            self.opera.set_tooltip_text("Opera is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/pidgin"):
            self.pidgin_img.set_from_file('categories/gtk-yes.png')
            self.pidgin.set_tooltip_text("Pidgin is installed.\nClick to remove it.")
        else:
            self.pidgin_img.set_from_file('categories/gtk-no.png')
            self.pidgin.set_tooltip_text("Pidgin is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/skype"):
            self.skype_img.set_from_file('categories/gtk-yes.png')
            self.skyp.set_tooltip_text("Skype is installed.\nClick to remove it.")
        else:
            self.skype_img.set_from_file('categories/gtk-no.png')
            self.skyp.set_tooltip_text("Skype is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/steam"):
            self.steam_img.set_from_file('categories/gtk-yes.png')
            self.steam.set_tooltip_text("Steam is installed.\nClick to remove it.")
        else:
            self.steam_img.set_from_file('categories/gtk-no.png')
            self.steam.set_tooltip_text("Steam is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/thunderbird"):
            self.thunderbird_img.set_from_file('categories/gtk-yes.png')
            self.thunderbird.set_tooltip_text("Thunderbird is installed.\nClick to remove it.")
        else:
            self.thunderbird_img.set_from_file('categories/gtk-no.png')
            self.thunderbird.set_tooltip_text("Thunderbird is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/transmission-gtk"):
            self.transmission_img.set_from_file('categories/gtk-yes.png')
            self.transmission.set_tooltip_text("Transmission is installed.\nClick to remove it.")
        else:
            self.transmission_img.set_from_file('categories/gtk-no.png')
            self.transmission.set_tooltip_text("Transmission is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/linuxdcpp"):
            self.linuxdcpp_img.set_from_file('categories/gtk-yes.png')
            self.linuxdcpp.set_tooltip_text("Linuxdcpp is installed.\nClick to remove it.")
        else:
            self.linuxdcpp_img.set_from_file('categories/gtk-no.png')
            self.linuxdcpp.set_tooltip_text("Linuxdcpp is not installed.\nClick to install it.")
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
        if os.path.isfile("/usr/bin/amarok"):
            self.amarok_img.set_from_file('categories/gtk-yes.png')
            self.amarok.set_tooltip_text("Amarok is installed.\nClick to remove it.")
        else:
            self.amarok_img.set_from_file('categories/gtk-no.png')
            self.amarok.set_tooltip_text("Amarok is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/audacious"):
            self.audacious_img.set_from_file('categories/gtk-yes.png')
            self.audacious.set_tooltip_text("Audacious is installed.\nClick to remove it.")
        else:
            self.audacious_img.set_from_file('categories/gtk-no.png')
            self.audacious.set_tooltip_text("Audacious is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/banshee"):
            self.banshee_img.set_from_file('categories/gtk-yes.png')
            self.banshee.set_tooltip_text("Banshee is installed.\nClick to remove it.")
        else:
            self.banshee_img.set_from_file('categories/gtk-no.png')
            self.banshee.set_tooltip_text("Banshee is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/cheese"):
            self.cheese_img.set_from_file('categories/gtk-yes.png')
            self.cheese.set_tooltip_text("Cheese is installed.\nClick to remove it.")
        else:
            self.cheese_img.set_from_file('categories/gtk-no.png')
            self.cheese.set_tooltip_text("Cheese is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/clementine"):
            self.clementine_img.set_from_file('categories/gtk-yes.png')
            self.clementine.set_tooltip_text("Clementine is installed.\nClick to remove it.")
        else:
            self.clementine_img.set_from_file('categories/gtk-no.png')
            self.clementine.set_tooltip_text("Clementine is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/flash-player-properties"):
            self.flashplayer_img.set_from_file('categories/gtk-yes.png')
            self.flashplayer.set_tooltip_text("Flashplayer is installed.\nClick to remove it.")
        else:
            self.flashplayer_img.set_from_file('categories/gtk-no.png')
            self.flashplayer.set_tooltip_text("Flashplayer is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/gtk-recordMyDesktop"):
            self.recordmydesktop_img.set_from_file('categories/gtk-yes.png')
            self.recordmydesktop.set_tooltip_text("RecordMyDesktop is installed.\nClick to remove it.")
        else:
            self.recordmydesktop_img.set_from_file('categories/gtk-no.png')
            self.recordmydesktop.set_tooltip_text("RecordMyDesktop is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/guayadeque"):
            self.guayadeque_img.set_from_file('categories/gtk-yes.png')
            self.guayadeque.set_tooltip_text("Guayadeque is installed.\nClick to remove it.")
        else:
            self.guayadeque_img.set_from_file('categories/gtk-no.png')
            self.guayadeque.set_tooltip_text("Guayadeque is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/mplayer"):
            self.mplayer_img.set_from_file('categories/gtk-yes.png')
            self.mplayer.set_tooltip_text("Mplayer is installed.\nClick to remove it.")
        else:
            self.mplayer_img.set_from_file('categories/gtk-no.png')
            self.mplayer.set_tooltip_text("Mplayer is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/openshot"):
            self.openshot_img.set_from_file('categories/gtk-yes.png')
            self.openshot.set_tooltip_text("Openshot is installed.\nClick to remove it.")
        else:
            self.openshot_img.set_from_file('categories/gtk-no.png')
            self.openshot.set_tooltip_text("Openshot is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/pitivi"):
            self.pitivi_img.set_from_file('categories/gtk-yes.png')
            self.pitivi.set_tooltip_text("PiTiVi is installed.\nClick to install it.")
        else:
            self.pitivi_img.set_from_file('categories/gtk-no.png')
            self.pitivi.set_tooltip_text("PiTiVi is not installed.\nClick to remove it.")

        if os.path.isfile("/usr/bin/rhythmbox"):
            self.rhythmbox_img.set_from_file('categories/gtk-yes.png')
            self.rhythmbox.set_tooltip_text("Rhythmbox is installed.\nClick to remove it.")
        else:
            self.rhythmbox_img.set_from_file('categories/gtk-no.png')
            self.rhythmbox.set_tooltip_text("Rhythmbox is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/soundconverter"):
            self.soundconverter_img.set_from_file('categories/gtk-yes.png')
            self.soundconverter.set_tooltip_text("Soundconverter is installed.\nClick to remove it.")
        else:
            self.soundconverter_img.set_from_file('categories/gtk-no.png')
            self.soundconverter.set_tooltip_text("Soundconverter is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/totem"):
            self.totem_img.set_from_file('categories/gtk-yes.png')
            self.totem.set_tooltip_text("Totem is installed.\nClick to remove it.")
        else:
            self.totem_img.set_from_file('categories/gtk-no.png')
            self.totem.set_tooltip_text("Totem is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/vlc"):
            self.vlc_img.set_from_file('categories/gtk-yes.png')
            self.vlc.set_tooltip_text("Vlc is installed.\nClick to remove it.")
        else:
            self.vlc_img.set_from_file('categories/gtk-no.png')
            self.vlc.set_tooltip_text("Vlc is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/winff"):
            self.winff_img.set_from_file('categories/gtk-yes.png')
            self.winff.set_tooltip_text("Winff is installed.\nClick to remove it.")
        else:
            self.winff_img.set_from_file('categories/gtk-no.png')
            self.winff.set_tooltip_text("Winff is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/xfburn"):
            self.xfburn_img.set_from_file('categories/gtk-yes.png')
            self.xfburn.set_tooltip_text("Xfburn is installed.\nClick to remove it.")
        else:
            self.xfburn_img.set_from_file('categories/gtk-no.png')
            self.xfbrun.set_tooltip_text("Xfburn is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/kdenlive"):
            self.kdenlive_img.set_from_file('categories/gtk-yes.png')
            self.kdenlive.set_tooltip_text("Kdenlive is installed.\nClick to remove it.")
        else:
            self.kdenlive_img.set_from_file('categories/gtk-no.png')
            self.kdenlive.set_tooltip_text("Kdenlive is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/simplescreenrecorder"):
            self.simplescreenrecorder_img.set_from_file('categories/gtk-yes.png')
            self.simplescreenrecorder.set_tooltip_text("Simple screen recorder is installed.\nClick to remove it.")
        else:
            self.simplescreenrecorder_img.set_from_file('categories/gtk-no.png')
            self.simplescreenrecorder.set_tooltip_text("Simple screen recorder is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/vokoscreen"):
            self.vokoscreen_img.set_from_file('categories/gtk-yes.png')
            self.vokoscreen.set_tooltip_text("Vokoscreen is installed.\nClick to remove it.")
        else:
            self.vokoscreen_img.set_from_file('categories/gtk-no.png')
            self.vokoscreen.set_tooltip_text("Vokoscreen is not installed.\nClick to install it.")
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
        if os.path.isfile("/usr/bin/gparted"):
            self.gparted_img.set_from_file('categories/gtk-yes.png')
            self.gparted.set_tooltip_text("Gparted is installed.\nClick to remove it.")
        else:
            self.gparted_img.set_from_file('categories/gtk-no.png')
            self.gparted.set_tooltip_text("Gparted is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/guake"):
            self.guake_img.set_from_file('categories/gtk-yes.png')
            self.guake.set_tooltip_text("Guake is installed.\nClick to remove it.")
        else:
            self.guake_img.set_from_file('categories/gtk-no.png')
            self.guake.set_tooltip_text("Guake is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/hardinfo"):
            self.hardinfo_img.set_from_file('categories/gtk-yes.png')
            self.hardinfo.set_tooltip_text("Hardinfo is installed.\nClick to remove it.")
        else:
            self.hardinfo_img.set_from_file('categories/gtk-no.png')
            self.hardinfo.set_tooltip_text("Hardinfo is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/htop"):
            self.htop_img.set_from_file('categories/gtk-yes.png')
            self.htop.set_tooltip_text("Htop is installed.\nClick to remove it.")
        else:
            self.htop_img.set_from_file('categories/gtk-no.png')
            self.htop.set_tooltip_text("Htop is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/keepassx"):
            self.keepassx_img.set_from_file('categories/gtk-yes.png')
            self.keepassx.set_tooltip_text("Keepassx is installed.\nClick to remove it.")
        else:
            self.keepassx_img.set_from_file('categories/gtk-no.png')
            self.keepassx.set_tooltip_text("Keepassx is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/playonlinux"):
            self.playonlinux_img.set_from_file('categories/gtk-yes.png')
            self.playonlinux.set_tooltip_text("Playonlinux is installed.\nClick to remove it.")
        else:
            self.playonlinux_img.set_from_file('categories/gtk-no.png')
            self.playonlinux.set_tooltip_text("Playonlinux is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/terminator"):
            self.terminator_img.set_from_file('categories/gtk-yes.png')
            self.terminator.set_tooltip_text("Terminator is installed.\nClick to remove it.")
        else:
            self.terminator_img.set_from_file('categories/gtk-no.png')
            self.terminator.set_tooltip_text("Terminator is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/thunar"):
            self.thunar_img.set_from_file('categories/gtk-yes.png')
            self.thunar.set_tooltip_text("Thunar is installed.\nClick to remove it.")
        else:
            self.thunar_img.set_from_file('categories/gtk-no.png')
            self.thunar.set_tooltip_text("Thunar is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/truecrypt"):
            self.truecrypt_img.set_from_file('categories/gtk-yes.png')
            self.truecrypt.set_tooltip_text("Truecrypt is installed.\nClick to remove it.")
        else:
            self.truecrypt_img.set_from_file('categories/gtk-no.png')
            self.truecrypt.set_tooltip_text("Truecrypt is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/unetbootin"):
            self.unetbootin_img.set_from_file('categories/gtk-yes.png')
            self.unetbootin.set_tooltip_text("Unetbootin is installed.\nClick to remove it.")
        else:
            self.unetbootin_img.set_from_file('categories/gtk-no.png')
            self.unetbootin.set_tooltip_text("Unetbootin is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/virtualbox"):
            self.virtualbox_img.set_from_file('categories/gtk-yes.png')
            self.virtualbox.set_tooltip_text("Virtualbox is installed.\nClick to remove it.")
        else:
            self.virtualbox_img.set_from_file('categories/gtk-no.png')
            self.virtualbox.set_tooltip_text("Virtualbox is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/wine"):
            self.wine_img.set_from_file('categories/gtk-yes.png')
            self.wine.set_tooltip_text("Wine is installed.\nClick to remove it.")
        else:
            self.wine_img.set_from_file('categories/gtk-no.png')
            self.wine.set_tooltip_text("Wine is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/wireshark"):
            self.wireshark_img.set_from_file('categories/gtk-yes.png')
            self.wireshark.set_tooltip_text("Wireshark is installed.\nClick to remove it.")
        else:
            self.wireshark_img.set_from_file('categories/gtk-no.png')
            self.wireshark.set_tooltip_text("Wireshark is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/xbmc"):
            self.xbmc_img.set_from_file('categories/gtk-yes.png')
            self.xbmc.set_tooltip_text("XBMC is installed.\nClick to remove it.")
        else:
            self.xbmc_img.set_from_file('categories/gtk-no.png')
            self.xbmc.set_tooltip_text("XBMC is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/gufw"):
            self.gufw_img.set_from_file('categories/gtk-yes.png')
            self.gufw.set_tooltip_text("Gufw is installed.\nClick to remove it.")
        else:
            self.gufw_img.set_from_file('categories/gtk-no.png')
            self.gufw.set_tooltip_text("Gufw is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/octopi"):
            self.octopi_img.set_from_file('categories/gtk-yes.png')
            self.octopi.set_tooltip_text("Octopi is installed.\nClick to remove it.")
        else:
            self.octopi_img.set_from_file('categories/gtk-no.png')
            self.octopi.set_tooltip_text("Octopi is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/pamac-manager"):
            self.pamac_img.set_from_file('categories/gtk-yes.png')
            self.pamac.set_tooltip_text("Pamac is installed.\nClick to remove it.")
        else:
            self.pamac_img.set_from_file('categories/gtk-no.png')
            self.pamac.set_tooltip_text("Pamac is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin//usr/bin/gnome-system-monitor"):
            self.gnome_system_monitor_img.set_from_file('categories/gtk-yes.png')
            self.gnome_system_monitor.set_tooltip_text("Gnome system monitor is installed.\nClick to remove it.")
        else:
            self.gnome_system_monitor_img.set_from_file('categories/gtk-no.png')
            self.gnome_system_monitor.set_tooltip_text("Gnome system monitor is not installed.\nClick to install it.")
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
        if os.path.isfile("/usr/bin/docky"):
            self.docky_img.set_from_file('categories/gtk-yes.png')
            self.docky.set_tooltip_text("Docky is installed.\nClick to remove it.")
        else:
            self.docky_img.set_from_file('categories/gtk-no.png')
            self.docky.set_tooltip_text("Docky is not installed.\nClick to install it.")

        self.emacs_img = self.builder7.get_object("emacs_img")
        if os.path.isfile("/usr/bin/emacs"):
            self.emacs_img.set_from_file('categories/gtk-yes.png')
            self.emacs.set_tooltip_text("Emacs is installed.\nClick to remove it.")
        else:
            self.emacs_img.set_from_file('categories/gtk-no.png')
            self.emacs.set_tooltip_text("Emacs is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/vim"):
            self.vim_img.set_from_file('categories/gtk-yes.png')
            self.vim.set_tooltip_text("Vim is installed.\nClick to remove it.")
        else:
            self.vim_img.set_from_file('categories/gtk-no.png')
            self.vim.set_tooltip_text("Vim is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/galculator"):
            self.galculator_img.set_from_file('categories/gtk-yes.png')
            self.galculator.set_tooltip_text("Galculator is installed.\nClick to remove it.")
        else:
            self.galculator_img.set_from_file('categories/gtk-no.png')
            self.galculator.set_tooltip_text("Galculator is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/gedit"):
            self.gedit_img.set_from_file('categories/gtk-yes.png')
            self.gedit.set_tooltip_text("gedit is installed.\nClick to remove it.")
        else:
            self.gedit_img.set_from_file('categories/gtk-no.png')
            self.gedit.set_tooltip_text("gedit is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/gloobus-preview"):
            self.gloobus_img.set_from_file('categories/gtk-yes.png')
            self.gloobus.set_tooltip_text("Gloobus is installed.\nClick to remove it.")
        else:
            self.gloobus_img.set_from_file('categories/gtk-no.png')
            self.gloobus.set_tooltip_text("Gloobus is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/leafpad"):
            self.leafpad_img.set_from_file('categories/gtk-yes.png')
            self.leafpad.set_tooltip_text("Leafpad is installed.\nClick to remove it.")
        else:
            self.leafpad_img.set_from_file('categories/gtk-no.png')
            self.leafpad.set_tooltip_text("Leafpad is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/scribes"):
            self.scribes_img.set_from_file('categories/gtk-yes.png')
            self.scribes.set_tooltip_text("Scribes is installed.\nClick to remove it.")
        else:
            self.scribes_img.set_from_file('categories/gtk-no.png')
            self.scribes.set_tooltip_text("Scribes is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/tomboy"):
            self.tomboy_img.set_from_file('categories/gtk-yes.png')
            self.tomboy.set_tooltip_text("Tomboy is installed.\nClick to remove it.")
        else:
            self.tomboy_img.set_from_file('categories/gtk-no.png')
            self.tomboy.set_tooltip_text("Tomboy is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/tuxcards"):
            self.tuxcards_img.set_from_file('categories/gtk-yes.png')
            self.tuxcards.set_tooltip_text("Tuxcards is installed.\nClick to remove it.")
        else:
            self.tuxcards_img.set_from_file('categories/gtk-no.png')
            self.tuxcards.set_tooltip_text("Tuxcards is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/imagewriter"):
            self.imagewriter_img.set_from_file('categories/gtk-yes.png')
            self.imagewriter.set_tooltip_text("Imagewriter is installed.\nClick to remove it.")
        else:
            self.imagewriter_img.set_from_file('categories/gtk-no.png')
            self.imagewriter.set_tooltip_text("Imagewriter is not installed.\nClick to install it.")

        if os.path.isfile("/usr/bin/7zFM"):
            self.sevenzip_img.set_from_file('categories/gtk-yes.png')
            self.sevenzip.set_tooltip_text("7-zip is installed.\nClick to remove it.")
        else:
            self.sevenzip_img.set_from_file('categories/gtk-no.png')
            self.sevenzip.set_tooltip_text("7-zip is not installed.\nClick to install it.")
        self.vbox.add(self.grid_utilities)

    def on_button7_clicked(self, widget):
        aboutdialog = Gtk.AboutDialog()
        aboutdialog.set_program_name("Yo I\'m not pro")
        aboutdialog.set_logo(GdkPixbuf.Pixbuf.new_from_file("ui/yoimnotpro_icon.png"))
        aboutdialog.set_comments("Small app center\n")
        aboutdialog.set_website("http://linux.sytes.net/")
        aboutdialog.set_website_label("Developer Website")
        aboutdialog.set_authors(["Aaron Caffrey\nhttp://linux.sytes.net/", "\nSuggestions:\nexcalibur1234\nKorrode\ntetrahderon\nAyceman\nAJ1000", "\nComments:\nRichad\ndrumBE\nVerandert2.0\nLukimya\naaditya\nHardyH\ndcell\nrfkill 2.0"])
        aboutdialog.set_license('GPLv3 - http://www.gnu.org/licenses/gpl.html\nor read the COPYING file')
        aboutdialog.run()
        aboutdialog.destroy()

    def draw_transparency(self, widget, cr):
        cr.set_source_rgba(.1, .1, .1, 0.95)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('ui/main2.ui')

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

        # get the applications buttons images, once category or application button is selected or clicked it will check if those applications exist and will display appropriate sign
        self.anjuta_img = self.builder2.get_object("anjuta_img")
        self.blender_img = self.builder2.get_object("blender_img")
        self.bluefish_img = self.builder2.get_object("bluefish_img")
        self.eclipse_img = self.builder2.get_object("eclipse_img")
        self.geany_img = self.builder2.get_object("geany_img")
        self.glade_img = self.builder2.get_object("glade_img")
        self.openjdk_img = self.builder2.get_object("openjdk_img")
        self.meld_img = self.builder2.get_object("meld_img")
        self.netbeans_img = self.builder2.get_object("netbeans_img")
        self.qt4_img = self.builder2.get_object("qt4_img")
        self.qt5_img = self.builder2.get_object("qt5_img")
        self.qtcreator_img = self.builder2.get_object("qtcreator_img")
        self.ninja_ide_img = self.builder2.get_object("ninja_ide_img")
        self.evince_img = self.builder3.get_object("evince_img")
        self.f_spot_img = self.builder3.get_object("f_spot_img")
        self.gimp_img = self.builder3.get_object("gimp_img")
        self.gwenview_img = self.builder3.get_object("gwenview_img")
        self.imagemagick_img = self.builder3.get_object("imagemagick_img")
        self.inkscape_img = self.builder3.get_object("inkscape_img")
        self.mypaint_img = self.builder3.get_object("mypaint_img")
        self.pinta_img = self.builder3.get_object("pinta_img")
        self.shotwell_img = self.builder3.get_object("shotwell_img")
        self.stellarium_img = self.builder3.get_object("stellarium_img")
        self.chromium_img = self.builder4.get_object("chromium_img")
        self.deluge_img = self.builder4.get_object("deluge_img")
        self.evolution_img = self.builder4.get_object("evolution_img")
        self.filezilla_img = self.builder4.get_object("filezilla_img")
        self.firefox_img = self.builder4.get_object("firefox_img")
        self.chrome_img = self.builder4.get_object("chrome_img")
        self.xchat_img = self.builder4.get_object("xchat_img")
        self.liferea_img = self.builder4.get_object("liferea_img")
        self.midori_img = self.builder4.get_object("midori_img")
        self.minitube_img = self.builder4.get_object("minitube_img")
        self.opera_img = self.builder4.get_object("opera_img")
        self.pidgin_img = self.builder4.get_object("pidgin_img")
        self.skype_img = self.builder4.get_object("skype_img")
        self.steam_img = self.builder4.get_object("steam_img")
        self.thunderbird_img = self.builder4.get_object("thunderbird_img")
        self.transmission_img = self.builder4.get_object("transmission_img")
        self.linuxdcpp_img = self.builder4.get_object("linuxdcpp_img")
        self.amarok_img = self.builder5.get_object("amarok_img")
        self.audacious_img = self.builder5.get_object("audacious_img")
        self.banshee_img = self.builder5.get_object("banshee_img")
        self.cheese_img = self.builder5.get_object("cheese_img")
        self.clementine_img = self.builder5.get_object("clementine_img")
        self.flashplayer_img = self.builder5.get_object("flashplayer_img")
        self.recordmydesktop_img = self.builder5.get_object("recordmydesktop_img")
        self.guayadeque_img = self.builder5.get_object("guayadeque_img")
        self.mplayer_img = self.builder5.get_object("mplayer_img")
        self.openshot_img = self.builder5.get_object("openshot_img")
        self.pitivi_img = self.builder5.get_object("pitivi_img")
        self.rhythmbox_img = self.builder5.get_object("rhythmbox_img")
        self.soundconverter_img = self.builder5.get_object("soundconverter_img")
        self.totem_img = self.builder5.get_object("totem_img")
        self.vlc_img = self.builder5.get_object("vlc_img")
        self.winff_img = self.builder5.get_object("winff_img")
        self.xfburn_img = self.builder5.get_object("xfburn_img")
        self.kdenlive_img = self.builder5.get_object("kdenlive_img")
        self.simplescreenrecorder_img = self.builder5.get_object("simplescreenrecorder_img")
        self.vokoscreen_img = self.builder5.get_object("vokoscreen_img")
        self.gparted_img = self.builder6.get_object("gparted_img")
        self.guake_img = self.builder6.get_object("guake_img")
        self.hardinfo_img = self.builder6.get_object("hardinfo_img")
        self.htop_img = self.builder6.get_object("htop_img")
        self.keepassx_img = self.builder6.get_object("keepassx_img")
        self.playonlinux_img = self.builder6.get_object("playonlinux_img")
        self.terminator_img = self.builder6.get_object("terminator_img")
        self.thunar_img = self.builder6.get_object("thunar_img")
        self.truecrypt_img = self.builder6.get_object("truecrypt_img")
        self.unetbootin_img = self.builder6.get_object("unetbootin_img")
        self.virtualbox_img = self.builder6.get_object("virtualbox_img")
        self.wine_img = self.builder6.get_object("wine_img")
        self.wireshark_img = self.builder6.get_object("wireshark_img")
        self.xbmc_img = self.builder6.get_object("xbmc_img")
        self.gufw_img = self.builder6.get_object("gufw_img")
        self.octopi_img = self.builder6.get_object("octopi_img")
        self.pamac_img = self.builder6.get_object("pamac_img")
        self.gnome_system_monitor_img = self.builder6.get_object("gnome_system_monitor_img")
        self.docky_img = self.builder7.get_object("docky_img")
        self.vim_img = self.builder7.get_object("vim_img")
        self.galculator_img = self.builder7.get_object("galculator_img")
        self.gedit_img = self.builder7.get_object("gedit_img")
        self.gloobus_img = self.builder7.get_object("gloobus_img")
        self.leafpad_img = self.builder7.get_object("leafpad_img")
        self.scribes_img = self.builder7.get_object("scribes_img")
        self.tomboy_img = self.builder7.get_object("tomboy_img")
        self.tuxcards_img = self.builder7.get_object("tuxcards_img")
        self.imagewriter_img = self.builder7.get_object("imagewriter_img")
        self.sevenzip_img = self.builder7.get_object("sevenzip_img")

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
        # add tooltip for each application icon
        self.geany_icon_tooltip_ = self.builder8.get_object("geany_icon_tooltip_")
        self.geany_icon_tooltip_.set_tooltip_text("Geany is a small and lightweight integrated development environment.")
        self.blender_icon_tooltip_ = self.builder8.get_object("blender_icon_tooltip_")
        self.blender_icon_tooltip_.set_tooltip_text("Blender is the open source, cross platform suite of tools for 3D creation.")
        self.ninja_ide_icon_tooltip_ = self.builder8.get_object("ninja_ide_icon_tooltip_")
        self.ninja_ide_icon_tooltip_.set_tooltip_text("Ninja-IDE is a cross-platform integrated development environment designed to build Python applications.")
        self.glade_icon_tooltip_ = self.builder8.get_object("glade_icon_tooltip_")
        self.glade_icon_tooltip_.set_tooltip_text("Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment.")
        self.audacious_icon_tooltip_ = self.builder8.get_object("audacious_icon_tooltip_")
        self.audacious_icon_tooltip_.set_tooltip_text("Audio player with support for many formats, and it has support for third-party plugins.")
        self.gimp_icon_tooltip_ = self.builder8.get_object("gimp_icon_tooltip_")
        self.gimp_icon_tooltip_.set_tooltip_text("GIMP is an image retouching and editing tool, similar to Photoshop.")
        self.evince_icon_tooltip_ = self.builder8.get_object("evince_icon_tooltip_")
        self.evince_icon_tooltip_.set_tooltip_text("Evince is a document viewer for multiple document formats.")
        self.xfburn_icon_tooltip_ = self.builder8.get_object("xfburn_icon_tooltip_")
        self.xfburn_icon_tooltip_.set_tooltip_text("Xfburn is a simple CD/DVD burning tool")
        self.flashplayer_icon_tooltip_ = self.builder8.get_object("flashplayer_icon_tooltip_")
        self.flashplayer_icon_tooltip_.set_tooltip_text("Cross-platform plugin plays animations, videos and sound files.")
        self.openshot_icon_tooltip_ = self.builder8.get_object("openshot_icon_tooltip_")
        self.openshot_icon_tooltip_.set_tooltip_text("A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style")
        self.chromium_icon_tooltip_ = self.builder8.get_object("chromium_icon_tooltip_")
        self.chromium_icon_tooltip_.set_tooltip_text("Chromium is the open source web browser project from which Google Chrome draws its source code.")
        self.deluge_icon_tooltip_ = self.builder8.get_object("deluge_icon_tooltip_")
        self.deluge_icon_tooltip_.set_tooltip_text("Open source, cross-platform BitTorrent client.")
        self.liferea_icon_tooltip_ = self.builder8.get_object("liferea_icon_tooltip_")
        self.liferea_icon_tooltip_.set_tooltip_text("Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds.")
        self.htop_icon_tooltip_ = self.builder8.get_object("htop_icon_tooltip_")
        self.htop_icon_tooltip_.set_tooltip_text("Htop is an interactive system-monitor process-viewer.")
        self.skype_icon_tooltip_ = self.builder8.get_object("skype_icon_tooltip_")
        self.skype_icon_tooltip_.set_tooltip_text("Skype is a freemium voice-over-IP service and instant messaging client")
        self.wireshark_icon_tooltip_ = self.builder8.get_object("wireshark_icon_tooltip_")
        self.wireshark_icon_tooltip_.set_tooltip_text("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development.")
        self.virtualbox_icon_tooltip_ = self.builder8.get_object("virtualbox_icon_tooltip_")
        self.virtualbox_icon_tooltip_.set_tooltip_text("VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC.")
        self.steam_icon_tooltip_ = self.builder8.get_object("steam_icon_tooltip_")
        self.steam_icon_tooltip_.set_tooltip_text("Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses.")
        self.xchat_icon_tooltip_ = self.builder8.get_object("xchat_icon_tooltip_")
        self.xchat_icon_tooltip_.set_tooltip_text("XChat is a popular Internet Relay Chat (IRC) client.")
        self.gedit_icon_tooltip_ = self.builder8.get_object("gedit_icon_tooltip_")
        self.gedit_icon_tooltip_.set_tooltip_text("gedit is lightweight text editor.")
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
            self.geany_.set_tooltip_text("Geany is installed.\nClick to remove it.")
        else:
            self.geany__img.set_from_file('categories/gtk-no.png')
            self.geany_.set_tooltip_text("Geany is not installed.\nClick to install it.")

        self.blender__img = self.builder8.get_object("blender_img_")
        if os.path.isfile("/usr/bin/blender"):
            self.blender__img.set_from_file('categories/gtk-yes.png')
            self.blender_.set_tooltip_text("Blender is installed.\nClick to remove it.")
        else:
            self.blender__img.set_from_file('categories/gtk-no.png')
            self.blender_.set_tooltip_text("Blender is not installed.\nClick to install it.")

        self.ninja_ide__img = self.builder8.get_object("ninja_ide_img_")
        if os.path.isfile("/usr/bin/ninja-ide"):
            self.ninja_ide__img.set_from_file('categories/gtk-yes.png')
            self.ninja_ide_.set_tooltip_text("Ninja-IDE is installed.\nClick to remove it.")
        else:
            self.ninja_ide__img.set_from_file('categories/gtk-no.png')
            self.ninja_ide_.set_tooltip_text("Ninja-IDE is not installed.\nClick to install it.")

        self.glade__img = self.builder8.get_object("glade_img_")
        if os.path.isfile("/usr/bin/glade"):
            self.glade__img.set_from_file('categories/gtk-yes.png')
            self.glade_.set_tooltip_text("Glade is installed.\nClick to remove it.")
        else:
            self.glade__img.set_from_file('categories/gtk-no.png')
            self.glade_.set_tooltip_text("Glade is not installed.\nClick to install it.")

        self.audacious__img = self.builder8.get_object("audacious_img_")
        if os.path.isfile("/usr/bin/audacious"):
            self.audacious__img.set_from_file('categories/gtk-yes.png')
            self.audacious_.set_tooltip_text("Audacious is installed.\nClick to remove it.")
        else:
            self.audacious__img.set_from_file('categories/gtk-no.png')
            self.audacious_.set_tooltip_text("Audacious is not installed.\nClick to install it.")

        self.gimp__img = self.builder8.get_object("gimp_img_")
        if os.path.isfile("/usr/bin/gimp"):
            self.gimp__img.set_from_file('categories/gtk-yes.png')
            self.gimp_.set_tooltip_text("Gimp is installed.\nClick to remove it.")
        else:
            self.gimp__img.set_from_file('categories/gtk-no.png')
            self.gimp_.set_tooltip_text("Gimp is not installed.\nClick to install it.")

        self.evince__img = self.builder8.get_object("evince_img_")
        if os.path.isfile("/usr/bin/evince"):
            self.evince__img.set_from_file('categories/gtk-yes.png')
            self.evince_.set_tooltip_text("Evince is installed.\nClick to remove it.")
        else:
            self.evince__img.set_from_file('categories/gtk-no.png')
            self.evince_.set_tooltip_text("Evince is not installed.\nClick to install it.")

        self.xfburn__img = self.builder8.get_object("xfburn_img_")
        if os.path.isfile("/usr/bin/xfburn"):
            self.xfburn__img.set_from_file('categories/gtk-yes.png')
            self.xfburn_.set_tooltip_text("Xfburn is installed.\nClick to remove it.")
        else:
            self.xfburn__img.set_from_file('categories/gtk-no.png')
            self.xfburn_.set_tooltip_text("Xfburn is installed.\nClick to install it.")

        self.flashplayer__img = self.builder8.get_object("flashplayer_img_")
        if os.path.isfile("/usr/bin/flash-player-properties"):
            self.flashplayer__img.set_from_file('categories/gtk-yes.png')
            self.flashplayer_.set_tooltip_text("Flashplayer is installed.\nClick to remove it.")
        else:
            self.flashplayer__img.set_from_file('categories/gtk-no.png')
            self.flashplayer_.set_tooltip_text("Flashplayer is not installed.\nClick to install it.")

        self.openshot__img = self.builder8.get_object("openshot_img_")
        if os.path.isfile("/usr/bin/openshot"):
            self.openshot__img.set_from_file('categories/gtk-yes.png')
            self.openshot_.set_tooltip_text("Openshot is installed.\nClick to remove it.")
        else:
            self.openshot__img.set_from_file('categories/gtk-no.png')
            self.openshot_.set_tooltip_text("Openshot is not installed.\nClick to install it.")

        self.chromium__img = self.builder8.get_object("chromium_img_")
        if os.path.isfile("/usr/bin/chromium"):
            self.chromium__img.set_from_file('categories/gtk-yes.png')
            self.chromium_.set_tooltip_text("Chromium is installed.\nClick to remove it.")
        else:
            self.chromium__img.set_from_file('categories/gtk-no.png')
            self.chromium_.set_tooltip_text("Chromium is not installed.\nClick to install it.")

        self.deluge__img = self.builder8.get_object("deluge_img_")
        if os.path.isfile("/usr/bin/deluge"):
            self.deluge__img.set_from_file('categories/gtk-yes.png')
            self.deluge_.set_tooltip_text("Deluge is installed.\nClick to remove it.")
        else:
            self.deluge__img.set_from_file('categories/gtk-no.png')
            self.deluge_.set_tooltip_text("Deluge is notinstalled.\nClick to insall it.")

        self.liferea__img = self.builder8.get_object("liferea_img_")
        if os.path.isfile("/usr/bin/liferea"):
            self.liferea__img.set_from_file('categories/gtk-yes.png')
            self.liferea_.set_tooltip_text("Liferea is installed.\nClick to remove it.")
        else:
            self.liferea__img.set_from_file('categories/gtk-no.png')
            self.liferea_.set_tooltip_text("Liferea is not installed.\nClick to install it.")

        self.htop__img = self.builder8.get_object("htop_img_")
        if os.path.isfile("/usr/bin/htop"):
            self.htop__img.set_from_file('categories/gtk-yes.png')
            self.htop_.set_tooltip_text("Htop is installed.\nClick to remove it.")
        else:
            self.htop__img.set_from_file('categories/gtk-no.png')
            self.htop_.set_tooltip_text("Htop is not installed.\nClick to install it.")

        self.skype__img = self.builder8.get_object("skype_img_")
        if os.path.isfile("/usr/bin/skype"):
            self.skype__img.set_from_file('categories/gtk-yes.png')
            self.skype_.set_tooltip_text("Skype is installed.\nClick to remove it.")
        else:
            self.skype__img.set_from_file('categories/gtk-no.png')
            self.skype_.set_tooltip_text("Skype is not installed.\nClick to install it.")

        self.wireshark__img = self.builder8.get_object("wireshark_img_")
        if os.path.isfile("/usr/bin/wireshark"):
            self.wireshark__img.set_from_file('categories/gtk-yes.png')
            self.wireshark_.set_tooltip_text("Wireshark is installed.\nClick to remove it.")
        else:
            self.wireshark__img.set_from_file('categories/gtk-no.png')
            self.wireshark_.set_tooltip_text("Wireshark is not installed.\nClick to install it.")

        self.virtualbox__img = self.builder8.get_object("virtualbox_img_")
        if os.path.isfile("/usr/bin/virtualbox"):
            self.virtualbox__img.set_from_file('categories/gtk-yes.png')
            self.virtualbox_.set_tooltip_text("Virtualbox is installed.\nClick to remove it.")
        else:
            self.virtualbox__img.set_from_file('categories/gtk-no.png')
            self.virtualbox_.set_tooltip_text("Virtualbox is not installed.\nClick to install it.")

        self.steam__img = self.builder8.get_object("steam_img_")
        if os.path.isfile("/usr/bin/steam"):
            self.steam__img.set_from_file('categories/gtk-yes.png')
            self.steam_.set_tooltip_text("Steam is installed.\nClick to remove it.")
        else:
            self.steam__img.set_from_file('categories/gtk-no.png')
            self.steam_.set_tooltip_text("Steam is not installed.\nClick to insall it.")

        self.xchat__img = self.builder8.get_object("xchat_img_")
        if os.path.isfile("/usr/bin/xchat"):
            self.xchat__img.set_from_file('categories/gtk-yes.png')
            self.xchat_.set_tooltip_text("Xchat is installed.\nClick to remove it.")
        else:
            self.xchat__img.set_from_file('categories/gtk-no.png')
            self.xchat_.set_tooltip_text("Xchat is not installed.\nClick to install it.")

        self.gedit__img = self.builder8.get_object("gedit_img_")
        if os.path.isfile("/usr/bin/gedit"):
            self.gedit__img.set_from_file('categories/gtk-yes.png')
            self.gedit_.set_tooltip_text("Gedit is installed.\nClick to remove it.")
        else:
            self.gedit__img.set_from_file('categories/gtk-no.png')
            self.gedit_.set_tooltip_text("Gedit is not installed.\nClick to install it.")

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
        self.imagewriter = self.builder7.get_object("imagewriter")
        self.sevenzip = self.builder7.get_object("sevenzip")
        # add tooltip for each application icon
        self.docky_icon_tooltip = self.builder7.get_object("docky_icon_tooltip")
        self.docky_icon_tooltip.set_tooltip_text("Docky is an advanced shortcut bar that sits at the edges of your screen.")
        self.emacs_icon_tooltip = self.builder7.get_object("emacs_icon_tooltip")
        self.emacs_icon_tooltip.set_tooltip_text("Emacs is a text editor.")
        self.vim_icon_tooltip = self.builder7.get_object("vim_icon_tooltip")
        self.vim_icon_tooltip.set_tooltip_text("Vim is a text editor")
        self.galculator_icon_tooltip = self.builder7.get_object("galculator_icon_tooltip")
        self.galculator_icon_tooltip.set_tooltip_text("galculator is an open source scientific calculator with a modern GUI.")
        self.gedit_icon_tooltip = self.builder7.get_object("gedit_icon_tooltip")
        self.gedit_icon_tooltip.set_tooltip_text("gedit is lightweight text editor.")
        self.gloobus_icon_tooltip = self.builder7.get_object("gloobus_icon_tooltip")
        self.gloobus_icon_tooltip.set_tooltip_text(" Gloobus Preview is a program designed to preview the contents of a file or folder on Linux OS")
        self.leafpad_icon_tooltip = self.builder7.get_object("leafpad_icon_tooltip")
        self.leafpad_icon_tooltip.set_tooltip_text("Leafpad is a text editor")
        self.scribes_icon_tooltip = self.builder7.get_object("scribes_icon_tooltip")
        self.scribes_icon_tooltip.set_tooltip_text("Simple, slim and sleek, yet powerful text editor.")
        self.tomboy_icon_tooltip = self.builder7.get_object("tomboy_icon_tooltip")
        self.tomboy_icon_tooltip.set_tooltip_text("Tomboy is a desktop note-taking application")
        self.tuxcards_icon_tooltip = self.builder7.get_object("tuxcards_icon_tooltip")
        self.tuxcards_icon_tooltip.set_tooltip_text("TuxCards is a hierarical notebook.")
        self.imagewriter_icon_tooltip = self.builder7.get_object("imagewriter_icon_tooltip")
        self.imagewriter_icon_tooltip.set_tooltip_text("This tool is used for writing images to USB sticks.")
        self.sevenzip_icon_tooltip = self.builder7.get_object("sevenzip_icon_tooltip")
        self.sevenzip_icon_tooltip.set_tooltip_text("7-Zip is an open source file archiver")
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
        self.imagewriter.connect("clicked", self.on_imagewriter_clicked)
        self.sevenzip.connect("clicked", self.on_sevenzip_clicked)

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
        self.gufw = self.builder6.get_object("gufw")
        self.octopi = self.builder6.get_object("octopi")
        self.pamac = self.builder6.get_object("pamac")
        self.gnome_system_monitor = self.builder6.get_object("gnome_system_monitor")
        # add tooltip for each application icon
        self.gparted_icon_tooltip = self.builder6.get_object("gparted_icon_tooltip")
        self.gparted_icon_tooltip.set_tooltip_text("GParted is a free partition editor for graphically managing your disk partitions. ")
        self.guake_icon_tooltip = self.builder6.get_object("guake_icon_tooltip")
        self.guake_icon_tooltip.set_tooltip_text("Guake is a drop-down terminal.")
        self.hardinfo_icon_tooltip = self.builder6.get_object("hardinfo_icon_tooltip")
        self.hardinfo_icon_tooltip.set_tooltip_text("Hardinfo provides comprehensive details of your PC's software and hardware and allows you to benchmark its performance.")
        self.htop_icon_tooltip = self.builder6.get_object("htop_icon_tooltip")
        self.htop_icon_tooltip.set_tooltip_text("Htop is an interactive process viewer.")
        self.keepassx_icon_tooltip = self.builder6.get_object("keepassx_icon_tooltip")
        self.keepassx_icon_tooltip.set_tooltip_text("KeePassX is an application for people with extremly high demands on secure personal data management.")
        self.playonlinux_icon_tooltip = self.builder6.get_object("playonlinux_icon_tooltip")
        self.playonlinux_icon_tooltip.set_tooltip_text("PlayOnLinux will allow you to play your favorite games on Linux easily.")
        self.terminator_icon_tooltip = self.builder6.get_object("terminator_icon_tooltip")
        self.terminator_icon_tooltip.set_tooltip_text(" Terminator is a cross-platform GPL terminal emulator with advanced features not yet found elsewhere.")
        self.thunar_icon_tooltip = self.builder6.get_object("thunar_icon_tooltip")
        self.thunar_icon_tooltip.set_tooltip_text("Thunar is a file manager.")
        self.truecrypt_icon_tooltip = self.builder6.get_object("truecrypt_icon_tooltip")
        self.truecrypt_icon_tooltip.set_tooltip_text("TrueCrypt is free open-source disk encryption software.")
        self.unetbootin_icon_tooltip = self.builder6.get_object("unetbootin_icon_tooltip")
        self.unetbootin_icon_tooltip.set_tooltip_text("UNetbootin allows you to create bootable Live USB drives for GNU/Linux distributions without burning a CD")
        self.virtualbox_icon_tooltip = self.builder6.get_object("virtualbox_icon_tooltip")
        self.virtualbox_icon_tooltip.set_tooltip_text("VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC.")
        self.wine_icon_tooltip = self.builder6.get_object("wine_icon_tooltip")
        self.wine_icon_tooltip.set_tooltip_text("Wine is a compatibility layer for running windows applications on GNU/Linux.")
        self.wireshark_icon_tooltip = self.builder6.get_object("wireshark_icon_tooltip")
        self.wireshark_icon_tooltip.set_tooltip_text("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development.")
        self.xbmc_icon_tooltip = self.builder6.get_object("xbmc_icon_tooltip")
        self.xbmc_icon_tooltip.set_tooltip_text("XBMC Media Center is a free cross-platform media player software and entertainment system application framework.")
        self.gufw_icon_tooltip = self.builder6.get_object("gufw_icon_tooltip")
        self.gufw_icon_tooltip.set_tooltip_text("One of the easiest firewalls in the world!")
        self.octopi_icon_tooltip = self.builder6.get_object("octopi_icon_tooltip")
        self.octopi_icon_tooltip.set_tooltip_text("Octopi is a powerful tool to manage (Arch | Manjaro) Linux packages.")
        self.pamac_icon_tooltip = self.builder6.get_object("pamac_icon_tooltip")
        self.pamac_icon_tooltip.set_tooltip_text("pamac - simple graphical package manager for Manjaro Linux.")
        self.gnome_system_monitor_icon_tooltip = self.builder6.get_object("gnome_system_monitor_icon_tooltip")
        self.gnome_system_monitor_icon_tooltip.set_tooltip_text("Gnome System Monitor is a GNOME process viewer and system monitor with a nice easy-to-use interface")
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
        self.gufw.connect("clicked", self.on_gufw_clicked)
        self.octopi.connect("clicked", self.on_octopi_clicked)
        self.pamac.connect("clicked", self.on_pamac_clicked)
        self.gnome_system_monitor.connect("clicked", self.on_gnome_system_monitor_clicked)

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
        self.winff.set_tooltip_text("WinFF is a video converter.")
        self.xfburn = self.builder5.get_object("xfburn")
        self.kdenlive = self.builder5.get_object("kdenlive")
        self.simplescreenrecorder = self.builder5.get_object("simplescreenrecorder")
        self.vokoscreen = self.builder5.get_object("vokoscreen")
        # add tooltip for each application icon
        self.amarok_icon_tooltip = self.builder5.get_object("amarok_icon_tooltip")
        self.amarok_icon_tooltip.set_tooltip_text("Amarok is a cross-platform free and open source music player.")
        self.audacious_icon_tooltip = self.builder5.get_object("audacious_icon_tooltip")
        self.audacious_icon_tooltip.set_tooltip_text("Audacious is a free and open source audio player.")
        self.banshee_icon_tooltip = self.builder5.get_object("banshee_icon_tooltip")
        self.banshee_icon_tooltip.set_tooltip_text("Banshee is a cross-platform open-source media player.")
        self.cheese_icon_tooltip = self.builder5.get_object("cheese_icon_tooltip")
        self.cheese_icon_tooltip.set_tooltip_text("Cheese uses your webcam to take photos and videos, applies fancy special effects, and lets you share the fun with others.")
        self.clementine_icon_tooltip = self.builder5.get_object("clementine_icon_tooltip")
        self.clementine_icon_tooltip.set_tooltip_text("Clementine is a cross-platform free and open source music player and library organizer. ")
        self.flashplayer_icon_tooltip = self.builder5.get_object("flashplayer_icon_tooltip")
        self.flashplayer_icon_tooltip.set_tooltip_text("Cross-platform plugin plays animations, videos and sound files.")
        self.recordmydesktop_icon_tooltip = self.builder5.get_object("recordmydesktop_icon_tooltip")
        self.recordmydesktop_icon_tooltip.set_tooltip_text("recordMyDesktop is a desktop session recorder.")
        self.guayadeque_icon_tooltip = self.builder5.get_object("guayadeque_icon_tooltip")
        self.guayadeque_icon_tooltip.set_tooltip_text("Guayadeque is a music management program designed for all music enthusiasts.")
        self.mplayer_icon_tooltip = self.builder5.get_object("mplayer_icon_tooltip")
        self.mplayer_icon_tooltip.set_tooltip_text("MPlayer is a free software and open source media player.")
        self.openshot_icon_tooltip = self.builder5.get_object("openshot_icon_tooltip")
        self.openshot_icon_tooltip.set_tooltip_text("A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style.")
        self.pitivi_icon_tooltip = self.builder5.get_object("pitivi_icon_tooltip")
        self.pitivi_icon_tooltip.set_tooltip_text("Pitivi is an open source, non-linear video editor.")
        self.rhythmbox_icon_tooltip = self.builder5.get_object("rhythmbox_icon_tooltip")
        self.rhythmbox_icon_tooltip.set_tooltip_text("Rhythmbox is an integrated music management application, originally inspired by Apple's iTunes.")
        self.soundconverter_icon_tooltip = self.builder5.get_object("soundconverter_icon_tooltip")
        self.soundconverter_icon_tooltip.set_tooltip_text("SoundConverter is the leading audio file converter.")
        self.totem_icon_tooltip = self.builder5.get_object("totem_icon_tooltip")
        self.totem_icon_tooltip.set_tooltip_text("Totem is a media player.")
        self.vlc_icon_tooltip = self.builder5.get_object("vlc_icon_tooltip")
        self.vlc_icon_tooltip.set_tooltip_text("VLC is a multimedia player for various audio and video formats.")
        self.winff_icon_tooltip = self.builder5.get_object("winff_icon_tooltip")
        self.winff_icon_tooltip.set_tooltip_text("WinFF is a video converter.")
        self.xfburn_icon_tooltip = self.builder5.get_object("xfburn_icon_tooltip")
        self.xfburn_icon_tooltip.set_tooltip_text("Xfburn is a simple CD/DVD burning tool.")
        self.kdenlive_icon_tooltip = self.builder5.get_object("kdenlive_icon_tooltip")
        self.kdenlive_icon_tooltip.set_tooltip_text("Kdenlive (KDE Non-Linear Video Editor) is an open source video editing software")
        self.simplescreenrecorder_icon_tooltip = self.builder5.get_object("simplescreenrecorder_icon_tooltip")
        self.simplescreenrecorder_icon_tooltip.set_tooltip_text("SimpleScreenRecorder is capable of recording video from full-screen and window-size captures of Opengl applications(and games).")
        self.vokoscreen_icon_tooltip = self.builder5.get_object("vokoscreen_icon_tooltip")
        self.vokoscreen_icon_tooltip.set_tooltip_text("Vokoscreen is an easy to use screencast creator to record educational videos, live recordings of browser, installation, videoconferences, etc.")
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
        self.kdenlive.connect("clicked", self.on_kdenlive_clicked)
        self.simplescreenrecorder.connect("clicked", self.on_simplescreenrecorder_clicked)
        self.vokoscreen.connect("clicked", self.on_vokoscreen_clicked)


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
        self.linuxdcpp = self.builder4.get_object("linuxdcpp")
        # add tooltip for each application icon
        self.chromium_icon_tooltip = self.builder4.get_object("chromium_icon_tooltip")
        self.chromium_icon_tooltip.set_tooltip_text("Chromium is the open source web browser project from which Google Chrome draws its source code.")
        self.deluge_icon_tooltip = self.builder4.get_object("deluge_icon_tooltip")
        self.deluge_icon_tooltip.set_tooltip_text("Open source, cross-platform BitTorrent client.")
        self.evolution_icon_tooltip = self.builder4.get_object("evolution_icon_tooltip")
        self.evolution_icon_tooltip.set_tooltip_text("Evolution is a fully featured open source powerful, flexible and generally great email client.")
        self.filezilla_icon_tooltip = self.builder4.get_object("filezilla_icon_tooltip")
        self.filezilla_icon_tooltip.set_tooltip_text("Open-source FTP client.")
        self.firefox_icon_tooltip = self.builder4.get_object("firefox_icon_tooltip")
        self.firefox_icon_tooltip.set_tooltip_text("Firefox is a free and open-source web browser")
        self.chrome_icon_tooltip = self.builder4.get_object("chrome_icon_tooltip")
        self.chrome_icon_tooltip.set_tooltip_text("Google Chrome is a browser that combines a minimal design with sophisticated technology to make the web faster, safer and easier.")
        self.xchat_icon_tooltip = self.builder4.get_object("xchat_icon_tooltip")
        self.xchat_icon_tooltip.set_tooltip_text("XChat is a popular Internet Relay Chat (IRC) client.")
        self.liferea_icon_tooltip = self.builder4.get_object("liferea_icon_tooltip")
        self.liferea_icon_tooltip.set_tooltip_text("Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds.")
        self.midori_icon_tooltip = self.builder4.get_object("midori_icon_tooltip")
        self.midori_icon_tooltip.set_tooltip_text("Midori is a lightweight Webkit-based web browser.")
        self.minitube_icon_tooltip = self.builder4.get_object("minitube_icon_tooltip")
        self.minitube_icon_tooltip.set_tooltip_text("Minitube is a native YouTube client. With it you can watch YouTube videos in a new way.")
        self.opera_icon_tooltip = self.builder4.get_object("opera_icon_tooltip")
        self.opera_icon_tooltip.set_tooltip_text("Opera is a web browser.")
        self.pidgin_icon_tooltip = self.builder4.get_object("pidgin_icon_tooltip")
        self.pidgin_icon_tooltip.set_tooltip_text("Pidgin is universal chat client.")
        self.skype_icon_tooltip = self.builder4.get_object("skype_icon_tooltip")
        self.skype_icon_tooltip.set_tooltip_text("Skype is a freemium voice-over-IP service and instant messaging client.")
        self.steam_icon_tooltip = self.builder4.get_object("steam_icon_tooltip")
        self.steam_icon_tooltip.set_tooltip_text("Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses.")
        self.thunderbird_icon_tooltip = self.builder4.get_object("thunderbird_icon_tooltip")
        self.thunderbird_icon_tooltip.set_tooltip_text("Thunderbird is an email program.")
        self.transmission_icon_tooltip = self.builder4.get_object("transmission_icon_tooltip")
        self.transmission_icon_tooltip.set_tooltip_text("Transmission is a BitTorrent client.")
        self.linuxdcpp_icon_tooltip = self.builder4.get_object("linuxdcpp_icon_tooltip")
        self.linuxdcpp_icon_tooltip.set_tooltip_text("A port of DC++ to GNU/Linux")
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
        self.linuxdcpp.connect("clicked", self.on_linuxdcpp_clicked)

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
        # add tooltip for each application icon
        self.evince_icon_tooltip = self.builder3.get_object("evince_icon_tooltip")
        self.evince_icon_tooltip.set_tooltip_text("Evince is a document viewer for multiple document formats.")
        self.f_spot_icon_tooltip = self.builder3.get_object("f_spot_icon_tooltip")
        self.f_spot_icon_tooltip.set_tooltip_text("F-Spot is a full-featured personal photo management application.")
        self.gimp_icon_tooltip = self.builder3.get_object("gimp_icon_tooltip")
        self.gimp_icon_tooltip.set_tooltip_text("GIMP is an image retouching and editing tool, similar to Photoshop.")
        self.gwenview_icon_tooltip = self.builder3.get_object("gwenview_icon_tooltip")
        self.gwenview_icon_tooltip.set_tooltip_text("Gwenview is an image viewer.")
        self.imagemagick_icon_tooltip = self.builder3.get_object("imagemagick_icon_tooltip")
        self.imagemagick_icon_tooltip.set_tooltip_text("Use ImageMagick to convert, edit, or compose bitmap images in a variety of formats.")
        self.inkscape_icon_tooltip = self.builder3.get_object("inkscape_icon_tooltip")
        self.inkscape_icon_tooltip.set_tooltip_text("Inkscape is an open source vector graphics editor.")
        self.mypaint_icon_tooltip = self.builder3.get_object("mypaint_icon_tooltip")
        self.mypaint_icon_tooltip.set_tooltip_text("MyPaint is a fast and easy open-source graphics application for digital painters.")
        self.pinta_icon_tooltip = self.builder3.get_object("pinta_icon_tooltip")
        self.pinta_icon_tooltip.set_tooltip_text("Pinta is an open-source, cross-platform bitmap image drawing and editing program inspired by Paint.NET")
        self.shotwell_icon_tooltip = self.builder3.get_object("shotwell_icon_tooltip")
        self.shotwell_icon_tooltip.set_tooltip_text("Shotwell is an image organizer.")
        self.stellarium_icon_tooltip = self.builder3.get_object("stellarium_icon_tooltip")
        self.stellarium_icon_tooltip.set_tooltip_text("Stellarium is a planetarium software that shows exactly what you see when you look up at the stars.")
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
        # add tooltip for each application icon
        self.anjuta_icon_tooltip = self.builder2.get_object("anjuta_icon_tooltip")
        self.anjuta_icon_tooltip.set_tooltip_text("Anjuta is an integrated development environment.")
        self.blender_icon_tooltip = self.builder2.get_object("blender_icon_tooltip")
        self.blender_icon_tooltip.set_tooltip_text("Blender is a free and open-source 3D computer graphics software product used for creating animated films, \nvisual effects, art, 3D printed models and so on.")
        self.bluefish_icon_tooltip = self.builder2.get_object("bluefish_icon_tooltip")
        self.bluefish_icon_tooltip.set_tooltip_text("Bluefish is a free and open source advanced text editor with a variety of tools for programming in general\nand the development of dynamic websites")
        self.eclipse_icon_tooltip = self.builder2.get_object("eclipse_icon_tooltip")
        self.eclipse_icon_tooltip.set_tooltip_text("Eclipse is IDE.")
        self.geany_icon_tooltip = self.builder2.get_object("geany_icon_tooltip")
        self.geany_icon_tooltip.set_tooltip_text("Geany is a small and lightweight integrated development environment.")
        self.glade_icon_tooltip = self.builder2.get_object("glade_icon_tooltip")
        self.glade_icon_tooltip.set_tooltip_text("Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment.")
        self.openjdk_icon_tooltip = self.builder2.get_object("openjdk_icon_tooltip")
        self.openjdk_icon_tooltip.set_tooltip_text("OpenJDK (Open Java Development Kit) is a free and open source implementation of the Java Platform, Standard Edition (Java SE).")
        self.meld_icon_tooltip = self.builder2.get_object("meld_icon_tooltip")
        self.meld_icon_tooltip.set_tooltip_text("Meld is a visual diff and merge tool targeted at developers.")
        self.netbeans_icon_tooltip = self.builder2.get_object("netbeans_icon_tooltip")
        self.netbeans_icon_tooltip.set_tooltip_text("Fully-featured Java IDE written completely in Java, with many modules available.")
        self.qt4_icon_tooltip = self.builder2.get_object("qt4_icon_tooltip")
        self.qt4_icon_tooltip.set_tooltip_text("Qt4 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface.")
        self.qt5_icon_tooltip = self.builder2.get_object("qt5_icon_tooltip")
        self.qt5_icon_tooltip.set_tooltip_text("Qt5 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface.")
        self.qtcreator_icon_tooltip = self.builder2.get_object("qtcreator_icon_tooltip")
        self.qtcreator_icon_tooltip.set_tooltip_text("Qt Creator is a cross-platform C++ IDE")
        self.ninja_ide_icon_tooltip = self.builder2.get_object("ninja_ide_icon_tooltip")
        self.ninja_ide_icon_tooltip.set_tooltip_text("Ninja-IDE is a cross-platform integrated development environment designed to build Python applications.")
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

        # get the categories images, will be used once you click on some the categories to change those images with active or inactive
        self.image1 = self.builder.get_object("image1")
        self.image2 = self.builder.get_object("image2")
        self.image3 = self.builder.get_object("image3")
        self.image4 = self.builder.get_object("image4")
        self.image5 = self.builder.get_object("image5")
        self.image6 = self.builder.get_object("image6")

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