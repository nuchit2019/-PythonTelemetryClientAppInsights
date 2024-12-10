
---

# **Azure Application Insights Logging Example**

This project demonstrates how to log messages to **Azure Application Insights** and the console in a Python application. The setup includes logging for various process stages like start, success, warnings, and exceptions.

---

## **Project Structure**

```
my_project/
│
├── app.py                   # Main application flow
├── app_insights_config.py   # Azure Application Insights configuration
├── app_insights_helper.py   # Log helper class for centralized logging
└── app_logging_constants.py # Log message templates
```

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.7 or higher installed
- Azure Application Insights account with an Instrumentation Key

---

### **2. Install Dependencies**

Run the following commands to install the required libraries:

```bash
pip install python-dotenv
pip install opencensus-ext-azure
pip install opencensus-ext-logging 
pip install applicationinsights


```

---

### **3. Configuration**

Update the `app_insights_config.py` file with your **Instrumentation Key**:

```python
# app_insights_config.py
INSTRUMENTATION_KEY = 'your-application-insights-instrumentation-key'
```

---

### **4. Project Files**

#### **app_logging_constants.py**
Contains templates for log messages.

```python
APPLICATION_NAME = "PythonConsoleApp"

START_PROCESS = f"{APPLICATION_NAME} Start Process: {{}}"
WARNING_PROCESS = f"{APPLICATION_NAME} Warning Process: {{}}"
SUCCESS_PROCESS = f"{APPLICATION_NAME} Success Process: {{}}"
EXCEPTION_PROCESS = f"{APPLICATION_NAME} Exception Process: {{}}" 
```

---

#### **app_insights_helper.py**
Provides centralized logging to both console and Azure Application Insights.

```python
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.tracer import Tracer
from opencensus.trace.execution_context import set_opencensus_tracer
from opencensus.trace.samplers import ProbabilitySampler
from app_logging_constants import START_PROCESS, SUCCESS_PROCESS, WARNING_PROCESS, EXCEPTION_PROCESS
from app_insights_config import INSTRUMENTATION_KEY


class AppInsightsLogHelper:
    """Helper for logging to console and Azure Application Insights."""

    def __init__(self):
        # Set up logger
        self.logger = logging.getLogger("AzureLogger")
        self.logger.setLevel(logging.INFO)
        azure_handler = AzureLogHandler(connection_string=f"InstrumentationKey={INSTRUMENTATION_KEY}")
        self.logger.addHandler(azure_handler)

        # Set up tracer
        self.tracer = Tracer(
            exporter=AzureExporter(connection_string=f"InstrumentationKey={INSTRUMENTATION_KEY}"),
            sampler=ProbabilitySampler(1.0)
        )
        set_opencensus_tracer(self.tracer)

    def log_start_process(self, log_template, process_name):
        """Logs the start of a process."""
        message = log_template.format(process_name)
        self.logger.info(message)
        with self.tracer.span(name=f"Start {process_name}"):
            pass

    def log_success_process(self, log_template, process_name):
        """Logs the successful completion of a process."""
        message = log_template.format(process_name)
        self.logger.info(message)
        with self.tracer.span(name=f"Success {process_name}"):
            pass

    def log_warning_process(self, log_template, process_name):
        """Logs a warning during a process."""
        message = log_template.format(process_name)
        self.logger.warning(message)
        with self.tracer.span(name=f"Warning {process_name}"):
            pass

    def log_exception_process(self, log_template, process_name, exception):
        """Logs an exception that occurs during a process."""
        message = log_template.format(process_name)
        self.logger.error(message, exc_info=True)
        with self.tracer.span(name=f"Exception {process_name}"):
            self.tracer.add_attribute("exception.message", str(exception))
            self.tracer.add_attribute("exception.stack_trace", str(exception))
```

---

#### **app.py**
Main application flow with logging examples.

```python
from app_insights_helper import AppInsightsLogHelper
from app_logging_constants import START_PROCESS, SUCCESS_PROCESS, WARNING_PROCESS, EXCEPTION_PROCESS


def process_flow():
    log_helper = AppInsightsLogHelper()
    process_name = "HOME"

    try:
        # Log Start Process
        log_helper.log_start_process(START_PROCESS, process_name)
        print(f"Start {process_name} Process")
        
        # Log Warning Process
        log_helper.log_start_process(WARNING_PROCESS, process_name)
        print(f"Warning {process_name} Process")

        # Log Success Process
        log_helper.log_success_process(SUCCESS_PROCESS, process_name)
        print(f"Success {process_name} Process")
  
    except Exception as e:
        # Log Exception Process
        log_helper.log_exception_process(EXCEPTION_PROCESS, process_name, e)
        print(f"Exception in {process_name} Process")
        raise


if __name__ == "__main__":
    process_flow()
```

---

## **Running the Application**

Run the application with:

```bash
python app.py
```

---

## **Features**

- Logs key process stages (`Start`, `Success`, `Warning`, `Exception`) to both **Azure Application Insights** and the console.
- Centralized helper class for consistent logging.
- Uses **OpenCensus** for distributed tracing.

---

## **Customization**

1. Update `app_logging_constants.py` to add or modify log templates.
2. Use the `AppInsightsLogHelper` class in other modules for consistent logging.

---

## **Example Output**

**Console Output:**

```text
Start HOME Process
Warning HOME Process
Success HOME Process
```

**Azure Application Insights:**

- Logs appear under **Traces** and **Exceptions** in your Application Insights resource.

---

## **Dependencies**

- `opencensus-ext-azure`
- `opencensus-ext-logging`