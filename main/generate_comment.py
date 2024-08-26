from argparse import ArgumentParser
import pyfiglet
import textwrap


def main(topic, comment, font, width, letter, border="|"):
    """
    Generate an ASCII banner comment for separating code blocks via pyfiglet.

    Args:
        topic (str): The topic used in the top border and as a figlet.
        comment (str): The comment used in the bottom section. Single or multiline.
        font (str): One of the possible fonts used for figlet.
        width (int): Total width of the banner.
        letter (str): The letter(s) used at every line's beginning.
    """
    result = []
    effective_width = width - 4 # Account for border and letter space
    comment_width   = width - 6 # Same as effective width but also includes whitepaces in beginning and ending of comment

    # Generate top, bottom, and middle horizontal ruler
    corner_symbols = [".", "+", "'"]
    first_line = True
    for symbol in corner_symbols:
        if first_line:
            # Insert topic into the top border
            topic_in_border = topic.ljust(effective_width - 2, '-')
            horizontal_ruler = "--" + topic_in_border
            first_line = False
        else:
            horizontal_ruler = "-" * (effective_width)
        line = f"{letter} {symbol}{horizontal_ruler}{symbol}"
        result.append(line)

    # Generate ASCII art using pyfiglet and insert it
    fig = pyfiglet.figlet_format(topic, font=font)
    fig_lines = fig.splitlines()

    for line in fig_lines:
        line_content = line.center(effective_width)  # Center the figlet text
        ascii_line = f"{letter} {border}{line_content}{border}"
        result.insert(-2, ascii_line)

    # Generate comment line(s)
    wrapped_comment = textwrap.wrap(comment, width=comment_width)
    print(wrapped_comment)
    for comment_line in wrapped_comment:
        padded_comment = comment_line.ljust(comment_width)
        comment_ascii = f"{letter} {border} {padded_comment} {border}"
        result.insert(-1, comment_ascii)

    # Print result
    for elem in result:
        print(len(elem), elem)


if __name__ == '__main__':
    parser = ArgumentParser(description="Generate an ASCII banner comment")
    parser.add_argument('-t', '--topic',
                        help='The topic string',
                        type=str,
                        required=True
                        )
    parser.add_argument('-c', '--comment',
                        help='The comment string',
                        type=str,
                        required=True
                        )
    parser.add_argument('-f', '--font',
                        help='The font string. Default: standard',
                        type=str,
                        default='standard'
                        )
    parser.add_argument('-w', '--width',
                        help='The width of the banner. Default: 72',
                        type=int,
                        default=72
                        )
    parser.add_argument('-l', '--letter',
                        help='The character used at the beginning of every line. Default: #',
                        type=str,
                        default="#"
                        )

    args = parser.parse_args()

    main(**vars(args))
