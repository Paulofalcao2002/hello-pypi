#!/usr/bin/env python3
from dev_aberto import hello
from datetime import datetime
from babel.dates import format_date
import gettext

if __name__ == "__main__":
    gettext.bindtextdomain("cli", "locale")
    gettext.textdomain("cli")
    _ = gettext.gettext

    date, name = hello()
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%Sz")
    print(_("Last commit made in:"), format_date(date, format="long"), _("by"), name)
