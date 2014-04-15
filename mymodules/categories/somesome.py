import os
from mymodules.buttons_images import Img
from mymodules.action.dial import SetToolTip, action, CurrentCategoryDict

class Inherit(object):
    def __init__(self, dicti):
        self.dicti = dicti
    def init_set_file_n_tooltip(*args):
        for val in args[1].values():
            set_file_n_tooltip(val[0], val[1], val[2], val[3])

class set_file_n_tooltip(object):
    def __init__(self, *args):
        no = action.gtk_no
        yes = action.gtk_yes
        if (os.path.isfile(args[0]) if not args[0]
            == "/usr/share/licenses/jre7-openjdk/" else
            os.path.exists(args[0])):
            args[1].set_from_file(yes)
            args[2].set_tooltip_markup(format(SetToolTip(args[3],
                action.installed, action.remove_it)))
        else:
            args[1].set_from_file(no)
            args[2].set_tooltip_markup(format(SetToolTip(args[3],
                action.not_here, action.install_it)))

class menu7(Inherit):
    pass
    @staticmethod
    def load():
        from mymodules.categories.menu7_button import Menu7
        men7 = menu7({
        "gedit": ("/usr/bin/gedit", Img.gedit__img, Menu7.gedit_, "Gedit"),
        "blender": ("/usr/bin/blender", Img.blender__img, Menu7.blender_, "Blender"),
        "geany": ("/usr/bin/geany", Img.geany__img, Menu7.geany_, "Geany"),
        "glade": ("/usr/bin/glade", Img.glade__img, Menu7.glade_, 'Glade'),
        "ninja-ide": ("/usr/bin/ninja-ide", Img.ninja_ide__img, Menu7.ninja_ide_, 'Ninja-IDE'),
        "evince": ("/usr/bin/evince", Img.evince__img, Menu7.evince_, 'Evince'),
        "gimp": ("/usr/bin/gimp", Img.gimp__img, Menu7.gimp_, 'GIMP'),
        "chromium": ("/usr/bin/chromium", Img.chromium__img, Menu7.chromium_, 'Chromium'),
        "deluge": ("/usr/bin/deluge", Img.deluge__img, Menu7.deluge_, 'Deluge'),
        "xchat": ("/usr/bin/xchat", Img.xchat__img, Menu7.xchat_, 'Xchat'),
        "liferea": ("/usr/bin/liferea", Img.liferea__img, Menu7.liferea_, 'Liferea'),
        "skype": ("/usr/bin/skype", Img.skype__img, Menu7.skype_, 'Skype'),
        "steam": ("/usr/bin/steam", Img.steam__img, Menu7.steam_, 'Steam'),
        "audacious": ("/usr/bin/audacious", Img.audacious__img, Menu7.audacious_, 'Audacious'),
        "openshot": ("/usr/bin/openshot", Img.openshot__img, Menu7.openshot_, 'Openshot'),
        "flashplugin": ("/usr/bin/flash-player-properties", Img.flashplayer__img,
            Menu7.flashplayer_, 'Adobe Flashplayer'),
        "xfburn": ("/usr/bin/xfburn", Img.xfburn__img, Menu7.xfburn_, 'Xfburn'),
        "htop": ("/usr/bin/htop", Img.htop__img, Menu7.htop_, 'Htop'),
        "virtualbox": ("/usr/bin/virtualbox", Img.virtualbox__img, Menu7.virtualbox_, 'Virtualbox'),
        "wireshark-gtk": ("/usr/bin/wireshark", Img.wireshark__img, Menu7.wireshark_, 'Wireshark')})
        attr = getattr(men7, 'dicti')
        men7.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu6(Inherit):
    pass
    @staticmethod
    def load():
        from mymodules.categories.menu6_button import Menu6
        men6 = menu6({
        "docky": ("/usr/bin/docky", Img.docky_img, Menu6.docky, "Docky"),
        "emacs": ("/usr/bin/emacs", Img.emacs_img, Menu6.emacs, "Emacs"),
        "vim": ("/usr/bin/vim", Img.vim_img, Menu6.vim, "Vim"),
        "galculator": ("/usr/bin/galculator", Img.galculator_img, Menu6.galculator, "Galculator"),
        "gedit": ("/usr/bin/gedit", Img.gedit_img, Menu6.gedit, "Gedit"),
        "gloobus-preview": ("/usr/bin/gloobus-preview",Img.gloobus_img, Menu6.gloobus, "Gloobus"),
        "leafpad": ("/usr/bin/leafpad", Img.leafpad_img, Menu6.leafpad, "Leafpad"),
        "scribes": ("/usr/bin/scribes", Img.scribes_img, Menu6.scribes, "Scribes"),
        "tomboy": ("/usr/bin/tomboy", Img.tomboy_img, Menu6.tomboy, "Tomboy"),
        "tuxcards": ("/usr/bin/tuxcards", Img.tuxcards_img, Menu6.tuxcards, "Tuxcards"),
        "imagewriter": ("/usr/bin/imagewriter", Img.imagewriter_img, Menu6.imagewriter, "Imagewriter"),
        "p7zip": ("/usr/bin/7zFM", Img.sevenzip_img, Menu6.sevenzip, "7zip")})
        attr = getattr(men6, 'dicti')
        men6.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu5(Inherit):
    pass
    @staticmethod
    def load():
        from mymodules.categories.menu5_button import Menu5
        men5 = menu5({
        "gparted": ("/usr/bin/gparted", Img.gparted_img, Menu5.gparted, 'Gparted'),
        "guake": ("/usr/bin/guake", Img.guake_img, Menu5.guake, 'Guake'),
        "hardinfo": ("/usr/bin/hardinfo", Img.hardinfo_img, Menu5.hardinfo, 'Hardinfo'),
        "htop": ("/usr/bin/htop", Img.htop_img, Menu5.htop, 'Htop'),
        "keepassx": ("/usr/bin/keepassx", Img.keepassx_img, Menu5.keepassx, 'KeepassX'),
        "playonlinux": ("/usr/bin/playonlinux", Img.playonlinux_img, Menu5.playonlinux, 'PlayOnLinux'),
        "terminator": ("/usr/bin/terminator", Img.terminator_img, Menu5.terminator, 'Terminator'),
        "thunar": ("/usr/bin/thunar", Img.thunar_img, Menu5.thunar, 'Thunar'),
        "truecrypt": ("/usr/bin/truecrypt", Img.truecrypt_img, Menu5.truecrypt, 'Truecrypt'),
        "unetbootin": ("/usr/bin/unetbootin", Img.unetbootin_img, Menu5.unetbootin, 'Unetbootin'),
        "virtualbox": ("/usr/bin/virtualbox", Img.virtualbox_img, Menu5.virtualbox, 'Virtualbox'),
        "wine": ("/usr/bin/wine", Img.wine_img, Menu5.wine, 'Wine'),
        "wireshark-gtk": ("/usr/bin/wireshark", Img.wireshark_img, Menu5.wireshark, 'Wireshark'),
        "xbmc": ("/usr/bin/xbmc", Img.xbmc_img, Menu5.xbmc, 'XBMC'),
        "gufw": ("/usr/bin/gufw", Img.gufw_img, Menu5.gufw, 'Gufw'),
        "octopi": ("/usr/bin/octopi", Img.octopi_img, Menu5.octopi, 'Octopi'),
        "pamac": ("/usr/bin/pamac-manager", Img.pamac_img, Menu5.pamac, 'Pamac'),
        "gnome-system-monitor": ("/usr/bin//usr/bin/gnome-system-monitor", Img.gnome_system_monitor_img, 
            Menu5.gnome_system_monitor, 'Gnome System Monitor')})
        attr = getattr(men5, 'dicti')
        men5.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu4(Inherit):
    pass
    @staticmethod
    def load():
        from mymodules.categories.menu4_button import Menu4
        men4 = menu4({
        "amarok": ("/usr/bin/amarok", Img.amarok_img, Menu4.amarok, 'Amarok'),
        "audacious": ("/usr/bin/audacious", Img.audacious_img, Menu4.audacious, 'Audacious'),
        "banshee": ("/usr/bin/banshee", Img.banshee_img, Menu4.banshee, 'Banshee'),
        "cheese": ("/usr/bin/cheese", Img.cheese_img, Menu4.cheese, 'Cheese'),
        "clementine": ("/usr/bin/clementine", Img.clementine_img, Menu4.clementine, 'Clementine'),
        "flashplugin": ("/usr/bin/flash-player-properties", Img.flashplayer_img, Menu4.flashplayer, 'Adobe Flashplayer'),
        "gtk-recordmydesktop": ("/usr/bin/gtk-recordMyDesktop", Img.recordmydesktop_img, Menu4.recordmydesktop, 'RecordMyDesktop'),
        "guayadeque": ("/usr/bin/guayadeque", Img.guayadeque_img, Menu4.guayadeque, 'Guayadeque'),
        "mplayer": ("/usr/bin/mplayer", Img.mplayer_img, Menu4.mplayer, 'Mplayer'),
        "openshot": ("/usr/bin/openshot", Img.openshot_img, Menu4.openshot, 'Openshot'),
        "pitivi": ("/usr/bin/pitivi", Img.pitivi_img, Menu4.pitivi, 'PiTiVi'),
        "rhythmbox": ("/usr/bin/rhythmbox", Img.rhythmbox_img, Menu4.rhythmbox, 'Rhythmbox'),
        "soundconverter": ("/usr/bin/soundconverter", Img.soundconverter_img, Menu4.soundconverter, 'SoundConverter'),
        "totem": ("/usr/bin/totem", Img.totem_img, Menu4.totem, 'Totem'),
        "vlc": ("/usr/bin/vlc", Img.vlc_img, Menu4.vlc, 'VLC'),
        "winff": ("/usr/bin/winff", Img.winff_img, Menu4.winff, 'Winff'),
        "xfburn": ("/usr/bin/xfburn", Img.xfburn_img, Menu4.xfburn, 'Xfburn'),
        "kdenlive": ("/usr/bin/kdenlive", Img.kdenlive_img, Menu4.kdenlive, 'Kdenlive'),
        "simplescreenrecorder": ("/usr/bin/simplescreenrecorder", Img.simplescreenrecorder_img, 
            Menu4.simplescreenrecorder, 'Simple Screen Recorder'),
        "vokoscreen": ("/usr/bin/vokoscreen", Img.vokoscreen_img, Menu4.vokoscreen, 'Vokoscreen')})
        attr = getattr(men4, 'dicti')
        men4.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu3(Inherit):
    pass
    @staticmethod
    def load():
        from mymodules.categories.menu3_button import Menu3
        men3 = menu3({
        "chromium": ("/usr/bin/chromium", Img.chromium_img, Menu3.chromium, 'Chromium'),
        "deluge": ("/usr/bin/deluge", Img.deluge_img, Menu3.deluge, 'Deluge'),
        "evolution": ("/usr/bin/evolution", Img.evolution_img, Menu3.evolution, 'Evolution'),
        "filezilla": ("/usr/bin/filezilla", Img.filezilla_img, Menu3.filezilla, 'Filezilla'),
        "firefox": ("/usr/bin/firefox", Img.firefox_img, Menu3.firefox, 'Firefox'),
        "google-chrome": ("/usr/bin/google-chrome-stable", Img.chrome_img, Menu3.chrome, 'Google Chrome'),
        "xchat": ("/usr/bin/xchat", Img.xchat_img, Menu3.xchat, 'Xchat'),
        "liferea": ("/usr/bin/liferea", Img.liferea_img, Menu3.liferea, 'Liferea'),
        "midori": ("/usr/bin/midori", Img.midori_img, Menu3.midori, 'Midori'),
        "minitube": ("/usr/bin/minitube", Img.minitube_img, Menu3.minitube, 'MiniTube'),
        "opera": ("/usr/bin/opera", Img.opera_img, Menu3.opera, 'Opera'),
        "pidgin": ("/usr/bin/pidgin", Img.pidgin_img, Menu3.pidgin, 'Pidgin'),
        "skype": ("/usr/bin/skype", Img.skype_img, Menu3.skyp, 'Skype'),
        "steam": ("/usr/bin/steam", Img.steam_img,  Menu3.steam, 'Steam'),
        "thunderbird": ("/usr/bin/thunderbird", Img.thunderbird_img, Menu3.thunderbird, 'ThunderBird'),
        "transmission-gtk": ("/usr/bin/transmission-gtk", Img.transmission_img, Menu3.transmission, 'Transmission'),
        "linuxdcpp": ("/usr/bin/linuxdcpp", Img.linuxdcpp_img, Menu3.linuxdcpp, 'Linuxdcpp')})
        attr = getattr(men3, 'dicti')
        men3.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu2(Inherit):
    pass
    @staticmethod
    def load():
        from mymodules.categories.menu2_button import Menu2
        men2 = menu2({
        "evince": ("/usr/bin/evince", Img.evince_img, Menu2.evince, 'Evince'),
        "f-spot": ("/usr/bin/f-spot", Img.f_spot_img, Menu2.f_spot, 'F-spot'),
        "gimp": ("/usr/bin/gimp", Img.gimp_img, Menu2.gimp, 'GIMP'),
        "gwenview": ("/usr/bin/gwenview", Img.gwenview_img, Menu2.gwenview, 'Gwenview'),
        "inkscape": ("/usr/bin/inkscape", Img.inkscape_img, Menu2.inkscape, 'Inkscape'),
        "mypaint": ("/usr/bin/mypaint", Img.mypaint_img, Menu2.mypaint, 'MyPaint'),
        "pinta": ("/usr/bin/pinta", Img.pinta_img, Menu2.pinta, 'Pinta'),
        "shotwell": ("/usr/bin/shotwell", Img.shotwell_img, Menu2.shotwell, 'Shotwell'),
        "stellarium": ("/usr/bin/stellarium", Img.stellarium_img, Menu2.stellarium, 'Stellarium'),
        "imagemagick": ("/usr/bin/convert", Img.imagemagick_img, Menu2.imagemagick,"ImageMagick")})
        attr = getattr(men2, 'dicti')
        men2.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu1(Inherit):
    pass
    @staticmethod
    def load():
        from mymodules.categories.menu1_button import Menu1
        men1 = menu1({
        "anjuta": ("/usr/bin/anjuta", Img.anjuta_img, Menu1.anjuta, 'Anjuta'),
        "blender": ("/usr/bin/blender", Img.blender_img, Menu1.blender, "Blender"),
        "bluefish": ("/usr/bin/bluefish", Img.bluefish_img, Menu1.bluefish, 'Bluefish'),
        "eclipse": ("/usr/bin/eclipse", Img.eclipse_img, Menu1.eclipse, 'Eclipse'),
        "geany": ("/usr/bin/geany", Img.geany_img, Menu1.geany, "Geany"),
        "glade": ("/usr/bin/glade", Img.glade_img, Menu1.glade, 'Glade'),
        "meld": ("/usr/bin/meld", Img.meld_img, Menu1.meld, 'Meld'),
        "netbeans": ("/usr/bin/netbeans", Img.netbeans_img, Menu1.netbeans, 'NetBeans'),
        "qt4": ("/usr/lib/qt4/bin/designer", Img.qt4_img, Menu1.qt4, 'Qt4'),
        "qt5-base": ("/usr/lib/qt/bin/designer", Img.qt5_img, Menu1.qt5, 'Qt5'),
        "qtcreator": ("/usr/bin/qtcreator", Img.qtcreator_img, Menu1.qtcreator, 'QtCreator'),
        "ninja-ide": ("/usr/bin/ninja-ide", Img.ninja_ide_img, Menu1.ninja_ide, 'Ninja-IDE'),
        "openjdk": ("/usr/share/licenses/jre7-openjdk/", Img.openjdk_img, Menu1.openjdk, "OpenJDK")})
        attr = getattr(men1, 'dicti')
        men1.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)