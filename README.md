Here’s a summarized README file for your program:

---

# Python Console Application with Application Insights

This Python application demonstrates how to log process flows and telemetry data to Application Insights. It uses the Application Insights SDK and a helper class `TelemetryHelper` to streamline logging. The program tracks different stages of a process (`START`, `WARNING`, `SUCCESS`, `EXCEPTION`) and sends logs and telemetry data to Azure Application Insights.

## Features

- Logs events to Application Insights.
- Supports structured logging with custom context.
- Provides severity-level mapping for log messages.
- Demonstrates logging for **Start**, **Warning**, **Success**, and **Exception** stages.

---

## Project Structure

- **`.env`**: Stores the Application Insights Instrumentation Key.
- **`telemetry_helper.py`**: Contains helper classes for logging and telemetry integration.
- **`app.py`**: Main application logic, including the `process_flow` function that simulates a sample process.

---

## Prerequisites

1. **Python 3.7 or later**.
2. **Azure Application Insights**:
   - Create an Application Insights resource in Azure.
   - Copy the Instrumentation Key.

---

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository
   ```

2. Install dependencies:

   ```bash
   pip install python-dotenv
   pip install opencensus-ext-azure
   pip install opencensus-ext-logging 
   pip install applicationinsights
   ```

3. Create a `.env` file in the project root and add your Application Insights Instrumentation Key:

   ```env
   APPINSIGHTS_INSTRUMENTATION_KEY=your-application-insights-instrumentation-key
   ```

4. Verify `requirements.txt` contains:

   ```text
   python-dotenv
   applicationinsights
   ```

---

## Running the Program

1. Run the application using the command:

   ```bash
   python app.py
   ```

2. The program logs the following stages to the console and Application Insights:
   - Start Process
   - Warning Process
   - Success Process
   - Exception Process (simulated)

---

## Example Output

Console logs:

```plaintext
Start Sample Process Process
Warning Sample Process Process
Success Sample Process Process
********** 0 Exception in Sample Process Process
```

Azure Application Insights logs will reflect the same events with additional telemetry details.

---

## Troubleshooting

- **Missing Instrumentation Key**: Ensure the `.env` file contains a valid Application Insights Instrumentation Key.
- **Telemetry Errors**: Check internet connectivity and ensure the Azure resource is active.

---

## Author

For questions or support, please contact:  
**Nuchit Atjanawat**  
**Email**: nuchit@outlook.com  
**GitHub**: [nuchit2019](https://github.com/nuchit2019)


---

This README file serves as a guide for setting up, running, and understanding the program. Add more sections as needed for advanced use cases or future features.
