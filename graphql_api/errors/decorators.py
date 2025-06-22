import logging
from functools import wraps
from graphql_api.errors.api_errors import APIError
from sqlalchemy.exc import (
    SQLAlchemyError,
    IntegrityError,
    DisconnectionError,
    InternalError,
    ProgrammingError
)

logger = logging.getLogger(__name__)


def catch_db_errors(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except APIError as e:
            raise e
        except ValueError as e:
            raise APIError(f"Value error: {str(e)}",
                           code="VALUE_ERROR", status_code=400)
        except TypeError as e:
            logger.error(f"TypeError: {e}")
            raise APIError(f"Type error: {str(e)}",
                           code="TYPE_ERROR", status_code=400)
        except ProgrammingError as e:
            logger.error(f"ProgrammingError: {e}")
            raise APIError("Programming error (syntax or configuration)",
                           code="PROGRAMMING_ERROR", status_code=400)
        except IntegrityError as e:
            logger.error(f"IntegrityError: {e}")
            raise APIError("Integrity error (duplicate or constraint)",
                           code="INTEGRITY_ERROR", status_code=409)
        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemyError: {e}")
            raise APIError("Database error", code="DB_ERROR", status_code=500)
        except InternalError as e:
            logger.error(f"InternalError: {e}")
            raise APIError("Internal database error",
                           code="INTERNAL_DB_ERROR", status_code=500)
        except DisconnectionError as e:
            logger.error(f"DisconnectionError: {e}")
            raise APIError("Database connection error",
                           code="DB_CONNECTION_ERROR", status_code=503)
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            raise APIError(f"Unexpected error: {str(e)}",
                           code="UNEXPECTED_ERROR", status_code=500)
    return wrapper


def require_positive_id(arg_name: str = "id"):
    """
    Ensures that the given argument is a positive integer.
    Converts strings that look like ints, and raises APIError otherwise.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            raw = kwargs.get(arg_name, None)
            try:
                val = int(raw)
            except (TypeError, ValueError):
                message = (
                    f"Invalid '{arg_name}'—must be a positive integer, "
                    f"got {raw!r} of type {type(raw).__name__}"
                )
                raise APIError(message=message,
                               code="INVALID_INPUT", status_code=400)
            if val <= 0:
                raise APIError(f"'{arg_name}' must be a positive integer",
                               code="INVALID_INPUT", status_code=400)
            kwargs[arg_name] = val
            return fn(*args, **kwargs)
        return wrapper
    return decorator
