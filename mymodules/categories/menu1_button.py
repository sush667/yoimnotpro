import os
from mymodules.builder import Builder
from mymodules.action.find_program import Find
from mymodules.buttons_images import Img
from mymodules.action.dial import SetToolTip, action

class Menu1:
    # get menu 1 application buttons
    anjuta = Builder.builder2.get_object("anjuta")
    blender = Builder.builder2.get_object("blender")
    bluefish = Builder.builder2.get_object("bluefish")
    eclipse = Builder.builder2.get_object("eclipse")
    geany = Builder.builder2.get_object("geany")
    glade = Builder.builder2.get_object("glade")
    openjdk = Builder.builder2.get_object("openjdk")
    meld = Builder.builder2.get_object("meld")
    netbeans = Builder.builder2.get_object("netbeans")
    qt4 = Builder.builder2.get_object("qt4")
    qt5 = Builder.builder2.get_object("qt5")
    qtcreator = Builder.builder2.get_object("qtcreator")
    ninja_ide = Builder.builder2.get_object("ninja_ide")
    # add tooltip for each application icon
    anjuta_icon_tooltip = Builder.builder2.get_object("anjuta_icon_tooltip")
    anjuta_icon_tooltip.set_tooltip_text("Anjuta is an integrated development environment.")
    blender_icon_tooltip = Builder.builder2.get_object("blender_icon_tooltip")
    blender_icon_tooltip.set_tooltip_text("Blender is a free and open-source 3D computer graphics software product used for creating animated films, \nvisual effects, art, 3D printed models and so on.")
    bluefish_icon_tooltip = Builder.builder2.get_object("bluefish_icon_tooltip")
    bluefish_icon_tooltip.set_tooltip_text("Bluefish is a free and open source advanced text editor with a variety of tools for programming in general\nand the development of dynamic websites")
    eclipse_icon_tooltip = Builder.builder2.get_object("eclipse_icon_tooltip")
    eclipse_icon_tooltip.set_tooltip_text("Eclipse is IDE.")
    geany_icon_tooltip = Builder.builder2.get_object("geany_icon_tooltip")
    geany_icon_tooltip.set_tooltip_text("Geany is a small and lightweight integrated development environment.")
    glade_icon_tooltip = Builder.builder2.get_object("glade_icon_tooltip")
    glade_icon_tooltip.set_tooltip_text("Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment.")
    openjdk_icon_tooltip = Builder.builder2.get_object("openjdk_icon_tooltip")
    openjdk_icon_tooltip.set_tooltip_text("OpenJDK (Open Java Development Kit) is a free and open source implementation of the Java Platform, Standard Edition (Java SE).")
    meld_icon_tooltip = Builder.builder2.get_object("meld_icon_tooltip")
    meld_icon_tooltip.set_tooltip_text("Meld is a visual diff and merge tool targeted at developers.")
    netbeans_icon_tooltip = Builder.builder2.get_object("netbeans_icon_tooltip")
    netbeans_icon_tooltip.set_tooltip_text("Fully-featured Java IDE written completely in Java, with many modules available.")
    qt4_icon_tooltip = Builder.builder2.get_object("qt4_icon_tooltip")
    qt4_icon_tooltip.set_tooltip_text("Qt4 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface.")
    qt5_icon_tooltip = Builder.builder2.get_object("qt5_icon_tooltip")
    qt5_icon_tooltip.set_tooltip_text("Qt5 is a cross-platform application framework that is widely used\nfor developing application software with a graphical user interface.")
    qtcreator_icon_tooltip = Builder.builder2.get_object("qtcreator_icon_tooltip")
    qtcreator_icon_tooltip.set_tooltip_text("Qt Creator is a cross-platform C++ IDE")
    ninja_ide_icon_tooltip = Builder.builder2.get_object("ninja_ide_icon_tooltip")
    ninja_ide_icon_tooltip.set_tooltip_text("Ninja-IDE is a cross-platform integrated development environment designed to build Python applications.")

    @staticmethod
    def on_button1_clicked():
        Img.image1.set_from_file(action.menu_img_11)
        Img.image2.set_from_file(action.menu_img_2)
        Img.image3.set_from_file(action.menu_img_3)
        Img.image4.set_from_file(action.menu_img_4)
        Img.image5.set_from_file(action.menu_img_5)
        Img.image6.set_from_file(action.menu_img_6)

        # check if those programs are installed and set appropriate sign
        if os.path.isfile(Find.program['anjuta']):
            Img.anjuta_img.set_from_file(action.gtk_yes)
            Menu1.anjuta.set_tooltip_text(format(SetToolTip('anjuta', action.installed, action.remove_it)))
        else:
            Img.anjuta_img.set_from_file(action.gtk_no)
            Menu1.anjuta.set_tooltip_text(format(SetToolTip('anjuta', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['blender']):
            Img.blender_img.set_from_file(action.gtk_yes)
            Menu1.blender.set_tooltip_text(format(SetToolTip('blender', action.installed, action.remove_it)))
        else:
            Img.blender_img.set_from_file(action.gtk_no)
            Menu1.blender.set_tooltip_text(format(SetToolTip('blender', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['bluefish']):
            Img.bluefish_img.set_from_file(action.gtk_yes)
            Menu1.bluefish.set_tooltip_text(format(SetToolTip('bluefish', action.installed, action.remove_it)))
        else:
            Img.bluefish_img.set_from_file(action.gtk_no)
            Menu1.bluefish.set_tooltip_text(format(SetToolTip('bluefish', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['eclipse']):
            Img.eclipse_img.set_from_file(action.gtk_yes)
            Menu1.eclipse.set_tooltip_text(format(SetToolTip('eclipse', action.installed, action.remove_it)))
        else:
            Img.eclipse_img.set_from_file(action.gtk_no)
            Menu1.eclipse.set_tooltip_text(format(SetToolTip('eclipse', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['geany']):
            Img.geany_img.set_from_file(action.gtk_yes)
            Menu1.geany.set_tooltip_text(format(SetToolTip('geany', action.installed, action.remove_it)))
        else:
            Img.geany_img.set_from_file(action.gtk_no)
            Menu1.geany.set_tooltip_text(format(SetToolTip('geany', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['glade']):
            Img.glade_img.set_from_file(action.gtk_yes)
            Menu1.glade.set_tooltip_text(format(SetToolTip('glade', action.installed, action.remove_it)))
        else:
            Img.glade_img.set_from_file(action.gtk_no)
            Menu1.glade.set_tooltip_text(format(SetToolTip('glade', action.not_here, action.install_it)))

        if os.path.exists(Find.program['openjdk']):
            Img.openjdk_img.set_from_file(action.gtk_yes)
            Menu1.openjdk.set_tooltip_text(format(SetToolTip('openJDK', action.installed, action.remove_it)))
        else:
            Img.openjdk_img.set_from_file(action.gtk_no)
            Menu1.openjdk.set_tooltip_text(format(SetToolTip('openJDK', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['meld']):
            Img.meld_img.set_from_file(action.gtk_yes)
            Menu1.meld.set_tooltip_text(format(SetToolTip('meld', action.installed, action.remove_it)))
        else:
            Img.meld_img.set_from_file(action.gtk_no)
            Menu1.meld.set_tooltip_text(format(SetToolTip('meld', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['netbeans']):
            Img.netbeans_img.set_from_file(action.gtk_yes)
            Menu1.netbeans.set_tooltip_text(format(SetToolTip('netbeans', action.installed, action.remove_it)))
        else:
            Img.netbeans_img.set_from_file(action.gtk_no)
            Menu1.netbeans.set_tooltip_text(format(SetToolTip('netbeans', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['qt4']):
            Img.qt4_img.set_from_file(action.gtk_yes)
            Menu1.qt4.set_tooltip_text(format(SetToolTip('qt4', action.installed, action.remove_it)))
        else:
            Img.qt4_img.set_from_file(action.gtk_no)
            Menu1.qt4.set_tooltip_text(format(SetToolTip('qt4', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['qt5-base']):
<<<<<<< HEAD
            Img.qt5_img.set_from_file(action.gtk_yes)
            Menu1.qt5.set_tooltip_text(format(SetToolTip('qt5', action.installed, action.remove_it)))
=======
            Img.qt5_img.set_from_file('./categories/gtk-yes.png')
            Menu1.qt5.set_tooltip_text("Qt5 is installed.\nClick to remove it.")
>>>>>>> branch 'master' of https://github.com/wifiextender/yoimnotpro
        else:
            Img.qt5_img.set_from_file(action.gtk_no)
            Menu1.qt5.set_tooltip_text(format(SetToolTip('qt5', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['qtcreator']):
            Img.qtcreator_img.set_from_file(action.gtk_yes)
            Menu1.qtcreator.set_tooltip_text(format(SetToolTip('qtcreator', action.installed, action.remove_it)))
        else:
            Img.qtcreator_img.set_from_file(action.gtk_no)
            Menu1.qtcreator.set_tooltip_text(format(SetToolTip('qtcreator', action.installed, action.remove_it)))

        if os.path.isfile(Find.program['ninja-ide']):
            Img.ninja_ide_img.set_from_file(action.gtk_yes)
            Menu1.ninja_ide.set_tooltip_text(format(SetToolTip('ninja-IDE', action.installed, action.remove_it)))
        else:
            Img.ninja_ide_img.set_from_file(action.gtk_no)
            Menu1.ninja_ide.set_tooltip_text(format(SetToolTip('ninja-IDE', action.not_here, action.install_it)))
