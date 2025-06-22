from graphql import GraphQLError


class APIError(GraphQLError):
    def __init__(self, message, code="BAD_REQUEST", status_code=400, **kwargs):
        code = code.upper()
        status_code = status_code or 400
        extensions = {
            "code": code,
            "status": status_code,
            "message": message,
            **kwargs
        }
        super().__init__(message, extensions=extensions)
