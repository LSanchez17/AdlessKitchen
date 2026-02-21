from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends

# Can tie it to the route file itself, or specific routes that should be protected
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Helper to get the login form data
def get_login_form(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> OAuth2PasswordRequestForm:
    return form_data