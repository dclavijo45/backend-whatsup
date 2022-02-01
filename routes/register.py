from controllers.register import RegisterController

register_v1 = {
    "register": "/register/v1/",
    "register_controller": RegisterController.as_view("register_v1"),
    # ----------------------------------------------------------------
}