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

    path = os.path.join(os.path.dirname(sys.argv[0]), 'lang')

    lang = gettext.translation('unruly_puzzle', path, [_locale])
    return lang.gettext
