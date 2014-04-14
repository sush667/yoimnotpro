import os
from mymodules.action.dial import SetToolTip, action, dial

class StartKickingSomeNinjas:

    def locate_the_penguin(batman, f):
        if f == 'Menu7':
            from mymodules.categories.somesome import menu7
            batman.Find = menu7.dicti[batman.freeze]
        if f == 'Menu6':
            from mymodules.categories.somesome import menu6
            batman.Find = menu6.dicti[batman.freeze]
        if f == 'Menu5':
            from mymodules.categories.somesome import menu5
            batman.Find = menu5.dicti[batman.freeze]
        if f == 'Menu4':
            from mymodules.categories.somesome import menu4
            batman.Find = menu4.dicti[batman.freeze]
        if f == 'Menu3':
            from mymodules.categories.somesome import menu3
            batman.Find = menu3.dicti[batman.freeze]
        if f == 'Menu2':
            from mymodules.categories.somesome import menu2
            batman.Find = menu2.dicti[batman.freeze]
        if f == 'Menu1':
            from mymodules.categories.somesome import menu1
            batman.Find = menu1.dicti[batman.freeze]

        batman.nope = format(SetToolTip(batman.Find[3], action.not_here, action.install_it))
        batman.duh = format(SetToolTip(batman.Find[3], action.installed, action.remove_it))

    def __init__(batman, _, mister_freeze, and_feed_the_cat):
        #[0]executable_file, [1]img, [2]tooltip, [3]program_name
        #[0]executable_file, [1]img, [2]img, [3]tooltip, [4]tooltip, [5]program_name

        batman.freeze = mister_freeze
        no = action.gtk_no
        yes = action.gtk_yes
        batman.locate_the_penguin(and_feed_the_cat)

        def if_robin_has_spare_bike(*kill_mister_freeze):
            arg = kill_mister_freeze
            if not len(batman.Find) > 4:
                batman.Find[1].set_from_file(arg[0])
                batman.Find[2].set_tooltip_markup(arg[1])
                dial(batman.Find[3], arg[2])
            else:
                batman.Find[1].set_from_file(arg[0])
                batman.Find[2].set_from_file(arg[0])
                batman.Find[3].set_tooltip_markup(arg[1])
                batman.Find[4].set_tooltip_markup(arg[1])
                dial(batman.Find[5], arg[2])

        if os.path.isfile(batman.Find[0]):
            os.system('pacman -R {program} --noconfirm'.format(program=batman.freeze))
            if not os.path.isfile(batman.Find[0]):
                if_robin_has_spare_bike(no, batman.nope, action.remove_it)
        else:
            os.system('pacman -S {program} --noconfirm'.format(program=batman.freeze))
            if os.path.isfile(batman.Find[0]):
                if_robin_has_spare_bike(yes, batman.duh, action.installed)