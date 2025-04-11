# import logging
# from pythonjsonlogger import jsonlogger
#
# def setup_logging():
#     """
#     Configures logging for both the application and Uvicorn.
#     """
#     # Root logger
#     root_logger = logging.getLogger()
#     root_logger.setLevel(logging.INFO)
#
#     # JSON formatter
#     formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(funcName)s %(message)s %(filename)s %(lineno)d')
#
#     # Stream handler for console output
#     handler = logging.StreamHandler()
#     handler.setFormatter(formatter)
#     root_logger.addHandler(handler)
#
#     # Uvicorn access logger
#     uvicorn_access_logger = logging.getLogger("uvicorn.access")
#     uvicorn_access_logger.handlers = [handler]
#     uvicorn_access_logger.propagate = False
#
#     # Uvicorn error logger
#     uvicorn_error_logger = logging.getLogger("uvicorn.error")
#     uvicorn_error_logger.handlers = [handler]
#     uvicorn_error_logger.propagate = False