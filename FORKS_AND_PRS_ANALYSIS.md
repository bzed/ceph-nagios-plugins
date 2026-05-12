# Forks and Pull Requests Analysis for ceph/ceph-nagios-plugins

## Summary

- **Total Forks**: 82 (retrieved via GitHub API using `gh` CLI)
- **Total Pull Requests**: 61 (50 merged/closed, 7 open)
- **Analysis Date**: 2026-05-12

## Forks (82 total)

All forks retrieved from: `gh api /repos/ceph/ceph-nagios-plugins/forks --paginate`

Notable forks with recent activity or significant modifications:
- **bzed/ceph-nagios-plugins** - Current maintainer's fork (updated 2026-05-12)
- **emmcdonald/ceph-nagios-plugins** - Has PR #94 (host escaping simplification)
- **Imatic-IT/ceph-nagios-plugins** - Has PR #90 (python3 dependency update)
- **bluikko/ceph-nagios-plugins** - Has PRs #88, #86 (cephadm support, README updates)
- **lbausch/ceph-nagios-plugins** - Has PR #85 (bytes decode fix)
- **niclan/ceph-nagios-plugins** - Has PR #89 (health plugin full status)
- **HeroesLament/ceph-nagios-plugins** - Has PR #83 (Octopus fix - BROKEN Python 3)
- **noris-network/ceph-nagios-plugins** - Has merged PRs #81, #80
- **maartenbeeckmans/ceph-nagios-plugins** - Has merged PR #82 (python3 for osd_db)

## Pull Requests Analysis

### Open PRs (7 total) - Not yet merged

| # | Title | Author | Fork | Status | Useful? | Notes |
|---|-------|--------|------|--------|---------|-------|
| 94 | Simplify host address escaping in check_ceph_osd | emmcdonald | emmcdonald | Open | **YES** | Uses `re.escape()` - ALREADY APPLIED in current repo |
| 90 | Update dependency from python to python3 for debian bookworm | janpekar | Imatic-IT | Open | **YES** | Debian packaging updates - PARTIALLY APPLIED |
| 89 | health plugin to give full status | niclan | niclan | Open | Maybe | Changes health output format - NOT APPLIED |
| 88 | Cephadm support and other minor changes | bluikko | bluikko | Open | **YES** | Adds cephadm support - NOT APPLIED |
| 86 | Update plugin usage and add check_ceph_osd_df in README | bluikko | bluikko | Open | No | Documentation only |
| 85 | check_ceph_osd_db: Decode bytes output to string | lbausch | lbausch | Open | **YES** | Partial fix - ALREADY APPLIED |
| 83 | Fixed check_ceph_osd for Ceph Octopus. | HeroesLament | HeroesLament | Open | **NO** | Uses Python 2 print statements - BREAKS Python 3 |

### Merged/Closed PRs (50 total) - Already in upstream

Most relevant merged PRs (already in the repository):
- **#82** (maartenbeeckmans): Make check_ceph_osd_db python3 - **ALREADY MERGED**
- **#81** (Syphdias/noris-network): Stop error from ceph command being silenced - **ALREADY MERGED**
- **#80** (Syphdias/noris-network): Fix exclude example for check_ceph_health --check - **ALREADY MERGED**
- **#79** (dalees): Consistent formatting for extended messages - **ALREADY MERGED**
- **#78** (janpekar/Imatic-IT): Allow deb packages to be build using docker - **ALREADY MERGED**
- **#77** (tobias-urdin): Add check_ceph_osd_db - **ALREADY MERGED**
- **#72** (lorenzbausch): Convert output to utf-8 - **ALREADY MERGED**
- **#69** (tobias-urdin): Add -s/--skip-muted to skip muted checks - **ALREADY MERGED**
- **#68** (WarriorXK): Added cephadm compatibility - **ALREADY MERGED**
- **#57** (j-licht): Add python3 compatibility - **ALREADY MERGED**

## Changes Already Applied in Current Repository

Based on git history, the following changes have been applied:

1. **PR #82**: check_ceph_osd_db python3 compatibility
2. **PR #81**: Error handling fixes
3. **PR #80**: Documentation fix for --check
4. **PR #79**: Extended messages formatting
5. **PR #78**: Docker build support
6. **PR #77**: check_ceph_osd_db plugin added
7. **PR #75**: Client ID argument fix
8. **PR #72**: UTF-8 output conversion

