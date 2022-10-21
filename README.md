# ASCII banner-comment-generator

This script generates a ASCII banner for commenting purpose and seperating code blocks. 

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
| Short | Argument   | Description                                 | Value | Default       |
|:-----:|------------|---------------------------------------------|:-----:|:-------------:|
| -t    | --topic    | The short string that is used in the banner | str   | -             |
| -c    | --comment  | The comment that is output under the banner | str   | -             |
| -f    | --font     | The used figlet font                        | str   | standard      |
| -w    | --width    | The width of the banner in chars            | int   | 72            |

Possible figlet fonts:
[fonts](http://www.figlet.org/fontdb.cgi)