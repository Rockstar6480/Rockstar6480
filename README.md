# Rockstar6480

Scripts for Google Cloud Monitoring setup, including alerting policies and dashboards.

## Files

- `gcloud_command.sh`: Lists notification channels for the project.
- `gcloud_policy.sh`: Creates an alerting policy for downtime alerts.
- `uptime_alert_policy.json`: JSON definition for the alerting policy.
- `sovereign_dashboard.json`: JSON definition for the operations dashboard.
- `setup_monitoring.sh`: Combined script to list channels, create the policy, and create the dashboard.

## Usage

1. Install Google Cloud CLI (`gcloud`).
2. Authenticate: `gcloud auth login`
3. Set project: `gcloud config set project bridge-master-richard`
4. Run the scripts: `bash setup_monitoring.sh`

Note: Ensure you have the necessary permissions for the project.
