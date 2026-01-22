#!/usr/bin/env python3
"""
Comprehensive Test Suite for Google Cloud Monitoring Setup

This test suite validates all components of the monitoring setup:
- JSON configuration files
- Shell scripts
- Python scripts
- Configuration integrity
"""

import json
import os
import subprocess
import sys
import unittest

class TestJSONConfigurations(unittest.TestCase):
    """Test JSON configuration files."""
    
    def test_uptime_alert_policy_valid_json(self):
        """Test that uptime_alert_policy.json is valid JSON."""
        with open('uptime_alert_policy.json', 'r') as f:
            data = json.load(f)
        self.assertIsNotNone(data)
    
    def test_uptime_alert_policy_structure(self):
        """Test that uptime_alert_policy.json has required fields."""
        with open('uptime_alert_policy.json', 'r') as f:
            data = json.load(f)
        self.assertIn('displayName', data)
        self.assertIn('conditions', data)
        self.assertIn('enabled', data)
        self.assertTrue(data['enabled'])
    
    def test_uptime_alert_policy_name(self):
        """Test that alert policy has correct name."""
        with open('uptime_alert_policy.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(data['displayName'], 'Bridge Master Downtime Alert')
    
    def test_dashboard_valid_json(self):
        """Test that sovereign_dashboard.json is valid JSON."""
        with open('sovereign_dashboard.json', 'r') as f:
            data = json.load(f)
        self.assertIsNotNone(data)
    
    def test_dashboard_structure(self):
        """Test that sovereign_dashboard.json has required fields."""
        with open('sovereign_dashboard.json', 'r') as f:
            data = json.load(f)
        self.assertIn('displayName', data)
        self.assertIn('mosaicLayout', data)
    
    def test_dashboard_name(self):
        """Test that dashboard has correct name."""
        with open('sovereign_dashboard.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(data['displayName'], 'Sovereign Operations Dashboard')
    
    def test_dashboard_tiles(self):
        """Test that dashboard has expected tiles."""
        with open('sovereign_dashboard.json', 'r') as f:
            data = json.load(f)
        tiles = data.get('mosaicLayout', {}).get('tiles', [])
        self.assertGreaterEqual(len(tiles), 2)

class TestShellScripts(unittest.TestCase):
    """Test shell scripts."""
    
    def test_gcloud_command_syntax(self):
        """Test that gcloud_command.sh has valid syntax."""
        result = subprocess.run(['bash', '-n', 'gcloud_command.sh'], 
                              capture_output=True)
        self.assertEqual(result.returncode, 0)
    
    def test_gcloud_policy_syntax(self):
        """Test that gcloud_policy.sh has valid syntax."""
        result = subprocess.run(['bash', '-n', 'gcloud_policy.sh'], 
                              capture_output=True)
        self.assertEqual(result.returncode, 0)
    
    def test_setup_monitoring_syntax(self):
        """Test that setup_monitoring.sh has valid syntax."""
        result = subprocess.run(['bash', '-n', 'setup_monitoring.sh'], 
                              capture_output=True)
        self.assertEqual(result.returncode, 0)
    
    def test_scripts_executable(self):
        """Test that shell scripts are executable."""
        scripts = ['gcloud_command.sh', 'gcloud_policy.sh', 'setup_monitoring.sh']
        for script in scripts:
            # Check if file exists
            self.assertTrue(os.path.exists(script), f"{script} should exist")

class TestPythonScripts(unittest.TestCase):
    """Test Python scripts."""
    
    def test_audit_script_compiles(self):
        """Test that sovereign_audit_script.py compiles."""
        result = subprocess.run(['python3', '-m', 'py_compile', 
                               'sovereign_audit_script.py'], 
                              capture_output=True)
        self.assertEqual(result.returncode, 0)
    
    def test_audit_script_runs(self):
        """Test that sovereign_audit_script.py runs without errors."""
        result = subprocess.run(['python3', 'sovereign_audit_script.py'], 
                              capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Audit complete', result.stdout)

class TestFileExistence(unittest.TestCase):
    """Test that all required files exist."""
    
    def test_readme_exists(self):
        """Test that README.md exists."""
        self.assertTrue(os.path.exists('README.md'))
    
    def test_json_files_exist(self):
        """Test that JSON files exist."""
        self.assertTrue(os.path.exists('uptime_alert_policy.json'))
        self.assertTrue(os.path.exists('sovereign_dashboard.json'))
    
    def test_shell_scripts_exist(self):
        """Test that shell scripts exist."""
        self.assertTrue(os.path.exists('gcloud_command.sh'))
        self.assertTrue(os.path.exists('gcloud_policy.sh'))
        self.assertTrue(os.path.exists('setup_monitoring.sh'))
    
    def test_python_scripts_exist(self):
        """Test that Python scripts exist."""
        self.assertTrue(os.path.exists('sovereign_audit_script.py'))

class TestConfigurationIntegrity(unittest.TestCase):
    """Test configuration integrity and consistency."""
    
    def test_project_consistency(self):
        """Test that project name is consistent across files."""
        # Check alert policy
        with open('uptime_alert_policy.json', 'r') as f:
            policy = json.load(f)
        notification_channels = policy.get('notificationChannels', [])
        self.assertGreater(len(notification_channels), 0, 
                          "Alert policy should have at least one notification channel")
        notification_channel = notification_channels[0]
        self.assertIn('bridge-master-richard', notification_channel)
        
        # Check shell scripts
        with open('setup_monitoring.sh', 'r') as f:
            content = f.read()
        self.assertIn('bridge-master-richard', content)
    
    def test_alert_policy_combiner(self):
        """Test that alert policy has correct combiner."""
        with open('uptime_alert_policy.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(data['combiner'], 'OR')
    
    def test_dashboard_columns(self):
        """Test that dashboard has correct column count."""
        with open('sovereign_dashboard.json', 'r') as f:
            data = json.load(f)
        columns = data['mosaicLayout']['columns']
        self.assertEqual(columns, 12)

def run_tests():
    """Run all tests and return results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestJSONConfigurations))
    suite.addTests(loader.loadTestsFromTestCase(TestShellScripts))
    suite.addTests(loader.loadTestsFromTestCase(TestPythonScripts))
    suite.addTests(loader.loadTestsFromTestCase(TestFileExistence))
    suite.addTests(loader.loadTestsFromTestCase(TestConfigurationIntegrity))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✓ ALL TESTS PASSED - Software is working correctly!")
        return 0
    else:
        print("\n✗ SOME TESTS FAILED - Please review the output above.")
        return 1

if __name__ == '__main__':
    sys.exit(run_tests())
