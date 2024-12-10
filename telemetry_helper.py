import json

class LoggingConstants:
    """Defines logging message templates."""
    START_PROCESS = "PythonConsoleApp2  Start Process: {}"
    SUCCESS_PROCESS = "PythonConsoleApp2  Success Process: {}"
    WARNING_PROCESS = "PythonConsoleApp2 Warning Process: {}"
    EXCEPTION_PROCESS = "PythonConsoleApp2  Exception Process: {}"


class TelemetryHelper:

    @staticmethod
    def log_process(logger, telemetry_client, process_name, log_type, context=None, ex=None):
        # Ensure telemetry_client is valid
        if telemetry_client is None:
            raise ValueError("telemetry_client cannot be None")

        # Format the log message
        message_template = log_type.format(process_name)
        
        # Add context to telemetry if provided
        if context is not None:
            try:
                # Convert context to JSON string if it's a complex object
                context_json = json.dumps(context) if isinstance(context, (dict, list)) else context
                telemetry_client.track_trace(message_template, properties={"Context": context_json})
            except Exception as e:
                logger.error(f"Failed to log context: {e}")

        # Log to console and Application Insights based on the log type
        if log_type == LoggingConstants.START_PROCESS or log_type == LoggingConstants.SUCCESS_PROCESS:
            logger.info(message_template)
        elif log_type == LoggingConstants.WARNING_PROCESS:
            logger.warning(message_template)
        elif log_type == LoggingConstants.EXCEPTION_PROCESS:
            logger.error(message_template, exc_info=ex)

    @staticmethod
    def get_severity_level(log_type):
        """
        Maps log type to a severity level.

        :param log_type: The type of log to determine severity level for.
        :return: Severity level string.
        """
        if log_type == LoggingConstants.WARNING_PROCESS:
            return "Warning"
        elif log_type == LoggingConstants.EXCEPTION_PROCESS:
            return "Error"
        else:
            return "Information"