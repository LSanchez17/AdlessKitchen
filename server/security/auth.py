from fastapi.security import OAuth2PasswordBearer

# Can tie it to the route file itself, or specific routes that should be protected
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")
