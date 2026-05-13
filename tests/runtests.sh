#!/bin/bash
# Run all tests for the Ceph Nagios plugins

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Running Ceph Nagios Plugin Tests"
echo "================================"
echo ""

# Run the OSD check tests
python3 "${SCRIPT_DIR}/test_osd_checks.py"
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "Tests FAILED with exit code $EXIT_CODE"
    exit $EXIT_CODE
fi

echo ""
echo "All tests PASSED!"
exit 0
