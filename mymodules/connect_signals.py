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

        # connect "clicked" signal to those Menu7 buttons
        Menu7.geany_.connect("clicked", ninja, 'geany')
        Menu7.blender_.connect("clicked", ninja, 'blender')
        Menu7.ninja_ide_.connect("clicked", ninja, 'ninja-ide')
        Menu7.glade_.connect("clicked", ninja, 'glade')
        Menu7.audacious_.connect("clicked", ninja, 'audacious')
        Menu7.gimp_.connect("clicked", ninja, 'gimp')
        Menu7.evince_.connect("clicked", ninja, 'evince')
        Menu7.xfburn_.connect("clicked", ninja, 'xfburn')
        Menu7.flashplayer_.connect("clicked", ninja, 'flashplugin')
        Menu7.openshot_.connect("clicked", ninja, 'openshot')
        Menu7.chromium_.connect("clicked", ninja, 'chromium')
        Menu7.deluge_.connect("clicked", ninja, 'deluge')
        Menu7.liferea_.connect("clicked", ninja, 'liferea')
        Menu7.htop_.connect("clicked", ninja, 'htop')
        Menu7.skype_.connect("clicked", ninja, 'skype')
        Menu7.wireshark_.connect("clicked", ninja, 'wireshark')
        Menu7.virtualbox_.connect("clicked", ninja, 'virtualbox')
        Menu7.steam_.connect("clicked", ninja, 'steam')
        Menu7.xchat_.connect("clicked", ninja, 'xchat')
        Menu7.gedit_.connect("clicked", ninja, 'gedit')

        # connect "clicked" signal to those Menu6 buttons
        Menu6.docky.connect("clicked", ninja, 'docky')
        Menu6.emacs.connect("clicked", ninja, 'emacs')
        Menu6.vim.connect("clicked", ninja, 'vim')
        Menu6.galculator.connect("clicked", ninja, 'galculator')
        Menu6.gedit.connect("clicked", ninja, 'gedit')
        Menu6.gloobus.connect("clicked", ninja, 'gloobus')
        Menu6.leafpad.connect("clicked", ninja, 'leafpad')
        Menu6.scribes.connect("clicked", ninja, 'scribes')
        Menu6.tomboy.connect("clicked", ninja, 'tomboy')
        Menu6.tuxcards.connect("clicked", ninja, 'tuxcards')
        Menu6.imagewriter.connect("clicked", ninja, 'imagewriter')
        Menu6.sevenzip.connect("clicked", OPC.on_sevenzip_clicked)

        # connect "clicked" signal to those Menu5 buttons
        Menu5.gparted.connect("clicked", ninja, 'gparted')
        Menu5.guake.connect("clicked", ninja, 'guake')
        Menu5.hardinfo.connect("clicked", ninja, 'hardinfo')
        Menu5.htop.connect("clicked", ninja, 'htop')
        Menu5.keepassx.connect("clicked", ninja, 'keepassx')
        Menu5.playonlinux.connect("clicked", ninja, 'playonlinux')
        Menu5.terminator.connect("clicked", ninja, 'terminator')
        Menu5.thunar.connect("clicked", ninja, 'thunar')
        Menu5.truecrypt.connect("clicked", ninja, 'truecrypt')
        Menu5.unetbootin.connect("clicked", ninja, 'unetbootin')
        Menu5.virtualbox.connect("clicked", ninja, 'virtualbox')
        Menu5.wine.connect("clicked", ninja, 'wine')
        Menu5.wireshark.connect("clicked", ninja, 'wireshark')
        Menu5.xbmc.connect("clicked", ninja, 'xbmc')
        Menu5.gufw.connect("clicked", ninja, 'gufw')
        Menu5.octopi.connect("clicked", ninja, 'octopi')
        Menu5.pamac.connect("clicked", ninja, 'pamac')
        Menu5.gnome_system_monitor.connect("clicked", ninja, 'gnome-system-monitor')

        # connect "clicked" signal to those Menu4 buttons
        Menu4.amarok.connect("clicked", ninja, 'amarok')
        Menu4.audacious.connect("clicked", ninja, 'audacious')
        Menu4.banshee.connect("clicked", ninja, 'banshee')
        Menu4.cheese.connect("clicked", ninja, 'cheese')
        Menu4.clementine.connect("clicked", ninja, 'clementine')
        Menu4.flashplayer.connect("clicked", ninja, 'flashplugin')
        Menu4.recordmydesktop.connect("clicked", ninja, 'gtk-recordmydesktop')
        Menu4.guayadeque.connect("clicked", ninja, 'guayadeque')
        Menu4.mplayer.connect("clicked", ninja, 'mplayer')
        Menu4.openshot.connect("clicked", ninja, 'openshot')
        Menu4.pitivi.connect("clicked", ninja, 'pitivi')
        Menu4.rhythmbox.connect("clicked", ninja, 'rhythmbox')
        Menu4.soundconverter.connect("clicked", ninja, 'soundconverter')
        Menu4.totem.connect("clicked", ninja, 'totem')
        Menu4.vlc.connect("clicked", ninja, 'vlc')
        Menu4.winff.connect("clicked", ninja, 'winff')
        Menu4.xfburn.connect("clicked", ninja, 'xfburn')
        Menu4.kdenlive.connect("clicked", ninja, 'kdenlive')
        Menu4.simplescreenrecorder.connect("clicked", ninja, 'simplescreenrecorder')
        Menu4.vokoscreen.connect("clicked", ninja, 'vokoscreen')

        # connect "clicked" signal to those Menu3 buttons
        Menu3.chromium.connect("clicked", ninja, 'chromium')
        Menu3.deluge.connect("clicked", ninja, 'deluge')
        Menu3.evolution.connect("clicked", ninja, 'evolution')
        Menu3.filezilla.connect("clicked", ninja, 'filezilla')
        Menu3.firefox.connect("clicked", ninja, 'firefox')
        Menu3.chrome.connect("clicked", ninja, 'google-chrome')
        Menu3.xchat.connect("clicked", ninja, 'xchat')
        Menu3.liferea.connect("clicked", ninja, 'liferea')
        Menu3.midori.connect("clicked", ninja, 'midori')
        Menu3.minitube.connect("clicked", ninja, 'minitube')
        Menu3.opera.connect("clicked", ninja, 'opera')
        Menu3.pidgin.connect("clicked", ninja, 'pidgin')
        Menu3.skyp.connect("clicked", ninja, 'skype')
        Menu3.steam.connect("clicked", ninja, 'steam')
        Menu3.thunderbird.connect("clicked", ninja, 'thunderbird')
        Menu3.transmission.connect("clicked", ninja, 'transmission')
        Menu3.linuxdcpp.connect("clicked", ninja, 'linuxdcpp')

        # connect "clicked" signal to those Menu2 buttons
        Menu2.evince.connect("clicked", ninja, 'evince')
        Menu2.f_spot.connect("clicked", ninja, 'f-spot')
        Menu2.gimp.connect("clicked", ninja, 'gimp')
        Menu2.gwenview.connect("clicked", ninja, 'gwenview')
        Menu2.imagemagick.connect("clicked", OPC.on_imagemagick_clicked)
        Menu2.inkscape.connect("clicked", ninja, 'inkscape')
        Menu2.mypaint.connect("clicked", ninja, 'mypaint')
        Menu2.pinta.connect("clicked", ninja, 'pinta')
        Menu2.shotwell.connect("clicked", ninja, 'shotwell')
        Menu2.stellarium.connect("clicked", ninja, 'stellarium')

        # connect "clicked" signal to those Menu1 buttons
        Menu1.anjuta.connect("clicked", ninja, 'anjuta')
        Menu1.blender.connect("clicked", ninja, 'blender')
        Menu1.bluefish.connect("clicked", ninja, 'bluefish')
        Menu1.eclipse.connect("clicked", ninja, 'eclipse')
        Menu1.geany.connect("clicked", ninja, 'geany')
        Menu1.glade.connect("clicked", ninja, 'glade')
        Menu1.openjdk.connect("clicked", OPC.on_openjdk_clicked)
        Menu1.meld.connect("clicked", ninja, 'meld')
        Menu1.netbeans.connect("clicked", ninja, 'netbeans')
        Menu1.qt4.connect("clicked", ninja, 'qt4')
        Menu1.qt5.connect("clicked", ninja, 'qt5-base')
        Menu1.qtcreator.connect("clicked", ninja, 'qtcreator')
        Menu1.ninja_ide.connect("clicked", ninja, 'ninja-ide')