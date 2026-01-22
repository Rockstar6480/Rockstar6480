#!/bin/bash

# Comprehensive Software Verification Script
# This script verifies that all components of the monitoring setup are working correctly

echo "=========================================="
echo "Software Verification Suite"
echo "=========================================="
echo ""

# Track verification results
PASSED=0
FAILED=0

# Function to report test result
report_result() {
    if [ $1 -eq 0 ]; then
        echo "✓ $2"
        PASSED=$((PASSED + 1))
    else
        echo "✗ $2"
        FAILED=$((FAILED + 1))
    fi
}

echo "1. JSON Configuration File Validation"
echo "--------------------------------------"
python3 -m json.tool uptime_alert_policy.json > /dev/null 2>&1
report_result $? "uptime_alert_policy.json is valid JSON"

python3 -m json.tool sovereign_dashboard.json > /dev/null 2>&1
report_result $? "sovereign_dashboard.json is valid JSON"

echo ""
echo "2. Shell Script Syntax Validation"
echo "--------------------------------------"
bash -n gcloud_command.sh 2>&1
report_result $? "gcloud_command.sh has valid syntax"

bash -n gcloud_policy.sh 2>&1
report_result $? "gcloud_policy.sh has valid syntax"

bash -n setup_monitoring.sh 2>&1
report_result $? "setup_monitoring.sh has valid syntax"

echo ""
echo "3. Python Script Validation"
echo "--------------------------------------"
python3 -m py_compile sovereign_audit_script.py 2>&1
report_result $? "sovereign_audit_script.py compiles successfully"

echo ""
echo "4. Running Audit Script"
echo "--------------------------------------"
python3 sovereign_audit_script.py
report_result $? "Audit script executed successfully"

echo ""
echo "5. File Existence Check"
echo "--------------------------------------"
[ -f "README.md" ]
report_result $? "README.md exists"

[ -f "uptime_alert_policy.json" ]
report_result $? "uptime_alert_policy.json exists"

[ -f "sovereign_dashboard.json" ]
report_result $? "sovereign_dashboard.json exists"

[ -f "gcloud_command.sh" ]
report_result $? "gcloud_command.sh exists"

[ -f "gcloud_policy.sh" ]
report_result $? "gcloud_policy.sh exists"

[ -f "setup_monitoring.sh" ]
report_result $? "setup_monitoring.sh exists"

[ -f "sovereign_audit_script.py" ]
report_result $? "sovereign_audit_script.py exists"

echo ""
echo "=========================================="
echo "Verification Summary"
echo "=========================================="
echo "Tests Passed: $PASSED"
echo "Tests Failed: $FAILED"
echo ""

if [ $FAILED -eq 0 ]; then
    echo "✓ All verification checks passed!"
    echo "Software is working correctly."
    exit 0
else
    echo "✗ Some verification checks failed."
    echo "Please review the output above."
    exit 1
fi
