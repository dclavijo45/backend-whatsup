from controllers.login import LoginController

login_v1 = {
    "login": "/login/v1/",
    "login_controller": LoginController.as_view("login_v1"),
    # ----------------------------------------------------------------
}