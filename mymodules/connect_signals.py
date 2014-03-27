from mymodules.builder import Builder
from mymodules.action.on_program_clicked import OPC
from mymodules.categories.menu7_button import Menu7
from mymodules.categories.menu6_button import Menu6
from mymodules.categories.menu5_button import Menu5
from mymodules.categories.menu4_button import Menu4
from mymodules.categories.menu3_button import Menu3
from mymodules.categories.menu2_button import Menu2
from mymodules.categories.menu1_button import Menu1

class InitConnectMeSignals:
    def __init__(self):

        Builder.builder.connect_signals(self)

        # connect "clicked" signal to those Menu7 buttons
        Menu7.geany_.connect("clicked", OPC.on_geany__clicked)
        Menu7.blender_.connect("clicked", OPC.on_blender__clicked)
        Menu7.ninja_ide_.connect("clicked", OPC.on_ninja_ide__clicked)
        Menu7.glade_.connect("clicked", OPC.on_glade__clicked)
        Menu7.audacious_.connect("clicked", OPC.on_audacious__clicked)
        Menu7.gimp_.connect("clicked", OPC.on_gimp__clicked)
        Menu7.evince_.connect("clicked", OPC.on_evince__clicked)
        Menu7.xfburn_.connect("clicked", OPC.on_xfburn__clicked)
        Menu7.flashplayer_.connect("clicked", OPC.on_flashplayer__clicked)
        Menu7.openshot_.connect("clicked", OPC.on_openshot__clicked)
        Menu7.chromium_.connect("clicked", OPC.on_chromium__clicked)
        Menu7.deluge_.connect("clicked", OPC.on_deluge__clicked)
        Menu7.liferea_.connect("clicked", OPC.on_liferea__clicked)
        Menu7.htop_.connect("clicked", OPC.on_htop__clicked)
        Menu7.skype_.connect("clicked", OPC.on_skype__clicked)
        Menu7.wireshark_.connect("clicked", OPC.on_wireshark__clicked)
        Menu7.virtualbox_.connect("clicked", OPC.on_virtualbox__clicked)
        Menu7.steam_.connect("clicked", OPC.on_steam__clicked)
        Menu7.xchat_.connect("clicked", OPC.on_xchat__clicked)
        Menu7.gedit_.connect("clicked", OPC.on_gedit__clicked)

        # connect "clicked" signal to those Menu6 buttons
        Menu6.docky.connect("clicked", OPC.on_docky_clicked)
        Menu6.emacs.connect("clicked", OPC.on_emacs_clicked)
        Menu6.vim.connect("clicked", OPC.on_vim_clicked)
        Menu6.galculator.connect("clicked", OPC.on_galculator_clicked)
        Menu6.gedit.connect("clicked", OPC.on_gedit_clicked)
        Menu6.gloobus.connect("clicked", OPC.on_gloobus_clicked)
        Menu6.leafpad.connect("clicked", OPC.on_leafpad_clicked)
        Menu6.scribes.connect("clicked", OPC.on_scribes_clicked)
        Menu6.tomboy.connect("clicked", OPC.on_tomboy_clicked)
        Menu6.tuxcards.connect("clicked", OPC.on_tuxcards_clicked)
        Menu6.imagewriter.connect("clicked", OPC.on_imagewriter_clicked)
        Menu6.sevenzip.connect("clicked", OPC.on_sevenzip_clicked)

        # connect "clicked" signal to those Menu5 buttons
        Menu5.gparted.connect("clicked", OPC.on_gparted_clicked)
        Menu5.guake.connect("clicked", OPC.on_guake_clicked)
        Menu5.hardinfo.connect("clicked", OPC.on_hardinfo_clicked)
        Menu5.htop.connect("clicked", OPC.on_htop_clicked)
        Menu5.keepassx.connect("clicked", OPC.on_keepassx_clicked)
        Menu5.playonlinux.connect("clicked", OPC.on_playonlinux_clicked)
        Menu5.terminator.connect("clicked", OPC.on_terminator_clicked)
        Menu5.thunar.connect("clicked", OPC.on_thunar_clicked)
        Menu5.truecrypt.connect("clicked", OPC.on_truecrypt_clicked)
        Menu5.unetbootin.connect("clicked", OPC.on_unetbootin_clicked)
        Menu5.virtualbox.connect("clicked", OPC.on_virtualbox_clicked)
        Menu5.wine.connect("clicked", OPC.on_wine_clicked)
        Menu5.wireshark.connect("clicked", OPC.on_wireshark_clicked)
        Menu5.xbmc.connect("clicked", OPC.on_xbmc_clicked)
        Menu5.gufw.connect("clicked", OPC.on_gufw_clicked)
        Menu5.octopi.connect("clicked", OPC.on_octopi_clicked)
        Menu5.pamac.connect("clicked", OPC.on_pamac_clicked)
        Menu5.gnome_system_monitor.connect("clicked", OPC.on_gnome_system_monitor_clicked)

        # connect "clicked" signal to those buttons
        Menu4.amarok.connect("clicked", OPC.on_amarok_clicked)
        Menu4.audacious.connect("clicked", OPC.on_audacious_clicked)
        Menu4.banshee.connect("clicked", OPC.on_banshee_clicked)
        Menu4.cheese.connect("clicked", OPC.on_cheese_clicked)
        Menu4.clementine.connect("clicked", OPC.on_clementine_clicked)
        Menu4.flashplayer.connect("clicked", OPC.on_flashplayer_clicked)
        Menu4.recordmydesktop.connect("clicked", OPC.on_recordmydesktop_clicked)
        Menu4.guayadeque.connect("clicked", OPC.on_guayadeque_clicked)
        Menu4.mplayer.connect("clicked", OPC.on_mplayer_clicked)
        Menu4.openshot.connect("clicked", OPC.on_openshot_clicked)
        Menu4.pitivi.connect("clicked", OPC.on_pitivi_clicked)
        Menu4.rhythmbox.connect("clicked", OPC.on_rhythmbox_clicked)
        Menu4.soundconverter.connect("clicked", OPC.on_soundconverter_clicked)
        Menu4.totem.connect("clicked", OPC.on_totem_clicked)
        Menu4.vlc.connect("clicked", OPC.on_vlc_clicked)
        Menu4.winff.connect("clicked", OPC.on_winff_clicked)
        Menu4.xfburn.connect("clicked", OPC.on_xfburn_clicked)
        Menu4.kdenlive.connect("clicked", OPC.on_kdenlive_clicked)
        Menu4.simplescreenrecorder.connect("clicked", OPC.on_simplescreenrecorder_clicked)
        Menu4.vokoscreen.connect("clicked", OPC.on_vokoscreen_clicked)

        # connect "clicked" signal to those Menu3 buttons
        Menu3.chromium.connect("clicked", OPC.on_chromium_clicked)
        Menu3.deluge.connect("clicked", OPC.on_deluge_clicked)
        Menu3.evolution.connect("clicked", OPC.on_evolution_clicked)
        Menu3.filezilla.connect("clicked", OPC.on_filezilla_clicked)
        Menu3.firefox.connect("clicked", OPC.on_firefox_clicked)
        Menu3.chrome.connect("clicked", OPC.on_chrome_clicked)
        Menu3.xchat.connect("clicked", OPC.on_xchat_clicked)
        Menu3.liferea.connect("clicked", OPC.on_liferea_clicked)
        Menu3.midori.connect("clicked", OPC.on_midori_clicked)
        Menu3.minitube.connect("clicked", OPC.on_minitube_clicked)
        Menu3.opera.connect("clicked", OPC.on_opera_clicked)
        Menu3.pidgin.connect("clicked", OPC.on_pidgin_clicked)
        Menu3.skyp.connect("clicked", OPC.on_skyp_clicked)
        Menu3.steam.connect("clicked", OPC.on_steam_clicked)
        Menu3.thunderbird.connect("clicked", OPC.on_thunderbird_clicked)
        Menu3.transmission.connect("clicked", OPC.on_transmission_clicked)
        Menu3.linuxdcpp.connect("clicked", OPC.on_linuxdcpp_clicked)

        # connect "clicked" signal to those Menu2 buttons
        Menu2.evince.connect("clicked", OPC.on_evince_clicked)
        Menu2.f_spot.connect("clicked", OPC.on_f_spot_clicked)
        Menu2.gimp.connect("clicked", OPC.on_gimp_clicked)
        Menu2.gwenview.connect("clicked", OPC.on_gwenview_clicked)
        Menu2.imagemagick.connect("clicked", OPC.on_imagemagick_clicked)
        Menu2.inkscape.connect("clicked", OPC.on_inkscape_clicked)
        Menu2.mypaint.connect("clicked", OPC.on_mypaint_clicked)
        Menu2.pinta.connect("clicked", OPC.on_pinta_clicked)
        Menu2.shotwell.connect("clicked", OPC.on_shotwell_clicked)
        Menu2.stellarium.connect("clicked", OPC.on_stellarium_clicked)

        # connect "clicked" signal to those Menu1 buttons
        Menu1.anjuta.connect("clicked", OPC.on_anjuta_clicked)
        Menu1.blender.connect("clicked", OPC.on_blender_clicked)
        Menu1.bluefish.connect("clicked", OPC.on_bluefish_clicked)
        Menu1.eclipse.connect("clicked", OPC.on_eclipse_clicked)
        Menu1.geany.connect("clicked", OPC.on_geany_clicked)
        Menu1.glade.connect("clicked", OPC.on_glade_clicked)
        Menu1.openjdk.connect("clicked", OPC.on_openjdk_clicked)
        Menu1.meld.connect("clicked", OPC.on_meld_clicked)
        Menu1.netbeans.connect("clicked", OPC.on_netbeans_clicked)
        Menu1.qt4.connect("clicked", OPC.on_qt4_clicked)
        Menu1.qt5.connect("clicked", OPC.on_qt5_clicked)
        Menu1.qtcreator.connect("clicked", OPC.on_qtcreator_clicked)
        Menu1.ninja_ide.connect("clicked", OPC.on_ninja_ide_clicked)