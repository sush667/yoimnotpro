from random import choice
#from string import Template
from gi.repository import Gtk

class dial:
    def __init__(self, *arg):
        self._name = arg[0]
        self._action = arg[1]
        self._dict_with_phrases = {
        'installed': ('good choice', 'that\'s my boy', 'I like it too',
                    '- Cheers !', '>:-)'),
        'removed': (', how dare you ?', 'pitty to see it go', '>:-(', 'was douchebag...',
                    'LMAO', 'LOL')}
        if self._action == "installed":
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "{program_name} was installed successfully."
                    .format(program_name=self._name),
                    title="{program_name} {random_message}"
                    .format(program_name=self._name, random_message=choice(self._dict_with_phrases['installed'])))
            dialog.run()
            dialog.destroy()
        else:
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "{program_name} was removed successfully."
                    .format(program_name=self._name),
                    title="{program_name} {random_message}"
                    .format(program_name=self._name, random_message=choice(self._dict_with_phrases['removed'])))
            dialog.run()
            dialog.destroy()

#class SpamSpamBaby(type):
    #def __call__(self, *arg):
        #return Template('$program_name is $maybe_here.\nClick to $apply_some_action_to it.')\
        #.substitute(program_name=arg[0], maybe_here=arg[1], apply_some_action_to=arg[2])

#class SetToolTip(metaclass=SpamSpamBaby):
    #pass

class SetToolTip:
    def __init__(self, *arg):
        self._arg = arg
    def __repr__(self):
        return '{program_name} is {maybe_here}.\nClick to {apply_some_action_to} it.'\
        .format(program_name=self._arg[0].capitalize(), maybe_here=self._arg[1], apply_some_action_to=self._arg[2])

class action:
    program_description = 'Small app center'
    dev_website = "Developer Website"
    license = 'License'
    suggestions = 'Suggestions'
    comments = 'Comments'
    program_name = "Yo I\'m not pro"
    not_here = 'not installed'
    install_it = 'install'
    remove_it = 'remove'
    installed = 'installed'
    development = "Development"
    graphics = "Graphics"
    internet = "Internet"
    multimedia = "Multimedia"
    system = "System"
    utilities = "Utilities"
    about = "About"
    gtk_yes = './categories/gtk-yes.png'
    gtk_no = './categories/gtk-no.png'
    menu_img_66 = './categories/menu66.png'
    menu_img_5 = './categories/menu5.xpm'
    menu_img_4 = './categories/menu4.png'
    menu_img_3 = './categories/menu3.png'
    menu_img_2 = './categories/menu2.png'
    menu_img_1 = './categories/menu1.png'
    menu_img_55 = './categories/menu55.xpm'
    menu_img_11 = './categories/menu11.png'
    menu_img_22 = './categories/menu22.png'
    menu_img_33 = './categories/menu33.png'
    menu_img_44 = './categories/menu44.png'
    menu_img_6 = './categories/menu6.png'