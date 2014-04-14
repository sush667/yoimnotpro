from mymodules.builder import Builder
from mymodules.buttons_images import Img
from mymodules.action.dial import action

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

        from mymodules.categories.somesome import menu1
        menu1.load()