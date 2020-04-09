import pytest
import os


user = {"login": os.getenv("login"), "pwd": os.getenv("pwd")}


@pytest.mark.usefixtures("ukr_net")
@pytest.mark.usefixtures("driver")
class TestUkrNet:

    def test_ukr_net_login_logout(self):
        self.ukr_net.go_main_page()
        result = self.ukr_net.logging_in(user.get("login"), user.get("pwd"))
        assert result["email"] == f"{user['login']}@ukr.net" and result["text"] == "Увійти", \
            f"Test failed with unexpected result. Expected are: {user['login']}@ukr.net on logged in screen and" \
            f" button 'Увійти' available on the page. Actual: email - {result['email']}, button - {result['text']}"
