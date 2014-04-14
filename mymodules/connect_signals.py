from mymodules.builder import Builder
from mymodules.action.on_program_clicked import OPC
from mymodules.action.OPC_related.apply_decoration import StartKickingSomeNinjas
from mymodules.categories.menu7_button import Menu7
from mymodules.categories.menu6_button import Menu6
from mymodules.categories.menu5_button import Menu5
from mymodules.categories.menu4_button import Menu4
from mymodules.categories.menu3_button import Menu3
from mymodules.categories.menu2_button import Menu2
from mymodules.categories.menu1_button import Menu1

class InitConnectMeSignals:
    def __init__(self):
        ninja = StartKickingSomeNinjas
        Builder.builder.connect_signals(self)

        m7 = 'Menu7'
        # connect "clicked" signal to those Menu7 buttons
        Menu7.geany_.connect("clicked", ninja, 'geany', m7)
        Menu7.blender_.connect("clicked", ninja, 'blender', m7)
        Menu7.ninja_ide_.connect("clicked", ninja, 'ninja-ide', m7)
        Menu7.glade_.connect("clicked", ninja, 'glade', m7)
        Menu7.audacious_.connect("clicked", ninja, 'audacious', m7)
        Menu7.gimp_.connect("clicked", ninja, 'gimp', m7)
        Menu7.evince_.connect("clicked", ninja, 'evince', m7)
        Menu7.xfburn_.connect("clicked", ninja, 'xfburn', m7)
        Menu7.flashplayer_.connect("clicked", ninja, 'flashplugin', m7)
        Menu7.openshot_.connect("clicked", ninja, 'openshot', m7)
        Menu7.chromium_.connect("clicked", ninja, 'chromium', m7)
        Menu7.deluge_.connect("clicked", ninja, 'deluge', m7)
        Menu7.liferea_.connect("clicked", ninja, 'liferea', m7)
        Menu7.htop_.connect("clicked", ninja, 'htop', m7)
        Menu7.skype_.connect("clicked", ninja, 'skype', m7)
        Menu7.wireshark_.connect("clicked", ninja, 'wireshark', m7)
        Menu7.virtualbox_.connect("clicked", ninja, 'virtualbox', m7)
        Menu7.steam_.connect("clicked", ninja, 'steam', m7)
        Menu7.xchat_.connect("clicked", ninja, 'xchat', m7)
        Menu7.gedit_.connect("clicked", ninja, 'gedit', m7)

        m6 = 'Menu6'
        # connect "clicked" signal to those Menu6 buttons
        Menu6.docky.connect("clicked", ninja, 'docky', m6)
        Menu6.emacs.connect("clicked", ninja, 'emacs', m6)
        Menu6.vim.connect("clicked", ninja, 'vim', m6)
        Menu6.galculator.connect("clicked", ninja, 'galculator', m6)
        Menu6.gedit.connect("clicked", ninja, 'gedit', m6)
        Menu6.gloobus.connect("clicked", ninja, 'gloobus', m6)
        Menu6.leafpad.connect("clicked", ninja, 'leafpad', m6)
        Menu6.scribes.connect("clicked", ninja, 'scribes', m6)
        Menu6.tomboy.connect("clicked", ninja, 'tomboy', m6)
        Menu6.tuxcards.connect("clicked", ninja, 'tuxcards', m6)
        Menu6.imagewriter.connect("clicked", ninja, 'imagewriter', m6)
        Menu6.sevenzip.connect("clicked", OPC.on_sevenzip_clicked)

        m5 = 'Menu5'
        # connect "clicked" signal to those Menu5 buttons
        Menu5.gparted.connect("clicked", ninja, 'gparted', m5)
        Menu5.guake.connect("clicked", ninja, 'guake', m5)
        Menu5.hardinfo.connect("clicked", ninja, 'hardinfo', m5)
        Menu5.htop.connect("clicked", ninja, 'htop', m5)
        Menu5.keepassx.connect("clicked", ninja, 'keepassx', m5)
        Menu5.playonlinux.connect("clicked", ninja, 'playonlinux', m5)
        Menu5.terminator.connect("clicked", ninja, 'terminator', m5)
        Menu5.thunar.connect("clicked", ninja, 'thunar', m5)
        Menu5.truecrypt.connect("clicked", ninja, 'truecrypt', m5)
        Menu5.unetbootin.connect("clicked", ninja, 'unetbootin', m5)
        Menu5.virtualbox.connect("clicked", ninja, 'virtualbox', m5)
        Menu5.wine.connect("clicked", ninja, 'wine', m5)
        Menu5.wireshark.connect("clicked", ninja, 'wireshark', m5)
        Menu5.xbmc.connect("clicked", ninja, 'xbmc', m5)
        Menu5.gufw.connect("clicked", ninja, 'gufw', m5)
        Menu5.octopi.connect("clicked", ninja, 'octopi', m5)
        Menu5.pamac.connect("clicked", ninja, 'pamac', m5)
        Menu5.gnome_system_monitor.connect("clicked", ninja, 'gnome-system-monitor', m5)

        m4 = 'Menu4'
        # connect "clicked" signal to those Menu4 buttons
        Menu4.amarok.connect("clicked", ninja, 'amarok', m4)
        Menu4.audacious.connect("clicked", ninja, 'audacious', m4)
        Menu4.banshee.connect("clicked", ninja, 'banshee', m4)
        Menu4.cheese.connect("clicked", ninja, 'cheese', m4)
        Menu4.clementine.connect("clicked", ninja, 'clementine', m4)
        Menu4.flashplayer.connect("clicked", ninja, 'flashplugin', m4)
        Menu4.recordmydesktop.connect("clicked", ninja, 'gtk-recordmydesktop', m4)
        Menu4.guayadeque.connect("clicked", ninja, 'guayadeque', m4)
        Menu4.mplayer.connect("clicked", ninja, 'mplayer', m4)
        Menu4.openshot.connect("clicked", ninja, 'openshot', m4)
        Menu4.pitivi.connect("clicked", ninja, 'pitivi', m4)
        Menu4.rhythmbox.connect("clicked", ninja, 'rhythmbox', m4)
        Menu4.soundconverter.connect("clicked", ninja, 'soundconverter', m4)
        Menu4.totem.connect("clicked", ninja, 'totem', m4)
        Menu4.vlc.connect("clicked", ninja, 'vlc', m4)
        Menu4.winff.connect("clicked", ninja, 'winff', m4)
        Menu4.xfburn.connect("clicked", ninja, 'xfburn', m4)
        Menu4.kdenlive.connect("clicked", ninja, 'kdenlive', m4)
        Menu4.simplescreenrecorder.connect("clicked", ninja, 'simplescreenrecorder', m4)
        Menu4.vokoscreen.connect("clicked", ninja, 'vokoscreen', m4)

        m3 = 'Menu3'
        # connect "clicked" signal to those Menu3 buttons
        Menu3.chromium.connect("clicked", ninja, 'chromium', m3)
        Menu3.deluge.connect("clicked", ninja, 'deluge', m3)
        Menu3.evolution.connect("clicked", ninja, 'evolution', m3)
        Menu3.filezilla.connect("clicked", ninja, 'filezilla', m3)
        Menu3.firefox.connect("clicked", ninja, 'firefox', m3)
        Menu3.chrome.connect("clicked", ninja, 'google-chrome', m3)
        Menu3.xchat.connect("clicked", ninja, 'xchat', m3)
        Menu3.liferea.connect("clicked", ninja, 'liferea', m3)
        Menu3.midori.connect("clicked", ninja, 'midori', m3)
        Menu3.minitube.connect("clicked", ninja, 'minitube', m3)
        Menu3.opera.connect("clicked", ninja, 'opera', m3)
        Menu3.pidgin.connect("clicked", ninja, 'pidgin', m3)
        Menu3.skyp.connect("clicked", ninja, 'skype', m3)
        Menu3.steam.connect("clicked", ninja, 'steam', m3)
        Menu3.thunderbird.connect("clicked", ninja, 'thunderbird', m3)
        Menu3.transmission.connect("clicked", ninja, 'transmission', m3)
        Menu3.linuxdcpp.connect("clicked", ninja, 'linuxdcpp', m3)

        m2 = 'Menu2'
        # connect "clicked" signal to those Menu2 buttons
        Menu2.evince.connect("clicked", ninja, 'evince', m2)
        Menu2.f_spot.connect("clicked", ninja, 'f-spot', m2)
        Menu2.gimp.connect("clicked", ninja, 'gimp', m2)
        Menu2.gwenview.connect("clicked", ninja, 'gwenview', m2)
        Menu2.imagemagick.connect("clicked", OPC.on_imagemagick_clicked)
        Menu2.inkscape.connect("clicked", ninja, 'inkscape', m2)
        Menu2.mypaint.connect("clicked", ninja, 'mypaint', m2)
        Menu2.pinta.connect("clicked", ninja, 'pinta', m2)
        Menu2.shotwell.connect("clicked", ninja, 'shotwell', m2)
        Menu2.stellarium.connect("clicked", ninja, 'stellarium', m2)

        m1 = 'Menu1'
        # connect "clicked" signal to those Menu1 buttons
        Menu1.anjuta.connect("clicked", ninja, 'anjuta', m1)
        Menu1.blender.connect("clicked", ninja, 'blender', m1)
        Menu1.bluefish.connect("clicked", ninja, 'bluefish', m1)
        Menu1.eclipse.connect("clicked", ninja, 'eclipse', m1)
        Menu1.geany.connect("clicked", ninja, 'geany', m1)
        Menu1.glade.connect("clicked", ninja, 'glade', m1)
        Menu1.openjdk.connect("clicked", OPC.on_openjdk_clicked, m1)
        Menu1.meld.connect("clicked", ninja, 'meld', m1)
        Menu1.netbeans.connect("clicked", ninja, 'netbeans', m1)
        Menu1.qt4.connect("clicked", ninja, 'qt4', m1)
        Menu1.qt5.connect("clicked", ninja, 'qt5-base', m1)
        Menu1.qtcreator.connect("clicked", ninja, 'qtcreator', m1)
        Menu1.ninja_ide.connect("clicked", ninja, 'ninja-ide', m1)