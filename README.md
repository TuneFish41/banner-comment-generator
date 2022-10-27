# ASCII banner-comment-generator

This script generates a ASCII banner for commenting purpose and seperating code blocks using pyfiglet. 

# Example

Use from command line:
```
>>> ./generate_comment.py -t 'Config' -c 'The user can override and set variables in config.cfg'
```

Prints:
```
# .--Config---------------------------------------------------------------.
# |                       ____             __ _                           |
# |                      / ___|___  _ __  / _(_) __ _                     |
# |                     | |   / _ \| '_ \| |_| |/ _` |                    |
# |                     | |__| (_) | | | |  _| | (_| |                    |
# |                      \____\___/|_| |_|_| |_|\__, |                    |
# |                                             |___/                     |
# +-----------------------------------------------------------------------+
# | The user can override and set variables in config.cfg                 |
# '-----------------------------------------------------------------------'
```

# Arguments
| Short | Argument   | Description                                                     | Value | Default       |
|:-----:|------------|-----------------------------------------------------------------|:-----:|:-------------:|
| -t    | --topic    | The topic used in top border and as figlet                      | str   | -             |
| -c    | --comment  | The comment used in the bottom section. Single or multiline.    | str   | -             |
| -f    | --font     | One of the possible fonts used for figlet                       | str   | standard      |
| -w    | --width    | Total width if the banner (except the line beginning e.g. "# ") | int   | 72            |
| -l    | --letter   | The letter(s) used at every line beginning                      | str   | #             |

Possible figlet fonts:
[fonts](http://www.figlet.org/fontdb.cgi)
