from argparse import ArgumentParser
import pyfiglet
import textwrap


def main(topic, comment, font, width, letter, border="|"):
    """Generate a ASCII Banner comment for separating code blocks via pyfiglet.

    Args:
        topic (str): The topic used in top border and as figlet
        comment (str): The comment used in the bottom section. Single or multiline.
        font (str): One of the possible fonts used for figlet
        width (int): Total width if the banner
        letter (str): The letter(s) used at every line beginning
    """
    result = []

    effective_width = width - 2


    """First generate top, bottom and middle border"""
    corner_symbols = [".", "+", "'"]

    topic_length = len(topic)
    first = True
    for symbol in corner_symbols:
        dotted = ""
        for i in range(effective_width):
            dotted += "-"
        if first is True:
            dotted = dotted[:2] + topic + dotted[2 + topic_length:]
            first = False
        line = f"{letter} {symbol}{dotted}{symbol}"


        result.append(line)


    """Generate ASCII figure using pyfiglet and insert it between top and middle border"""
    fig = pyfiglet.figlet_format(topic, font)

    position = 1
    for line in fig.splitlines():
        diff = effective_width - 2 - len(line)
        left_right = diff / 2

        if (left_right % 2) == 0:   # Width is even
            fill_r = ""
        else:                       # Width is odd
            fill_r = "  "           # FIXME

        #fill_r = ""
        fill_l = ""

        for i in range(int(diff / 2)):
            fill_l += " "
            fill_r += " "
        fill_r += f"{border}"

        line = f'{letter} {border} {fill_l}{line}{fill_r}'
        result.insert(position, line)
        position += 1


    """Next generate comment line and insert it between middle and bottom border"""
    comment_length = len(comment)

    if comment_length > effective_width:
        wrapped = textwrap.fill(comment, width = effective_width)   # FIXME

    else:
        diff = width - 3 - comment_length
        fill = ""
        for i in range(diff):
            fill += " "
        fill += f"{border}"
        line = f"{letter} {border} {comment}{fill}"
        result.insert(-1, line)


    """Print result list"""
    for elem in result:
        print(elem)


if __name__ == '__main__':
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
    parser.add_argument('-l', '--letter',
                        help='The letters used as line beginning. Default: #',
                        type=str,
                        default="#"
                        )

    args = parser.parse_args()

    main(**vars(args))
