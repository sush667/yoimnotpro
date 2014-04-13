import os
from mymodules.action.find_program2 import Find as find2
from mymodules.action.dial import SetToolTip, action, dial

class StartKickingSomeNinjas:

    def __init__(batman, _, mister_freeze):
        #[0]executable_file, [1]img, [2]tooltip, [3]program_name
        #[0]executable_file, [1]img, [2]img, [3]tooltip, [4]tooltip, [5]program_name
        Find = find2.program[mister_freeze]
        freeze = mister_freeze

        if not len(Find) > 4:
            nope = format(SetToolTip(Find[3], action.not_here, action.install_it))
            duh = format(SetToolTip(Find[3], action.installed, action.remove_it))
        else:
            nope = format(SetToolTip(Find[5], action.not_here, action.install_it))
            duh = format(SetToolTip(Find[5], action.installed, action.remove_it))
        no = action.gtk_no
        yes = action.gtk_yes

        def if_robin_has_spare_bike(*kill_mister_freeze):
            arg = [x for x in kill_mister_freeze]
            if not len(Find) > 4:
                Find[1].set_from_file(arg[0])
                Find[2].set_tooltip_markup(arg[1])
                dial(Find[3], arg[2])
            else:
                Find[1].set_from_file(arg[0])
                Find[2].set_from_file(arg[0])
                Find[3].set_tooltip_markup(arg[1])
                Find[4].set_tooltip_markup(arg[1])
                dial(Find[5], arg[2])

        if os.path.isfile(Find[0]):
            os.system('pacman -R {program} --noconfirm'.format(program=freeze))
            if not os.path.isfile(Find[0]):
                if_robin_has_spare_bike(no, nope, action.remove_it)
        else:
            os.system('pacman -S {program} --noconfirm'.format(program=freeze))
            if os.path.isfile(Find[0]):
                if_robin_has_spare_bike(yes, duh, action.installed)