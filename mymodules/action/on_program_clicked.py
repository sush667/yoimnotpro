import os
from functools import wraps
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
from mymodules.action.OPC_related.apply_decoration import StartKickingSomeNinjas

class OPC:

    def batmans_decorator(batmobile):
        @wraps(batmobile)
        def batmans_wrapper(*number_of_attacking_positional_arguments):
            StartKickingSomeNinjas(batmobile.__name__)
            return batmobile(*number_of_attacking_positional_arguments)
        return batmans_wrapper

    # menu 7 button actions
    @staticmethod
    @batmans_decorator
    def on_geany__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_blender__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_ninja_ide__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_glade__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_audacious__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_gimp__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_evince__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_xfburn__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_flashplayer__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_openshot__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_chromium__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_deluge__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_liferea__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_htop__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_skype__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_wireshark__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_virtualbox__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_steam__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_xchat__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_gedit__clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    # menu 6 button actions
    def on_docky_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_emacs_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_vim_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_galculator_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_gedit_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_gloobus_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_leafpad_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_scribes_clicked(self):
    	pass

    @staticmethod
    @batmans_decorator
    def on_tomboy_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_tuxcards_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_imagewriter_clicked(self):
        pass

    @staticmethod
    def on_sevenzip_clicked(self):
        if os.path.isfile(find.program['7zip']):
            os.system('pacman -Rdd p7zip --noconfirm')
            if not os.path.isfile(find.program['7zip']):
                Img.sevenzip_img.set_from_file('./categories/gtk-no.png')
                dial('7zip','removed')
                Menu6.sevenzip.set_tooltip_text("7-zip is not installed.\nClick to install it.")
        else:
            os.system('pacman -S p7zip --noconfirm')
            if os.path.isfile(find.program['7zip']):
                Img.sevenzip_img.set_from_file('./categories/gtk-yes.png')
                dial('7zip','installed')
                Menu6.sevenzip.set_tooltip_text("7-zip is installed.\nClick to remove it.")

    @staticmethod
    @batmans_decorator
    # menu 5 button actions
    def on_gparted_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_guake_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_hardinfo_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_htop_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_keepassx_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_playonlinux_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_terminator_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_thunar_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_truecrypt_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_unetbootin_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_virtualbox_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_wine_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_wireshark_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_xbmc_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_gufw_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_octopi_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_pamac_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_gnome_system_monitor_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    # menu 4 button actions
    def on_amarok_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_audacious_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_banshee_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_cheese_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_clementine_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_flashplayer_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_recordmydesktop_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_guayadeque_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_mplayer_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_openshot_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_pitivi_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_rhythmbox_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_soundconverter_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_totem_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_vlc_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_winff_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_xfburn_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_kdenlive_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_simplescreenrecorder_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_vokoscreen_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    # menu 3 button actions
    def on_linuxdcpp_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_chromium_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_deluge_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_evolution_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_filezilla_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_firefox_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_chrome_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_xchat_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_liferea_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_midori_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_minitube_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_opera_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_pidgin_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_skyp_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_steam_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_thunderbird_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_transmission_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    # menu 2 button actions
    def on_evince_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_f_spot_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_gimp_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_gwenview_clicked(self):
        pass

    @staticmethod
    def on_imagemagick_clicked(self):
        if os.path.isfile(find.program['imagemagick']):
            os.system('pacman -Rdd imagemagick --noconfirm')
            if not os.path.isfile(find.program['imagemagick']):
                Img.imagemagick_img.set_from_file('./categories/gtk-no.png')
                dial('ImageMagick', 'removed')
                Menu2.imagemagick.set_tooltip_text("ImageMagick is not installed.\nClick to install it.")
        else:
            os.system('pacman -S imagemagick --noconfirm')
            if os.path.isfile(find.program['imagemagick']):
                Img.imagemagick_img.set_from_file('./categories/gtk-yes.png')
                dial('ImageMagick', 'installed')
                Menu2.imagemagick.set_tooltip_text("ImageMagick is installed.\nClick to remove it.")

    @staticmethod
    @batmans_decorator
    def on_inkscape_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_mypaint_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_pinta_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_shotwell_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_stellarium_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    # menu 1 button actions
    def on_anjuta_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_blender_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_bluefish_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_eclipse_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_geany_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_glade_clicked(self):
        pass

    @staticmethod
    def on_openjdk_clicked(self):
        if os.path.exists(find.program['openjdk']):
            os.system('pacman -R jre7-openjdk --noconfirm')
            if not os.path.exists(find.program['openjdk']):
                Img.openjdk_img.set_from_file('./categories/gtk-no.png')
                dial('OpenJDK', 'removed')
                Menu1.openjdk.set_tooltip_text("OpenJDK is not installed.\nClick to install it.")
        else:
            os.system('pacman -S jre7-openjdk --noconfirm')
            if os.path.exists(find.program['openjdk']):
                Img.openjdk_img.set_from_file('./categories/gtk-yes.png')
                dial('OpenJDK', 'installed')
                Menu1.openjdk.set_tooltip_text("OpenJDK is installed.\nClick to remove it.")

    @staticmethod
    @batmans_decorator
    def on_meld_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_netbeans_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_qt4_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_qt5_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_qtcreator_clicked(self):
        pass

    @staticmethod
    @batmans_decorator
    def on_ninja_ide_clicked(self):
        pass