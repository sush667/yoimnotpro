from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.dial import action

class Menu2:

    # get menu 2 application buttons
    evince = Builder.builder3.get_object("evince")
    f_spot = Builder.builder3.get_object("f_spot")
    gimp = Builder.builder3.get_object("gimp")
    gwenview = Builder.builder3.get_object("gwenview")
    imagemagick = Builder.builder3.get_object("imagemagick")
    inkscape = Builder.builder3.get_object("inkscape")
    mypaint = Builder.builder3.get_object("mypaint")
    pinta = Builder.builder3.get_object("pinta")
    shotwell = Builder.builder3.get_object("shotwell")
    stellarium = Builder.builder3.get_object("stellarium")
    # add tooltip for each application icon
    evince_icon_tooltip = Builder.builder3.get_object("evince_icon_tooltip")
    evince_icon_tooltip.set_tooltip_text("Evince is a document viewer for multiple document formats.")
    f_spot_icon_tooltip = Builder.builder3.get_object("f_spot_icon_tooltip")
    f_spot_icon_tooltip.set_tooltip_text("F-Spot is a full-featured personal photo management application.")
    gimp_icon_tooltip = Builder.builder3.get_object("gimp_icon_tooltip")
    gimp_icon_tooltip.set_tooltip_text("GIMP is an image retouching and editing tool, similar to Photoshop.")
    gwenview_icon_tooltip = Builder.builder3.get_object("gwenview_icon_tooltip")
    gwenview_icon_tooltip.set_tooltip_text("Gwenview is an image viewer.")
    imagemagick_icon_tooltip = Builder.builder3.get_object("imagemagick_icon_tooltip")
    imagemagick_icon_tooltip.set_tooltip_text("Use ImageMagick to convert, edit, or compose bitmap images in a variety of formats.")
    inkscape_icon_tooltip = Builder.builder3.get_object("inkscape_icon_tooltip")
    inkscape_icon_tooltip.set_tooltip_text("Inkscape is an open source vector graphics editor.")
    mypaint_icon_tooltip = Builder.builder3.get_object("mypaint_icon_tooltip")
    mypaint_icon_tooltip.set_tooltip_text("MyPaint is a fast and easy open-source graphics application for digital painters.")
    pinta_icon_tooltip = Builder.builder3.get_object("pinta_icon_tooltip")
    pinta_icon_tooltip.set_tooltip_text("Pinta is an open-source, cross-platform bitmap image drawing and editing program inspired by Paint.NET")
    shotwell_icon_tooltip = Builder.builder3.get_object("shotwell_icon_tooltip")
    shotwell_icon_tooltip.set_tooltip_text("Shotwell is an image organizer.")
    stellarium_icon_tooltip = Builder.builder3.get_object("stellarium_icon_tooltip")
    stellarium_icon_tooltip.set_tooltip_text("Stellarium is a planetarium software that shows exactly what you see when you look up at the stars.")

    @staticmethod
    def on_button2_clicked():
        Img.image1.set_from_file(action.menu_img_1)
        Img.image2.set_from_file(action.menu_img_22)
        Img.image3.set_from_file(action.menu_img_3)
        Img.image4.set_from_file(action.menu_img_4)
        Img.image5.set_from_file(action.menu_img_5)
        Img.image6.set_from_file(action.menu_img_6)

        from somesome import menu2
        menu2.load()