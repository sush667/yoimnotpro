from gi.repository import Gtk

def dial(name, action):
    if action == "1":
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "{program} was installed successfully."\
                .format(program=name))
        dialog.run()
        dialog.destroy()
    else:
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "{program} was removed successfully."\
                .format(program=name))
        dialog.run()
        dialog.destroy()
