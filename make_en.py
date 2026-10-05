# -*- coding: utf-8 -*-
"""Geriye dönük uyum: make_en.py <tr-kaynak> <çıkış-kökü> [sayfa ...]  ==  make_lang.py en ...
Asıl kod make_lang.py içinde (en | de)."""
import sys
from make_lang import *            # load_mem, _unph, make ... (export_todo.py bunları buradan alır)
from make_lang import _unph, main

if __name__ == "__main__":
    main("en", sys.argv[1:])
