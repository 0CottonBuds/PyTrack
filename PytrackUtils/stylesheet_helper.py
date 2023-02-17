from PySide6.QtWidgets import QApplication
from .config_helper import *

def change_stylesheet(object, theme: str, app:QApplication):
    '''Function that changes the stylesheet of application.
    Params:
        object: After changing the stylesheet this object will use its update() method to see the changes.
        style : (str) Theme to use.
        app : (QApplication) Application object that we want to apply the stylesheet.
    '''
    _theme = open(f"themes/{theme}_theme.css","r").read()
    app.setStyleSheet(_theme)
    print(f"Changed theme to {theme} theme.")
    object.update()

def get_themes():
    """Function that returns a list of themes that is recorded in the config file.
    
    Return:
        A list of stings containing the names for themes.
    """
    themes = str(read_config("settingsConfig.ini", "App", "themes"))
    themes = themes.split("-")
    return themes

get_themes()
