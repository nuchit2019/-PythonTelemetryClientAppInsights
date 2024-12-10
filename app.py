import logging
import os
from dotenv import load_dotenv
from applicationinsights import TelemetryClient
from applicationinsights.logging import LoggingHandler
from telemetry_helper import LoggingConstants, TelemetryHelper

def process_flow(): 
    load_dotenv()
 
    INSTRUMENTATION_KEY = os.getenv('APPINSIGHTS_INSTRUMENTATION_KEY')
 
    if INSTRUMENTATION_KEY is None:
        print("Error: Application Insights Instrumentation Key is missing.")
        exit(1)

    telemetry_client = TelemetryClient(INSTRUMENTATION_KEY)
    logger = logging.getLogger("appLogger")
    logger.setLevel(logging.INFO)

    logging_handler = LoggingHandler(INSTRUMENTATION_KEY)
    logger.addHandler(logging_handler)

    # Example process name
    process_name = "Sample Process"

    try:
        # Log start process
        request = {"UserId": "user123", "Action": "Login", "Time": "2024-12-08T14:00:00"}
        
        TelemetryHelper.log_process(logger, telemetry_client, process_name, LoggingConstants.START_PROCESS,request)
        print(f"Start {process_name} Process")

        # Log warning process
        TelemetryHelper.log_process(logger, telemetry_client, process_name, LoggingConstants.WARNING_PROCESS,request)
        print(f"Warning {process_name} Process")

        # Log success process
        TelemetryHelper.log_process(logger, telemetry_client, process_name, LoggingConstants.SUCCESS_PROCESS,request)
        print(f"Success {process_name} Process")

        # Simulate an error
        #raise ValueError("Simulated error for testing")
        TelemetryHelper.log_process(logger, telemetry_client, process_name, LoggingConstants.EXCEPTION_PROCESS)
        print(f"********** 0 Exception in {process_name} Process")
    except Exception as e:
        # Log exception process
        TelemetryHelper.log_process(logger, telemetry_client, process_name, LoggingConstants.EXCEPTION_PROCESS, ex=e)
        print(f"Exception in {process_name} Process")

# Run the process flow when the script is executed
if __name__ == "__main__":
    process_flow()
