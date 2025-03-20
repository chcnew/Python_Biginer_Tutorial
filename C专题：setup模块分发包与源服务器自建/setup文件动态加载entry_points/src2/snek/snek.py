# _*_ coding: utf-8 _*_


"""Print an ASCII Snek.

Usage:
    snek [--type=TYPE]

"""
import docopt

normal_snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""

fancy_snek = """\
                          _,..,,,_
                     '``````^~"-,_`"-,_
       .-~c~-.                    `~:. ^-.
   `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
         `.   ;      _,--~~~~-._       `:.   ~. .~          `.
          .` ;'   .:`           `:       `:.   `    _.:-,.    `.
        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
       :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
       :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
        `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                     ~--..--'     ':.         .:'
                                                     ':..___.:'
"""


def get_sneks():
    return {
        'normal': normal_snek,
        'fancy': fancy_snek,
    }


def main():
    args = docopt.docopt(__doc__)
    snek_type = args['--type'] or 'normal'
    print(snek_type)
    print(get_sneks()[snek_type])


if __name__ == '__main__':
    main()
