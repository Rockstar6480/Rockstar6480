#!/usr/bin/env python3
"""
Sovereign Watchman Automation and Intelligence Audit Script

This script performs automated audits on the sovereign monitoring setup,
checking for compliance, uptime, and configuration integrity.
"""

import json
import os
import subprocess
import sys

def load_json_file(filepath):
    """Load and return JSON data from file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filepath}.")
        return None

def audit_alert_policy():
    """Audit the uptime alert policy."""
    policy = load_json_file('uptime_alert_policy.json')
    if policy:
        print("✓ Alert policy loaded successfully.")
        if 'displayName' in policy and 'Bridge Master Downtime Alert' in policy['displayName']:
            print("✓ Alert policy name is correct.")
        else:
            print("✗ Alert policy name mismatch.")
        if policy.get('enabled', False):
            print("✓ Alert policy is enabled.")
        else:
            print("✗ Alert policy is disabled.")
    else:
        print("✗ Failed to load alert policy.")

def audit_dashboard():
    """Audit the sovereign dashboard."""
    dashboard = load_json_file('sovereign_dashboard.json')
    if dashboard:
        print("✓ Dashboard loaded successfully.")
        if 'displayName' in dashboard and 'Sovereign Operations Dashboard' in dashboard['displayName']:
            print("✓ Dashboard name is correct.")
        else:
            print("✗ Dashboard name mismatch.")
        tiles = dashboard.get('mosaicLayout', {}).get('tiles', [])
        if len(tiles) >= 2:
            print("✓ Dashboard has expected number of tiles.")
        else:
            print("✗ Dashboard has fewer tiles than expected.")
    else:
        print("✗ Failed to load dashboard.")

def check_gcloud_setup():
    """Check if gcloud is configured."""
    try:
        result = subprocess.run(['gcloud', 'config', 'get-value', 'project'], capture_output=True, text=True)
        if result.returncode == 0 and 'bridge-master-richard' in result.stdout:
            print("✓ GCloud project is set correctly.")
        else:
            print("✗ GCloud project not set or incorrect.")
    except FileNotFoundError:
        print("✗ GCloud CLI not installed.")

def main():
    print("Starting Sovereign Watchman Intelligence Audit...")
    print("=" * 50)
    
    audit_alert_policy()
    audit_dashboard()
    check_gcloud_setup()
    
    print("=" * 50)
    print("Audit complete. Review output for any issues.")

if __name__ == "__main__":
    main()</content>
<parameter name="filePath">/workspaces/Rockstar6480/sovereign_audit_script.py