import os
from random import choice
from configparser import ConfigParser
from gi.repository import Gtk

class ChangeLang(object):
    def save_lang(self, lang):
        with open('/tmp/.yoimnotpro.conf', 'wt') as f:
            f.write(lang)
    def combo_changed(self, combobox):
        from mymodules.builder import SetMenuCategoriesTooltipNames
        active = self.combobox.get_active_text()
        if active == "Български".encode('cp1251').decode('cp1251'):
            self.save_lang('bulgarian,cp1251')
            OpenCFGnSetLang()
            SetMenuCategoriesTooltipNames()
        if active == 'English':
            self.save_lang('english,utf-8')
            OpenCFGnSetLang()
            SetMenuCategoriesTooltipNames()
    def __init__(self):
        self.window = Gtk.Window()
        self.combobox = Gtk.ComboBoxText()
        self.combobox.append("", "Languages:")
        self.combobox.append("", "English")
        self.combobox.append("", "Български"\
            .encode('cp1251').decode('cp1251'))
        self.combobox.set_active(0)
        self.combobox.connect("changed", self.combo_changed)
        self.window.add(self.combobox)
        self.window.show_all()
        self.window.connect("destroy", lambda q: Gtk.main_quit())
        Gtk.main()
class OpenCFGnSetLang(object):
    def __init__(self):
        if os.path.isfile("/tmp/.yoimnotpro.conf"):
            with open('/tmp/.yoimnotpro.conf', 'rt') as f:
               read = f.read().split(',')
               action.encoding = read[1]
               action.section = read[0]
        else:
            action.encoding = 'utf-8'
            action.section = 'english'
        cfg = ConfigParser()
        cfg.readfp(open('mymodules/langs.ini'))
        enc = action.encoding
        for key, val in cfg.items(action.section):
            dec = val.encode(enc).decode(enc)
            #print(dec.decode('cp1251'))
            if key in ['development','graphics','internet','system',
            'multimedia','utilities','about', 'langs']:
                setattr(action, key, '<b>{}</b>'.format(dec))
            elif key in ['installed', 'not_here']:
                setattr(action, key, '<span foreground="{0}" weight="bold">{1}</span>'
                    .format(('green' if key == 'installed' else 'red'), dec))
            else:
                setattr(action, key, dec)
class CurrentCategoryDict(object):
    pass
class dial(object):
    def display_message(self, action2):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "{program_name} {was2} {inst_or_rem} {sucs}."
                .format(program_name=self._name, was2=action.was,
                    inst_or_rem=action2, sucs=action.successfully),
                title="{program_name} {random_message}"
                .format(program_name=self._name,
                    random_message=choice(self._dict_with_phrases[action2])))
        dialog.run()
        dialog.destroy()
    def __init__(self, *arg):
        self._name = arg[0]
        self._action = arg[1]
        self._dict_with_phrases = {
        action.installed2: (action.good_choice, action.thats_my_boy, action.i_like_it_too,
                    action.cheers, '>:-)', action.eyecandy),
        (action.not_here2 if action.section
            == 'bulgarian' else 'removed'): (action.how_dare_you, action.pitty_to_see_it_go, '>:-(', action.was_douchebag,
                    'LMAO', 'LOL', action.damn_you_bro)}
        self.display_message(action.installed2
                        if self._action == action.installed else (action.not_here2 if action.section
            == 'bulgarian' else 'removed'))
class SetToolTip(object):
    def __init__(self, *arg):
        self._arg = arg
    def __repr__(self):
        return '<b><i>{program_name}</i></b> {iz2} {maybe_here}.\n{click_to2} {apply_some_action_to} {it2}'\
        .format(program_name=self._arg[0].capitalize(), iz2=(('is' if action.section == 'english' else action.iz if self._arg[1]
        == action.installed else str())),
            maybe_here=self._arg[1], click_to2=action.click_to, apply_some_action_to=self._arg[2],
            it2=('it' if action.section == 'english' else action.it))
class action(object):
    encoding = str()
    section = str()
    langs = str()
    damn_you_bro = str()
    was_douchebag = str()
    pitty_to_see_it_go = str()
    how_dare_you = str()
    cheers = str()
    eyecandy = str()
    i_like_it_too = str()
    good_choice = str()
    thats_my_boy = str()
    program_description = str()
    dev_website = str()
    license = str()
    suggestions = str()
    comments = str()
    program_name = str()
    not_here = str()
    install_it = str()
    remove_it = str()
    installed = str()
    development = str()
    graphics = str()
    internet = str()
    multimedia = str()
    system = str()
    utilities = str()
    about = str()
    was = str()
    successfully = str()
    installed2 = str()
    not_here2 = str()
    iz = str()
    click_to = str()
    it = str()
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