# Rockstar6480

Scripts for Google Cloud Monitoring setup, including alerting policies and dashboards.

## Files

- `gcloud_command.sh`: Lists notification channels for the project.
- `gcloud_policy.sh`: Creates an alerting policy for downtime alerts.
- `uptime_alert_policy.json`: JSON definition for the alerting policy.
- `sovereign_dashboard.json`: JSON definition for the operations dashboard.
- `setup_monitoring.sh`: Combined script to list channels, create the policy, and create the dashboard.
- `sovereign_audit_script.py`: Audit script to verify configuration integrity.
- `verify_software.sh`: Comprehensive shell-based verification script.
- `test_suite.py`: Python-based test suite for thorough validation.

## Usage

1. Install Google Cloud CLI (`gcloud`).
2. Authenticate: `gcloud auth login`
3. Set project: `gcloud config set project bridge-master-richard`
4. Run the scripts: `bash setup_monitoring.sh`

Note: Ensure you have the necessary permissions for the project.

## Verification

To verify that the software is working correctly, run any of the following:

### Quick Verification
```bash
python3 sovereign_audit_script.py
```

### Comprehensive Shell-Based Verification
```bash
bash verify_software.sh
```

### Full Test Suite
```bash
python3 test_suite.py
```

All verification methods will validate:
- JSON configuration file syntax and structure
- Shell script syntax
- Python script functionality
- Configuration integrity and consistency
- File existence and completeness
