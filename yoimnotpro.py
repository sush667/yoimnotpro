#!/usr/bin/env python3
import os
import sys
from mymodules.builder import Builder, SetMenuCategoriesTooltipNames
from mymodules.categories.menu7_button import Menu7, InitConnectMeSignals
import mymodules.categories.somesome
from mymodules.action.dial import action, OpenCFGnSetLang, ChangeLang
import cairo
from gi.repository import Gtk, GdkPixbuf, Gdk

class iod:

    # check if the program is started as root, else start it with gksudo
    if os.geteuid() != 0:
        arguments = ['', sys.executable] + sys.argv + [os.environ]
        os.execlpe('gksudo', *arguments)

    def on_button1_clicked(self, widget):
        mymodules.categories.somesome.menu1.load()
        self.vbox.remove(self.current_category)
        self.current_category = Builder.grid_development
        self.vbox.add(Builder.grid_development)

    def on_button2_clicked(self, widget):
        mymodules.categories.somesome.menu2.load()
        self.vbox.remove(self.current_category)
        self.current_category = Builder.grid_graphics
        self.vbox.add(Builder.grid_graphics)

    def on_button3_clicked(self, widget):
        mymodules.categories.somesome.menu3.load()
        self.vbox.remove(self.current_category)
        self.current_category = Builder.grid_internet
        self.vbox.add(Builder.grid_internet)

    def on_button4_clicked(self, widget):
        mymodules.categories.somesome.menu4.load()
        self.vbox.remove(self.current_category)
        self.current_category = Builder.grid_multimedia
        self.vbox.add(Builder.grid_multimedia)

    def on_button5_clicked(self, widget):
        mymodules.categories.somesome.menu5.load()
        self.vbox.remove(self.current_category)
        self.current_category = Builder.grid_system
        self.vbox.add(Builder.grid_system)

    def on_button6_clicked(self, widget):
        mymodules.categories.somesome.menu6.load()
        self.vbox.remove(self.current_category)
        self.current_category = Builder.grid_utilities
        self.vbox.add(Builder.grid_utilities)

    def on_button7_clicked(self, widget):
        aboutdialog = Gtk.AboutDialog()
        aboutdialog.set_program_name("1.7")
        aboutdialog.set_version(action.program_name)
        aboutdialog.set_logo(GdkPixbuf.Pixbuf.new_from_file("ui/yoimnotpro_icon.png"))
        aboutdialog.set_comments(action.program_description)
        aboutdialog.set_website("http://linux.sytes.net/")
        aboutdialog.set_website_label(action.dev_website)
        aboutdialog.set_authors(["Aaron Caffrey\nhttp://linux.sytes.net/",\
         "\n{Suggestions}:\nexcalibur1234\nKorrode\ntetrahderon\nAyceman\nAJ1000".format(Suggestions=action.suggestions), \
         "\n{Comments}:\nRichad\ndrumBE\nVerandert2.0\nLukimya\naaditya\nHardyH\ndcell\nrfkill 2.0".format(Comments=action.comments)])
        aboutdialog.set_copyright('{License}: GPLv3 - http://www.gnu.org/licenses/gpl.html'.format(License=action.license))
        aboutdialog.run()
        aboutdialog.destroy()

    def on_button8_clicked(self, widget):
        ChangeLang()

    def draw_transparency(self, widget, cr):
        cr.set_source_rgba(.1, .1, .1, 0.8)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

    def __init__(self):

        Builder.builder.connect_signals(self)

        self.current_category = Builder.grid_custom

        self.window = Builder.builder.get_object("window1")

        # it's horizontal box, separating the menu buttons from the ui files
        self.vbox = Builder.builder.get_object("box1")
        self.vbox.add(Builder.grid_custom)

        # transparancy
        self.window.screen = self.window.get_screen()
        self.window.visual = self.window.screen.get_rgba_visual()
        if self.window.visual is not None and self.window.screen.is_composited():
            self.window.set_visual(self.window.visual)
        self.window.set_app_paintable(True)
        self.window.connect("draw", self.draw_transparency)

        # css
        self.screen = Gdk.Screen.get_default()
        self.css_provider = Gtk.CssProvider()
        self.css_provider.load_from_path('ui/style.css')
        self.priority = Gtk.STYLE_PROVIDER_PRIORITY_USER
        self.context = Gtk.StyleContext()
        self.context.add_provider_for_screen(self.screen, self.css_provider, self.priority)

        OpenCFGnSetLang()
        InitConnectMeSignals()
        Menu7.load_icons_n_tooltips_at_startup()
        SetMenuCategoriesTooltipNames()

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

if __name__ == '__main__':
    iod()
    Gtk.main()