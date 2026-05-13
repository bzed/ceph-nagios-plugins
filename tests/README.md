# Test Suite for Ceph Nagios Plugins

This directory contains test data and test scripts for the Ceph Nagios plugins.

## Files

- `ceph.conf` - Anonymized Ceph configuration file with monitor hostnames and IPs
- `osd_dump` - Anonymized Ceph OSD dump output
- `test_osd_checks.py` - Test suite for OSD check functions

## Running Tests

```bash
python3 tests/test_osd_checks.py
```

## Test Data

The test data uses the following anonymized values:

| Original | Anonymized |
|---------|------------|
| con-abn-pve-dc6-001 | mon-node-001 |
| con-abn-pve-dc6-002 | mon-node-002 |
| con-abn-pve-dc6-003 | mon-node-003 |
| 10.43.43.1 | 192.168.1.1 |
| 10.43.43.2 | 192.168.2.1 |
| 10.43.43.3 | 192.168.3.1 |
| 10.43.43.0/24 | 192.168.0.0/24 |

## What the Tests Verify

1. `test_get_host_ips_from_config` - Verifies that hostnames are correctly resolved to IPs from the ceph.conf `[mon.<hostname>]` sections
2. `test_extract_ips_from_osd_line` - Verifies that IP addresses are correctly extracted from OSD dump lines
3. `test_match_osds_for_host` - Verifies that OSDs are correctly matched to hostnames using both config IPs and OSD dump IPs
4. `test_with_direct_ip` - Verifies that matching works when using IP addresses directly
