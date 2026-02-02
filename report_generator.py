from datetime import datetime
import os

LOG_FILE = "logs/file_activity.log"
REPORT_FILE = "reports/audit_report.txt"

def generate_report():
    if not os.path.exists(LOG_FILE):
        print("No log file found.")
        return

    with open(LOG_FILE, "r") as log:
        lines = log.readlines()

    if not lines:
        print("Log file is empty. No events to report.")
        return

    with open(REPORT_FILE, "w") as report:
        report.write("==== FILE TRANSFER AUDIT REPORT ====\n")
        report.write(f"Generated on: {datetime.now()}\n\n")

        for line in lines:
            report.write(line)

    print("Audit report generated successfully.")

def generate_report():
    with open("logs/file_activity.log", "r") as log:
        data = log.read()

    with open("reports/audit_report.txt", "w") as report:
        report.write("SECURE FILE TRANSFER MONITORING REPORT\n")
        report.write("="*45 + "\n\n")
        report.write(data)

    print("Audit report generated successfully")


if __name__ == "__main__":
    generate_report()
