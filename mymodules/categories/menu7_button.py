import os
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.find_program import Find
from mymodules.action.dial import SetToolTip, action

class Menu7:
    # get menu 7 application buttons
    geany_ = Builder.builder8.get_object("geany_")
    blender_ = Builder.builder8.get_object("blender_")
    ninja_ide_ = Builder.builder8.get_object("ninja_ide_")
    glade_ = Builder.builder8.get_object("glade_")
    audacious_ = Builder.builder8.get_object("audacious_")
    gimp_ = Builder.builder8.get_object("gimp_")
    evince_ = Builder.builder8.get_object("evince_")
    xfburn_ = Builder.builder8.get_object("xfburn_")
    flashplayer_ = Builder.builder8.get_object("flashplayer_")
    openshot_ = Builder.builder8.get_object("openshot_")
    chromium_ = Builder.builder8.get_object("chromium_")
    deluge_ = Builder.builder8.get_object("deluge_")
    liferea_ = Builder.builder8.get_object("liferea_")
    htop_ = Builder.builder8.get_object("htop_")
    skype_ = Builder.builder8.get_object("skype_")
    wireshark_ = Builder.builder8.get_object("wireshark_")
    virtualbox_ = Builder.builder8.get_object("virtualbox_")
    steam_ = Builder.builder8.get_object("steam_")
    xchat_ = Builder.builder8.get_object("xchat_")
    gedit_ = Builder.builder8.get_object("gedit_")
    # add tooltip for each application icon
    geany_icon_tooltip_ = Builder.builder8.get_object("geany_icon_tooltip_")
    geany_icon_tooltip_.set_tooltip_text("Geany is a small and lightweight integrated development environment.")
    blender_icon_tooltip_ = Builder.builder8.get_object("blender_icon_tooltip_")
    blender_icon_tooltip_.set_tooltip_text("Blender is the open source, cross platform suite of tools for 3D creation.")
    ninja_ide_icon_tooltip_ = Builder.builder8.get_object("ninja_ide_icon_tooltip_")
    ninja_ide_icon_tooltip_.set_tooltip_text("Ninja-IDE is a cross-platform integrated development environment designed to build Python applications.")
    glade_icon_tooltip_ = Builder.builder8.get_object("glade_icon_tooltip_")
    glade_icon_tooltip_.set_tooltip_text("Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment.")
    audacious_icon_tooltip_ = Builder.builder8.get_object("audacious_icon_tooltip_")
    audacious_icon_tooltip_.set_tooltip_text("Audio player with support for many formats, and it has support for third-party plugins.")
    gimp_icon_tooltip_ = Builder.builder8.get_object("gimp_icon_tooltip_")
    gimp_icon_tooltip_.set_tooltip_text("GIMP is an image retouching and editing tool, similar to Photoshop.")
    evince_icon_tooltip_ = Builder.builder8.get_object("evince_icon_tooltip_")
    evince_icon_tooltip_.set_tooltip_text("Evince is a document viewer for multiple document formats.")
    xfburn_icon_tooltip_ = Builder.builder8.get_object("xfburn_icon_tooltip_")
    xfburn_icon_tooltip_.set_tooltip_text("Xfburn is a simple CD/DVD burning tool")
    flashplayer_icon_tooltip_ = Builder.builder8.get_object("flashplayer_icon_tooltip_")
    flashplayer_icon_tooltip_.set_tooltip_text("Cross-platform plugin plays animations, videos and sound files.")
    openshot_icon_tooltip_ = Builder.builder8.get_object("openshot_icon_tooltip_")
    openshot_icon_tooltip_.set_tooltip_text("A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style")
    chromium_icon_tooltip_ = Builder.builder8.get_object("chromium_icon_tooltip_")
    chromium_icon_tooltip_.set_tooltip_text("Chromium is the open source web browser project from which Google Chrome draws its source code.")
    deluge_icon_tooltip_ = Builder.builder8.get_object("deluge_icon_tooltip_")
    deluge_icon_tooltip_.set_tooltip_text("Open source, cross-platform BitTorrent client.")
    liferea_icon_tooltip_ = Builder.builder8.get_object("liferea_icon_tooltip_")
    liferea_icon_tooltip_.set_tooltip_text("Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds.")
    htop_icon_tooltip_ = Builder.builder8.get_object("htop_icon_tooltip_")
    htop_icon_tooltip_.set_tooltip_text("Htop is an interactive system-monitor process-viewer.")
    skype_icon_tooltip_ = Builder.builder8.get_object("skype_icon_tooltip_")
    skype_icon_tooltip_.set_tooltip_text("Skype is a freemium voice-over-IP service and instant messaging client")
    wireshark_icon_tooltip_ = Builder.builder8.get_object("wireshark_icon_tooltip_")
    wireshark_icon_tooltip_.set_tooltip_text("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development.")
    virtualbox_icon_tooltip_ = Builder.builder8.get_object("virtualbox_icon_tooltip_")
    virtualbox_icon_tooltip_.set_tooltip_text("VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC.")
    steam_icon_tooltip_ = Builder.builder8.get_object("steam_icon_tooltip_")
    steam_icon_tooltip_.set_tooltip_text("Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses.")
    xchat_icon_tooltip_ = Builder.builder8.get_object("xchat_icon_tooltip_")
    xchat_icon_tooltip_.set_tooltip_text("XChat is a popular Internet Relay Chat (IRC) client.")
    gedit_icon_tooltip_ = Builder.builder8.get_object("gedit_icon_tooltip_")
    gedit_icon_tooltip_.set_tooltip_text("Gedit is lightweight text editor.")

    @staticmethod
    def load_icons_n_tooltips_at_startup():
        # check if those programs are installed and set appropriate sign
        if os.path.isfile(Find.program['geany']):
            Img.geany__img.set_from_file(action.gtk_yes)
            Menu7.geany_.set_tooltip_text(format(SetToolTip('geany', action.installed, action.remove_it)))
        else:
            Img.geany__img.set_from_file(action.gtk_no)
            Menu7.geany_.set_tooltip_text(format(SetToolTip('geany', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['blender']):
            Img.blender__img.set_from_file(action.gtk_yes)
            Menu7.blender_.set_tooltip_text(format(SetToolTip('blnder', action.installed, action.remove_it)))
        else:
            Img.blender__img.set_from_file(action.gtk_no)
            Menu7.blender_.set_tooltip_text(format(SetToolTip('blender', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['ninja-ide']):
            Img.ninja_ide__img.set_from_file(action.gtk_yes)
            Menu7.ninja_ide_.set_tooltip_text(format(SetToolTip('ninja-IDE', action.installed, action.remove_it)))
        else:
            Img.ninja_ide__img.set_from_file(action.gtk_no)
            Menu7.ninja_ide_.set_tooltip_text(format(SetToolTip('ninja-IDE', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['glade']):
            Img.glade__img.set_from_file(action.gtk_yes)
            Menu7.glade_.set_tooltip_text(format(SetToolTip('glade', action.installed, action.remove_it)))
        else:
            Img.glade__img.set_from_file(action.gtk_no)
            Menu7.glade_.set_tooltip_text(format(SetToolTip('glade', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['audacious']):
            Img.audacious__img.set_from_file(action.gtk_yes)
            Menu7.audacious_.set_tooltip_text(format(SetToolTip('audacious', action.installed, action.remove_it)))
        else:
            Img.audacious__img.set_from_file(action.gtk_no)
            Menu7.audacious_.set_tooltip_text(format(SetToolTip('audacious', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['gimp']):
            Img.gimp__img.set_from_file(action.gtk_yes)
            Menu7.gimp_.set_tooltip_text(format(SetToolTip('gimp', action.installed, action.remove_it)))
        else:
            Img.gimp__img.set_from_file(action.gtk_no)
            Menu7.gimp_.set_tooltip_text(format(SetToolTip('gimp', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['evince']):
            Img.evince__img.set_from_file(action.gtk_yes)
            Menu7.evince_.set_tooltip_text(format(SetToolTip('evince', action.installed, action.remove_it)))
        else:
            Img.evince__img.set_from_file(action.gtk_no)
            Menu7.evince_.set_tooltip_text(format(SetToolTip('evince', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['xfburn']):
            Img.xfburn__img.set_from_file(action.gtk_yes)
            Menu7.xfburn_.set_tooltip_text(format(SetToolTip('xfburn', action.installed, action.remove_it)))
        else:
            Img.xfburn__img.set_from_file(action.gtk_no)
            Menu7.xfburn_.set_tooltip_text(format(SetToolTip('xfburn', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['flashplugin']):
<<<<<<< HEAD
            Img.flashplayer__img.set_from_file(action.gtk_yes)
            Menu7.flashplayer_.set_tooltip_text(format(SetToolTip('adobe Flashplayer', action.installed, action.remove_it)))
=======
            Img.flashplayer__img.set_from_file('./categories/gtk-yes.png')
            Menu7.flashplayer_.set_tooltip_text("Flashplayer is installed.\nClick to remove it.")
>>>>>>> branch 'master' of https://github.com/wifiextender/yoimnotpro
        else:
            Img.flashplayer__img.set_from_file(action.gtk_no)
            Menu7.flashplayer_.set_tooltip_text(format(SetToolTip('adobe Flashplayer', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['openshot']):
            Img.openshot__img.set_from_file(action.gtk_yes)
            Menu7.openshot_.set_tooltip_text(format(SetToolTip('openShot', action.installed, action.remove_it)))
        else:
            Img.openshot__img.set_from_file(action.gtk_no)
            Menu7.openshot_.set_tooltip_text(format(SetToolTip('openShot', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['chromium']):
            Img.chromium__img.set_from_file(action.gtk_yes)
            Menu7.chromium_.set_tooltip_text(format(SetToolTip('chromium', action.installed, action.remove_it)))
        else:
            Img.chromium__img.set_from_file(action.gtk_no)
            Menu7.chromium_.set_tooltip_text(format(SetToolTip('chromium', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['deluge']):
            Img.deluge__img.set_from_file(action.gtk_yes)
            Menu7.deluge_.set_tooltip_text(format(SetToolTip('deluge', action.installed, action.remove_it)))
        else:
            Img.deluge__img.set_from_file(action.gtk_no)
            Menu7.deluge_.set_tooltip_text(format(SetToolTip('deluge', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['liferea']):
            Img.liferea__img.set_from_file(action.gtk_yes)
            Menu7.liferea_.set_tooltip_text(format(SetToolTip('liferea', action.installed, action.remove_it)))
        else:
            Img.liferea__img.set_from_file(action.gtk_no)
            Menu7.liferea_.set_tooltip_text(format(SetToolTip('liferea', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['htop']):
            Img.htop__img.set_from_file(action.gtk_yes)
            Menu7.htop_.set_tooltip_text(format(SetToolTip('htop', action.installed, action.remove_it)))
        else:
            Img.htop__img.set_from_file(action.gtk_no)
            Menu7.htop_.set_tooltip_text(format(SetToolTip('htop', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['skype']):
            Img.skype__img.set_from_file(action.gtk_yes)
            Menu7.skype_.set_tooltip_text(format(SetToolTip('skype', action.installed, action.remove_it)))
        else:
            Img.skype__img.set_from_file(action.gtk_no)
            Menu7.skype_.set_tooltip_text(format(SetToolTip('skype', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['wireshark-gtk']):
<<<<<<< HEAD
            Img.wireshark__img.set_from_file(action.gtk_yes)
            Menu7.wireshark_.set_tooltip_text(format(SetToolTip('wireshark', action.installed, action.remove_it)))
=======
            Img.wireshark__img.set_from_file('./categories/gtk-yes.png')
            Menu7.wireshark_.set_tooltip_text("Wireshark is installed.\nClick to remove it.")
>>>>>>> branch 'master' of https://github.com/wifiextender/yoimnotpro
        else:
            Img.wireshark__img.set_from_file(action.gtk_no)
            Menu7.wireshark_.set_tooltip_text(format(SetToolTip('wireshark', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['virtualbox']):
            Img.virtualbox__img.set_from_file(action.gtk_yes)
            Menu7.virtualbox_.set_tooltip_text(format(SetToolTip('virtualbox', action.installed, action.remove_it)))
        else:
            Img.virtualbox__img.set_from_file(action.gtk_no)
            Menu7.virtualbox_.set_tooltip_text(format(SetToolTip('virtualbox', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['steam']):
            Img.steam__img.set_from_file(action.gtk_yes)
            Menu7.steam_.set_tooltip_text(format(SetToolTip('steam', action.installed, action.remove_it)))
        else:
            Img.steam__img.set_from_file(action.gtk_no)
            Menu7.steam_.set_tooltip_text(format(SetToolTip('steam', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['xchat']):
            Img.xchat__img.set_from_file(action.gtk_yes)
            Menu7.xchat_.set_tooltip_text(format(SetToolTip('xchat', action.installed, action.remove_it)))
        else:
            Img.xchat__img.set_from_file(action.gtk_no)
            Menu7.xchat_.set_tooltip_text(format(SetToolTip('xchat', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['gedit']):
            Img.gedit__img.set_from_file(action.gtk_yes)
            Menu7.gedit_.set_tooltip_text(format(SetToolTip('gedit', action.installed, action.remove_it)))
        else:
            Img.gedit__img.set_from_file(action.gtk_no)
            Menu7.gedit_.set_tooltip_text(format(SetToolTip('gedit', action.not_here, action.install_it)))