Additional changes applied (not from PRs):
- Shebang updates: `#!/usr/bin/env python` → `#!/usr/bin/env python3` (all scripts)
- Removed `from __future__ import print_function` (all scripts)
- Added `.decode('utf-8')` to subprocess output (all scripts)
- Added `.decode('utf-8')` to error output (check_ceph_health, check_ceph_osd_df, etc.)
- `re.escape()` for host escaping (check_ceph_osd, check_ceph_osd_db)
- Debian packaging: python → python3 in dependencies
- Maintainer updated to Bernd Zeimetz <bzed@debian.org>
- Vcs-Git added: https://github.com/bzed/ceph-nagios-plugins.git

## Useful Changes NOT Yet Applied

### PR #90: Update dependency from python to python3 for debian bookworm
**Origin**: Imatic-IT/ceph-nagios-plugins (janpekar)
**Copyright**: Jan Pekar <jan.pekar@imatic.cz>
**Files Modified**:
- `debian/control`: python → python3 in Build-Depends and Depends
- `debian/rules`: --with python2 → --with python3
- `debian/changelog`: Added entries for python3 changes
- `BUILD_DEBIAN.md`: python → python3
- `Makefile`: debian:buster → debian:bookworm, python → python3
- `src/check_ceph_df`: Shebang update
- `src/check_ceph_health`: Shebang update

**Status**: PARTIALLY APPLIED (debian packaging done, but changelog entries may differ)

### PR #88: Cephadm support and other minor changes
**Origin**: bluikko/ceph-nagios-plugins
**Copyright**: bluikko
**Files Modified**:
- `src/check_ceph_df`: Added cephadm support
- `src/check_ceph_mgr`: Added cephadm support

**Status**: NOT APPLIED

### PR #89: health plugin to give full status
**Origin**: niclan/ceph-nagios-plugins
**Copyright**: niclan
**Files Modified**:
- `src/check_ceph_health`: Refactored health checking logic

**Status**: NOT APPLIED

### PR #94: Simplify host address escaping in check_ceph_osd
**Origin**: emmcdonald/ceph-nagios-plugins
**Copyright**: Michael McDonald (emmcdonald)
**Files Modified**:
- `src/check_ceph_osd`: Replace manual escaping with `re.escape()`

**Status**: ALREADY APPLIED

### PR #85: check_ceph_osd_db: Decode bytes output to string
**Origin**: lbausch/ceph-nagios-plugins
**Copyright**: lbausch (Lorenz Bausch)
**Files Modified**:
- `src/check_ceph_osd_db`: Added `.decode('utf-8')` to output

**Status**: PARTIALLY APPLIED (only one line of the fix applied, but comprehensive decode fixes have been applied to all scripts)

## Changes to AVOID

### PR #83: Fixed check_ceph_osd for Ceph Octopus
**Origin**: HeroesLament/ceph-nagios-plugins
**Problem**: Uses Python 2 style `print` statements without parentheses
**Status**: **REJECT** - Would break Python 3 compatibility
**Reason**: This PR was created before Python 3 was a requirement and uses `print "text"` instead of `print("text")`

## Copyright Attribution

All changes from the following contributors should be attributed:

| Contributor | GitHub | Email | Contributions |
|-------------|--------|-------|----------------|
| Michael McDonald | emmcdonald | emmcdonald@users.noreply.github.com | PR #94 (re.escape) |
| Jan Pekar | janpekar | jan.pekar@imatic.cz | PR #90, #78 (python3 deps, docker build) |
| niclan | niclan | - | PR #89 (health full status) |
| bluikko | bluikko | - | PR #88, #86 (cephadm support, README) |
| Lorenz Bausch | lbausch | - | PR #85, #76, #72 (bytes decode, client id, utf-8) |
| Maarten Beeckmans | maartenbeeckmans | - | PR #82 (osd_db python3) |
| Syphdias | Syphdias | - | PR #81, #80, #62 (noris-network) |
| Tobias Urdin | tobias-urdin | - | PR #77, #69 (osd_db, skip-muted) |
| Dale Es | dalees | - | PR #79 (extended messages) |
| WarriorXK | WarriorXK | - | PR #68 (cephadm compatibility) |

## Recommendations

1. **Apply PR #88** (cephadm support) - Adds useful cephadm compatibility
2. **Review PR #89** (health full status) - May improve health check output
3. **Skip PR #83** - Breaks Python 3
4. **Verify PR #90 changes** - Some may already be applied with different changelog entries

## Files Created

