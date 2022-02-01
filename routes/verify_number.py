from controllers.verify_number import VerifyNumberController

verify_number_v1 = {
    "verify_number": "/verify_number/v1/",
    "verify_number_controller": VerifyNumberController.as_view("verify_number_v1"),
    # ----------------------------------------------------------------
}