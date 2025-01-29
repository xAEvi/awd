from ..Services.create_user_service import CreateUserService
from ..Services.login_service import LoginService

def load_routes(api):
    api.add_resource(CreateUserService, '/create/user')
    api.add_resource(LoginService, '/user/login')