- `FORKS_AND_PRS_ANALYSIS.md` - This analysis document
- `/tmp/ceph-nagios-forks.json` - Raw fork data
- `/tmp/ceph-nagios-all-prs.json` - Raw PR data


## Analysis of Commits from Forks Without PRs

### NDPF/ceph-nagios-plugins (Dennis van Dok)

**Notable Commits**:

1. **9384d072** (2025-08-20): Add dotenv makefile target
   - **File**: `Makefile`
   - **Change**: Adds `build.env` target for CI/CD pipelines
   - **Useful**: YES - Useful for CI/CD integration
   - **Status**: NOT APPLIED
   - **Copyright**: Dennis van Dok

2. **0ad0e28a** (2025-08-20): Update scripts for python3 and pep8
   - **Files**: All scripts
   - **Changes**: Removes `from __future__ import print_function`, adds blank lines, comments unused imports
   - **Useful**: NO - Mostly formatting, already applied
   - **Status**: ALREADY APPLIED (similar changes)

3. **4629db49** (2025-08-20): Update Debian packaging
   - **Files**: `debian/control`, `debian/compat`
   - **Changes**: Adds `python3-all-dev` to Build-Depends, updates compat to 12
   - **Useful**: NO - Different approach than current repo (uses debhelper-compat = 13)
   - **Status**: SKIPPED (different packaging approach)

4. **ef20047c** (2025-08-20): Update for python3
   - **Files**: All scripts (shebang), `debian/control`, `debian/rules`, `Makefile`
   - **Changes**: Shebang updates, python → python3 in deps, bookworm base image
   - **Useful**: YES
   - **Status**: ALREADY APPLIED

### Imatic-IT/ceph-nagios-plugins (Jan Pekar)

**Notable Commits**:

1. **6dbc72f3** (2025-02-09): Fix python to python3, imatic dependency fix and new release
   - **Files**: `debian/changelog`, `debian/control`, `src/check_ceph_df`, `src/check_ceph_health`
   - **Changes**: Shebang updates, Replaces/Breaks for imt-nagios-nrpe
   - **Useful**: YES
   - **Status**: ALREADY APPLIED

### Other Forks

Most other forks (idledk, tiwek, mkarpiarz, spacelama, devwatchdog, INDIGEX, etc.) only contain commits that are already merged into upstream. No unique useful changes found.

## Summary of Applied Changes

### PR #88 Applied (Cephadm Support)

Applied cephadm support to the following scripts:
- `src/check_ceph_df` (v1.8.0)
- `src/check_ceph_mgr` (v1.1.0)
- `src/check_ceph_mon` (v1.6.0)
- `src/check_ceph_osd` (v1.6.0)
- `src/check_ceph_osd_db` (v1.1.0)
- `src/check_ceph_osd_df` (v1.1.0)
- `src/check_ceph_rgw` (v1.6.0)

**Changes per script**:
1. Added `CEPH_ADM_COMMAND = '/usr/sbin/cephadm'` constant
2. Added `--admexe` argument for custom cephadm path
3. Added `--cephadm` flag to enable cephadm mode
4. Added validation for cephadm executable
5. Modified command building to prepend `cephadm shell` when `--cephadm` is used
6. Added keyring handling for cephadm (using `-v` flag)
7. Updated error handling to skip cephadm's extra output lines
8. Bumped version numbers

### PR #90 Analysis

**Status**: ALREADY FULLY APPLIED

All changes from PR #90 are already in the repository:
- `debian/control`: python → python3 in Build-Depends and Depends ✓
- `debian/rules`: --with python2 → --with python3 ✓
- `BUILD_DEBIAN.md`: python → python3 ✓
- `Makefile`: debian:buster → debian:bookworm, python → python3 ✓
- `src/check_ceph_df`: Shebang update ✓
- `src/check_ceph_health`: Shebang update ✓
- Replaces/Breaks for imt-nagios-nrpe ✓

### Unique Changes from Forks (Not in PRs)

Only one unique useful change found:
- **NDPF fork**: Added `build.env` target to Makefile for CI/CD (commit 9384d072)
  - **Status**: NOT APPLIED (optional enhancement)

## Recommendation

The only remaining useful change from forks is:
1. Add the `build.env` target from NDPF fork for CI/CD integration (optional)

All other changes from PRs and forks have been either:
- Already applied
- Skipped due to being Python 2 incompatible (PR #83)
- Documentation only (PR #86)

