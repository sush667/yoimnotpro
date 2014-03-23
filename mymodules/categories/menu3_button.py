import os
from mymodules.action.find_program import Find
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.dial import SetToolTip, action

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
        Img.image1.set_from_file(action.menu_img_1)
        Img.image2.set_from_file(action.menu_img_2)
        Img.image3.set_from_file(action.menu_img_33)
        Img.image4.set_from_file(action.menu_img_4)
        Img.image5.set_from_file(action.menu_img_5)
        Img.image6.set_from_file(action.menu_img_6)

        # check if those programs are installed and set appropriate sign
        no = action.gtk_no
        yes = action.gtk_yes
        if os.path.isfile(Find.program['chromium']):
            Img.chromium_img.set_from_file(yes)
            Menu3.chromium.set_tooltip_text(format(SetToolTip('chromium', action.installed, action.remove_it)))
        else:
            Img.chromium_img.set_from_file(no)
            Menu3.chromium.set_tooltip_text(format(SetToolTip('chromium', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['deluge']):
            Img.deluge_img.set_from_file(yes)
            Menu3.deluge.set_tooltip_text(format(SetToolTip('deluge', action.installed, action.remove_it)))
        else:
            Img.deluge_img.set_from_file(no)
            Menu3.deluge.set_tooltip_text(format(SetToolTip('deluge', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['evolution']):
            Img.evolution_img.set_from_file(yes)
            Menu3.evolution.set_tooltip_text(format(SetToolTip('evolution', action.installed, action.remove_it)))
        else:
            Img.evolution_img.set_from_file(no)
            Menu3.evolution.set_tooltip_text(format(SetToolTip('evolution', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['filezilla']):
            Img.filezilla_img.set_from_file(yes)
            Menu3.filezilla.set_tooltip_text(format(SetToolTip('filezilla', action.installed, action.remove_it)))
        else:
            Img.filezilla_img.set_from_file(no)
            Menu3.filezilla.set_tooltip_text(format(SetToolTip('filezilla', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['firefox']):
            Img.firefox_img.set_from_file(yes)
            Menu3.firefox.set_tooltip_text(format(SetToolTip('firefox', action.installed, action.remove_it)))
        else:
            Img.firefox_img.set_from_file(no)
            Menu3.firefox.set_tooltip_text(format(SetToolTip('firefox', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['google-chrome']):
            Img.chrome_img.set_from_file(yes)
            Menu3.chrome.set_tooltip_text(format(SetToolTip('google Chrome', action.installed, action.remove_it)))
        else:
            Img.chrome_img.set_from_file(no)
            Menu3.chrome.set_tooltip_text(format(SetToolTip('google Chrome', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['xchat']):
            Img.xchat_img.set_from_file(yes)
            Menu3.xchat.set_tooltip_text(format(SetToolTip('xchat', action.installed, action.remove_it)))
        else:
            Img.xchat_img.set_from_file(no)
            Menu3.xchat.set_tooltip_text(format(SetToolTip('xchat', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['liferea']):
            Img.liferea_img.set_from_file(yes)
            Menu3.liferea.set_tooltip_text(format(SetToolTip('liferea', action.installed, action.remove_it)))
        else:
            Img.liferea_img.set_from_file(no)
            Menu3.liferea.set_tooltip_text(format(SetToolTip('liferea', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['midori']):
            Img.midori_img.set_from_file(yes)
            Menu3.midori.set_tooltip_text(format(SetToolTip('midori', action.installed, action.remove_it)))
        else:
            Img.midori_img.set_from_file(no)
            Menu3.midori.set_tooltip_text(format(SetToolTip('midori', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['minitube']):
            Img.minitube_img.set_from_file(yes)
            Menu3.minitube.set_tooltip_text(format(SetToolTip('minitube', action.installed, action.remove_it)))
        else:
            Img.minitube_img.set_from_file(no)
            Menu3.minitube.set_tooltip_text(format(SetToolTip('minitube', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['opera']):
            Img.opera_img.set_from_file(yes)
            Menu3.opera.set_tooltip_text(format(SetToolTip('opera', action.installed, action.remove_it)))
        else:
            Img.opera_img.set_from_file(no)
            Menu3.opera.set_tooltip_text(format(SetToolTip('opera', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['pidgin']):
            Img.pidgin_img.set_from_file(yes)
            Menu3.pidgin.set_tooltip_text(format(SetToolTip('pidgin', action.installed, action.remove_it)))
        else:
            Img.pidgin_img.set_from_file(no)
            Menu3.pidgin.set_tooltip_text(format(SetToolTip('pidgin', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['skype']):
            Img.skype_img.set_from_file(yes)
            Menu3.skyp.set_tooltip_text(format(SetToolTip('skype', action.installed, action.remove_it)))
        else:
            Img.skype_img.set_from_file(no)
            Menu3.skyp.set_tooltip_text(format(SetToolTip('skype', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['steam']):
            Img.steam_img.set_from_file(yes)
            Menu3.steam.set_tooltip_text(format(SetToolTip('steam', action.installed, action.remove_it)))
        else:
            Img.steam_img.set_from_file(no)
            Menu3.steam.set_tooltip_text(format(SetToolTip('steam', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['thunderbird']):
            Img.thunderbird_img.set_from_file(yes)
            Menu3.thunderbird.set_tooltip_text(format(SetToolTip('thunderbird', action.installed, action.remove_it)))
        else:
            Img.thunderbird_img.set_from_file(no)
            Menu3.thunderbird.set_tooltip_text(format(SetToolTip('thunderbird', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['transmission-gtk']):
            Img.transmission_img.set_from_file(yes)
            Menu3.transmission.set_tooltip_text(format(SetToolTip('transmission', action.installed, action.remove_it)))
        else:
            Img.transmission_img.set_from_file(no)
            Menu3.transmission.set_tooltip_text(format(SetToolTip('transmission', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['linuxdcpp']):
            Img.linuxdcpp_img.set_from_file(yes)
            Menu3.linuxdcpp.set_tooltip_text(format(SetToolTip('linuxdcpp', action.installed, action.remove_it)))
        else:
            Img.linuxdcpp_img.set_from_file(no)
            Menu3.linuxdcpp.set_tooltip_text(format(SetToolTip('linuxdcpp', action.not_here, action.install_it)))