from gi.repository import Gtk

class Builder:
    builder = Gtk.Builder()
    builder.add_from_file('./ui/main.ui')

    builder2 = Gtk.Builder()
    builder2.add_from_file('./ui/menu1.ui')
    grid_development = builder2.get_object("grid1")

    builder3 = Gtk.Builder()
    builder3.add_from_file('./ui/menu2.ui')
    grid_graphics = builder3.get_object("grid1")

    builder4 = Gtk.Builder()
    builder4.add_from_file('./ui/menu3.ui')
    grid_internet = builder4.get_object("grid1")

    builder5 = Gtk.Builder()
    builder5.add_from_file('./ui/menu4.ui')
    grid_multimedia = builder5.get_object("grid1")

    builder6 = Gtk.Builder()
    builder6.add_from_file('./ui/menu5.ui')
    grid_system = builder6.get_object("grid1")

    builder7 = Gtk.Builder()
    builder7.add_from_file('./ui/menu6.ui')
    grid_utilities = builder7.get_object("grid1")

    builder8 = Gtk.Builder()
    builder8.add_from_file('./ui/menu7.ui')
    grid_custom = builder8.get_object("grid1")

    # display text for each category while hovering it with your mouse
    button1 = builder.get_object("button1")
    button2 = builder.get_object("button2")
    button3 = builder.get_object("button3")
    button4 = builder.get_object("button4")
    button5 = builder.get_object("button5")
    button6 = builder.get_object("button6")
    button7 = builder.get_object("button7")

class SetMenuCategoriesTooltipNames:
    def __init__(self):
        Builder.button1.set_tooltip_text("Development")
        Builder.button2.set_tooltip_text("Graphics")
        Builder.button3.set_tooltip_text("Internet")
        Builder.button4.set_tooltip_text("Multimedia")
        Builder.button5.set_tooltip_text("System")
        Builder.button6.set_tooltip_text("Utilities")
        Builder.button7.set_tooltip_text("About")