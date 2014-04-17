import os
from copy import deepcopy
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.install_remove import StartKickingSomeNinjas
from mymodules.action.dial import SetToolTip, action, CurrentCategoryDict

class Inherit(object):
    def __init__(self, dicti):
        self.dicti = dicti
        self.first_run = str()
    def init_set_file_n_tooltip(*args):
        for val in args[1].values():
            if (os.path.isfile(val[0]) if not val[0]
                == "/usr/share/licenses/jre7-openjdk/" else
                os.path.exists(val[0])):
                val[1].set_from_file(action.gtk_yes)
                val[2].set_tooltip_markup(format(SetToolTip(val[3],
                    action.installed, action.remove_it)))
            else:
                val[1].set_from_file(action.gtk_no)
                val[2].set_tooltip_markup(format(SetToolTip(val[3],
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
    first_run = str()
    @staticmethod
    def load():
        from mymodules.categories.menu6_button import Menu6
        local_dict = {
        "docky": ("/usr/bin/docky", "Docky", "Docky is an advanced shortcut bar that sits at the edges of your screen."),
        "emacs": ("/usr/bin/emacs", "Emacs", "Emacs is a text editor."),
        "vim": ("/usr/bin/vim", "Vim", "Vim is a text editor"),
        "galculator": ("/usr/bin/galculator", "Galculator", "Galculator is an open source scientific calculator with a modern GUI."),
        "gedit": ("/usr/bin/gedit", "Gedit", "Gedit is lightweight text editor."),
        "gloobus-preview": ("/usr/bin/gloobus-preview", "Gloobus", 'gloobus', "Gloobus Preview is a program designed to preview the contents of a file or folder on Linux OS"),
        "leafpad": ("/usr/bin/leafpad", "Leafpad", "Leafpad is a text editor"),
        "scribes": ("/usr/bin/scribes", "Scribes", "Simple, slim and sleek, yet powerful text editor."),
        "tomboy": ("/usr/bin/tomboy", "Tomboy", "Tomboy is a desktop note-taking application"),
        "tuxcards": ("/usr/bin/tuxcards", "Tuxcards", "TuxCards is a hierarical notebook."),
        "imagewriter": ("/usr/bin/imagewriter", "Imagewriter", "This tool is used for writing images to USB sticks."),
        "p7zip": ("/usr/bin/7zFM", "7zip", 'sevenzip', "7-Zip is an open source file archiver")}
        deep_copy = deepcopy(local_dict)
        for key, value in local_dict.items():
            key2 = (key if not len(value) > 3 else value[2])
            setattr(Menu6, key2, Builder.builder7.get_object(key2))          # install_remove_button
            setattr(Img, '{}_img'.format(key2),
                Builder.builder7.get_object('{}_img'.format(key2)))          # install_remove_button image
            setattr(Menu6, '{}_icon_tooltip'.format(key2),
                Builder.builder7.get_object('{}_icon_tooltip'.format(key2))) # faenza icon

                            #exe_file or path, Img.program_name, Menu6.program_name, program_name.capitalize()
            deep_copy[key] = (value[0], getattr(Img, '{}_img'.format(key2)), getattr(Menu6, key2), value[1])
            getattr(Menu6, '{}_icon_tooltip'.format(key2)).set_tooltip_text(
            (value[2] if not len(value) > 3 else value[3]))                  # faenza icon tooltip text

        if not menu6.first_run:
            for key, value in local_dict.items():
                key2 = (key if not len(value) > 3 else value[2])
                getattr(Menu6, key2).connect('clicked', StartKickingSomeNinjas, key)
            menu6.first_run = 'not first run'
        men6 = menu6(deep_copy)
        attr = getattr(men6, 'dicti')
        men6.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu5(Inherit):
    first_run = str()
    @staticmethod
    def load():
        from mymodules.categories.menu5_button import Menu5
        local_dict = {
        "gparted": ("/usr/bin/gparted", 'Gparted', "GParted is a free partition editor for graphically managing your disk partitions. "),
        "guake": ("/usr/bin/guake", 'Guake', "Guake is a drop-down terminal."),
        "hardinfo": ("/usr/bin/hardinfo", 'Hardinfo', "Hardinfo provides comprehensive details of your PC's software and hardware and allows you to benchmark its performance."),
        "htop": ("/usr/bin/htop", 'Htop', "Htop is an interactive process viewer."),
        "keepassx": ("/usr/bin/keepassx", 'KeepassX', "KeePassX is an application for people with extremly high demands on secure personal data management."),
        "playonlinux": ("/usr/bin/playonlinux", 'PlayOnLinux', "PlayOnLinux will allow you to play your favorite games on Linux easily."),
        "terminator": ("/usr/bin/terminator", 'Terminator', "Terminator is a cross-platform GPL terminal emulator with advanced features not yet found elsewhere."),
        "thunar": ("/usr/bin/thunar", 'Thunar', "Thunar is a file manager."),
        "truecrypt": ("/usr/bin/truecrypt", 'Truecrypt', "TrueCrypt is free open-source disk encryption software."),
        "unetbootin": ("/usr/bin/unetbootin", 'Unetbootin', "UNetbootin allows you to create bootable Live USB drives for GNU/Linux distributions without burning a CD"),
        "virtualbox": ("/usr/bin/virtualbox", 'Virtualbox', "VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC."),
        "wine": ("/usr/bin/wine", 'Wine', "Wine is a compatibility layer for running windows applications on GNU/Linux."),
        "wireshark-gtk": ("/usr/bin/wireshark", 'Wireshark', 'wireshark', "Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development."),
        "xbmc": ("/usr/bin/xbmc", 'XBMC', "XBMC Media Center is a free cross-platform media player software and entertainment system application framework."),
        "gufw": ("/usr/bin/gufw", 'Gufw', "One of the easiest firewalls in the world!"),
        "octopi": ("/usr/bin/octopi", 'Octopi', "Octopi is a powerful tool to manage (Arch | Manjaro) Linux packages."),
        "pamac": ("/usr/bin/pamac-manager", 'Pamac', "Pamac - simple graphical package manager for Manjaro Linux."),
        "gnome-system-monitor": ("/usr/bin/gnome-system-monitor", 
            'Gnome System Monitor', 'gnome_system_monitor', "Gnome System Monitor is a GNOME process viewer and system monitor with a nice easy-to-use interface")}
        deep_copy = deepcopy(local_dict)
        for key, value in local_dict.items():
            key2 = (key if not len(value) > 3 else value[2])
            setattr(Menu5, key2, Builder.builder6.get_object(key2))          # install_remove_button
            setattr(Img, '{}_img'.format(key2),
                Builder.builder6.get_object('{}_img'.format(key2)))          # install_remove_button image
            setattr(Menu5, '{}_icon_tooltip'.format(key2),
                Builder.builder6.get_object('{}_icon_tooltip'.format(key2))) # faenza icon

                            #exe_file or path, Img.program_name, Menu5.program_name, program_name.capitalize()
            deep_copy[key] = (value[0], getattr(Img, '{}_img'.format(key2)), getattr(Menu5, key2), value[1])
            getattr(Menu5, '{}_icon_tooltip'.format(key2)).set_tooltip_text(
            (value[2] if not len(value) > 3 else value[3]))                  # faenza icon tooltip text

        if not menu5.first_run:
            for key, value in local_dict.items():
                key2 = (key if not len(value) > 3 else value[2])
                getattr(Menu5, key2).connect('clicked', StartKickingSomeNinjas, key)
            menu5.first_run = 'not first run'

        men5 = menu5(deep_copy)
        attr = getattr(men5, 'dicti')
        men5.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu4(Inherit):
    first_run = str()
    @staticmethod
    def load():
        from mymodules.categories.menu4_button import Menu4
        local_dict = {
        "amarok": ("/usr/bin/amarok", 'Amarok', "Amarok is a cross-platform free and open source music player."),
        "audacious": ("/usr/bin/audacious", 'Audacious', 'Audacious is a free and open source audio player.'),
        "banshee": ("/usr/bin/banshee", 'Banshee', 'Banshee is a cross-platform open-source media player.'),
        "cheese": ("/usr/bin/cheese", 'Cheese', 'Cheese uses your webcam to take photos and videos, applies fancy special effects, and lets you share the fun with others.'),
        "clementine": ("/usr/bin/clementine", 'Clementine', 'Clementine is a cross-platform free and open source music player and library organizer.'),
        "flashplugin": ("/usr/bin/flash-player-properties", 'Adobe Flashplayer', 'flashplayer', 'Cross-platform plugin plays animations, videos and sound files.'),
        "gtk-recordmydesktop": ("/usr/bin/gtk-recordMyDesktop", 'RecordMyDesktop', 'recordmydesktop', 'RecordMyDesktop is a desktop session recorder.'),
        "guayadeque": ("/usr/bin/guayadeque", 'Guayadeque', 'Guayadeque is a music management program designed for all music enthusiasts.'),
        "mplayer": ("/usr/bin/mplayer", 'Mplayer', 'Mplayer is a free software and open source media player.'),
        "openshot": ("/usr/bin/openshot", 'Openshot', 'A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style.'),
        "pitivi": ("/usr/bin/pitivi", 'PiTiVi', 'Pitivi is an open source, non-linear video editor.'),
        "rhythmbox": ("/usr/bin/rhythmbox", 'Rhythmbox', 'Rhythmbox is an integrated music management application, originally inspired by Apple\'s iTunes.'),
        "soundconverter": ("/usr/bin/soundconverter", 'SoundConverter', 'SoundConverter is the leading audio file converter.'),
        "totem": ("/usr/bin/totem", 'Totem', 'Totem is a media player.'),
        "vlc": ("/usr/bin/vlc", 'VLC', 'VLC is a multimedia player for various audio and video formats.'),
        "winff": ("/usr/bin/winff", 'Winff', 'WinFF is a video converter.'),
        "xfburn": ("/usr/bin/xfburn", 'Xfburn', 'Xfburn is a simple CD/DVD burning tool.'),
        "kdenlive": ("/usr/bin/kdenlive", 'Kdenlive', 'Kdenlive (KDE Non-Linear Video Editor) is an open source video editing software'),
        "simplescreenrecorder": ("/usr/bin/simplescreenrecorder", 'Simple Screen Recorder', 'SimpleScreenRecorder is capable of recording video from full-screen and window-size captures of Opengl applications(and games).'),
        "vokoscreen": ("/usr/bin/vokoscreen", 'Vokoscreen', 'Vokoscreen is an easy to use screencast creator to record educational videos, live recordings of browser, installation, videoconferences, etc.')}
        deep_copy = deepcopy(local_dict)
        for key, value in local_dict.items():
            key2 = (key if not len(value) > 3 else value[2])
            setattr(Menu4, key2, Builder.builder5.get_object(key2))          # install_remove_button
            setattr(Img, '{}_img'.format(key2),
                Builder.builder5.get_object('{}_img'.format(key2)))          # install_remove_button image
            setattr(Menu4, '{}_icon_tooltip'.format(key2),
                Builder.builder5.get_object('{}_icon_tooltip'.format(key2))) # faenza icon

                            #exe_file or path, Img.program_name, Menu4.program_name, program_name.capitalize()
            deep_copy[key] = (value[0], getattr(Img, '{}_img'.format(key2)), getattr(Menu4, key2), value[1])
            getattr(Menu4, '{}_icon_tooltip'.format(key2)).set_tooltip_text(
            (value[2] if not len(value) > 3 else value[3]))                  # faenza icon tooltip text

        if not menu4.first_run:
            for key, value in local_dict.items():
                key2 = (key if not len(value) > 3 else value[2])
                getattr(Menu4, key2).connect('clicked', StartKickingSomeNinjas, key)
            menu4.first_run = 'not first run'

        men4 = menu4(deep_copy)
        attr = getattr(men4, 'dicti')
        men4.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu3(Inherit):
    first_run = str()
    @staticmethod
    def load():
        from mymodules.categories.menu3_button import Menu3
        local_dict = {
        "chromium": ("/usr/bin/chromium", 'Chromium', "Chromium is the open source web browser project from which Google Chrome draws its source code."),
        "deluge": ("/usr/bin/deluge", 'Deluge', "Open source, cross-platform BitTorrent client."),
        "evolution": ("/usr/bin/evolution", 'Evolution', "Evolution is a fully featured open source powerful, flexible and generally great email client."),
        "filezilla": ("/usr/bin/filezilla", 'Filezilla', "Open-source FTP client."),
        "firefox": ("/usr/bin/firefox", 'Firefox', "Firefox is a free and open-source web browser"),
        "google-chrome": ("/usr/bin/google-chrome-stable", 'Google Chrome', 'chrome', "Google Chrome is a browser that combines a minimal design with sophisticated technology to make the web faster, safer and easier."),
        "xchat": ("/usr/bin/xchat", 'Xchat', "XChat is a popular Internet Relay Chat (IRC) client."),
        "liferea": ("/usr/bin/liferea", 'Liferea', "Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds."),
        "midori": ("/usr/bin/midori", 'Midori', "Midori is a lightweight Webkit-based web browser."),
        "minitube": ("/usr/bin/minitube", 'MiniTube', "Minitube is a native YouTube client. With it you can watch YouTube videos in a new way."),
        "opera": ("/usr/bin/opera", 'Opera', "Opera is a web browser."),
        "pidgin": ("/usr/bin/pidgin", 'Pidgin', "Pidgin is universal chat client."),
        "skype": ("/usr/bin/skype", 'Skype', "Skype is a freemium voice-over-IP service and instant messaging client."),
        "steam": ("/usr/bin/steam", 'Steam', "Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses."),
        "thunderbird": ("/usr/bin/thunderbird", 'ThunderBird', "Thunderbird is an email program."),
        "transmission-gtk": ("/usr/bin/transmission-gtk", 'Transmission', 'transmission', "Transmission is a BitTorrent client."),
        "linuxdcpp": ("/usr/bin/linuxdcpp", 'Linuxdcpp', "A port of DC++ to GNU/Linux")}
        deep_copy = deepcopy(local_dict)
        for key, value in local_dict.items():
            key2 = (key if not len(value) > 3 else value[2])
            skyp_or_not = (key2 if not key2 == 'skype' else 'skyp')
            setattr(Menu3, skyp_or_not, 
            Builder.builder4.get_object(skyp_or_not))                        # install_remove_button
            setattr(Img, '{}_img'.format(key2),
                Builder.builder4.get_object('{}_img'.format(key2)))          # install_remove_button image
            setattr(Menu3, '{}_icon_tooltip'.format(key2),
                Builder.builder4.get_object('{}_icon_tooltip'.format(key2))) # faenza icon
                            #exe_file or path, Img.program_name, Menu3.program_name, program_name.capitalize()
            deep_copy[key] = (value[0], getattr(Img, '{}_img'.format(key2)), getattr(Menu3, skyp_or_not), value[1])
            getattr(Menu3, '{}_icon_tooltip'.format(key2)).set_tooltip_text(
            (value[2] if not len(value) > 3 else value[3]))                  # faenza icon tooltip text

        if not menu3.first_run:
            for key, value in local_dict.items():
                key2 = (key if not len(value) > 3 else value[2])
                skyp_or_not = (key2 if not key2 == 'skype' else 'skyp')
                getattr(Menu3, skyp_or_not).connect('clicked', StartKickingSomeNinjas, key)
            menu3.first_run = 'not first run'

        men3 = menu3(deep_copy)
        attr = getattr(men3, 'dicti')
        men3.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)
        
class menu2(Inherit):
    first_run = str()
    @staticmethod
    def load():
        from mymodules.categories.menu2_button import Menu2
        local_dict = {
        "evince": ("/usr/bin/evince", 'Evince', "Evince is a document viewer for multiple document formats."),
        "f-spot": ("/usr/bin/f-spot", 'F-spot', "F-Spot is a full-featured personal photo management application."),
        "gimp": ("/usr/bin/gimp", 'GIMP', "GIMP is an image retouching and editing tool, similar to Photoshop."),
        "gwenview": ("/usr/bin/gwenview", 'Gwenview', "Gwenview is an image viewer."),
        "inkscape": ("/usr/bin/inkscape", 'Inkscape', "Inkscape is an open source vector graphics editor."),
        "mypaint": ("/usr/bin/mypaint", 'MyPaint', "MyPaint is a fast and easy open-source graphics application for digital painters."),
        "pinta": ("/usr/bin/pinta", 'Pinta', "Pinta is an open-source, cross-platform bitmap image drawing and editing program inspired by Paint.NET"),
        "shotwell": ("/usr/bin/shotwell", 'Shotwell', "Shotwell is an image organizer."),
        "stellarium": ("/usr/bin/stellarium", 'Stellarium', "Stellarium is a planetarium software that shows exactly what you see when you look up at the stars."),
        "imagemagick": ("/usr/bin/convert", "ImageMagick", "Use ImageMagick to convert, edit, or compose bitmap images in a variety of formats.")}
        deep_copy = deepcopy(local_dict)
        for key, value in local_dict.items():
            key2 = (key if not key == 'f-spot' else 'f_spot')
            setattr(Menu2, key2, Builder.builder3.get_object(key2))          # install_remove_button
            setattr(Img, '{}_img'.format(key2),
                Builder.builder3.get_object('{}_img'.format(key2)))          # install_remove_button image
            setattr(Menu2, '{}_icon_tooltip'.format(key2),
                Builder.builder3.get_object('{}_icon_tooltip'.format(key2))) # faenza icon

                            #exe_file or path, Img.program_name, Menu2.program_name, program_name.capitalize()
            deep_copy[key] = (value[0], getattr(Img, '{}_img'.format(key2)), getattr(Menu2, key2), value[1])
            getattr(Menu2, '{}_icon_tooltip'.format(key2)).set_tooltip_text(value[2]) # faenza icon tooltip text

        if not menu2.first_run:
            for key in local_dict.keys():
                key2 = (key if not key == 'f-spot' else 'f_spot')
                getattr(Menu2, key2).connect('clicked', StartKickingSomeNinjas, key)
            menu2.first_run = 'not first run'

        men2 = menu2(deep_copy)
        attr = getattr(men2, 'dicti')
        men2.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)

class menu1(Inherit):
    first_run = str()
    @staticmethod
    def load():
        from mymodules.categories.menu1_button import Menu1
        local_dict = {
        "anjuta": ("/usr/bin/anjuta", 'Anjuta', "Anjuta is an integrated development environment."),
        "blender": ("/usr/bin/blender", "Blender", "Blender is a free and open-source 3D computer graphics software product used for creating animated films, \nvisual effects, art, 3D printed models and so on."),
        "bluefish": ("/usr/bin/bluefish", 'Bluefish', "Bluefish is a free and open source advanced text editor with a variety of tools for programming in general\nand the development of dynamic websites"),
        "eclipse": ("/usr/bin/eclipse", 'Eclipse', "Eclipse is IDE."),
        "geany": ("/usr/bin/geany", "Geany", "Geany is a small and lightweight integrated development environment."),
        "glade": ("/usr/bin/glade", 'Glade', "Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment."),
        "meld": ("/usr/bin/meld", 'Meld', "Meld is a visual diff and merge tool targeted at developers."),
        "netbeans": ("/usr/bin/netbeans", 'NetBeans', "Fully-featured Java IDE written completely in Java, with many modules available."),
        "qt4": ("/usr/lib/qt4/bin/designer", 'Qt4', "Qt4 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface."),
        "qt5-base": ("/usr/lib/qt/bin/designer", 'Qt5', 'qt5', "Qt5 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface."),
        "qtcreator": ("/usr/bin/qtcreator", 'QtCreator', "Qt Creator is a cross-platform C++ IDE"),
        "ninja-ide": ("/usr/bin/ninja-ide", 'Ninja-IDE', 'ninja_ide', "Ninja-IDE is a cross-platform integrated development environment designed to build Python applications."),
        "openjdk": ("/usr/share/licenses/jre7-openjdk/", "OpenJDK", "OpenJDK (Open Java Development Kit) is a free and open source implementation of the Java Platform, Standard Edition (Java SE).")}
        deep_copy = deepcopy(local_dict)
        for key, value in local_dict.items():
            key2 = (key if not len(value) > 3 else value[2])
            setattr(Menu1, key2, Builder.builder2.get_object(key2))          # install_remove_button
            setattr(Img, '{}_img'.format(key2),
                Builder.builder2.get_object('{}_img'.format(key2)))          # install_remove_button image
            setattr(Menu1, '{}_icon_tooltip'.format(key2),
                Builder.builder2.get_object('{}_icon_tooltip'.format(key2))) # faenza icon

                            #exe_file or path, Img.program_name, Menu1.program_name, program_name.capitalize()
            deep_copy[key] = (value[0], getattr(Img, '{}_img'.format(key2)), getattr(Menu1, key2), value[1])
            getattr(Menu1, '{}_icon_tooltip'.format(key2)).set_tooltip_text(
            (value[2] if not len(value) > 3 else value[3]))                  # faenza icon tooltip text

        if not menu1.first_run:
            for key, value in local_dict.items():
                key2 = (key if not len(value) > 3 else value[2])
                getattr(Menu1, key2).connect('clicked', StartKickingSomeNinjas, key)
            menu1.first_run = 'not first run'

        men1 = menu1(deep_copy)
        attr = getattr(men1, 'dicti')
        men1.init_set_file_n_tooltip(attr)
        setattr(CurrentCategoryDict, 'dicti', attr)