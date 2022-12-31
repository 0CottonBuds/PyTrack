import plyer


class NotificationManager:
    def take_a_break(self):
        plyer.notification.notify(
            title="Hey bud, Take a break you've been working too hard.",
            message="You've been working too hard. Don't forget that taking breaks is beneficial for productivity!",
            app_icon=r"notificationIcons\break.ico",
            timeout=10,
        )  # type: ignore

    def get_back_to_work(self):
        plyer.notification.notify(
            title="Get nack to work!!",
            message="You've been procrastinating and your points are super low, Get back to work.",
            app_icon=r"notificationIcons\warning.ico",
            timeout=10,
        )  # type: ignore
