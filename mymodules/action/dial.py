from random import choice
from gi.repository import Gtk

class CurrentCategoryDict(object):
    pass

class dial(object):
    def display_message(self, action):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "{program_name} was {inst_or_rem} successfully."
                .format(program_name=self._name, inst_or_rem=action),
                title="{program_name} {random_message}"
                .format(program_name=self._name,
                    random_message=choice(self._dict_with_phrases[action])))
        dialog.run()
        dialog.destroy()

    def __init__(self, *arg):
        self._name = arg[0]
        self._action = arg[1]
        self._dict_with_phrases = {
        'installed': ('good choice', 'that\'s my boy', 'I like it too',
                    '- Cheers !', '>:-)', ' - Eyecandy ;-]'),
        'removed': (', how dare you ?', 'pitty to see it go', '>:-(', 'was douchebag...',
                    'LMAO', 'LOL', 'Damn You BRO !')}
        self.display_message('installed' 
                        if self._action == action.installed else 'removed')

class SetToolTip(object):
    def __init__(self, *arg):
        self._arg = arg
    def __repr__(self):
        return '<b><i>{program_name}</i></b> is {maybe_here}.\nClick to {apply_some_action_to} it.'\
        .format(program_name=self._arg[0].capitalize(), maybe_here=self._arg[1], apply_some_action_to=self._arg[2])

class action(object):
    program_description = 'Small app center'
    dev_website = "Developer Website"
    license = 'License'
    suggestions = 'Suggestions'
    comments = 'Comments'
    program_name = "Yo I\'m not pro"
    not_here = '<span foreground="red" weight="bold">not installed</span>'
    install_it = 'install'
    remove_it = 'remove'
    installed = '<span foreground="green" weight="bold">installed</span>'
    development = "<b>Development</b>"
    graphics = "<b>Graphics</b>"
    internet = "<b>Internet</b>"
    multimedia = "<b>Multimedia</b>"
    system = "<b>System</b>"
    utilities = "<b>Utilities</b>"
    about = "<b>About</b>"
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