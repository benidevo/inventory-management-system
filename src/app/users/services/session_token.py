import logging

from flask import current_app

from app.users.models import User
from core.error_handlers import APPError
from core.resources.jwt import JWTClient

logger = logging.getLogger(__name__)


class SessionTokenService:
    def generate_token(self, data):
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            raise APPError(401, "Invalid Credentials")

        jwt_token = self.jwt.create_token(user.id)

        return jwt_token

    @property
    def jwt(self):
        config = current_app.config
        return JWTClient(config)
