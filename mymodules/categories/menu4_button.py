import os
from mymodules.action.find_program import Find
from mymodules.buttons_images import Img
from mymodules.builder import Builder

class Menu4:
    # get menu 4 application buttons
    amarok = Builder.builder5.get_object("amarok")
    audacious = Builder.builder5.get_object("audacious")
    banshee = Builder.builder5.get_object("banshee")
    cheese = Builder.builder5.get_object("cheese")
    clementine = Builder.builder5.get_object("clementine")
    flashplayer = Builder.builder5.get_object("flashplayer")
    recordmydesktop = Builder.builder5.get_object("recordmydesktop")
    guayadeque = Builder.builder5.get_object("guayadeque")
    mplayer = Builder.builder5.get_object("mplayer")
    openshot = Builder.builder5.get_object("openshot")
    pitivi = Builder.builder5.get_object("pitivi")
    rhythmbox = Builder.builder5.get_object("rhythmbox")
    soundconverter = Builder.builder5.get_object("soundconverter")
    totem = Builder.builder5.get_object("totem")
    vlc = Builder.builder5.get_object("vlc")
    winff = Builder.builder5.get_object("winff")
    winff.set_tooltip_text("WinFF is a video converter.")
    xfburn = Builder.builder5.get_object("xfburn")
    kdenlive = Builder.builder5.get_object("kdenlive")
    simplescreenrecorder = Builder.builder5.get_object("simplescreenrecorder")
    vokoscreen = Builder.builder5.get_object("vokoscreen")
    # add tooltip for each application icon
    amarok_icon_tooltip = Builder.builder5.get_object("amarok_icon_tooltip")
    amarok_icon_tooltip.set_tooltip_text("Amarok is a cross-platform free and open source music player.")
    audacious_icon_tooltip = Builder.builder5.get_object("audacious_icon_tooltip")
    audacious_icon_tooltip.set_tooltip_text("Audacious is a free and open source audio player.")
    banshee_icon_tooltip = Builder.builder5.get_object("banshee_icon_tooltip")
    banshee_icon_tooltip.set_tooltip_text("Banshee is a cross-platform open-source media player.")
    cheese_icon_tooltip = Builder.builder5.get_object("cheese_icon_tooltip")
    cheese_icon_tooltip.set_tooltip_text("Cheese uses your webcam to take photos and videos, applies fancy special effects, and lets you share the fun with others.")
    clementine_icon_tooltip = Builder.builder5.get_object("clementine_icon_tooltip")
    clementine_icon_tooltip.set_tooltip_text("Clementine is a cross-platform free and open source music player and library organizer. ")
    flashplayer_icon_tooltip = Builder.builder5.get_object("flashplayer_icon_tooltip")
    flashplayer_icon_tooltip.set_tooltip_text("Cross-platform plugin plays animations, videos and sound files.")
    recordmydesktop_icon_tooltip = Builder.builder5.get_object("recordmydesktop_icon_tooltip")
    recordmydesktop_icon_tooltip.set_tooltip_text("recordMyDesktop is a desktop session recorder.")
    guayadeque_icon_tooltip = Builder.builder5.get_object("guayadeque_icon_tooltip")
    guayadeque_icon_tooltip.set_tooltip_text("Guayadeque is a music management program designed for all music enthusiasts.")
    mplayer_icon_tooltip = Builder.builder5.get_object("mplayer_icon_tooltip")
    mplayer_icon_tooltip.set_tooltip_text("MPlayer is a free software and open source media player.")
    openshot_icon_tooltip = Builder.builder5.get_object("openshot_icon_tooltip")
    openshot_icon_tooltip.set_tooltip_text("A simple, powerful, and free open-source video editor for Linux with a focus on usability, flexibility, and style.")
    pitivi_icon_tooltip = Builder.builder5.get_object("pitivi_icon_tooltip")
    pitivi_icon_tooltip.set_tooltip_text("Pitivi is an open source, non-linear video editor.")
    rhythmbox_icon_tooltip = Builder.builder5.get_object("rhythmbox_icon_tooltip")
    rhythmbox_icon_tooltip.set_tooltip_text("Rhythmbox is an integrated music management application, originally inspired by Apple's iTunes.")
    soundconverter_icon_tooltip = Builder.builder5.get_object("soundconverter_icon_tooltip")
    soundconverter_icon_tooltip.set_tooltip_text("SoundConverter is the leading audio file converter.")
    totem_icon_tooltip = Builder.builder5.get_object("totem_icon_tooltip")
    totem_icon_tooltip.set_tooltip_text("Totem is a media player.")
    vlc_icon_tooltip = Builder.builder5.get_object("vlc_icon_tooltip")
    vlc_icon_tooltip.set_tooltip_text("VLC is a multimedia player for various audio and video formats.")
    winff_icon_tooltip = Builder.builder5.get_object("winff_icon_tooltip")
    winff_icon_tooltip.set_tooltip_text("WinFF is a video converter.")
    xfburn_icon_tooltip = Builder.builder5.get_object("xfburn_icon_tooltip")
    xfburn_icon_tooltip.set_tooltip_text("Xfburn is a simple CD/DVD burning tool.")
    kdenlive_icon_tooltip = Builder.builder5.get_object("kdenlive_icon_tooltip")
    kdenlive_icon_tooltip.set_tooltip_text("Kdenlive (KDE Non-Linear Video Editor) is an open source video editing software")
    simplescreenrecorder_icon_tooltip = Builder.builder5.get_object("simplescreenrecorder_icon_tooltip")
    simplescreenrecorder_icon_tooltip.set_tooltip_text("SimpleScreenRecorder is capable of recording video from full-screen and window-size captures of Opengl applications(and games).")
    vokoscreen_icon_tooltip = Builder.builder5.get_object("vokoscreen_icon_tooltip")
    vokoscreen_icon_tooltip.set_tooltip_text("Vokoscreen is an easy to use screencast creator to record educational videos, live recordings of browser, installation, videoconferences, etc.")

    @staticmethod
    def on_button4_clicked():
        Img.image1.set_from_file('./categories/menu1.png')
        Img.image2.set_from_file('./categories/menu2.png')
        Img.image3.set_from_file('./categories/menu3.png')
        Img.image4.set_from_file('./categories/menu44.png')
        Img.image5.set_from_file('./categories/menu5.xpm')
        Img.image6.set_from_file('./categories/menu6.png')

        # check if those programs are installed and set appropriate sign
        if os.path.isfile(Find.program['amarok']):
            Img.amarok_img.set_from_file('./categories/gtk-yes.png')
            Menu4.amarok.set_tooltip_text("Amarok is installed.\nClick to remove it.")
        else:
            Img.amarok_img.set_from_file('./categories/gtk-no.png')
            Menu4.amarok.set_tooltip_text("Amarok is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['audacious']):
            Img.audacious_img.set_from_file('./categories/gtk-yes.png')
            Menu4.audacious.set_tooltip_text("Audacious is installed.\nClick to remove it.")
        else:
            Img.audacious_img.set_from_file('./categories/gtk-no.png')
            Menu4.audacious.set_tooltip_text("Audacious is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['banshee']):
            Img.banshee_img.set_from_file('./categories/gtk-yes.png')
            Menu4.banshee.set_tooltip_text("Banshee is installed.\nClick to remove it.")
        else:
            Img.banshee_img.set_from_file('./categories/gtk-no.png')
            Menu4.banshee.set_tooltip_text("Banshee is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['cheese']):
            Img.cheese_img.set_from_file('./categories/gtk-yes.png')
            Menu4.cheese.set_tooltip_text("Cheese is installed.\nClick to remove it.")
        else:
            Img.cheese_img.set_from_file('./categories/gtk-no.png')
            Menu4.cheese.set_tooltip_text("Cheese is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['clementine']):
            Img.clementine_img.set_from_file('./categories/gtk-yes.png')
            Menu4.clementine.set_tooltip_text("Clementine is installed.\nClick to remove it.")
        else:
            Img.clementine_img.set_from_file('./categories/gtk-no.png')
            Menu4.clementine.set_tooltip_text("Clementine is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['flash-player']):
            Img.flashplayer_img.set_from_file('./categories/gtk-yes.png')
            Menu4.flashplayer.set_tooltip_text("Flashplayer is installed.\nClick to remove it.")
        else:
            Menu4.flashplayer_img.set_from_file('./categories/gtk-no.png')
            Menu4.flashplayer.set_tooltip_text("Flashplayer is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['recordmydesktop']):
            Img.recordmydesktop_img.set_from_file('./categories/gtk-yes.png')
            Menu4.recordmydesktop.set_tooltip_text("RecordMyDesktop is installed.\nClick to remove it.")
        else:
            Img.recordmydesktop_img.set_from_file('./categories/gtk-no.png')
            Menu4.recordmydesktop.set_tooltip_text("RecordMyDesktop is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['guayadeque']):
            Img.guayadeque_img.set_from_file('./categories/gtk-yes.png')
            Menu4.guayadeque.set_tooltip_text("Guayadeque is installed.\nClick to remove it.")
        else:
            Img.guayadeque_img.set_from_file('./categories/gtk-no.png')
            Menu4.guayadeque.set_tooltip_text("Guayadeque is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['mplayer']):
            Img.mplayer_img.set_from_file('./categories/gtk-yes.png')
            Menu4.mplayer.set_tooltip_text("Mplayer is installed.\nClick to remove it.")
        else:
            Img.mplayer_img.set_from_file('./categories/gtk-no.png')
            Menu4.mplayer.set_tooltip_text("Mplayer is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['openshot']):
            Img.openshot_img.set_from_file('./categories/gtk-yes.png')
            Menu4.openshot.set_tooltip_text("Openshot is installed.\nClick to remove it.")
        else:
            Img.openshot_img.set_from_file('./categories/gtk-no.png')
            Menu4.openshot.set_tooltip_text("Openshot is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['pitivi']):
            Img.pitivi_img.set_from_file('./categories/gtk-yes.png')
            Menu4.pitivi.set_tooltip_text("PiTiVi is installed.\nClick to install it.")
        else:
            Img.pitivi_img.set_from_file('./categories/gtk-no.png')
            Menu4.pitivi.set_tooltip_text("PiTiVi is not installed.\nClick to remove it.")

        if os.path.isfile(Find.program['rhythmbox']):
            Img.rhythmbox_img.set_from_file('./categories/gtk-yes.png')
            Menu4.rhythmbox.set_tooltip_text("Rhythmbox is installed.\nClick to remove it.")
        else:
            Img.rhythmbox_img.set_from_file('./categories/gtk-no.png')
            Menu4.rhythmbox.set_tooltip_text("Rhythmbox is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['soundconverter']):
            Img.soundconverter_img.set_from_file('./categories/gtk-yes.png')
            Menu4.soundconverter.set_tooltip_text("Soundconverter is installed.\nClick to remove it.")
        else:
            Img.soundconverter_img.set_from_file('./categories/gtk-no.png')
            Menu4.soundconverter.set_tooltip_text("Soundconverter is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['totem']):
            Img.totem_img.set_from_file('./categories/gtk-yes.png')
            Menu4.totem.set_tooltip_text("Totem is installed.\nClick to remove it.")
        else:
            Img.totem_img.set_from_file('./categories/gtk-no.png')
            Menu4.totem.set_tooltip_text("Totem is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['vlc']):
            Img.vlc_img.set_from_file('./categories/gtk-yes.png')
            Menu4.vlc.set_tooltip_text("Vlc is installed.\nClick to remove it.")
        else:
            Img.vlc_img.set_from_file('./categories/gtk-no.png')
            Menu4.vlc.set_tooltip_text("Vlc is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['winff']):
            Img.winff_img.set_from_file('./categories/gtk-yes.png')
            Menu4.winff.set_tooltip_text("Winff is installed.\nClick to remove it.")
        else:
            Img.winff_img.set_from_file('./categories/gtk-no.png')
            Menu4.winff.set_tooltip_text("Winff is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['xfburn']):
            Img.xfburn_img.set_from_file('./categories/gtk-yes.png')
            Menu4.xfburn.set_tooltip_text("Xfburn is installed.\nClick to remove it.")
        else:
            Img.xfburn_img.set_from_file('./categories/gtk-no.png')
            Menu4.xfburn.set_tooltip_text("Xfburn is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['kdenlive']):
            Img.kdenlive_img.set_from_file('./categories/gtk-yes.png')
            Menu4.kdenlive.set_tooltip_text("Kdenlive is installed.\nClick to remove it.")
        else:
            Img.kdenlive_img.set_from_file('./categories/gtk-no.png')
            Menu4.kdenlive.set_tooltip_text("Kdenlive is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['simplescreenrecorder']):
            Img.simplescreenrecorder_img.set_from_file('./categories/gtk-yes.png')
            Menu4.simplescreenrecorder.set_tooltip_text("Simple screen recorder is installed.\nClick to remove it.")
        else:
            Img.simplescreenrecorder_img.set_from_file('./categories/gtk-no.png')
            Menu4.simplescreenrecorder.set_tooltip_text("Simple screen recorder is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['vokoscreen']):
            Img.vokoscreen_img.set_from_file('./categories/gtk-yes.png')
            Menu4.vokoscreen.set_tooltip_text("Vokoscreen is installed.\nClick to remove it.")
        else:
            Img.vokoscreen_img.set_from_file('./categories/gtk-no.png')
            Menu4.vokoscreen.set_tooltip_text("Vokoscreen is not installed.\nClick to install it.")