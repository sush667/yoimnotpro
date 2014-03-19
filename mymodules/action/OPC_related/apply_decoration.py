import os
from mymodules.action.find_program import Find as find
from mymodules.buttons_images import Img
from mymodules.action.dial import dial
from mymodules.categories.menu7_button import Menu7
from mymodules.categories.menu6_button import Menu6
from mymodules.categories.menu5_button import Menu5
from mymodules.categories.menu4_button import Menu4
from mymodules.categories.menu3_button import Menu3
from mymodules.categories.menu2_button import Menu2
from mymodules.categories.menu1_button import Menu1 

class StartKickingSomeNinjas:

    def __init__(batman, and_robin):
        batman.and_robin = and_robin.split('_')[1]
        # if robin.has_spare_motorbike:
            #
        not_here = 'not installed'
        install_it = 'install'
        remove_it = 'remove'
        installed = 'installed'
        if batman.and_robin == 'flashplayer':
            batman.and_robin = 'flashplugin'
        if batman.and_robin == 'ninja':
            batman.and_robin = 'ninja-ide'
        if batman.and_robin == 'wireshark':
            batman.and_robin = 'wireshark-gtk'
        if batman.and_robin == 'f_spot':
            batman.and_robin = 'f-spot'
        if batman.and_robin == 'qt5':
            batman.and_robin = 'qt5-base'
        if batman.and_robin == 'chrome':
            batman.and_robin = 'google-chrome'
        if batman.and_robin == 'recordmydesktop':
            batman.and_robin = 'gtk-recordmydesktop'
        if batman.and_robin == 'gnome':
            batman.and_robin = 'gnome-system-monitor'
        if batman.and_robin == 'gloobus':
            batman.and_robin = 'gloobus-preview'
        if batman.and_robin == 'transmission':
            batman.and_robin = 'transmission-gtk'
        if os.path.isfile(find.program['{name}'.format(name=batman.and_robin)]):
            os.system('pacman -R {program} --noconfirm'.format(program=batman.and_robin))
            if not os.path.isfile(find.program['{name}'.format(name=batman.and_robin)]):
                gtk_img = "gtk-no.png"
                if batman.and_robin == 'geany':
                    Img.geany__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.geany_.set_tooltip_text("Geany is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.geany_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.geany.set_tooltip_text("Geany is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'blender':
                    Img.blender__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.blender_.set_tooltip_text("Blender is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.blender_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.blender.set_tooltip_text("Blender is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'flashplugin':
                    Img.flashplayer__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.flashplayer_.set_tooltip_text("Flashplayer is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.flashplayer_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.flashplayer.set_tooltip_text("Flashplayer is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('Adobe Flashplayer', remove_it)
                    return None
                if batman.and_robin == 'ninja-ide':
                    Img.ninja_ide_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.ninja_ide.set_tooltip_text("Ninja-IDE is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.ninja_ide__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.ninja_ide_.set_tooltip_text("Ninja-IDE is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('Ninja-IDE', remove_it)
                    return None
                if batman.and_robin == 'wireshark-gtk':
                    Img.wireshark__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.wireshark_.set_tooltip_text("Wireshark is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.wireshark_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.wireshark.set_tooltip_text("Wireshark is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('Wireshark', remove_it)
                    return None
                if batman.and_robin == 'f-spot':
                    Img.f_spot_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.f_spot.set_tooltip_text("F-spot is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('F-spot', remove_it)
                    return None
                if batman.and_robin == 'qt5-base':
                    Img.qt5_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.qt5.set_tooltip_text("Qt5 is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('Qt5', remove_it)
                    return None
                if batman.and_robin == 'google-chrome':
                    Img.chrome_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.chrome.set_tooltip_text("Google Chrome is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('Google Chrome', remove_it)
                    return None
                if batman.and_robin == 'gnome-system-monitor':
                    Img.gnome_system_monitor_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.gnome_system_monitor.set_tooltip_text("Gnome system monitor is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('Gnome System Monitor', remove_it)
                    return None
                if batman.and_robin == 'gloobus-preview':
                    Img.gloobus_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.gloobus.set_tooltip_text("Gloobus is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('Gloobus', remove_it)
                    return None
                if batman.and_robin == 'transmission-gtk':
                    Img.transmission_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.transmission.set_tooltip_text("Transmission is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('Transmission', remove_it)
                    return None
                if batman.and_robin == 'gtk-recordmydesktop':
                    Img.recordmydesktop_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.recordmydesktop.set_tooltip_text("RecordMyDesktop is {0}.\nClick to {1} it.".format(not_here, install_it))
                    dial('RecordMyDesktop', remove_it)
                    return None
                if batman.and_robin == 'deluge':
                    Img.deluge__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.deluge_.set_tooltip_text("Deluge is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.deluge_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.deluge.set_tooltip_text("Deluge is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'glade':
                    Img.glade__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.glade_.set_tooltip_text("Glade is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.glade_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.glade.set_tooltip_text("Glade is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'audacious':
                    Img.audacious__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.audacious_.set_tooltip_text("Audacious is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.audacious_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.audacious.set_tooltip_text("Audacious is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'gimp':
                    Img.gimp__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.gimp_.set_tooltip_text("Gimp is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.gimp_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.gimp.set_tooltip_text("GIMP is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'evince':
                    Img.evince__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.evince_.set_tooltip_text("Evince is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.evince_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.evince.set_tooltip_text("Evince is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'xfburn':
                    Img.xfburn__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.xfburn_.set_tooltip_text("Xfburn is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.xfburn_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.xfburn.set_tooltip_text("Xfburn is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'chromium':
                    Img.chromium__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.chromium_.set_tooltip_text("Chromium is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.chromium_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.chromium.set_tooltip_text("Chromium is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'openshot':
                    Img.openshot__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.openshot_.set_tooltip_text("Openshot is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.openshot_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.openshot.set_tooltip_text("Openshot is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'liferea':
                    Img.liferea__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.liferea_.set_tooltip_text("Liferea is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.liferea_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.liferea.set_tooltip_text("Liferea is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'htop':
                    Img.htop__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.htop_.set_tooltip_text("Htop is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.htop_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.htop.set_tooltip_text("Htop is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin in ['skype', 'skyp']:
                    Img.skype__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.skype_.set_tooltip_text("Skype is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.skype_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.skyp.set_tooltip_text("Skype is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'virtualbox':
                    Img.virtualbox__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.virtualbox_.set_tooltip_text("Virtualbox is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.virtualbox_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.virtualbox.set_tooltip_text("Virtualbox is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'steam':
                    Img.steam__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.steam_.set_tooltip_text("Steam is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.steam_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.steam.set_tooltip_text("Steam is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'xchat':
                    Img.xchat__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.xchat_.set_tooltip_text("Xchat is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.xchat_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.xchat.set_tooltip_text("Xchat is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'gedit':
                    Img.gedit__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.gedit_.set_tooltip_text("Gedit is {0}.\nClick to {1} it.".format(not_here, install_it))
                    Img.gedit_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.gedit.set_tooltip_text("Gedit is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'docky':
                    Img.docky_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.docky.set_tooltip_text("Docky is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'emacs':
                    Img.emacs_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.emacs.set_tooltip_text("Emacs is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'vim':
                    Img.vim_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.vim.set_tooltip_text("Vim is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'leafpad':
                    Img.leafpad_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.leafpad.set_tooltip_text("Leafpad is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'scribes':
                    Img.scribes_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.scribes.set_tooltip_text("Scribes is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'tomboy':
                    Img.tomboy_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.tomboy.set_tooltip_text("Tomboy is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'tuxcards':
                    Img.tuxcards_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.tuxcards.set_tooltip_text("Tuxcards is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'imagewriter':
                    Img.imagewriter_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.imagewriter.set_tooltip_text("Imagewriter is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'gparted':
                    Img.gparted_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.gparted.set_tooltip_text("Gparted is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'guake':
                    Img.guake_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.guake.set_tooltip_text("Guake is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'hardinfo':
                    Img.hardinfo_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.hardinfo.set_tooltip_text("Hardinfo is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'keepassx':
                    Img.keepassx_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.keepassx.set_tooltip_text("Keepassx is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'playonlinux':
                    Img.playonlinux_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.playonlinux.set_tooltip_text("Playonlinux is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'terminator':
                    Img.terminator_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.terminator.set_tooltip_text("Terminato is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'thunar':
                    Img.thunar_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.thunar.set_tooltip_text("Thunar is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'truecrypt':
                    Img.truecrypt_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.truecrypt.set_tooltip_text("Truecrypt is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'unetbootin':
                    Img.unetbootin_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.unetbootin.set_tooltip_text("Unetbootin is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'wine':
                    Img.wine_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.wine.set_tooltip_text("Wine is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'xbmc':
                    Img.xbmc_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.xbmc.set_tooltip_text("XBMC is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'gufw':
                    Img.gufw_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.gufw.set_tooltip_text("Gufw is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'octopi':
                    Img.octopi_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.octopi.set_tooltip_text("Octopi is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'pamac':
                    Img.pamac_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.pamac.set_tooltip_text("Pamac is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'amarok':
                    Img.amarok_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.amarok.set_tooltip_text("Amarok is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'banshee':
                    Img.banshee_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.banshee.set_tooltip_text("Banshee is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'cheese':
                    Img.cheese_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.cheese.set_tooltip_text("Cheese is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'clementine':
                    Img.clementine_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.clementine.set_tooltip_text("Clementine is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'guayadeque':
                    Img.guayadeque_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.guayadeque.set_tooltip_text("Guayadeque is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'mplayer':
                    Img.mplayer_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.mplayer.set_tooltip_text("Mplayer is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'pitivi':
                    Img.pitivi_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.pitivi.set_tooltip_text("PiTiVi is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'rhythmbox':
                    Img.rhythmbox_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.rhythmbox.set_tooltip_text("Rhythmbox is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'soundconverter':
                    Img.soundconverter_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.soundconverter.set_tooltip_text("Soundconverter is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'totem':
                    Img.totem_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.totem.set_tooltip_text("Totem is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'vlc':
                    Img.vlc_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.vlc.set_tooltip_text("Vlc is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'winff':
                    Img.winff_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.winff.set_tooltip_text("Winff is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'kdenlive':
                    Img.kdenlive_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.kdenlive.set_tooltip_text("Kdenlive is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'simplescreenrecorder':
                    Img.simplescreenrecorder_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.simplescreenrecorder.set_tooltip_text("Simple screen recorder is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'vokoscreen':
                    Img.vokoscreen_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.vokoscreen.set_tooltip_text("Vokoscreen is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'linuxdcpp':
                    Img.linuxdcpp_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.linuxdcpp.set_tooltip_text("Linuxdcpp is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'evolution':
                    Img.evolution_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.evolution.set_tooltip_text("Evolution is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'filezilla':
                    Img.filezilla_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.filezilla.set_tooltip_text("Filezilla is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'firefox':
                    Img.firefox_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.firefox.set_tooltip_text("Firefox is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'midori':
                    Img.midori_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.midori.set_tooltip_text("Midori is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'minitube':
                    Img.minitube_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.minitube.set_tooltip_text("MiniTube is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'opera':
                    Img.opera_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.opera.set_tooltip_text("Opera is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'pidgin':
                    Img.pidgin_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.pidgin.set_tooltip_text("Pidgin is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'thunderbird':
                    Img.thunderbird_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.thunderbird.set_tooltip_text("Thunderbird is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'gwenview':
                    Img.gwenview_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.gwenview.set_tooltip_text("Gwenview is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'inkscape':
                    Img.inkscape_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.inkscape.set_tooltip_text("Inkscape is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'mypaint':
                    Img.mypaint_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.mypaint.set_tooltip_text("MyPaint is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'pinta':
                    Img.pinta_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.pinta.set_tooltip_text("Pinta is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'shotwell':
                    Img.shotwell_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.shotwell.set_tooltip_text("Shotwell is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'stellarium':
                    Img.stellarium_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.stellarium.set_tooltip_text("Stellarium is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'anjuta':
                    Img.anjuta_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.anjuta.set_tooltip_text("Anjuta is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'bluefish':
                    Img.bluefish_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.bluefish.set_tooltip_text("Bluefish is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'eclipse':
                    Img.eclipse_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.eclipse.set_tooltip_text("Eclipse is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'meld':
                    Img.meld_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.meld.set_tooltip_text("Meld is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'netbeans':
                    Img.netbeans_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.netbeans.set_tooltip_text("NetBeans is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'qt4':
                    Img.qt4_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.qt4.set_tooltip_text("Qt4 is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'qtcreator':
                    Img.qtcreator_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.qtcreator.set_tooltip_text("QtCreator is {0}.\nClick to {1} it.".format(not_here, install_it))
                if batman.and_robin == 'galculator':
                    Img.galculator_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.galculator.set_tooltip_text("Galculator is {0}.\nClick to {1} it.".format(not_here, install_it))
                dial(batman.and_robin.capitalize(), remove_it)
        else:
            os.system('pacman -S {program} --noconfirm'.format(program=batman.and_robin))
            if os.path.isfile(find.program['{name}'.format(name=batman.and_robin)]):
                gtk_img = "gtk-yes.png"
                if batman.and_robin == 'galculator':
                    Img.galculator_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.galculator.set_tooltip_text("Galculator is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'geany':
                    Img.geany__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.geany_.set_tooltip_text("Geany is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.geany_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.geany.set_tooltip_text("Geany is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'blender':
                    Img.blender__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.blender_.set_tooltip_text("Blender is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.blender_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.blender.set_tooltip_text("Blender is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'flashplugin':
                    Img.flashplayer__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.flashplayer_.set_tooltip_text("Flashplayer is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.flashplayer_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.flashplayer.set_tooltip_text("Flashplayer is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('Adobe Flashplayer', installed)
                    return None
                if batman.and_robin == 'ninja-ide':
                    Img.ninja_ide_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.ninja_ide.set_tooltip_text("Ninja-IDE is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.ninja_ide__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.ninja_ide_.set_tooltip_text("Ninja-IDE is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('Ninja-IDE', installed)
                    return None
                if batman.and_robin == 'wireshark-gtk':
                    Img.wireshark__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.wireshark_.set_tooltip_text("Wireshark is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.wireshark_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.wireshark.set_tooltip_text("Wireshark is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('Wireshark', installed)
                    return None
                if batman.and_robin == 'f-spot':
                    Img.f_spot_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.f_spot.set_tooltip_text("F-spot is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('F-spot', installed)
                    return None
                if batman.and_robin == 'qt5-base':
                    Img.qt5_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.qt5.set_tooltip_text("Qt5 is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('Qt5', installed)
                    return None
                if batman.and_robin == 'google-chrome':
                    Img.chrome_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.chrome.set_tooltip_text("Google Chrome is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('Google Chrome', installed)
                    return None
                if batman.and_robin == 'gnome-system-monitor':
                    Img.gnome_system_monitor_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.gnome_system_monitor.set_tooltip_text("Gnome system monitor is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('Gnome System Monitor', installed)
                    return None
                if batman.and_robin == 'gloobus-preview':
                    Img.gloobus_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.gloobus.set_tooltip_text("Gloobus is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('Gloobus', installed)
                    return None
                if batman.and_robin == 'transmission-gtk':
                    Img.transmission_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.transmission.set_tooltip_text("Transmission is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('Transmission', installed)
                    return None
                if batman.and_robin == 'gtk-recordmydesktop':
                    Img.recordmydesktop_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.recordmydesktop.set_tooltip_text("RecordMyDesktop is {0}.\nClick to {1} it.".format(installed, remove_it))
                    dial('RecordMyDesktop', installed)
                    return None
                if batman.and_robin == 'deluge':
                    Img.deluge__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.deluge_.set_tooltip_text("Deluge is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.deluge_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.deluge.set_tooltip_text("Deluge is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'glade':
                    Img.glade__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.glade_.set_tooltip_text("Glade is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.glade_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.glade.set_tooltip_text("Glade is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'audacious':
                    Img.audacious__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.audacious_.set_tooltip_text("Audacious is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.audacious_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.audacious.set_tooltip_text("Audacious is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'gimp':
                    Img.gimp__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.gimp_.set_tooltip_text("Gimp is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.gimp_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.gimp.set_tooltip_text("GIMP is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'evince':
                    Img.evince__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.evince_.set_tooltip_text("Evince is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.evince_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.evince.set_tooltip_text("Evince is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'xfburn':
                    Img.xfburn__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.xfburn_.set_tooltip_text("Xfburn is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.xfburn_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.xfburn.set_tooltip_text("Xfburn is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'chromium':
                    Img.chromium__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.chromium_.set_tooltip_text("Chromium is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.chromium_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.chromium.set_tooltip_text("Chromium is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'openshot':
                    Img.openshot__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.openshot_.set_tooltip_text("Openshot is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.openshot_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.openshot.set_tooltip_text("Openshot is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'liferea':
                    Img.liferea__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.liferea_.set_tooltip_text("Liferea is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.liferea_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.liferea.set_tooltip_text("Liferea is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'htop':
                    Img.htop__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.htop_.set_tooltip_text("Htop is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.htop_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.htop.set_tooltip_text("Htop is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin in ['skype', 'skyp']:
                    Img.skype__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.skype_.set_tooltip_text("Skype is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.skype_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.skyp.set_tooltip_text("Skype is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'virtualbox':
                    Img.virtualbox__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.virtualbox_.set_tooltip_text("Virtualbox is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.virtualbox_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.virtualbox.set_tooltip_text("Virtualbox is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'steam':
                    Img.steam__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.steam_.set_tooltip_text("Steam is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.steam_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.steam.set_tooltip_text("Steam is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'xchat':
                    Img.xchat__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.xchat_.set_tooltip_text("Xchat is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.xchat_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.xchat.set_tooltip_text("Xchat is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'gedit':
                    Img.gedit__img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu7.gedit_.set_tooltip_text("Gedit is {0}.\nClick to {1} it.".format(installed, remove_it))
                    Img.gedit_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.gedit.set_tooltip_text("Gedit is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'docky':
                    Img.docky_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.docky.set_tooltip_text("Docky is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'emacs':
                    Img.emacs_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.emacs.set_tooltip_text("Emacs is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'vim':
                    Img.vim_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.vim.set_tooltip_text("Vim is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'leafpad':
                    Img.leafpad_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.leafpad.set_tooltip_text("Leafpad is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'scribes':
                    Img.scribes_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.scribes.set_tooltip_text("Scribes is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'tomboy':
                    Img.tomboy_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.tomboy.set_tooltip_text("Tomboy is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'tuxcards':
                    Img.tuxcards_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.tuxcards.set_tooltip_text("Tuxcards is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'imagewriter':
                    Img.imagewriter_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu6.imagewriter.set_tooltip_text("Imagewriter is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'gparted':
                    Img.gparted_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.gparted.set_tooltip_text("Gparted is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'guake':
                    Img.guake_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.guake.set_tooltip_text("Guake is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'hardinfo':
                    Img.hardinfo_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.hardinfo.set_tooltip_text("Hardinfo is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'keepassx':
                    Img.keepassx_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.keepassx.set_tooltip_text("Keepassx is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'playonlinux':
                    Img.playonlinux_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.playonlinux.set_tooltip_text("Playonlinux is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'terminator':
                    Img.terminator_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.terminator.set_tooltip_text("Terminato is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'thunar':
                    Img.thunar_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.thunar.set_tooltip_text("Thunar is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'truecrypt':
                    Img.truecrypt_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.truecrypt.set_tooltip_text("Truecrypt is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'unetbootin':
                    Img.unetbootin_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.unetbootin.set_tooltip_text("Unetbootin is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'wine':
                    Img.wine_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.wine.set_tooltip_text("Wine is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'xbmc':
                    Img.xbmc_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.xbmc.set_tooltip_text("XBMC is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'gufw':
                    Img.gufw_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.gufw.set_tooltip_text("Gufw is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'octopi':
                    Img.octopi_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.octopi.set_tooltip_text("Octopi is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'pamac':
                    Img.pamac_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu5.pamac.set_tooltip_text("Pamac is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'amarok':
                    Img.amarok_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.amarok.set_tooltip_text("Amarok is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'banshee':
                    Img.banshee_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.banshee.set_tooltip_text("Banshee is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'cheese':
                    Img.cheese_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.cheese.set_tooltip_text("Cheese is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'clementine':
                    Img.clementine_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.clementine.set_tooltip_text("Clementine is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'guayadeque':
                    Img.guayadeque_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.guayadeque.set_tooltip_text("Guayadeque is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'mplayer':
                    Img.mplayer_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.mplayer.set_tooltip_text("Mplayer is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'pitivi':
                    Img.pitivi_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.pitivi.set_tooltip_text("PiTiVi is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'rhythmbox':
                    Img.rhythmbox_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.rhythmbox.set_tooltip_text("Rhythmbox is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'soundconverter':
                    Img.soundconverter_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.soundconverter.set_tooltip_text("Soundconverter is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'totem':
                    Img.totem_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.totem.set_tooltip_text("Totem is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'vlc':
                    Img.vlc_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.vlc.set_tooltip_text("Vlc is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'winff':
                    Img.winff_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.winff.set_tooltip_text("Winff is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'kdenlive':
                    Img.kdenlive_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.kdenlive.set_tooltip_text("Kdenlive is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'simplescreenrecorder':
                    Img.simplescreenrecorder_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.simplescreenrecorder.set_tooltip_text("Simple screen recorder is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'vokoscreen':
                    Img.vokoscreen_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu4.vokoscreen.set_tooltip_text("Vokoscreen is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'linuxdcpp':
                    Img.linuxdcpp_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.linuxdcpp.set_tooltip_text("Linuxdcpp is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'evolution':
                    Img.evolution_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.evolution.set_tooltip_text("Evolution is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'filezilla':
                    Img.filezilla_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.filezilla.set_tooltip_text("Filezilla is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'firefox':
                    Img.firefox_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.firefox.set_tooltip_text("Firefox is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'midori':
                    Img.midori_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.midori.set_tooltip_text("Midori is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'minitube':
                    Img.minitube_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.minitube.set_tooltip_text("MiniTube is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'opera':
                    Img.opera_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.opera.set_tooltip_text("Opera is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'pidgin':
                    Img.pidgin_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.pidgin.set_tooltip_text("Pidgin is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'thunderbird':
                    Img.thunderbird_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu3.thunderbird.set_tooltip_text("Thunderbird is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'gwenview':
                    Img.gwenview_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.gwenview.set_tooltip_text("Gwenview is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'inkscape':
                    Img.inkscape_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.inkscape.set_tooltip_text("Inkscape is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'mypaint':
                    Img.mypaint_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.mypaint.set_tooltip_text("MyPaint is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'pinta':
                    Img.pinta_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.pinta.set_tooltip_text("Pinta is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'shotwell':
                    Img.shotwell_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.shotwell.set_tooltip_text("Shotwell is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'stellarium':
                    Img.stellarium_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu2.stellarium.set_tooltip_text("Stellarium is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'anjuta':
                    Img.anjuta_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.anjuta.set_tooltip_text("Anjuta is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'bluefish':
                    Img.bluefish_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.bluefish.set_tooltip_text("Bluefish is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'eclipse':
                    Img.eclipse_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.eclipse.set_tooltip_text("Eclipse is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'meld':
                    Img.meld_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.meld.set_tooltip_text("Meld is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'netbeans':
                    Img.netbeans_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.netbeans.set_tooltip_text("NetBeans is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'qt4':
                    Img.qt4_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.qt4.set_tooltip_text("Qt4 is {0}.\nClick to {1} it.".format(installed, remove_it))
                if batman.and_robin == 'qtcreator':
                    Img.qtcreator_img.set_from_file('./categories/{img}'.format(img=gtk_img))
                    Menu1.qtcreator.set_tooltip_text("QtCreator is {0}.\nClick to {1} it.".format(installed, remove_it))
                dial(batman.and_robin.capitalize(), installed)