import os
import subprocess
import json

class PrivacyProber:
    def __init__(self):
        self.results = {}

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout.strip()
        except subprocess.SubprocessError as e:
            print(f"Error executing command {command}: {e}")
            return None

    def check_windows_settings(self):
        print("Checking Windows privacy settings...")
        # Example: Check telemetry settings
        telemetry_status = self.run_command("reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection /v AllowTelemetry")
        self.results['Telemetry'] = 'Enabled' if '0x1' in telemetry_status else 'Disabled'
        
        # Add more Windows privacy settings checks as needed
    
    def check_installed_applications(self):
        print("Checking installed applications for potential privacy leaks...")
        # Example: List installed applications
        installed_apps = self.run_command("powershell \"Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName\"")
        self.results['InstalledApps'] = installed_apps.splitlines() if installed_apps else []

        # Add more application checks as needed

    def report(self):
        print("Generating report...")
        with open('privacy_report.json', 'w') as report_file:
            json.dump(self.results, report_file, indent=4)
        print("Report generated as 'privacy_report.json'")

    def run(self):
        self.check_windows_settings()
        self.check_installed_applications()
        self.report()

if __name__ == "__main__":
    prober = PrivacyProber()
    prober.run()