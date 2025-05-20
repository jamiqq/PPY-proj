import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

# === Cartoon Style Color Palette ===
PRIMARY = "#FF6F61"         # Coral
SECONDARY = "#FFD93D"       # Sunny yellow
BACKGROUND = "#FFF8E7"      # Soft cream
TEXT_COLOR = "#FF6F61"
TEXT = "#333"
BUTTON_BG = "#FF6F61"
BUTTON_HOVER = "#FF4B3E"
ENTRY_BG = "#FFF"
BORDER_COLOR = "#333333"
SUCCESS = "#4CAF50"
ERROR = "#F44336"

# === Fonts ===
FONT_TITLE = ("Comic Sans MS", 20, "bold")
FONT_NORMAL = ("Comic Sans MS", 14)
FONT_SMALL = ("Comic Sans MS", 12)

def setup_styles():
    style = ttk.Style()

    try:
        style.theme_use("clam")
    except:
        pass

    # Base widget styles
    style.configure("TFrame", background=BACKGROUND)
    style.configure("TLabel",
                    background=BACKGROUND,
                    foreground=TEXT,
                    font=FONT_NORMAL)

    style.configure("TEntry",
                    padding=8,
                    relief="flat",
                    borderwidth=2,
                    font=FONT_NORMAL,
                    fieldbackground=ENTRY_BG,
                    background=ENTRY_BG)

    style.configure("TButton",
                    background=BUTTON_BG,
                    foreground="white",
                    font=FONT_NORMAL,
                    borderwidth=0,
                    padding=(12, 6))
    style.map("TButton",
              background=[("active", BUTTON_HOVER)],
              relief=[("pressed", "sunken")])

    style.configure("Title.TLabel",
                    font=FONT_TITLE,
                    background=BACKGROUND,
                    foreground=PRIMARY)

    style.configure("Error.TLabel",
                    foreground=ERROR,
                    background=BACKGROUND,
                    font=FONT_SMALL)

    style.configure("Success.TLabel",
                    foreground=SUCCESS,
                    background=BACKGROUND,
                    font=FONT_SMALL)

    # Global font override for legacy widgets
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(family="Comic Sans MS", size=11)