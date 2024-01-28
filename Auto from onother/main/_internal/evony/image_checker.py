from lib.manage_screen import ManageScreen


class LoginFailedException(Exception):
    pass


class ImageChecker:
    def __init__(self, device):
        self.manage_screen = ManageScreen(device)
        self.current_screenshot = None

    def get_screenshot(self, is_force=False):
        return self.manage_screen.get_screenshot()

    def check_image(self, image_name, is_tap=True, screenshot=None):
        return self.manage_screen.find_and_tap_button(image_name, is_tap, screenshot)

    def is_restart_screen(self, is_tap=False):
        return self.check_image('restart_btn.png', is_tap, self.get_screenshot(True))

    def is_cancel_button(self):
        self.get_screenshot(True)
        return self.check_image('cancel_quit.png')

    def is_loading_game(self):
        return self.check_image('loading_game.png', False)

    def is_no_alliance(self):
        return self.check_image('no_alliance.png', False)

    def is_search_popup(self):
        return self.check_image('go_btn_in_search.png', False)

    def assert_logged_in(self):
        if not self.is_restart_screen():
            raise LoginFailedException("Login failed. Waiting for the next 10 minutes.")

    def solo_mode(self):
        return self.boss_available() and self.solo_button() and self.march_interface()

    def boss_available(self):
        return self.check_image('atk_btn.png') or self.check_image('atk_btn2.png')

    def general_available(self):
        return not self.check_image('no_general.png', False)

    def march_interface(self):
        return self.check_image('march_title.png', False)

    def solo_button(self):
        return self.check_image('solo_btn.png')

    def rally_button(self):
        return self.check_image('rally_btn.png')

    def rally_interface(self):
        return self.check_image('rally_interface.png', False)
