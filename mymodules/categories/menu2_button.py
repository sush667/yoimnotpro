import os
from mymodules.action.find_program import Find
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.dial import SetToolTip, action

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

        # check if those programs are installed and set appropriate sign
        no = action.gtk_no
        yes = action.gtk_yes
        if os.path.isfile(Find.program['evince']):
            Img.evince_img.set_from_file(yes)
            Menu2.evince.set_tooltip_markup(format(SetToolTip('evince', action.installed, action.remove_it)))
        else:
            Img.evince_img.set_from_file(no)
            Menu2.evince.set_tooltip_markup(format(SetToolTip('evince', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['f-spot']):
            Img.f_spot_img.set_from_file(yes)
            Menu2.f_spot.set_tooltip_markup(format(SetToolTip('f-Spot', action.installed, action.remove_it)))
        else:
            Img.f_spot_img.set_from_file(no)
            Menu2.f_spot.set_tooltip_markup(format(SetToolTip('f-Spot', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['gimp']):
            Img.gimp_img.set_from_file(yes)
            Menu2.gimp.set_tooltip_markup(format(SetToolTip('gimp', action.installed, action.remove_it)))
        else:
            Img.gimp_img.set_from_file(no)
            Menu2.gimp.set_tooltip_markup(format(SetToolTip('gimp', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['gwenview']):
            Img.gwenview_img.set_from_file(yes)
            Menu2.gwenview.set_tooltip_markup(format(SetToolTip('gwenview', action.installed, action.remove_it)))
        else:
            Img.gwenview_img.set_from_file(no)
            Menu2.gwenview.set_tooltip_markup(format(SetToolTip('gwenview', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['imagemagick']):
            Img.imagemagick_img.set_from_file(yes)
            Menu2.imagemagick.set_tooltip_markup(format(SetToolTip('imageMagick', action.installed, action.remove_it)))
        else:
            Img.imagemagick_img.set_from_file(no)
            Menu2.imagemagick.set_tooltip_markup(format(SetToolTip('imageMagick', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['inkscape']):
            Img.inkscape_img.set_from_file(yes)
            Menu2.inkscape.set_tooltip_markup(format(SetToolTip('inkscape', action.installed, action.remove_it)))
        else:
            Img.inkscape_img.set_from_file(no)
            Menu2.inkscape.set_tooltip_markup(format(SetToolTip('inkscape', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['mypaint']):
            Img.mypaint_img.set_from_file(yes)
            Menu2.mypaint.set_tooltip_markup(format(SetToolTip('mypaint', action.installed, action.remove_it)))
        else:
            Img.mypaint_img.set_from_file(no)
            Menu2.mypaint.set_tooltip_markup(format(SetToolTip('mypaint', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['pinta']):
            Img.pinta_img.set_from_file(yes)
            Menu2.pinta.set_tooltip_markup(format(SetToolTip('pinta', action.installed, action.remove_it)))
        else:
            Img.pinta_img.set_from_file(no)
            Menu2.pinta.set_tooltip_markup(format(SetToolTip('pinta', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['shotwell']):
            Img.shotwell_img.set_from_file(yes)
            Menu2.shotwell.set_tooltip_markup(format(SetToolTip('shotwell', action.installed, action.remove_it)))
        else:
            Img.shotwell_img.set_from_file(no)
            Menu2.shotwell.set_tooltip_markup(format(SetToolTip('shotwell', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['stellarium']):
            Img.stellarium_img.set_from_file(yes)
            Menu2.stellarium.set_tooltip_markup(format(SetToolTip('stellarium', action.installed, action.remove_it)))
        else:
            Img.stellarium_img.set_from_file(no)
            Menu2.stellarium.set_tooltip_markup(format(SetToolTip('stellarium', action.not_here, action.install_it)))