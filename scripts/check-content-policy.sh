#!/usr/bin/env bash
# Fails if public-facing content contains anything we've decided must not ship.
# Usage: scripts/check-content-policy.sh [file ...]   (defaults to the published files)

set -uo pipefail

if [ "$#" -gt 0 ]; then
    files=("$@")
else
    files=(README.md Resume-Tom-Dean.md Short-Bio-Tom-Dean.txt)
fi

# Each rule: "description|extended regex (case-insensitive)"
rules=(
    "Draft marker left in content|\[(TBD|CONFIRM)[^]]*\]"
    "Link to employer (solo-io) GitHub org|github\.com/solo-io"
    "Old email address (use tom@southsidedean.com)|dean33\.com"
    "Job-search wording (stance is open but quiet)|looking for [^.]*(role|position|opportunit)"
    "Stale SAA study note|working on SAA|studying for the AWS Certified Solutions Architect"
    "Phone number|\(?[0-9]{3}\)?[-. ][0-9]{3}[-. ][0-9]{4}"
)

status=0
for rule in "${rules[@]}"; do
    desc=${rule%%|*}
    pattern=${rule#*|}
    for f in "${files[@]}"; do
        [ -f "$f" ] || continue
        if matches=$(grep -n -i -E -- "$pattern" "$f"); then
            while IFS= read -r line; do
                lineno=${line%%:*}
                echo "::error file=$f,line=$lineno::$desc"
                echo "  $f:$lineno: ${line#*:}" | cut -c1-200
            done <<< "$matches"
            status=1
        fi
    done
done

if [ "$status" -eq 0 ]; then
    echo "Content policy: all checks passed for ${files[*]}"
fi
exit "$status"
