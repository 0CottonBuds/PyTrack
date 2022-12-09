import sqlite3


def check_app_type(last_active_window) -> str:
    productive_apps = ["Visual Studio Code"]
    bad_apps = ["Opera"]
    app_type = ""

    separated_title: list[str] = last_active_window.title.split("- ")
    for app in productive_apps:
        if separated_title[-1].upper() == app.upper():
            print(f"this is an productive app {str(separated_title)}")
            app_type = "good"
    for app in bad_apps:
        if separated_title[-1].upper() == app.upper():
            print(f"this is a bad app {str(separated_title)}")
            app_type = "bad"

    return app_type
