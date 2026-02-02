# Secure File Transfer Monitoring System

## Project Overview
This project monitors file system activities to detect unauthorized file transfers,
file modifications, and integrity violations in sensitive directories.

It helps in identifying suspicious file operations along with the active process
responsible for the activity.

## Objectives
- Monitor sensitive folders in real-time
- Detect file creation, modification, deletion
- Log the active process responsible for file changes
- Verify file integrity using hashing techniques
- Generate audit logs for security analysis

## Technologies Used
- Python
- watchdog
- psutil
- hashlib

## Project Deliverables
- File transfer monitoring toolkit
- Activity logs and screenshots
- File integrity verification evidence
- Flowcharts and architecture diagrams
- Final project documentation and presentation

## How to Run
1. Install dependencies:
   pip install watchdog psutil

2. Run the monitoring script:
   python monitor.py

3. Perform file operations inside the monitored directory.

## Output
- Real-time terminal alerts
- Log files containing event details
- Integrity check results
