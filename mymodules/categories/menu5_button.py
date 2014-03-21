import os
from mymodules.action.find_program import Find
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.dial import SetToolTip, action

class Menu5:
    # get menu 5 application buttons
    gparted = Builder.builder6.get_object("gparted")
    guake = Builder.builder6.get_object("guake")
    hardinfo = Builder.builder6.get_object("hardinfo")
    htop = Builder.builder6.get_object("htop")
    keepassx = Builder.builder6.get_object("keepassx")
    playonlinux = Builder.builder6.get_object("playonlinux")
    terminator = Builder.builder6.get_object("terminator")
    thunar = Builder.builder6.get_object("thunar")
    truecrypt = Builder.builder6.get_object("truecrypt")
    unetbootin = Builder.builder6.get_object("unetbootin")
    virtualbox = Builder.builder6.get_object("virtualbox")
    wine = Builder.builder6.get_object("wine")
    wireshark = Builder.builder6.get_object("wireshark")
    xbmc = Builder.builder6.get_object("xbmc")
    gufw = Builder.builder6.get_object("gufw")
    octopi = Builder.builder6.get_object("octopi")
    pamac = Builder.builder6.get_object("pamac")
    gnome_system_monitor = Builder.builder6.get_object("gnome_system_monitor")
    # add tooltip for each application icon
    gparted_icon_tooltip = Builder.builder6.get_object("gparted_icon_tooltip")
    gparted_icon_tooltip.set_tooltip_text("GParted is a free partition editor for graphically managing your disk partitions. ")
    guake_icon_tooltip = Builder.builder6.get_object("guake_icon_tooltip")
    guake_icon_tooltip.set_tooltip_text("Guake is a drop-down terminal.")
    hardinfo_icon_tooltip = Builder.builder6.get_object("hardinfo_icon_tooltip")
    hardinfo_icon_tooltip.set_tooltip_text("Hardinfo provides comprehensive details of your PC's software and hardware and allows you to benchmark its performance.")
    htop_icon_tooltip = Builder.builder6.get_object("htop_icon_tooltip")
    htop_icon_tooltip.set_tooltip_text("Htop is an interactive process viewer.")
    keepassx_icon_tooltip = Builder.builder6.get_object("keepassx_icon_tooltip")
    keepassx_icon_tooltip.set_tooltip_text("KeePassX is an application for people with extremly high demands on secure personal data management.")
    playonlinux_icon_tooltip = Builder.builder6.get_object("playonlinux_icon_tooltip")
    playonlinux_icon_tooltip.set_tooltip_text("PlayOnLinux will allow you to play your favorite games on Linux easily.")
    terminator_icon_tooltip = Builder.builder6.get_object("terminator_icon_tooltip")
    terminator_icon_tooltip.set_tooltip_text(" Terminator is a cross-platform GPL terminal emulator with advanced features not yet found elsewhere.")
    thunar_icon_tooltip = Builder.builder6.get_object("thunar_icon_tooltip")
    thunar_icon_tooltip.set_tooltip_text("Thunar is a file manager.")
    truecrypt_icon_tooltip = Builder.builder6.get_object("truecrypt_icon_tooltip")
    truecrypt_icon_tooltip.set_tooltip_text("TrueCrypt is free open-source disk encryption software.")
    unetbootin_icon_tooltip = Builder.builder6.get_object("unetbootin_icon_tooltip")
    unetbootin_icon_tooltip.set_tooltip_text("UNetbootin allows you to create bootable Live USB drives for GNU/Linux distributions without burning a CD")
    virtualbox_icon_tooltip = Builder.builder6.get_object("virtualbox_icon_tooltip")
    virtualbox_icon_tooltip.set_tooltip_text("VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.\nThe program is similar to Virtual PC.")
    wine_icon_tooltip = Builder.builder6.get_object("wine_icon_tooltip")
    wine_icon_tooltip.set_tooltip_text("Wine is a compatibility layer for running windows applications on GNU/Linux.")
    wireshark_icon_tooltip = Builder.builder6.get_object("wireshark_icon_tooltip")
    wireshark_icon_tooltip.set_tooltip_text("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis,\nsoftware and communications protocol development.")
    xbmc_icon_tooltip = Builder.builder6.get_object("xbmc_icon_tooltip")
    xbmc_icon_tooltip.set_tooltip_text("XBMC Media Center is a free cross-platform media player software and entertainment system application framework.")
    gufw_icon_tooltip = Builder.builder6.get_object("gufw_icon_tooltip")
    gufw_icon_tooltip.set_tooltip_text("One of the easiest firewalls in the world!")
    octopi_icon_tooltip = Builder.builder6.get_object("octopi_icon_tooltip")
    octopi_icon_tooltip.set_tooltip_text("Octopi is a powerful tool to manage (Arch | Manjaro) Linux packages.")
    pamac_icon_tooltip = Builder.builder6.get_object("pamac_icon_tooltip")
    pamac_icon_tooltip.set_tooltip_text("pamac - simple graphical package manager for Manjaro Linux.")
    gnome_system_monitor_icon_tooltip = Builder.builder6.get_object("gnome_system_monitor_icon_tooltip")
    gnome_system_monitor_icon_tooltip.set_tooltip_text("Gnome System Monitor is a GNOME process viewer and system monitor with a nice easy-to-use interface")

    @staticmethod
    def on_button5_clicked():
        Img.image1.set_from_file(action.menu_img_1)
        Img.image2.set_from_file(action.menu_img_2)
        Img.image3.set_from_file(action.menu_img_3)
        Img.image4.set_from_file(action.menu_img_4)
        Img.image5.set_from_file(action.menu_img_55)
        Img.image6.set_from_file(action.menu_img_6)

        # check if those programs are installed and set appropriate sign
        if os.path.isfile(Find.program['gparted']):
            Img.gparted_img.set_from_file(action.gtk_yes)
            Menu5.gparted.set_tooltip_text(format(SetToolTip('gparted', action.installed, action.remove_it)))
        else:
            Img.gparted_img.set_from_file(action.gtk_no)
            Menu5.gparted.set_tooltip_text(format(SetToolTip('gparted', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['guake']):
            Img.guake_img.set_from_file(action.gtk_yes)
            Menu5.guake.set_tooltip_text(format(SetToolTip('guake', action.installed, action.remove_it)))
        else:
            Img.guake_img.set_from_file(action.gtk_no)
            Menu5.guake.set_tooltip_text(format(SetToolTip('guake', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['hardinfo']):
            Img.hardinfo_img.set_from_file(action.gtk_yes)
            Menu5.hardinfo.set_tooltip_text(format(SetToolTip('hardinfo', action.installed, action.remove_it)))
        else:
            Img.hardinfo_img.set_from_file(action.gtk_no)
            Menu5.hardinfo.set_tooltip_text(format(SetToolTip('hardinfo', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['htop']):
            Img.htop_img.set_from_file(action.gtk_yes)
            Menu5.htop.set_tooltip_text(format(SetToolTip('htop', action.installed, action.remove_it)))
        else:
            Img.htop_img.set_from_file(action.gtk_no)
            Menu5.htop.set_tooltip_text(format(SetToolTip('htop', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['keepassx']):
            Img.keepassx_img.set_from_file(action.gtk_yes)
            Menu5.keepassx.set_tooltip_text(format(SetToolTip('keepassx', action.installed, action.remove_it)))
        else:
            Img.keepassx_img.set_from_file(action.gtk_no)
            Menu5.keepassx.set_tooltip_text(format(SetToolTip('keepassx', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['playonlinux']):
            Img.playonlinux_img.set_from_file(action.gtk_yes)
            Menu5.playonlinux.set_tooltip_text(format(SetToolTip('playonlinux', action.installed, action.remove_it)))
        else:
            Img.playonlinux_img.set_from_file(action.gtk_no)
            Menu5.playonlinux.set_tooltip_text(format(SetToolTip('playonlinux', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['terminator']):
            Img.terminator_img.set_from_file(action.gtk_yes)
            Menu5.terminator.set_tooltip_text(format(SetToolTip('terminator', action.installed, action.remove_it)))
        else:
            Img.terminator_img.set_from_file(action.gtk_no)
            Menu5.terminator.set_tooltip_text(format(SetToolTip('terminator', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['thunar']):
            Img.thunar_img.set_from_file(action.gtk_yes)
            Menu5.thunar.set_tooltip_text(format(SetToolTip('thunar', action.installed, action.remove_it)))
        else:
            Img.thunar_img.set_from_file(action.gtk_no)
            Menu5.thunar.set_tooltip_text(format(SetToolTip('thunar', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['truecrypt']):
            Img.truecrypt_img.set_from_file(action.gtk_yes)
            Menu5.truecrypt.set_tooltip_text(format(SetToolTip('truecrypt', action.installed, action.remove_it)))
        else:
            Img.truecrypt_img.set_from_file(action.gtk_no)
            Menu5.truecrypt.set_tooltip_text(format(SetToolTip('truecrypt', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['unetbootin']):
            Img.unetbootin_img.set_from_file(action.gtk_yes)
            Menu5.unetbootin.set_tooltip_text(format(SetToolTip('unetbootin', action.installed, action.remove_it)))
        else:
            Img.unetbootin_img.set_from_file(action.gtk_no)
            Menu5.unetbootin.set_tooltip_text(format(SetToolTip('unetbootin', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['virtualbox']):
            Img.virtualbox_img.set_from_file(action.gtk_yes)
            Menu5.virtualbox.set_tooltip_text(format(SetToolTip('virtualbox', action.installed, action.remove_it)))
        else:
            Img.virtualbox_img.set_from_file(action.gtk_no)
            Menu5.virtualbox.set_tooltip_text(format(SetToolTip('virtualbox', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['wine']):
            Img.wine_img.set_from_file(action.gtk_yes)
            Menu5.wine.set_tooltip_text(format(SetToolTip('wine', action.installed, action.remove_it)))
        else:
            Img.wine_img.set_from_file(action.gtk_no)
            Menu5.wine.set_tooltip_text(format(SetToolTip('wine', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['wireshark-gtk']):
            Img.wireshark_img.set_from_file(action.gtk_yes)
            Menu5.wireshark.set_tooltip_text(format(SetToolTip('wireshark', action.installed, action.remove_it)))
        else:
            Img.wireshark_img.set_from_file(action.gtk_no)
            Menu5.wireshark.set_tooltip_text(format(SetToolTip('wireshark', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['xbmc']):
            Img.xbmc_img.set_from_file(action.gtk_yes)
            Menu5.xbmc.set_tooltip_text(format(SetToolTip('xbmc', action.installed, action.remove_it)))
        else:
            Img.xbmc_img.set_from_file(action.gtk_no)
            Menu5.xbmc.set_tooltip_text(format(SetToolTip('xbmc', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['gufw']):
            Img.gufw_img.set_from_file(action.gtk_yes)
            Menu5.gufw.set_tooltip_text(format(SetToolTip('gufw', action.installed, action.remove_it)))
        else:
            Img.gufw_img.set_from_file(action.gtk_no)
            Menu5.gufw.set_tooltip_text(format(SetToolTip('gufw', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['octopi']):
            Img.octopi_img.set_from_file(action.gtk_yes)
            Menu5.octopi.set_tooltip_text(format(SetToolTip('octopi', action.installed, action.remove_it)))
        else:
            Img.octopi_img.set_from_file(action.gtk_no)
            Menu5.octopi.set_tooltip_text(format(SetToolTip('octopi', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['pamac']):
            Img.pamac_img.set_from_file(action.gtk_yes)
            Menu5.pamac.set_tooltip_text(format(SetToolTip('pamac', action.installed, action.remove_it)))
        else:
            Img.pamac_img.set_from_file(action.gtk_no)
            Menu5.pamac.set_tooltip_text(format(SetToolTip('pamac', action.installed, action.remove_it)))

        if os.path.isfile(Find.program['gnome-system-monitor']):
            Img.gnome_system_monitor_img.set_from_file(action.gtk_yes)
            Menu5.gnome_system_monitor.set_tooltip_text(format(SetToolTip('Gnome system monitor', action.installed, action.remove_it)))
        else:
            Img.gnome_system_monitor_img.set_from_file(action.gtk_no)
            Menu5.gnome_system_monitor.set_tooltip_text(format(SetToolTip('Gnome system monitor', action.not_here, action.install_it)))