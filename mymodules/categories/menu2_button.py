import os
from mymodules.action.find_program import Find
from mymodules.buttons_images import Img
from mymodules.builder import Builder

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
        Img.image1.set_from_file('./categories/menu1.png')
        Img.image2.set_from_file('./categories/menu22.png')
        Img.image3.set_from_file('./categories/menu3.png')
        Img.image4.set_from_file('./categories/menu4.png')
        Img.image5.set_from_file('./categories/menu5.xpm')
        Img.image6.set_from_file('./categories/menu6.png')

        # check if those programs are installed and set appropriate sign

        if os.path.isfile(Find.program['evince']):
            Img.evince_img.set_from_file('./categories/gtk-yes.png')
            Menu2.evince.set_tooltip_text("Evince is installed.\nClick to remove it.")
        else:
            Img.evince_img.set_from_file('./categories/gtk-no.png')
            Menu2.evince.set_tooltip_text("Evince is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['f-spot']):
            Img.f_spot_img.set_from_file('./categories/gtk-yes.png')
            Menu2.f_spot.set_tooltip_text("F-spot is installed.\nClick to remove it.")
        else:
            Img.f_spot_img.set_from_file('./categories/gtk-no.png')
            Menu2.f_spot.set_tooltip_text("F-spot is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['gimp']):
            Img.gimp_img.set_from_file('./categories/gtk-yes.png')
            Menu2.gimp.set_tooltip_text("Gimp is installed.\nClick to remove it.")
        else:
            Img.gimp_img.set_from_file('./categories/gtk-no.png')
            Menu2.gimp.set_tooltip_text("Gimp is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['gwenview']):
            Img.gwenview_img.set_from_file('./categories/gtk-yes.png')
            Menu2.gwenview.set_tooltip_text("Gwenview is installed.\nClick to remove it.")
        else:
            Img.gwenview_img.set_from_file('./categories/gtk-no.png')
            Menu2.gwenview.set_tooltip_text("Gwenview is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['imagemagick']):
            Img.imagemagick_img.set_from_file('./categories/gtk-yes.png')
            Menu2.imagemagick.set_tooltip_text("ImageMagick is installed.\nClick to remove it.")
        else:
            Img.imagemagick_img.set_from_file('./categories/gtk-no.png')
            Menu2.imagemagick.set_tooltip_text("ImageMagick is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['inkscape']):
            Img.inkscape_img.set_from_file('./categories/gtk-yes.png')
            Menu2.inkscape.set_tooltip_text("Inkscape is installed.\nClick to remove it.")
        else:
            Img.inkscape_img.set_from_file('./categories/gtk-no.png')
            Menu2.inkscape.set_tooltip_text("Inkscape is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['mypaint']):
            Img.mypaint_img.set_from_file('./categories/gtk-yes.png')
            Menu2.mypaint.set_tooltip_text("MyPaint is installed.\nClick to remove it.")
        else:
            Img.mypaint_img.set_from_file('./categories/gtk-no.png')
            Menu2.mypaint.set_tooltip_text("MyPaint is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['pinta']):
            Img.pinta_img.set_from_file('./categories/gtk-yes.png')
            Menu2.pinta.set_tooltip_text("Pinta is installed.\nClick to remove it.")
        else:
            Img.pinta_img.set_from_file('./categories/gtk-no.png')
            Menu2.pinta.set_tooltip_text("Pinta is not installed.\nClick to install it.")

        if os.path.isfile(Find.program['shotwell']):
            Img.shotwell_img.set_from_file('./categories/gtk-yes.png')
            Menu2.shotwell.set_tooltip_text("Shotwell is installed.\nClick to remove it.")
        else:
            Img.shotwell_img.set_from_file('./categories/gtk-no.png')
            Menu2.shotwell.set_tooltip_text("Shotwell is not installed.\nClick to install it.")