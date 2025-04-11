import logging
from pythonjsonlogger import jsonlogger


def setup_logging(logger_name: str = "myapp") -> logging.Logger:
	"""
	Configures logging for the application and Uvicorn, and returns a logger instance.

	Args:
		logger_name (str): Name of the application logger.

	Returns:
		logging.Logger: Configured application logger instance.
	"""
	# JSON formatter
	formatter = jsonlogger.JsonFormatter(
		'%(asctime)s %(levelname)s %(funcName)s %(message)s %(filename)s %(lineno)d'
	)

	# Stream handler
	handler = logging.StreamHandler()
	handler.setFormatter(formatter)

	# Root logger setup
	root_logger = logging.getLogger()
	if not root_logger.hasHandlers():
		root_logger.setLevel(logging.INFO)
		root_logger.addHandler(handler)

	# Uvicorn access logger setup
	uvicorn_access_logger = logging.getLogger("uvicorn.access")
	uvicorn_access_logger.handlers = [handler]
	uvicorn_access_logger.propagate = False

	# Uvicorn error logger setup
	uvicorn_error_logger = logging.getLogger("uvicorn.error")
	uvicorn_error_logger.handlers = [handler]
	uvicorn_error_logger.propagate = False

	# Application logger
	app_logger = logging.getLogger(logger_name)
	if not app_logger.hasHandlers():
		app_logger.setLevel(logging.INFO)
		app_logger.addHandler(handler)

	return app_logger
