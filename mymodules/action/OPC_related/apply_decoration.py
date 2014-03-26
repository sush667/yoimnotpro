import os
from mymodules.action.find_program import Find as find
from mymodules.buttons_images import Img
from mymodules.action.dial import SetToolTip, action, dial
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
        if batman.and_robin == 'flashplayer':
            batman.and_robin = 'flashplugin'
        if batman.and_robin == 'ninja':
            batman.and_robin = 'ninja-ide'
        if batman.and_robin == 'wireshark':
            batman.and_robin = 'wireshark-gtk'
        if batman.and_robin == 'f':
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
                nope = format(SetToolTip(batman.and_robin, action.not_here, action.install_it))
                no = action.gtk_no
                if batman.and_robin == 'geany':
                    Img.geany__img.set_from_file(no)
                    Menu7.geany_.set_tooltip_markup(nope)
                    Img.geany_img.set_from_file(no)
                    Menu1.geany.set_tooltip_markup(nope)
                if batman.and_robin == 'blender':
                    Img.blender__img.set_from_file(no)
                    Menu7.blender_.set_tooltip_markup(nope)
                    Img.blender_img.set_from_file(no)
                    Menu1.blender.set_tooltip_markup(nope)
                if batman.and_robin == 'flashplugin':
                    Img.flashplayer__img.set_from_file(no)
                    Menu7.flashplayer_.set_tooltip_markup(format(SetToolTip('Adobe Flashplayer', action.not_here, action.install_it)))
                    Img.flashplayer_img.set_from_file(no)
                    Menu4.flashplayer.set_tooltip_markup(format(SetToolTip('Adobe Flashplayer', action.not_here, action.install_it)))
                    dial('Adobe Flashplayer', action.remove_it)
                    return None
                if batman.and_robin == 'ninja-ide':
                    Img.ninja_ide_img.set_from_file(no)
                    Menu1.ninja_ide.set_tooltip_markup(format(SetToolTip('Ninja-IDE', action.not_here, action.install_it)))
                    Img.ninja_ide__img.set_from_file(no)
                    Menu7.ninja_ide_.set_tooltip_markup(format(SetToolTip('Ninja-IDE', action.not_here, action.install_it)))
                    dial('Ninja-IDE', action.remove_it)
                    return None
                if batman.and_robin == 'wireshark-gtk':
                    Img.wireshark__img.set_from_file(no)
                    Menu7.wireshark_.set_tooltip_markup(format(SetToolTip('Wireshark', action.not_here, action.install_it)))
                    Img.wireshark_img.set_from_file(no)
                    Menu5.wireshark.set_tooltip_markup(format(SetToolTip('Wireshark', action.not_here, action.install_it)))
                    dial('Wireshark', action.remove_it)
                    return None
                if batman.and_robin == 'f-spot':
                    Img.f_spot_img.set_from_file(no)
                    Menu2.f_spot.set_tooltip_markup(format(SetToolTip('F-spot', action.not_here, action.install_it)))
                    dial('F-spot', action.remove_it)
                    return None
                if batman.and_robin == 'qt5-base':
                    Img.qt5_img.set_from_file(no)
                    Menu1.qt5.set_tooltip_markup(format(SetToolTip('Qt5', action.not_here, action.install_it)))
                    dial('Qt5', action.remove_it)
                    return None
                if batman.and_robin == 'google-chrome':
                    Img.chrome_img.set_from_file(no)
                    Menu3.chrome.set_tooltip_markup(format(SetToolTip('Google Chrome', action.not_here, action.install_it)))
                    dial('Google Chrome', action.remove_it)
                    return None
                if batman.and_robin == 'gnome-system-monitor':
                    Img.gnome_system_monitor_img.set_from_file(no)
                    Menu5.gnome_system_monitor.set_tooltip_markup(format(SetToolTip('Gnome system monitor', action.not_here, action.install_it)))
                    dial('Gnome System Monitor', action.remove_it)
                    return None
                if batman.and_robin == 'gloobus-preview':
                    Img.gloobus_img.set_from_file(no)
                    Menu6.gloobus.set_tooltip_markup(format(SetToolTip('Gloobus', action.not_here, action.install_it)))
                    dial('Gloobus', action.remove_it)
                    return None
                if batman.and_robin == 'transmission-gtk':
                    Img.transmission_img.set_from_file(no)
                    Menu3.transmission.set_tooltip_markup(format(SetToolTip('Transmission', action.not_here, action.install_it)))
                    dial('Transmission', action.remove_it)
                    return None
                if batman.and_robin == 'gtk-recordmydesktop':
                    Img.recordmydesktop_img.set_from_file(no)
                    Menu4.recordmydesktop.set_tooltip_markup(format(SetToolTip('RecordMyDesktop', action.not_here, action.install_it)))
                    dial('RecordMyDesktop', action.remove_it)
                    return None
                if batman.and_robin == 'deluge':
                    Img.deluge__img.set_from_file(no)
                    Menu7.deluge_.set_tooltip_markup(nope)
                    Img.deluge_img.set_from_file(no)
                    Menu3.deluge.set_tooltip_markup(nope)
                if batman.and_robin == 'glade':
                    Img.glade__img.set_from_file(no)
                    Menu7.glade_.set_tooltip_markup(nope)
                    Img.glade_img.set_from_file(no)
                    Menu1.glade.set_tooltip_markup(nope)
                if batman.and_robin == 'audacious':
                    Img.audacious__img.set_from_file(no)
                    Menu7.audacious_.set_tooltip_markup(nope)
                    Img.audacious_img.set_from_file(no)
                    Menu4.audacious.set_tooltip_markup(nope)
                if batman.and_robin == 'gimp':
                    Img.gimp__img.set_from_file(no)
                    Menu7.gimp_.set_tooltip_markup(nope)
                    Img.gimp_img.set_from_file(no)
                    Menu2.gimp.set_tooltip_markup(nope)
                if batman.and_robin == 'evince':
                    Img.evince__img.set_from_file(no)
                    Menu7.evince_.set_tooltip_markup(nope)
                    Img.evince_img.set_from_file(no)
                    Menu2.evince.set_tooltip_markup(nope)
                if batman.and_robin == 'xfburn':
                    Img.xfburn__img.set_from_file(no)
                    Menu7.xfburn_.set_tooltip_markup(nope)
                    Img.xfburn_img.set_from_file(no)
                    Menu4.xfburn.set_tooltip_markup(nope)
                if batman.and_robin == 'chromium':
                    Img.chromium__img.set_from_file(no)
                    Menu7.chromium_.set_tooltip_markup(nope)
                    Img.chromium_img.set_from_file(no)
                    Menu3.chromium.set_tooltip_markup(nope)
                if batman.and_robin == 'openshot':
                    Img.openshot__img.set_from_file(no)
                    Menu7.openshot_.set_tooltip_markup(nope)
                    Img.openshot_img.set_from_file(no)
                    Menu4.openshot.set_tooltip_markup(nope)
                if batman.and_robin == 'liferea':
                    Img.liferea__img.set_from_file(no)
                    Menu7.liferea_.set_tooltip_markup(nope)
                    Img.liferea_img.set_from_file(no)
                    Menu3.liferea.set_tooltip_markup(nope)
                if batman.and_robin == 'htop':
                    Img.htop__img.set_from_file(no)
                    Menu7.htop_.set_tooltip_markup(nope)
                    Img.htop_img.set_from_file(no)
                    Menu5.htop.set_tooltip_markup(nope)
                if batman.and_robin in ['skype', 'skyp']:
                    Img.skype__img.set_from_file(no)
                    Menu7.skype_.set_tooltip_markup(nope)
                    Img.skype_img.set_from_file(no)
                    Menu3.skyp.set_tooltip_markup(nope)
                if batman.and_robin == 'virtualbox':
                    Img.virtualbox__img.set_from_file(no)
                    Menu7.virtualbox_.set_tooltip_markup(nope)
                    Img.virtualbox_img.set_from_file(no)
                    Menu5.virtualbox.set_tooltip_markup(nope)
                if batman.and_robin == 'steam':
                    Img.steam__img.set_from_file(no)
                    Menu7.steam_.set_tooltip_markup(nope)
                    Img.steam_img.set_from_file(no)
                    Menu3.steam.set_tooltip_markup(nope)
                if batman.and_robin == 'xchat':
                    Img.xchat__img.set_from_file(no)
                    Menu7.xchat_.set_tooltip_markup(nope)
                    Img.xchat_img.set_from_file(no)
                    Menu3.xchat.set_tooltip_markup(nope)
                if batman.and_robin == 'gedit':
                    Img.gedit__img.set_from_file(no)
                    Menu7.gedit_.set_tooltip_markup(nope)
                    Img.gedit_img.set_from_file(no)
                    Menu6.gedit.set_tooltip_markup(nope)
                if batman.and_robin == 'docky':
                    Img.docky_img.set_from_file(no)
                    Menu6.docky.set_tooltip_markup(nope)
                if batman.and_robin == 'emacs':
                    Img.emacs_img.set_from_file(no)
                    Menu6.emacs.set_tooltip_markup(nope)
                if batman.and_robin == 'vim':
                    Img.vim_img.set_from_file(no)
                    Menu6.vim.set_tooltip_markup(nope)
                if batman.and_robin == 'leafpad':
                    Img.leafpad_img.set_from_file(no)
                    Menu6.leafpad.set_tooltip_markup(nope)
                if batman.and_robin == 'scribes':
                    Img.scribes_img.set_from_file(no)
                    Menu6.scribes.set_tooltip_markup(nope)
                if batman.and_robin == 'tomboy':
                    Img.tomboy_img.set_from_file(no)
                    Menu6.tomboy.set_tooltip_markup(nope)
                if batman.and_robin == 'tuxcards':
                    Img.tuxcards_img.set_from_file(no)
                    Menu6.tuxcards.set_tooltip_markup(nope)
                if batman.and_robin == 'imagewriter':
                    Img.imagewriter_img.set_from_file(no)
                    Menu6.imagewriter.set_tooltip_markup(nope)
                if batman.and_robin == 'gparted':
                    Img.gparted_img.set_from_file(no)
                    Menu5.gparted.set_tooltip_markup(nope)
                if batman.and_robin == 'guake':
                    Img.guake_img.set_from_file(no)
                    Menu5.guake.set_tooltip_markup(nope)
                if batman.and_robin == 'hardinfo':
                    Img.hardinfo_img.set_from_file(no)
                    Menu5.hardinfo.set_tooltip_markup(nope)
                if batman.and_robin == 'keepassx':
                    Img.keepassx_img.set_from_file(no)
                    Menu5.keepassx.set_tooltip_markup(nope)
                if batman.and_robin == 'playonlinux':
                    Img.playonlinux_img.set_from_file(no)
                    Menu5.playonlinux.set_tooltip_markup(nope)
                if batman.and_robin == 'terminator':
                    Img.terminator_img.set_from_file(no)
                    Menu5.terminator.set_tooltip_markup(nope)
                if batman.and_robin == 'thunar':
                    Img.thunar_img.set_from_file(no)
                    Menu5.thunar.set_tooltip_markup(nope)
                if batman.and_robin == 'truecrypt':
                    Img.truecrypt_img.set_from_file(no)
                    Menu5.truecrypt.set_tooltip_markup(nope)
                if batman.and_robin == 'unetbootin':
                    Img.unetbootin_img.set_from_file(no)
                    Menu5.unetbootin.set_tooltip_markup(nope)
                if batman.and_robin == 'wine':
                    Img.wine_img.set_from_file(no)
                    Menu5.wine.set_tooltip_markup(nope)
                if batman.and_robin == 'xbmc':
                    Img.xbmc_img.set_from_file(no)
                    Menu5.xbmc.set_tooltip_markup(nope)
                if batman.and_robin == 'gufw':
                    Img.gufw_img.set_from_file(no)
                    Menu5.gufw.set_tooltip_markup(nope)
                if batman.and_robin == 'octopi':
                    Img.octopi_img.set_from_file(no)
                    Menu5.octopi.set_tooltip_markup(nope)
                if batman.and_robin == 'pamac':
                    Img.pamac_img.set_from_file(no)
                    Menu5.pamac.set_tooltip_markup(nope)
                if batman.and_robin == 'amarok':
                    Img.amarok_img.set_from_file(no)
                    Menu4.amarok.set_tooltip_markup(nope)
                if batman.and_robin == 'banshee':
                    Img.banshee_img.set_from_file(no)
                    Menu4.banshee.set_tooltip_markup(nope)
                if batman.and_robin == 'cheese':
                    Img.cheese_img.set_from_file(no)
                    Menu4.cheese.set_tooltip_markup(nope)
                if batman.and_robin == 'clementine':
                    Img.clementine_img.set_from_file(no)
                    Menu4.clementine.set_tooltip_markup(nope)
                if batman.and_robin == 'guayadeque':
                    Img.guayadeque_img.set_from_file(no)
                    Menu4.guayadeque.set_tooltip_markup(nope)
                if batman.and_robin == 'mplayer':
                    Img.mplayer_img.set_from_file(no)
                    Menu4.mplayer.set_tooltip_markup(nope)
                if batman.and_robin == 'pitivi':
                    Img.pitivi_img.set_from_file(no)
                    Menu4.pitivi.set_tooltip_markup(nope)
                if batman.and_robin == 'rhythmbox':
                    Img.rhythmbox_img.set_from_file(no)
                    Menu4.rhythmbox.set_tooltip_markup(nope)
                if batman.and_robin == 'soundconverter':
                    Img.soundconverter_img.set_from_file(no)
                    Menu4.soundconverter.set_tooltip_markup(nope)
                if batman.and_robin == 'totem':
                    Img.totem_img.set_from_file(no)
                    Menu4.totem.set_tooltip_markup(nope)
                if batman.and_robin == 'vlc':
                    Img.vlc_img.set_from_file(no)
                    Menu4.vlc.set_tooltip_markup(nope)
                if batman.and_robin == 'winff':
                    Img.winff_img.set_from_file(no)
                    Menu4.winff.set_tooltip_markup(nope)
                if batman.and_robin == 'kdenlive':
                    Img.kdenlive_img.set_from_file(no)
                    Menu4.kdenlive.set_tooltip_markup(nope)
                if batman.and_robin == 'simplescreenrecorder':
                    Img.simplescreenrecorder_img.set_from_file(no)
                    Menu4.simplescreenrecorder.set_tooltip_markup(format(SetToolTip('Simple Screen Recorder', action.not_here, action.install_it)))
                if batman.and_robin == 'vokoscreen':
                    Img.vokoscreen_img.set_from_file(no)
                    Menu4.vokoscreen.set_tooltip_markup(nope)
                if batman.and_robin == 'linuxdcpp':
                    Img.linuxdcpp_img.set_from_file(no)
                    Menu3.linuxdcpp.set_tooltip_markup(nope)
                if batman.and_robin == 'evolution':
                    Img.evolution_img.set_from_file(no)
                    Menu3.evolution.set_tooltip_markup(nope)
                if batman.and_robin == 'filezilla':
                    Img.filezilla_img.set_from_file(no)
                    Menu3.filezilla.set_tooltip_markup(nope)
                if batman.and_robin == 'firefox':
                    Img.firefox_img.set_from_file(no)
                    Menu3.firefox.set_tooltip_markup(nope)
                if batman.and_robin == 'midori':
                    Img.midori_img.set_from_file(no)
                    Menu3.midori.set_tooltip_markup(nope)
                if batman.and_robin == 'minitube':
                    Img.minitube_img.set_from_file(no)
                    Menu3.minitube.set_tooltip_markup(nope)
                if batman.and_robin == 'opera':
                    Img.opera_img.set_from_file(no)
                    Menu3.opera.set_tooltip_markup(nope)
                if batman.and_robin == 'pidgin':
                    Img.pidgin_img.set_from_file(no)
                    Menu3.pidgin.set_tooltip_markup(nope)
                if batman.and_robin == 'thunderbird':
                    Img.thunderbird_img.set_from_file(no)
                    Menu3.thunderbird.set_tooltip_markup(nope)
                if batman.and_robin == 'gwenview':
                    Img.gwenview_img.set_from_file(no)
                    Menu2.gwenview.set_tooltip_markup(nope)
                if batman.and_robin == 'inkscape':
                    Img.inkscape_img.set_from_file(no)
                    Menu2.inkscape.set_tooltip_markup(nope)
                if batman.and_robin == 'mypaint':
                    Img.mypaint_img.set_from_file(no)
                    Menu2.mypaint.set_tooltip_markup(nope)
                if batman.and_robin == 'pinta':
                    Img.pinta_img.set_from_file(no)
                    Menu2.pinta.set_tooltip_markup(nope)
                if batman.and_robin == 'shotwell':
                    Img.shotwell_img.set_from_file(no)
                    Menu2.shotwell.set_tooltip_markup(nope)
                if batman.and_robin == 'stellarium':
                    Img.stellarium_img.set_from_file(no)
                    Menu2.stellarium.set_tooltip_markup(nope)
                if batman.and_robin == 'anjuta':
                    Img.anjuta_img.set_from_file(no)
                    Menu1.anjuta.set_tooltip_markup(nope)
                if batman.and_robin == 'bluefish':
                    Img.bluefish_img.set_from_file(no)
                    Menu1.bluefish.set_tooltip_markup(nope)
                if batman.and_robin == 'eclipse':
                    Img.eclipse_img.set_from_file(no)
                    Menu1.eclipse.set_tooltip_markup(nope)
                if batman.and_robin == 'meld':
                    Img.meld_img.set_from_file(no)
                    Menu1.meld.set_tooltip_markup(nope)
                if batman.and_robin == 'netbeans':
                    Img.netbeans_img.set_from_file(no)
                    Menu1.netbeans.set_tooltip_markup(nope)
                if batman.and_robin == 'qt4':
                    Img.qt4_img.set_from_file(no)
                    Menu1.qt4.set_tooltip_markup(nope)
                if batman.and_robin == 'qtcreator':
                    Img.qtcreator_img.set_from_file(no)
                    Menu1.qtcreator.set_tooltip_markup(nope)
                if batman.and_robin == 'galculator':
                    Img.galculator_img.set_from_file(no)
                    Menu6.galculator.set_tooltip_markup(nope)
                dial(batman.and_robin.capitalize(), action.remove_it)
        else:
            os.system('pacman -S {program} --noconfirm'.format(program=batman.and_robin))
            if os.path.isfile(find.program['{name}'.format(name=batman.and_robin)]):
                duh = format(SetToolTip(batman.and_robin, action.installed, action.remove_it))
                yes = action.gtk_yes
                if batman.and_robin == 'galculator':
                    Img.galculator_img.set_from_file(yes)
                    Menu6.galculator.set_tooltip_markup(duh)
                if batman.and_robin == 'geany':
                    Img.geany__img.set_from_file(yes)
                    Menu7.geany_.set_tooltip_markup(duh)
                    Img.geany_img.set_from_file(yes)
                    Menu1.geany.set_tooltip_markup(duh)
                if batman.and_robin == 'blender':
                    Img.blender__img.set_from_file(yes)
                    Menu7.blender_.set_tooltip_markup(duh)
                    Img.blender_img.set_from_file(yes)
                    Menu1.blender.set_tooltip_markup(duh)
                if batman.and_robin == 'flashplugin':
                    Img.flashplayer__img.set_from_file(yes)
                    Menu7.flashplayer_.set_tooltip_markup(format(SetToolTip('Adobe Flashplayer', action.installed, action.remove_it)))
                    Img.flashplayer_img.set_from_file(yes)
                    Menu4.flashplayer.set_tooltip_markup(format(SetToolTip('Adobe Flashplayer', action.installed, action.remove_it)))
                    dial('Adobe Flashplayer', action.installed)
                    return None
                if batman.and_robin == 'ninja-ide':
                    Img.ninja_ide_img.set_from_file(yes)
                    Menu1.ninja_ide.set_tooltip_markup(format(SetToolTip('Ninja-IDE', action.installed, action.remove_it)))
                    Img.ninja_ide__img.set_from_file(yes)
                    Menu7.ninja_ide_.set_tooltip_markup(format(SetToolTip('Ninja-IDE', action.installed, action.remove_it)))
                    dial('Ninja-IDE', action.installed)
                    return None
                if batman.and_robin == 'wireshark-gtk':
                    Img.wireshark__img.set_from_file(yes)
                    Menu7.wireshark_.set_tooltip_markup(format(SetToolTip('Wireshark', action.installed, action.remove_it)))
                    Img.wireshark_img.set_from_file(yes)
                    Menu5.wireshark.set_tooltip_markup(format(SetToolTip('Wireshark', action.installed, action.remove_it)))
                    dial('Wireshark', action.installed)
                    return None
                if batman.and_robin == 'f-spot':
                    Img.f_spot_img.set_from_file(yes)
                    Menu2.f_spot.set_tooltip_markup(format(SetToolTip('F-spot', action.installed, action.remove_it)))
                    dial('F-spot', action.installed)
                    return None
                if batman.and_robin == 'qt5-base':
                    Img.qt5_img.set_from_file(yes)
                    Menu1.qt5.set_tooltip_markup(format(SetToolTip('Qt5', action.installed, action.remove_it)))
                    dial('Qt5', action.installed)
                    return None
                if batman.and_robin == 'google-chrome':
                    Img.chrome_img.set_from_file(yes)
                    Menu3.chrome.set_tooltip_markup(format(SetToolTip('Google Chrome', action.installed, action.remove_it)))
                    dial('Google Chrome', action.installed)
                    return None
                if batman.and_robin == 'gnome-system-monitor':
                    Img.gnome_system_monitor_img.set_from_file(yes)
                    Menu5.gnome_system_monitor.set_tooltip_markup(format(SetToolTip('Gnome system monitor', action.installed, action.remove_it)))
                    dial('Gnome System Monitor', action.installed)
                    return None
                if batman.and_robin == 'gloobus-preview':
                    Img.gloobus_img.set_from_file(yes)
                    Menu6.gloobus.set_tooltip_markup(format(SetToolTip('Gloobus', action.installed, action.remove_it)))
                    dial('Gloobus', action.installed)
                    return None
                if batman.and_robin == 'transmission-gtk':
                    Img.transmission_img.set_from_file(yes)
                    Menu3.transmission.set_tooltip_markup(format(SetToolTip('Transmission', action.installed, action.remove_it)))
                    dial('Transmission', action.installed)
                    return None
                if batman.and_robin == 'gtk-recordmydesktop':
                    Img.recordmydesktop_img.set_from_file(yes)
                    Menu4.recordmydesktop.set_tooltip_markup(format(SetToolTip('RecordMyDesktop', action.installed, action.remove_it)))
                    dial('RecordMyDesktop', action.installed)
                    return None
                if batman.and_robin == 'deluge':
                    Img.deluge__img.set_from_file(yes)
                    Menu7.deluge_.set_tooltip_markup(duh)
                    Img.deluge_img.set_from_file(yes)
                    Menu3.deluge.set_tooltip_markup(duh)
                if batman.and_robin == 'glade':
                    Img.glade__img.set_from_file(yes)
                    Menu7.glade_.set_tooltip_markup(duh)
                    Img.glade_img.set_from_file(yes)
                    Menu1.glade.set_tooltip_markup(duh)
                if batman.and_robin == 'audacious':
                    Img.audacious__img.set_from_file(yes)
                    Menu7.audacious_.set_tooltip_markup(duh)
                    Img.audacious_img.set_from_file(yes)
                    Menu4.audacious.set_tooltip_markup(duh)
                if batman.and_robin == 'gimp':
                    Img.gimp__img.set_from_file(yes)
                    Menu7.gimp_.set_tooltip_markup(duh)
                    Img.gimp_img.set_from_file(yes)
                    Menu2.gimp.set_tooltip_markup(duh)
                if batman.and_robin == 'evince':
                    Img.evince__img.set_from_file(yes)
                    Menu7.evince_.set_tooltip_markup(duh)
                    Img.evince_img.set_from_file(yes)
                    Menu2.evince.set_tooltip_markup(duh)
                if batman.and_robin == 'xfburn':
                    Img.xfburn__img.set_from_file(yes)
                    Menu7.xfburn_.set_tooltip_markup(duh)
                    Img.xfburn_img.set_from_file(yes)
                    Menu4.xfburn.set_tooltip_markup(duh)
                if batman.and_robin == 'chromium':
                    Img.chromium__img.set_from_file(yes)
                    Menu7.chromium_.set_tooltip_markup(duh)
                    Img.chromium_img.set_from_file(yes)
                    Menu3.chromium.set_tooltip_markup(duh)
                if batman.and_robin == 'openshot':
                    Img.openshot__img.set_from_file(yes)
                    Menu7.openshot_.set_tooltip_markup(duh)
                    Img.openshot_img.set_from_file(yes)
                    Menu4.openshot.set_tooltip_markup(duh)
                if batman.and_robin == 'liferea':
                    Img.liferea__img.set_from_file(yes)
                    Menu7.liferea_.set_tooltip_markup(duh)
                    Img.liferea_img.set_from_file(yes)
                    Menu3.liferea.set_tooltip_markup(duh)
                if batman.and_robin == 'htop':
                    Img.htop__img.set_from_file(yes)
                    Menu7.htop_.set_tooltip_markup(duh)
                    Img.htop_img.set_from_file(yes)
                    Menu5.htop.set_tooltip_markup(duh)
                if batman.and_robin in ['skype', 'skyp']:
                    Img.skype__img.set_from_file(yes)
                    Menu7.skype_.set_tooltip_markup(duh)
                    Img.skype_img.set_from_file(yes)
                    Menu3.skyp.set_tooltip_markup(duh)
                if batman.and_robin == 'virtualbox':
                    Img.virtualbox__img.set_from_file(yes)
                    Menu7.virtualbox_.set_tooltip_markup(duh)
                    Img.virtualbox_img.set_from_file(yes)
                    Menu5.virtualbox.set_tooltip_markup(duh)
                if batman.and_robin == 'steam':
                    Img.steam__img.set_from_file(yes)
                    Menu7.steam_.set_tooltip_markup(duh)
                    Img.steam_img.set_from_file(yes)
                    Menu3.steam.set_tooltip_markup(duh)
                if batman.and_robin == 'xchat':
                    Img.xchat__img.set_from_file(yes)
                    Menu7.xchat_.set_tooltip_markup(duh)
                    Img.xchat_img.set_from_file(yes)
                    Menu3.xchat.set_tooltip_markup(duh)
                if batman.and_robin == 'gedit':
                    Img.gedit__img.set_from_file(yes)
                    Menu7.gedit_.set_tooltip_markup(duh)
                    Img.gedit_img.set_from_file(yes)
                    Menu6.gedit.set_tooltip_markup(duh)
                if batman.and_robin == 'docky':
                    Img.docky_img.set_from_file(yes)
                    Menu6.docky.set_tooltip_markup(duh)
                if batman.and_robin == 'emacs':
                    Img.emacs_img.set_from_file(yes)
                    Menu6.emacs.set_tooltip_markup(duh)
                if batman.and_robin == 'vim':
                    Img.vim_img.set_from_file(yes)
                    Menu6.vim.set_tooltip_markup(duh)
                if batman.and_robin == 'leafpad':
                    Img.leafpad_img.set_from_file(yes)
                    Menu6.leafpad.set_tooltip_markup(duh)
                if batman.and_robin == 'scribes':
                    Img.scribes_img.set_from_file(yes)
                    Menu6.scribes.set_tooltip_markup(duh)
                if batman.and_robin == 'tomboy':
                    Img.tomboy_img.set_from_file(yes)
                    Menu6.tomboy.set_tooltip_markup(duh)
                if batman.and_robin == 'tuxcards':
                    Img.tuxcards_img.set_from_file(yes)
                    Menu6.tuxcards.set_tooltip_markup(duh)
                if batman.and_robin == 'imagewriter':
                    Img.imagewriter_img.set_from_file(yes)
                    Menu6.imagewriter.set_tooltip_markup(duh)
                if batman.and_robin == 'gparted':
                    Img.gparted_img.set_from_file(yes)
                    Menu5.gparted.set_tooltip_markup(duh)
                if batman.and_robin == 'guake':
                    Img.guake_img.set_from_file(yes)
                    Menu5.guake.set_tooltip_markup(duh)
                if batman.and_robin == 'hardinfo':
                    Img.hardinfo_img.set_from_file(yes)
                    Menu5.hardinfo.set_tooltip_markup(duh)
                if batman.and_robin == 'keepassx':
                    Img.keepassx_img.set_from_file(yes)
                    Menu5.keepassx.set_tooltip_markup(duh)
                if batman.and_robin == 'playonlinux':
                    Img.playonlinux_img.set_from_file(yes)
                    Menu5.playonlinux.set_tooltip_markup(duh)
                if batman.and_robin == 'terminator':
                    Img.terminator_img.set_from_file(yes)
                    Menu5.terminator.set_tooltip_markup(duh)
                if batman.and_robin == 'thunar':
                    Img.thunar_img.set_from_file(yes)
                    Menu5.thunar.set_tooltip_markup(duh)
                if batman.and_robin == 'truecrypt':
                    Img.truecrypt_img.set_from_file(yes)
                    Menu5.truecrypt.set_tooltip_markup(duh)
                if batman.and_robin == 'unetbootin':
                    Img.unetbootin_img.set_from_file(yes)
                    Menu5.unetbootin.set_tooltip_markup(duh)
                if batman.and_robin == 'wine':
                    Img.wine_img.set_from_file(yes)
                    Menu5.wine.set_tooltip_markup(duh)
                if batman.and_robin == 'xbmc':
                    Img.xbmc_img.set_from_file(yes)
                    Menu5.xbmc.set_tooltip_markup(duh)
                if batman.and_robin == 'gufw':
                    Img.gufw_img.set_from_file(yes)
                    Menu5.gufw.set_tooltip_markup(duh)
                if batman.and_robin == 'octopi':
                    Img.octopi_img.set_from_file(yes)
                    Menu5.octopi.set_tooltip_markup(duh)
                if batman.and_robin == 'pamac':
                    Img.pamac_img.set_from_file(yes)
                    Menu5.pamac.set_tooltip_markup(duh)
                if batman.and_robin == 'amarok':
                    Img.amarok_img.set_from_file(yes)
                    Menu4.amarok.set_tooltip_markup(duh)
                if batman.and_robin == 'banshee':
                    Img.banshee_img.set_from_file(yes)
                    Menu4.banshee.set_tooltip_markup(duh)
                if batman.and_robin == 'cheese':
                    Img.cheese_img.set_from_file(yes)
                    Menu4.cheese.set_tooltip_markup(duh)
                if batman.and_robin == 'clementine':
                    Img.clementine_img.set_from_file(yes)
                    Menu4.clementine.set_tooltip_markup(duh)
                if batman.and_robin == 'guayadeque':
                    Img.guayadeque_img.set_from_file(yes)
                    Menu4.guayadeque.set_tooltip_markup(duh)
                if batman.and_robin == 'mplayer':
                    Img.mplayer_img.set_from_file(yes)
                    Menu4.mplayer.set_tooltip_markup(duh)
                if batman.and_robin == 'pitivi':
                    Img.pitivi_img.set_from_file(yes)
                    Menu4.pitivi.set_tooltip_markup(duh)
                if batman.and_robin == 'rhythmbox':
                    Img.rhythmbox_img.set_from_file(yes)
                    Menu4.rhythmbox.set_tooltip_markup(duh)
                if batman.and_robin == 'soundconverter':
                    Img.soundconverter_img.set_from_file(yes)
                    Menu4.soundconverter.set_tooltip_markup(duh)
                if batman.and_robin == 'totem':
                    Img.totem_img.set_from_file(yes)
                    Menu4.totem.set_tooltip_markup(duh)
                if batman.and_robin == 'vlc':
                    Img.vlc_img.set_from_file(yes)
                    Menu4.vlc.set_tooltip_markup(duh)
                if batman.and_robin == 'winff':
                    Img.winff_img.set_from_file(yes)
                    Menu4.winff.set_tooltip_markup(duh)
                if batman.and_robin == 'kdenlive':
                    Img.kdenlive_img.set_from_file(yes)
                    Menu4.kdenlive.set_tooltip_markup(duh)
                if batman.and_robin == 'simplescreenrecorder':
                    Img.simplescreenrecorder_img.set_from_file(yes)
                    Menu4.simplescreenrecorder.set_tooltip_markup(format(SetToolTip('Simple Screen Recorder', action.installed, action.remove_it)))
                if batman.and_robin == 'vokoscreen':
                    Img.vokoscreen_img.set_from_file(yes)
                    Menu4.vokoscreen.set_tooltip_markup(duh)
                if batman.and_robin == 'linuxdcpp':
                    Img.linuxdcpp_img.set_from_file(yes)
                    Menu3.linuxdcpp.set_tooltip_markup(duh)
                if batman.and_robin == 'evolution':
                    Img.evolution_img.set_from_file(yes)
                    Menu3.evolution.set_tooltip_markup(duh)
                if batman.and_robin == 'filezilla':
                    Img.filezilla_img.set_from_file(yes)
                    Menu3.filezilla.set_tooltip_markup(duh)
                if batman.and_robin == 'firefox':
                    Img.firefox_img.set_from_file(yes)
                    Menu3.firefox.set_tooltip_markup(duh)
                if batman.and_robin == 'midori':
                    Img.midori_img.set_from_file(yes)
                    Menu3.midori.set_tooltip_markup(duh)
                if batman.and_robin == 'minitube':
                    Img.minitube_img.set_from_file(yes)
                    Menu3.minitube.set_tooltip_markup(duh)
                if batman.and_robin == 'opera':
                    Img.opera_img.set_from_file(yes)
                    Menu3.opera.set_tooltip_markup(duh)
                if batman.and_robin == 'pidgin':
                    Img.pidgin_img.set_from_file(yes)
                    Menu3.pidgin.set_tooltip_markup(duh)
                if batman.and_robin == 'thunderbird':
                    Img.thunderbird_img.set_from_file(yes)
                    Menu3.thunderbird.set_tooltip_markup(duh)
                if batman.and_robin == 'gwenview':
                    Img.gwenview_img.set_from_file(yes)
                    Menu2.gwenview.set_tooltip_markup(duh)
                if batman.and_robin == 'inkscape':
                    Img.inkscape_img.set_from_file(yes)
                    Menu2.inkscape.set_tooltip_markup(duh)
                if batman.and_robin == 'mypaint':
                    Img.mypaint_img.set_from_file(yes)
                    Menu2.mypaint.set_tooltip_markup(duh)
                if batman.and_robin == 'pinta':
                    Img.pinta_img.set_from_file(yes)
                    Menu2.pinta.set_tooltip_markup(duh)
                if batman.and_robin == 'shotwell':
                    Img.shotwell_img.set_from_file(yes)
                    Menu2.shotwell.set_tooltip_markup(duh)
                if batman.and_robin == 'stellarium':
                    Img.stellarium_img.set_from_file(yes)
                    Menu2.stellarium.set_tooltip_markup(duh)
                if batman.and_robin == 'anjuta':
                    Img.anjuta_img.set_from_file(yes)
                    Menu1.anjuta.set_tooltip_markup(duh)
                if batman.and_robin == 'bluefish':
                    Img.bluefish_img.set_from_file(yes)
                    Menu1.bluefish.set_tooltip_markup(duh)
                if batman.and_robin == 'eclipse':
                    Img.eclipse_img.set_from_file(yes)
                    Menu1.eclipse.set_tooltip_markup(duh)
                if batman.and_robin == 'meld':
                    Img.meld_img.set_from_file(yes)
                    Menu1.meld.set_tooltip_markup(duh)
                if batman.and_robin == 'netbeans':
                    Img.netbeans_img.set_from_file(yes)
                    Menu1.netbeans.set_tooltip_markup(duh)
                if batman.and_robin == 'qt4':
                    Img.qt4_img.set_from_file(yes)
                    Menu1.qt4.set_tooltip_markup(duh)
                if batman.and_robin == 'qtcreator':
                    Img.qtcreator_img.set_from_file(yes)
                    Menu1.qtcreator.set_tooltip_markup(duh)
                dial(batman.and_robin.capitalize(), action.installed)