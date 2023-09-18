# Apache Log Analyzer Python

This Python-based application is designed to analyze Apache server logs and provide useful statistics. It offers a range of features to help users gain insights from their server logs.

## Features

- **Log Parsing**: The application parses Apache server logs to extract relevant information like IP addresses, requested pages, status codes, and response sizes.

- **Basic Statistics**: It provides basic statistics such as total requests, unique IP addresses, most accessed pages, and common status codes.

- **Advanced Analytics**: Users can delve deeper into the data with advanced analytics like hourly traffic patterns, popular user agents, and more. (On going)

- **Search and Filter**: The application allows users to search and filter logs based on specific criteria such as IP address, date, page, and status code. (On going)

- **Export Reports**: Reports can be exported in various formats for further analysis or sharing with others. (On going)

- **User-Friendly Interface**: The application features an intuitive and easy-to-use interface for a seamless user experience. (Continuous Improvement)

- **Log Generation Tool**: Included in the `log Generator` folder is a program named `apache-fake-log-gen.py`, originally created by kiritbasu. It has been converted to Python 3.10 by Ricardo Saude to aid in testing the app.

## Getting Started

**Installation**:

1. Clone the repository to your local machine.
2. Install any required dependencies by running `pip install -r requirements.txt`.

**Usage**:

- Run the application with Python 3.10 using the command `python app.py`.
- Follow the prompts to load and analyze your Apache server log file.

**Testing**:

- To generate sample logs for testing, use the provided log generation tool in the `log Generator` folder.

## Dependencies

- Python 3.10
- Additional dependencies are listed in `requirements.txt`.

## Acknowledgements

- The log generation tool (`apache-fake-log-gen.py`) was originally created by kiritbasu. The Python 3.10 conversion was done by Ricardo Saude.
