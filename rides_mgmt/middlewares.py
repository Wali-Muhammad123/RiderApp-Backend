from urllib.parse import parse_qsl
from channels.middleware import BaseMiddleware
from channels.sessions import CookieMiddleware, SessionMiddleware
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth import get_user_model


class JwtAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        query_string = scope.get('query_string', b'').decode()
        token = dict(parse_qsl(query_string)).get('token', None)

        if token:
            try:
                # This will automatically validate the token and raise an error if token is invalid
                UntypedToken(token)
            except (InvalidToken, TokenError) as e:
                # Token is invalid
                scope['user'] = AnonymousUser()
                return await self.inner(scope, receive, send)

            # Then try to get User by ID contained in the token
            user_id = UntypedToken(token).get('user_id')
            user = get_user_model().objects.get(id=user_id)
            scope['user'] = user

        return await self.inner(scope, receive, send)


# Function that returns the middleware with the right configuration
def JwtAuthMiddlewareStack(inner):
    return CookieMiddleware(SessionMiddleware(JwtAuthMiddleware(inner)))
