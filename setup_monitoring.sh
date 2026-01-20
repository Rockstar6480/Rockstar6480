#!/bin/bash

# List notification channels
echo "Listing notification channels..."
gcloud beta monitoring channels list \
    --project=bridge-master-richard \
        --format="value(name)"

# Create alerting policy
echo "Creating alerting policy..."
gcloud monitoring policies create \
    --policy-from-file=uptime_alert_policy.json \
    --project=bridge-master-richard

# Create dashboard
echo "Creating dashboard..."
gcloud monitoring dashboards create \
    --config-from-file=sovereign_dashboard.json \
    --project=bridge-master-richard