import pyfiglet
from datetime import date
from argparse import ArgumentParser
#from __future__ import print_function


def argparse():
    # .--Argparse-------------------------------------------------------------.
    # |                 _                                                     |
    # |                / \   _ __ __ _ _ __   __ _ _ __ ___  ___              |
    # |               / _ \ | '__/ _` | '_ \ / _` | '__/ __|/ _ \             |
    # |              / ___ \| | | (_| | |_) | (_| | |  \__ \  __/             |
    # |             /_/   \_\_|  \__, | .__/ \__,_|_|  |___/\___|             |
    # |                          |___/|_|                                     |
    # +-----------------------------------------------------------------------+
    # | Parse input arguments                                                 |
    # '-----------------------------------------------------------------------'
    """
    Generate a ASCII Banner comment for separating code blocks via pyfiglet.
    :param topic: The topic string
    :param comment: The comment string
    :param font: the figlet font
    :param width: the column width of the banner
    :return: The generated ASCII banner comment
    """

    parser = ArgumentParser(description="Generate ASCII banner comment")
    parser.add_argument('-t', '--topic',
                        help='The topic string',
                        type=str
                        )
    parser.add_argument('-c', '--comment',
                        help='The comment string',
                        type=str
                        )
    parser.add_argument('-f', '--font',
                        help='The font string. Default: standard',
                        type=str,
                        default='standard'
                        )
    parser.add_argument('-w', '--width',
                        help='The width integer. Default: 72',
                        type=int,
                        default=72
                        )

    main(**vars(parser.parse_args()))


def main(topic, comment, font, width):

    result = []

    # .--Top line-------------------------------------------------------------.
    # |                    _____             _ _                              |
    # |                   |_   _|__  _ __   | (_)_ __   ___                   |
    # |                     | |/ _ \| '_ \  | | | '_ \ / _ \                  |
    # |                     | | (_) | |_) | | | | | | |  __/                  |
    # |                     |_|\___/| .__/  |_|_|_| |_|\___|                  |
    # |                             |_|                                       |
    # +-----------------------------------------------------------------------+
    prefix = ".--"

    fill = width - len(prefix) - len(topic)

    suffix = ""
    for i in range(fill):
        suffix += "-"
    suffix += "."

    top_line = "# " + prefix + topic + suffix
    result.append(top_line)


    # .--pyfiglet-------------------------------------------------------------.
    # |                                __ _       _      _                    |
    # |                   _ __  _   _ / _(_) __ _| | ___| |_                  |
    # |                  | '_ \| | | | |_| |/ _` | |/ _ \ __|                 |
    # |                  | |_) | |_| |  _| | (_| | |  __/ |_                  |
    # |                  | .__/ \__, |_| |_|\__, |_|\___|\__|                 |
    # |                  |_|    |___/       |___/                             |
    # +-----------------------------------------------------------------------+
    fig = pyfiglet.figlet_format(topic, font)

    for line in fig.splitlines():
        diff = width - 2 - len(line)
        left_right = diff / 2

        if (left_right % 2) == 0:
            fill_r = ""
        else:
            fill_r = " "

        fill_l = ""

        for i in range(int(diff / 2)):
            fill_l += " "
            fill_r += " "
            
        fill_r += "|"

        line = '# | ' + fill_l + line + fill_r
        result.append(line)


    # .--Separator line-------------------------------------------------------.
    # |    ____                             _               _ _               |
    # |   / ___|  ___ _ __   __ _ _ __ __ _| |_ ___  _ __  | (_)_ __   ___    |
    # |   \___ \ / _ \ '_ \ / _` | '__/ _` | __/ _ \| '__| | | | '_ \ / _ \   |
    # |    ___) |  __/ |_) | (_| | | | (_| | || (_) | |    | | | | | |  __/   |
    # |   |____/ \___| .__/ \__,_|_|  \__,_|\__\___/|_|    |_|_|_| |_|\___|   |
    # |              |_|                                                      |
    # +-----------------------------------------------------------------------+
    first = True
    if first:
        sep = "+"
    else: 
        sep = "'"
    
    line_str = ""
    for elem in range(width - 1):
        line_str += "-"
    
    line = "# " + sep + line_str + sep
    result.append(line)


    # .--Comment line---------------------------------------------------------.
    # |      ____                                     _     _ _               |
    # |     / ___|___  _ __ ___  _ __ ___   ___ _ __ | |_  | (_)_ __   ___    |
    # |    | |   / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __| | | | '_ \ / _ \   |
    # |    | |__| (_) | | | | | | | | | | |  __/ | | | |_  | | | | | |  __/   |
    # |     \____\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__| |_|_|_| |_|\___|   |
    # |                                                                       |
    # +-----------------------------------------------------------------------+
    comment_length = len(comment)

    if comment_length > width:
        #FIXME: Line break if comment too long
        print("Comment too long")
    else:
        diff = width - 2 - comment_length
        fill = ""
        for i in range(diff):
            fill += " "
        fill += "|"
        
        line = "# | " + comment + fill
        result.append(line)


    # .--Separator line-------------------------------------------------------.
    # |    ____                             _               _ _               |
    # |   / ___|  ___ _ __   __ _ _ __ __ _| |_ ___  _ __  | (_)_ __   ___    |
    # |   \___ \ / _ \ '_ \ / _` | '__/ _` | __/ _ \| '__| | | | '_ \ / _ \   |
    # |    ___) |  __/ |_) | (_| | | | (_| | || (_) | |    | | | | | |  __/   |
    # |   |____/ \___| .__/ \__,_|_|  \__,_|\__\___/|_|    |_|_|_| |_|\___|   |
    # |              |_|                                                      |
    # +-----------------------------------------------------------------------+
    first = False
    if first:
        sep = "+"
    else: 
        sep = "'"
    
    line_str = ""
    for elem in range(width - 1):
        line_str += "-"
    
    line = "# " + sep + line_str + sep
    result.append(line)


    # .--Print----------------------------------------------------------------.
    # |                         ____       _       _                          |
    # |                        |  _ \ _ __(_)_ __ | |_                        |
    # |                        | |_) | '__| | '_ \| __|                       |
    # |                        |  __/| |  | | | | | |_                        |
    # |                        |_|   |_|  |_|_| |_|\__|                       |
    # |                                                                       |
    # +-----------------------------------------------------------------------+
    for elem in result:
        print(elem)


if __name__ == '__main__':
    argparse()