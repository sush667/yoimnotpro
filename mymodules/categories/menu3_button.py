import os
from mymodules.action.find_program import Find
from mymodules.buttons_images import Img
from mymodules.builder import Builder

class Menu3:

    # get menu 3 application buttons
    chromium = Builder.builder4.get_object("chromium")
    deluge = Builder.builder4.get_object("deluge")
    evolution = Builder.builder4.get_object("evolution")
    filezilla = Builder.builder4.get_object("filezilla")
    firefox = Builder.builder4.get_object("firefox")
    chrome = Builder.builder4.get_object("chrome")
    xchat = Builder.builder4.get_object("xchat")
    liferea = Builder.builder4.get_object("liferea")
    midori = Builder.builder4.get_object("midori")
    minitube = Builder.builder4.get_object("minitube")
    opera = Builder.builder4.get_object("opera")
    pidgin = Builder.builder4.get_object("pidgin")
    skyp = Builder.builder4.get_object("skyp")
    steam = Builder.builder4.get_object("steam")
    thunderbird = Builder.builder4.get_object("thunderbird")
    transmission = Builder.builder4.get_object("transmission")
    linuxdcpp = Builder.builder4.get_object("linuxdcpp")
    # add tooltip for each application icon
    chromium_icon_tooltip = Builder.builder4.get_object("chromium_icon_tooltip")
    chromium_icon_tooltip.set_tooltip_text("Chromium is the open source web browser project from which Google Chrome draws its source code.")
    deluge_icon_tooltip = Builder.builder4.get_object("deluge_icon_tooltip")
    deluge_icon_tooltip.set_tooltip_text("Open source, cross-platform BitTorrent client.")
    evolution_icon_tooltip = Builder.builder4.get_object("evolution_icon_tooltip")
    evolution_icon_tooltip.set_tooltip_text("Evolution is a fully featured open source powerful, flexible and generally great email client.")
    filezilla_icon_tooltip = Builder.builder4.get_object("filezilla_icon_tooltip")
    filezilla_icon_tooltip.set_tooltip_text("Open-source FTP client.")
    firefox_icon_tooltip = Builder.builder4.get_object("firefox_icon_tooltip")
    firefox_icon_tooltip.set_tooltip_text("Firefox is a free and open-source web browser")
    chrome_icon_tooltip = Builder.builder4.get_object("chrome_icon_tooltip")
    chrome_icon_tooltip.set_tooltip_text("Google Chrome is a browser that combines a minimal design with sophisticated technology to make the web faster, safer and easier.")
    xchat_icon_tooltip = Builder.builder4.get_object("xchat_icon_tooltip")
    xchat_icon_tooltip.set_tooltip_text("XChat is a popular Internet Relay Chat (IRC) client.")
    liferea_icon_tooltip = Builder.builder4.get_object("liferea_icon_tooltip")
    liferea_icon_tooltip.set_tooltip_text("Liferea is an abbreviation for Linux Feed Reader, a news aggregator for online news feeds.")
    midori_icon_tooltip = Builder.builder4.get_object("midori_icon_tooltip")
    midori_icon_tooltip.set_tooltip_text("Midori is a lightweight Webkit-based web browser.")
    minitube_icon_tooltip = Builder.builder4.get_object("minitube_icon_tooltip")
    minitube_icon_tooltip.set_tooltip_text("Minitube is a native YouTube client. With it you can watch YouTube videos in a new way.")
    opera_icon_tooltip = Builder.builder4.get_object("opera_icon_tooltip")
    opera_icon_tooltip.set_tooltip_text("Opera is a web browser.")
    pidgin_icon_tooltip = Builder.builder4.get_object("pidgin_icon_tooltip")
    pidgin_icon_tooltip.set_tooltip_text("Pidgin is universal chat client.")
    skype_icon_tooltip = Builder.builder4.get_object("skype_icon_tooltip")
    skype_icon_tooltip.set_tooltip_text("Skype is a freemium voice-over-IP service and instant messaging client.")
    steam_icon_tooltip = Builder.builder4.get_object("steam_icon_tooltip")
    steam_icon_tooltip.set_tooltip_text("Steam is a digital distribution, digital rights management, multiplayer, and communications platform developed by\nValve Corporation. It is used to distribute games and related media online, from small independent developers to larger software houses.")
    thunderbird_icon_tooltip = Builder.builder4.get_object("thunderbird_icon_tooltip")
    thunderbird_icon_tooltip.set_tooltip_text("Thunderbird is an email program.")
    transmission_icon_tooltip = Builder.builder4.get_object("transmission_icon_tooltip")
    transmission_icon_tooltip.set_tooltip_text("Transmission is a BitTorrent client.")
    linuxdcpp_icon_tooltip = Builder.builder4.get_object("linuxdcpp_icon_tooltip")
    linuxdcpp_icon_tooltip.set_tooltip_text("A port of DC++ to GNU/Linux")

    @staticmethod
    def on_button3_clicked():
        Img.image1.set_from_file('./categories/menu1.png')
        Img.image2.set_from_file('./categories/menu2.png')
        Img.image3.set_from_file('./categories/menu33.png')
        Img.image4.set_from_file('./categories/menu4.png')
        Img.image5.set_from_file('./categories/menu5.xpm')
        Img.image6.set_from_file('./categories/menu6.png')

        # check if those programs are installed and set appropriate sign
        if os.path.isfile(Find.program['chromium']):
            Img.chromium_img.set_from_file('./categories/gtk-yes.png')
            Menu3.chromium.set_tooltip_text("Chromium is installed.\nClick to remove it.")
        else:
            Img.chromium_img.set_from_file('./categories/gtk-no.png')
            Menu3.chromium.set_tooltip_text("Chromium is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['deluge']):
            Img.deluge_img.set_from_file('./categories/gtk-yes.png')
            Menu3.deluge.set_tooltip_text("Deluge is not installed.\nClick to remove it.")
        else:
            Img.deluge_img.set_from_file('./categories/gtk-no.png')
            Menu3.deluge.set_tooltip_text("Deluge is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['evolution']):
            Img.evolution_img.set_from_file('./categories/gtk-yes.png')
            Menu3.evolution.set_tooltip_text("Evolution is installed.\nClick to remove it.")
        else:
            Img.evolution_img.set_from_file('./categories/gtk-no.png')
            Menu3.evolution.set_tooltip_text("Evolution is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['filezilla']):
            Img.filezilla_img.set_from_file('./categories/gtk-yes.png')
            Menu3.filezilla.set_tooltip_text("Filezilla is installed.\nClick to remove it.")
        else:
            Img.filezilla_img.set_from_file('./categories/gtk-no.png')
            Menu3.filezilla.set_tooltip_text("Filezilla is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['firefox']):
            Img.firefox_img.set_from_file('./categories/gtk-yes.png')
            Menu3.firefox.set_tooltip_text("Firefox is installed.\nClick to remove it.")
        else:
            Img.firefox_img.set_from_file('./categories/gtk-no.png')
            Menu3.firefox.set_tooltip_text("Firefox is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['google-chrome']):
            Img.chrome_img.set_from_file('./categories/gtk-yes.png')
            Menu3.chrome.set_tooltip_text("Google Chrome is installed.\nClick to remove it.")
        else:
            Img.chrome_img.set_from_file('./categories/gtk-no.png')
            Menu3.chrome.set_tooltip_text("Google Chrome is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['xchat']):
            Img.xchat_img.set_from_file('./categories/gtk-yes.png')
            Menu3.xchat.set_tooltip_text("Xchat is installed.\nClick to remove it.")
        else:
            Img.xchat_img.set_from_file('./categories/gtk-no.png')
            Menu3.xchat.set_tooltip_text("Xchat is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['liferea']):
            Img.liferea_img.set_from_file('./categories/gtk-yes.png')
            Menu3.liferea.set_tooltip_text("Liferea is installed.\nClick to remove it.")
        else:
            Img.liferea_img.set_from_file('./categories/gtk-no.png')
            Menu3.liferea.set_tooltip_text("Liferea is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['midori']):
            Img.midori_img.set_from_file('./categories/gtk-yes.png')
            Menu3.midori.set_tooltip_text("Midori is installed.\nClick to remove it.")
        else:
            Img.midori_img.set_from_file('./categories/gtk-no.png')
            Menu3.midori.set_tooltip_text("Midori is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['minitube']):
            Img.minitube_img.set_from_file('./categories/gtk-yes.png')
            Menu3.minitube.set_tooltip_text("Minitube is installed.\nClick to remove it.")
        else:
            Img.minitube_img.set_from_file('./categories/gtk-no.png')
            Menu3.minitube.set_tooltip_text("Minitube is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['opera']):
            Img.opera_img.set_from_file('./categories/gtk-yes.png')
            Menu3.opera.set_tooltip_text("Opera is installed.\nClick to remove it.")
        else:
            Img.opera_img.set_from_file('./categories/gtk-no.png')
            Menu3.opera.set_tooltip_text("Opera is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['pidgin']):
            Img.pidgin_img.set_from_file('./categories/gtk-yes.png')
            Menu3.pidgin.set_tooltip_text("Pidgin is installed.\nClick to remove it.")
        else:
            Img.pidgin_img.set_from_file('./categories/gtk-no.png')
            Menu3.pidgin.set_tooltip_text("Pidgin is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['skype']):
            Img.skype_img.set_from_file('./categories/gtk-yes.png')
            Menu3.skyp.set_tooltip_text("Skype is installed.\nClick to remove it.")
        else:
            Img.skype_img.set_from_file('./categories/gtk-no.png')
            Menu3.skyp.set_tooltip_text("Skype is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['steam']):
            Img.steam_img.set_from_file('./categories/gtk-yes.png')
            Menu3.steam.set_tooltip_text("Steam is installed.\nClick to remove it.")
        else:
            Img.steam_img.set_from_file('./categories/gtk-no.png')
            Menu3.steam.set_tooltip_text("Steam is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['thunderbird']):
            Img.thunderbird_img.set_from_file('./categories/gtk-yes.png')
            Menu3.thunderbird.set_tooltip_text("Thunderbird is installed.\nClick to remove it.")
        else:
            Img.thunderbird_img.set_from_file('./categories/gtk-no.png')
            Menu3.thunderbird.set_tooltip_text("Thunderbird is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['transmission-gtk']):
            Img.transmission_img.set_from_file('./categories/gtk-yes.png')
            Menu3.transmission.set_tooltip_text("Transmission is installed.\nClick to remove it.")
        else:
            Img.transmission_img.set_from_file('./categories/gtk-no.png')
            Menu3.transmission.set_tooltip_text("Transmission is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['linuxdcpp']):
            Img.linuxdcpp_img.set_from_file('./categories/gtk-yes.png')
            Menu3.linuxdcpp.set_tooltip_text("Linuxdcpp is installed.\nClick to remove it.")
        else:
            Img.linuxdcpp_img.set_from_file('./categories/gtk-no.png')
            Menu3.linuxdcpp.set_tooltip_text("Linuxdcpp is not installed.\nClick to install it.")