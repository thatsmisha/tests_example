from reqres_in.api_reqres_in import get_user
from reqres_in.api_reqres_in import return_user_email
from reqres_in.api_reqres_in import create_new_user
import pytest
import allure

@pytest.mark.TestCreateUser
class TestCreateUser:

    @pytest.mark.reqres_in
    @pytest.mark.api
    @allure.feature('User creating')
    @allure.story('Testing user creating')
    @allure.severity('Blocker')
    def test_create_new_user(self, driver_api):
        response = create_new_user('Mark', 'Driver')
        assert response.status_code == 201, 'User has not been created. Status code: ' + str(response.status_code)

@pytest.mark.TestGetUser
class TestGetUser:

    @pytest.mark.reqres_in
    @pytest.mark.api
    @allure.feature('User info getting')
    @allure.story('Testing user get info')
    @allure.severity('High')
    def test_get_user_info(self, driver_api):
        response = get_user('5')
        assert response.status_code == 200, 'User info has not been returned. Status code: ' + str(response.status_code)

    @pytest.mark.reqres_in
    @pytest.mark.api
    @allure.feature('Check user')
    @allure.story('Testing exact user data')
    @allure.severity('High')
    def test_get_user_info(self, driver_api):
        response = get_user('5')
        email_fact = return_user_email(response)
        assert email_fact == 'charles.morris@reqres.in', 'User email is not as expected. It is: ' + email_fact


