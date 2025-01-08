# PrivacyProber

## Overview

PrivacyProber is a Python-based tool designed to scan and identify potential privacy leaks in Windows settings and applications. The program evaluates various settings and installed applications to provide a report on potential privacy concerns.

## Features

- Scans Windows telemetry settings to check the status of data collection.
- Lists installed applications that may have privacy implications.
- Generates a report in JSON format highlighting potential privacy issues.

## Requirements

- Python 3.x
- Windows operating system
- Administrative privileges to access system settings and application lists

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/privacyprober.git
    ```
2. Navigate to the project directory:
    ```bash
    cd privacyprober
    ```

## Usage

Run the program using Python:

```bash
python privacy_prober.py
```

The output will be a JSON report (`privacy_report.json`) containing the results of the privacy scan.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any changes or enhancements you would like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

PrivacyProber is designed for educational and informational purposes only. Use at your own risk. The authors are not responsible for any misuse or damage caused by this program.