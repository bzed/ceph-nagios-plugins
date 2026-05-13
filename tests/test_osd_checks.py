#!/usr/bin/env python3
"""
Test suite for check_ceph_osd and check_ceph_osd_db
Tests that OSDs are correctly found for a given hostname using anonymized data.
"""

import sys
import os
import re
import socket

# Read the helper functions from the source file
def load_functions_from_file(filepath):
    """Load specific functions from a Python file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract function definitions
    functions = {}
    # Split by function definitions
    parts = re.split(r'\ndef ([a-zA-Z_][a-zA-Z0-9_]*)\(', content)
    
    # First part is before first function
    current_func = None
    func_code = {}
    
    for i, part in enumerate(parts[1:], 1):
        func_name = parts[i]
        # Find the matching closing or next function
        # This is a simple approach - look for the next 'def ' or end of file
        # We'll collect all code until the next 'def ' or end
        if current_func is None:
            # Get the rest of the function signature
            code = 'def ' + func_name + part
            current_func = func_name
        else:
            code = part
        
        # Check if this part starts with 'def ' or we're at the end
        if part.strip().startswith('def ') or i == len(parts) - 1:
            func_code[current_func] = code
            current_func = None
    
    # Handle last function
    if current_func:
        func_code[current_func] = 'def ' + current_func + part
    
    return func_code

# Load functions from check_ceph_osd
src_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'check_ceph_osd.py')
if not os.path.exists(src_path):
    src_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'check_ceph_osd')

# Read and execute the functions we need
exec(open(src_path).read().split('def main')[0])


def test_get_host_ips_from_config():
    """Test that get_host_ips extracts IPs from ceph.conf [mon.<hostname>] sections"""
    conf_path = os.path.join(os.path.dirname(__file__), 'ceph.conf')
    
    # Test with mon-node-001 (should get 192.168.1.1 from config)
    ips = get_host_ips('mon-node-001', conf_path)
    assert '192.168.1.1' in ips, f"Expected 192.168.1.1 in IPs for mon-node-001, got {ips}"
    print("PASS: get_host_ips for mon-node-001 from config")
    
    # Test with mon-node-002 (should get 192.168.2.1 from config)
    ips = get_host_ips('mon-node-002', conf_path)
    assert '192.168.2.1' in ips, f"Expected 192.168.2.1 in IPs for mon-node-002, got {ips}"
    print("PASS: get_host_ips for mon-node-002 from config")
    
    # Test with mon-node-003 (should get 192.168.3.1 from config)
    ips = get_host_ips('mon-node-003', conf_path)
    assert '192.168.3.1' in ips, f"Expected 192.168.3.1 in IPs for mon-node-003, got {ips}"
    print("PASS: get_host_ips for mon-node-003 from config")
    
    # Test with unknown host (should return empty or only DNS results)
    ips = get_host_ips('unknown-host', conf_path)
    # Should not have any of our test IPs
    assert '192.168.1.1' not in ips, f"Should not have IPs for unknown host"
    print("PASS: get_host_ips for unknown host")


def test_extract_ips_from_osd_line():
    """Test that extract_ips_from_osd_line correctly extracts IPs"""
    line = 'osd.0 up in weight 1 [v2:192.168.1.1:6906,v1:192.168.1.1:6907] [v2:192.168.1.1:6898,v1:192.168.1.1:6899]'
    ips = extract_ips_from_osd_line(line)
    assert '192.168.1.1' in ips, f"Expected 192.168.1.1 in extracted IPs, got {ips}"
    print(f"PASS: extract_ips_from_osd_line found {ips}")
    
    # Test with multiple IPs (shouldn't happen in one line but test anyway)
    line2 = 'osd.25 up in weight 1 [v2:192.168.2.1:6890,v1:192.168.2.1:6891]'
    ips2 = extract_ips_from_osd_line(line2)
    assert '192.168.2.1' in ips2, f"Expected 192.168.2.1 in extracted IPs, got {ips2}"
    print(f"PASS: extract_ips_from_osd_line for 192.168.2.1")


def test_match_osds_for_host():
    """Test that match_osds_for_host correctly finds OSDs for each hostname"""
    osd_dump_path = os.path.join(os.path.dirname(__file__), 'osd_dump')
    conf_path = os.path.join(os.path.dirname(__file__), 'ceph.conf')
    
    with open(osd_dump_path, 'r') as f:
        osd_dump = f.read()
    
    # Test mon-node-001 (IP 192.168.1.1) - should find OSDs on that IP
    result = match_osds_for_host(osd_dump, 'mon-node-001', '[^ ]*', conf_path)
    up_osds = result['up']
    assert len(up_osds) > 0, f"Expected to find OSDs for mon-node-001, got {len(up_osds)}"
    print(f"PASS: Found {len(up_osds)} up OSDs for mon-node-001: {up_osds[:5]}{'...' if len(up_osds) > 5 else ''}")
    
    # Test mon-node-002 (IP 192.168.2.1) - should find OSDs on that IP
    result = match_osds_for_host(osd_dump, 'mon-node-002', '[^ ]*', conf_path)
    up_osds = result['up']
    assert len(up_osds) > 0, f"Expected to find OSDs for mon-node-002, got {len(up_osds)}"
    print(f"PASS: Found {len(up_osds)} up OSDs for mon-node-002: {up_osds[:5]}{'...' if len(up_osds) > 5 else ''}")
    
    # Test mon-node-003 (IP 192.168.3.1) - should find OSDs on that IP
    result = match_osds_for_host(osd_dump, 'mon-node-003', '[^ ]*', conf_path)
    up_osds = result['up']
    assert len(up_osds) > 0, f"Expected to find OSDs for mon-node-003, got {len(up_osds)}"
    print(f"PASS: Found {len(up_osds)} up OSDs for mon-node-003: {up_osds[:5]}{'...' if len(up_osds) > 5 else ''}")
    
    # Verify that the OSDs for each host are different
    result1 = match_osds_for_host(osd_dump, 'mon-node-001', '[^ ]*', conf_path)
    result2 = match_osds_for_host(osd_dump, 'mon-node-002', '[^ ]*', conf_path)
    result3 = match_osds_for_host(osd_dump, 'mon-node-003', '[^ ]*', conf_path)
    
    # They should have some unique OSDs (not all the same)
    set1 = set(result1['up'])
    set2 = set(result2['up'])
    set3 = set(result3['up'])
    
    # Check that not all sets are identical
    assert set1 != set2 or set1 != set3 or set2 != set3, "All hosts found the same OSDs - matching may not be working correctly"
    print("PASS: Different hosts find different OSDs")


def test_with_direct_ip():
    """Test that matching works with direct IP addresses"""
    osd_dump_path = os.path.join(os.path.dirname(__file__), 'osd_dump')
    
    with open(osd_dump_path, 'r') as f:
        osd_dump = f.read()
    
    # Test with IP 192.168.1.1 directly
    result = match_osds_for_host(osd_dump, '192.168.1.1', '[^ ]*', None)
    up_osds = result['up']
    assert len(up_osds) > 0, f"Expected to find OSDs for IP 192.168.1.1, got {len(up_osds)}"
    print(f"PASS: Found {len(up_osds)} up OSDs for IP 192.168.1.1")


if __name__ == '__main__':
    print("Running OSD check tests...")
    print("=" * 60)
    
    try:
        test_get_host_ips_from_config()
        print()
        test_extract_ips_from_osd_line()
        print()
        test_match_osds_for_host()
        print()
        test_with_direct_ip()
        print()
        print("=" * 60)
        print("All tests PASSED!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\nTEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
