import os

from src.ukr_net import UkrNet

user = {"login": os.getenv("login"), "pwd": os.getenv("pwd")}


def test_ukr_net_login_logout(browser):
    ukr_net = UkrNet(browser)
    ukr_net.go_main_page()
    result = ukr_net.logging_in(user.get("login"), user.get("pwd"))
    assert result["email"] == f"{user['login']}@ukr.net", \
        f"Test failed with unexpected result. Expected are: {user['login']}@ukr.net on logged in screen and" \
        f" button 'Увійти' available on the page. Actual: email - {result['email']}"
    r = ukr_net.logging_out()
    assert r == "Увійти", \
        f"Test failed with unexpected result. Expected are: button 'Увійти' available on the page. Actual: " \
        f"button - {r}"
