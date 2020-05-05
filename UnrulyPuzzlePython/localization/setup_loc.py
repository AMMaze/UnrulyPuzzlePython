import sys
import os
import locale
import gettext


def lang_init():
    """
    Initialize a translation framework (gettext).
    Typical use::
        _ = lang_init()
    :return: A string translation function.
    :rtype: (str) -> str
    """
    _locale, _encoding = locale.getdefaultlocale()  # Default system values
    path = os.path.join(os.path.dirname(sys.argv[0]), 'localization/lang')
    if os.path.exists(path):
        lang = gettext.translation('UnrulyPuzzlePython', path, [_locale],
                                   fallback=True)
    else:
        lang = gettext.translation('UnrulyPuzzlePython', path,
                                   fallback=True)
    return lang.gettext
