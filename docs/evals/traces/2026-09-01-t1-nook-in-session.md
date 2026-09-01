# Trace

- Dummy: t1-nook
- Arm: this-chat (inherit; not a 004 routing arm)
- Date: 2026-09-01
- Model (picker name): not recorded (no picker scrape)
- Cost class: not scored — EVAL-TASK asks for a class; this run did not map the live picker
- Success: yes (Red exit 0 after patch; Keyboard + Retry lines unchanged)
- User turns until accepted: 1
- Tool calls (total): 5 (unittest red, patch page.py, patch design.md, Read design.md, unittest green)
- Extra tool calls (not Grep/Glob/Read or the named native): 0 (Shell = Red command; patches are the job; one Read of the owner)
- Tokens in / out (optional; skip if the dashboard is missing): skipped
- Notes: In-place patches only. Dummy restored to Coming soon. so the guidebook stays red. Do not promote 004.

## Keep check

Before: Empty copy Coming soon.; Keyboard `/` focuses search.; Retry one extra fetch.
After landing: copy No shelves yet.; Keyboard and Retry still present.
After restore: copy Coming soon. again.
