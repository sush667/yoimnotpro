import os
from mymodules.action.find_program import Find
from mymodules.buttons_images import Img
from mymodules.builder import Builder
from mymodules.action.dial import SetToolTip, action

class Menu6:
     # get menu 6 application buttons
    docky = Builder.builder7.get_object("docky")
    emacs = Builder.builder7.get_object("emacs")
    vim = Builder.builder7.get_object("vim")
    galculator = Builder.builder7.get_object("galculator")
    gedit = Builder.builder7.get_object("gedit")
    gloobus = Builder.builder7.get_object("gloobus")
    leafpad = Builder.builder7.get_object("leafpad")
    scribes = Builder.builder7.get_object("scribes")
    tomboy = Builder.builder7.get_object("tomboy")
    tuxcards = Builder.builder7.get_object("tuxcards")
    imagewriter = Builder.builder7.get_object("imagewriter")
    sevenzip = Builder.builder7.get_object("sevenzip")
    # add tooltip for each application icon
    docky_icon_tooltip = Builder.builder7.get_object("docky_icon_tooltip")
    docky_icon_tooltip.set_tooltip_text("Docky is an advanced shortcut bar that sits at the edges of your screen.")
    emacs_icon_tooltip = Builder.builder7.get_object("emacs_icon_tooltip")
    emacs_icon_tooltip.set_tooltip_text("Emacs is a text editor.")
    vim_icon_tooltip = Builder.builder7.get_object("vim_icon_tooltip")
    vim_icon_tooltip.set_tooltip_text("Vim is a text editor")
    galculator_icon_tooltip = Builder.builder7.get_object("galculator_icon_tooltip")
    galculator_icon_tooltip.set_tooltip_text("galculator is an open source scientific calculator with a modern GUI.")
    gedit_icon_tooltip = Builder.builder7.get_object("gedit_icon_tooltip")
    gedit_icon_tooltip.set_tooltip_text("Gedit is lightweight text editor.")
    gloobus_icon_tooltip = Builder.builder7.get_object("gloobus_icon_tooltip")
    gloobus_icon_tooltip.set_tooltip_text(" Gloobus Preview is a program designed to preview the contents of a file or folder on Linux OS")
    leafpad_icon_tooltip = Builder.builder7.get_object("leafpad_icon_tooltip")
    leafpad_icon_tooltip.set_tooltip_text("Leafpad is a text editor")
    scribes_icon_tooltip = Builder.builder7.get_object("scribes_icon_tooltip")
    scribes_icon_tooltip.set_tooltip_text("Simple, slim and sleek, yet powerful text editor.")
    tomboy_icon_tooltip = Builder.builder7.get_object("tomboy_icon_tooltip")
    tomboy_icon_tooltip.set_tooltip_text("Tomboy is a desktop note-taking application")
    tuxcards_icon_tooltip = Builder.builder7.get_object("tuxcards_icon_tooltip")
    tuxcards_icon_tooltip.set_tooltip_text("TuxCards is a hierarical notebook.")
    imagewriter_icon_tooltip = Builder.builder7.get_object("imagewriter_icon_tooltip")
    imagewriter_icon_tooltip.set_tooltip_text("This tool is used for writing images to USB sticks.")
    sevenzip_icon_tooltip = Builder.builder7.get_object("sevenzip_icon_tooltip")
    sevenzip_icon_tooltip.set_tooltip_text("7-Zip is an open source file archiver")

    @staticmethod
    def on_button6_clicked():
        Img.image1.set_from_file(action.menu_img_1)
        Img.image2.set_from_file(action.menu_img_2)
        Img.image3.set_from_file(action.menu_img_3)
        Img.image4.set_from_file(action.menu_img_4)
        Img.image5.set_from_file(action.menu_img_5)
        Img.image6.set_from_file(action.menu_img_66)

        # check if those programs are installed and set appropriate sign
        if os.path.isfile(Find.program['docky']):
            Img.docky_img.set_from_file(action.gtk_yes)
            Menu6.docky.set_tooltip_text(format(SetToolTip('docky', action.installed, action.remove_it)))
        else:
            Img.docky_img.set_from_file(action.gtk_no)
            Menu6.docky.set_tooltip_text(format(SetToolTip('docky', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['emacs']):
            Img.emacs_img.set_from_file(action.gtk_yes)
            Menu6.emacs.set_tooltip_text(format(SetToolTip('emacs', action.installed, action.remove_it)))
        else:
            Img.emacs_img.set_from_file(action.gtk_no)
            Menu6.emacs.set_tooltip_text(format(SetToolTip('emacs', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['vim']):
            Img.vim_img.set_from_file(action.gtk_yes)
            Menu6.vim.set_tooltip_text(format(SetToolTip('vim', action.installed, action.remove_it)))
        else:
            Img.vim_img.set_from_file(action.gtk_no)
            Menu6.vim.set_tooltip_text(format(SetToolTip('vim', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['galculator']):
            Img.galculator_img.set_from_file(action.gtk_yes)
            Menu6.galculator.set_tooltip_text(format(SetToolTip('galculator', action.installed, action.remove_it)))
        else:
            Img.galculator_img.set_from_file(action.gtk_no)
            Menu6.galculator.set_tooltip_text(format(SetToolTip('galculator', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['gedit']):
            Img.gedit_img.set_from_file(action.gtk_yes)
            Menu6.gedit.set_tooltip_text(format(SetToolTip('gedit', action.installed, action.remove_it)))
        else:
            Img.gedit_img.set_from_file(action.gtk_no)
            Menu6.gedit.set_tooltip_text(format(SetToolTip('gedit', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['gloobus-preview']):
<<<<<<< HEAD
            Img.gloobus_img.set_from_file(action.gtk_yes)
            Menu6.gloobus.set_tooltip_text(format(SetToolTip('gloobus', action.installed, action.remove_it)))
=======
            Img.gloobus_img.set_from_file('./categories/gtk-yes.png')
            Menu6.gloobus.set_tooltip_text("Gloobus is installed.\nClick to remove it.")
>>>>>>> branch 'master' of https://github.com/wifiextender/yoimnotpro
        else:
            Img.gloobus_img.set_from_file(action.gtk_no)
            Menu6.gloobus.set_tooltip_text(format(SetToolTip('gloobus', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['leafpad']):
            Img.leafpad_img.set_from_file(action.gtk_yes)
            Menu6.leafpad.set_tooltip_text(format(SetToolTip('leafpad', action.installed, action.remove_it)))
        else:
            Img.leafpad_img.set_from_file(action.gtk_no)
            Menu6.leafpad.set_tooltip_text(format(SetToolTip('leafpad', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['scribes']):
            Img.scribes_img.set_from_file(action.gtk_yes)
            Menu6.scribes.set_tooltip_text(format(SetToolTip('scribes', action.installed, action.remove_it)))
        else:
            Img.scribes_img.set_from_file(action.gtk_no)
            Menu6.scribes.set_tooltip_text(format(SetToolTip('scribes', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['tomboy']):
            Img.tomboy_img.set_from_file(action.gtk_yes)
            Menu6.tomboy.set_tooltip_text(format(SetToolTip('tomboy', action.installed, action.remove_it)))
        else:
            Img.tomboy_img.set_from_file(action.gtk_no)
            Menu6.tomboy.set_tooltip_text(format(SetToolTip('tomboy', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['tuxcards']):
            Img.tuxcards_img.set_from_file(action.gtk_yes)
            Menu6.tuxcards.set_tooltip_text(format(SetToolTip('tuxcards', action.installed, action.remove_it)))
        else:
            Img.tuxcards_img.set_from_file(action.gtk_no)
            Menu6.tuxcards.set_tooltip_text(format(SetToolTip('tuxcards', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['imagewriter']):
            Img.imagewriter_img.set_from_file(action.gtk_yes)
            Menu6.imagewriter.set_tooltip_text(format(SetToolTip('imagewriter', action.installed, action.remove_it)))
        else:
            Img.imagewriter_img.set_from_file(action.gtk_no)
            Menu6.imagewriter.set_tooltip_text(format(SetToolTip('imagewriter', action.not_here, action.install_it)))

        if os.path.isfile(Find.program['7zip']):
            Img.sevenzip_img.set_from_file(action.gtk_yes)
            Menu6.sevenzip.set_tooltip_text(format(SetToolTip('7zip', action.installed, action.remove_it)))
        else:
            Img.sevenzip_img.set_from_file(action.gtk_no)
            Menu6.sevenzip.set_tooltip_text(format(SetToolTip('7zip', action.not_here, action.install_it)))
