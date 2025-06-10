import os
from termcolor import cprint

os.system("cls" if os.name == "nt" else "clear")
print("LOGO PERTAMINA\n")

# logo_lines: (text, color, end) — jika end tidak ditentukan, default = '\n'
logo_lines = [
    ("                                        ███████████", "red", "\n"),
    ("                                          ███████████", "red", "\n"),
    ("                                            ███████████", "red", "\n"),
    ("                                              ███████████", "red", "\n"),
    ("                                                ███████████", "red", "\n"),
    ("                                                  ███████████", "red", "\n"),
    ("", None, "\n"),
    ("                             █████████████   ", "blue", ""),
    ("   ███████████  ", "green", ""),
    (" ████████    █████████  █████████   ████████    ███     ██      ██  ██  ██      ██      ███", "black", "\n"),
    ("                           █████████████   ", "blue", ""),
    ("   ███████████  ", "green", ""),
    ("   ██      ██  ██         ██      ██     ██      ██ ██    ████  ████  ██  █████   ██     ██ ██", "black", "\n"),
    ("                         █████████████   ", "blue", ""),
    ("   ███████████", "green", ""),
    ("       █████████   █████████  █████████      ██     ███████   ██  ██  ██  ███ ██  ███ ██    ███████", "black", "\n"),
    ("                      █████████████   ", "blue", ""),
    ("   ███████████", "green", ""),
    ("          ██          ██         ██      ██     ██    ██     ██  ██      ██  ██  ██    ████   ██     ██", "black", "\n"),
    ("                    █████████████   ", "blue", ""),
    ("   ███████████", "green", ""),
    ("            ██          █████████  ██       ██    ██   ██       ██ ██      ██  ██  ██      ██  ██       ██", "black", "\n"),
    ("                  █████████████    ", "blue", ""),
    ("   ███████████", "green", "\n"),
    ("                █████████████    ", "blue", "\n"),
    ("              █████████████    ", "blue", "\n")
]

# Cetak semua baris
for item in logo_lines:
    if len(item) == 3:
        text, color, end_char = item
    else:
        # fallback jika format hanya 2 elemen (text, color)
        text, color = item
        end_char = "\n"

    if color:
        cprint(text, color, end=end_char)
    else:
        print(text, end=end_char)
