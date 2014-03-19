from random import choice
from gi.repository import Gtk

def dial(name, action):
    dict_with_phrases = {
    'installed': ('good choice', 'that\'s my boy', 'I like it too',
                '- Cheers !', '>:-)'),
    'removed': (', how dare you ?', 'pitty to see it go', '>:-(', 'was douchebag...',
                'LMAO', 'LOL')}
    if action == "installed":
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "{program_name} was installed successfully."
                .format(program_name=name),
                title="{program_name} {random_message}"
                .format(program_name=name, random_message=choice(dict_with_phrases['installed'])))
        dialog.run()
        dialog.destroy()
    else:
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "{program_name} was removed successfully."
                .format(program_name=name),
                title="{program_name} {random_message}"
                .format(program_name=name, random_message=choice(dict_with_phrases['removed'])))
        dialog.run()
        dialog.destroy()