#!/usr/bin/env python3
"""Create a production delivery HTML report scaffold.

The script creates:
  .production-delivery-reports/YYYY-MM-DD_slug/index.html
  .production-delivery-reports/YYYY-MM-DD_slug/evidence/
  .production-delivery-reports/YYYY-MM-DD_slug/manifest.json

It only scaffolds stable structure. Agents must replace placeholders with real
task evidence before treating the report as final.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
from pathlib import Path


VALID_STATUSES = {"complete", "candidate", "partial", "blocked", "self-reviewed"}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "delivery-report"


def html_escape(value: str) -> str:
    return html.escape(value, quote=True)


def build_html(args: argparse.Namespace, report_id: str) -> str:
    title = html_escape(args.title)
    status = html_escape(args.status)
    generated = html_escape(args.generated_at)
    repository = html_escape(args.repository)
    delivery_target = html_escape(args.delivery_target)
    ci_status = html_escape(args.ci_status)
    ci_reference = html_escape(args.ci_reference)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Production Delivery Report - {title}</title>
  <style>
    body {{ margin: 0; font-family: Arial, sans-serif; color: #172033; background: #f6f7f9; }}
    main {{ max-width: 1120px; margin: 0 auto; padding: 32px 20px 56px; }}
    h1, h2, h3 {{ color: #111827; }}
    h1 {{ margin: 0 0 8px; font-size: 30px; }}
    h2 {{ margin-top: 32px; border-bottom: 1px solid #d9dee8; padding-bottom: 8px; font-size: 21px; }}
    h3 {{ margin-top: 20px; font-size: 16px; }}
    .meta, .grid {{ display: grid; gap: 12px; }}
    .meta {{ grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); margin: 20px 0; }}
    .grid {{ grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }}
    .panel {{ background: #fff; border: 1px solid #d9dee8; border-radius: 8px; padding: 16px; }}
    .status {{ display: inline-block; padding: 4px 8px; border-radius: 999px; font-weight: 700; }}
    .complete {{ background: #e7f7ed; color: #116236; }}
    .candidate, .self-reviewed {{ background: #fff7df; color: #8a5a00; }}
    .blocked, .partial {{ background: #fdecec; color: #9f1d1d; }}
    table {{ width: 100%; border-collapse: collapse; background: #fff; }}
    th, td {{ border: 1px solid #d9dee8; padding: 10px; text-align: left; vertical-align: top; }}
    th {{ background: #eef1f6; }}
    code {{ background: #eef1f6; padding: 2px 4px; border-radius: 4px; }}
    figure {{ margin: 16px 0; background: #fff; border: 1px solid #d9dee8; border-radius: 8px; padding: 12px; }}
    img {{ max-width: 100%; height: auto; border: 1px solid #d9dee8; }}
    figcaption {{ margin-top: 8px; color: #4b5563; font-size: 14px; }}
    .risk {{ border-left: 4px solid #d97706; }}
    .gap {{ border-left: 4px solid #b91c1c; }}
    .ok {{ border-left: 4px solid #15803d; }}
  </style>
</head>
<body>
<main>
  <h1>Production Delivery Report</h1>
  <p>{title}</p>

  <section class="meta">
    <div class="panel"><strong>Status</strong><br><span class="status {status}">{status}</span></div>
    <div class="panel"><strong>Generated</strong><br>{generated}</div>
    <div class="panel"><strong>Repository</strong><br>{repository}</div>
    <div class="panel"><strong>Delivery Target</strong><br>{delivery_target}</div>
    <div class="panel"><strong>Report ID</strong><br>{html_escape(report_id)}</div>
    <div class="panel"><strong>CI / Workflow</strong><br>{ci_status}<br>{ci_reference}</div>
  </section>

  <section class="panel ok" id="executive-validation">
    <h2>Executive Validation</h2>
    <p>Replace this paragraph with what was delivered, whether a user decision is needed, and why this is ready for human review.</p>
  </section>

  <section id="human-checkpoints">
    <h2>Human Checkpoints</h2>
    <ul>
      <li>[ ] Architecture boundary matches the intended product or engineering direction.</li>
      <li>[ ] Core flow matches the business rule.</li>
      <li>[ ] Evidence is sufficient for the risky surface.</li>
      <li>[ ] Residual risks are acceptable.</li>
    </ul>
  </section>

  <section id="architecture-review-surface">
    <h2>Architecture Review Surface</h2>
    <div class="grid">
      <div class="panel"><h3>Main Boundary</h3><p>Replace with changed boundary and ownership.</p></div>
      <div class="panel"><h3>Dependency Direction</h3><p>Replace with dependency direction and integration notes.</p></div>
      <div class="panel"><h3>Non-goals</h3><p>Replace with what intentionally did not change.</p></div>
    </div>
  </section>

  <section id="core-logic-review-surface">
    <h2>Core Logic Review Surface</h2>
    <ol>
      <li>Replace with critical flow step one.</li>
      <li>Replace with critical flow step two.</li>
      <li>Replace with critical flow step three.</li>
    </ol>
    <p><strong>Invariants:</strong> Replace with business, permission, tenant, audit, idempotency, or failure-path invariants.</p>
  </section>

  <section id="evidence-map">
    <h2>Evidence Map</h2>
    <table>
      <thead><tr><th>Evidence</th><th>Grade</th><th>Result</th><th>Proves</th><th>Limits</th></tr></thead>
      <tbody>
        <tr><td><code>Replace with command, CI job, browser check, or artifact</code></td><td>build_typecheck</td><td>not filled</td><td>Replace with proof.</td><td>Replace with limitation.</td></tr>
      </tbody>
    </table>
  </section>

  <section id="browser-evidence">
    <h2>Browser Evidence</h2>
    <p>Add screenshots only when browser/UI validation occurred. Screenshots prove visible state only; they do not by themselves prove backend correctness, permissions, data isolation, idempotency, or transactions.</p>
    <p>When a screenshot is bundled, add a figure with a relative image path, viewport, route, action path, console/network result, and evidence limitation.</p>
  </section>

  <section class="panel risk" id="steelman-counter-review">
    <h2>Steelman Counter-Review</h2>
    <p><strong>Strongest objection:</strong> Replace with the strongest reason this should not ship yet.</p>
    <p><strong>Evidence checked:</strong> Replace with files, tests, docs, commands, CI, browser evidence, or explicit assumptions.</p>
    <p><strong>Decision:</strong> fixed / verified / accepted residual risk / needs user decision.</p>
    <p><strong>Human validation surface:</strong> Replace with whether packet/report is complete, repaired, omitted with reason, or downgraded.</p>
  </section>

  <section id="workspace-and-integration">
    <h2>Workspace and Integration</h2>
    <p>Replace with original workspace, branch/worktree, delivery target, integration status, cleanup status, and unrelated changes.</p>
  </section>

  <section id="appendix">
    <h2>Appendix</h2>
    <p>Replace with concise file list, important diffs by intent, skipped checks, follow-up tasks, and evidence omissions.</p>
  </section>
</main>
</body>
</html>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a production delivery report scaffold.")
    parser.add_argument("--title", required=True, help="Human-readable report title.")
    parser.add_argument("--slug", help="Short URL/file-system safe slug. Defaults to title slug.")
    parser.add_argument("--status", default="candidate", choices=sorted(VALID_STATUSES))
    parser.add_argument("--repository", default="not specified")
    parser.add_argument("--delivery-target", default="not specified")
    parser.add_argument("--output-root", default=".production-delivery-reports")
    parser.add_argument("--date", help="Report date in YYYY-MM-DD. Defaults to local date.")
    parser.add_argument("--generated-at", help="Generated timestamp. Defaults to local time.")
    parser.add_argument("--ci-status", default="not run")
    parser.add_argument("--ci-reference", default="not provided")
    parser.add_argument("--force", action="store_true", help="Overwrite existing index.html and manifest.json.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    now = dt.datetime.now().replace(microsecond=0)
    report_date = args.date or now.date().isoformat()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", report_date):
        raise SystemExit("--date must use YYYY-MM-DD format.")
    args.generated_at = args.generated_at or now.isoformat(sep=" ")
    slug = slugify(args.slug or args.title)
    if slug == "delivery-report" and not args.slug:
        slug = f"delivery-report-{now.strftime('%H%M%S')}"
    report_id = f"{report_date}_{slug}"
    report_dir = Path(args.output_root).expanduser().resolve() / report_id
    evidence_dir = report_dir / "evidence"
    index_path = report_dir / "index.html"
    manifest_path = report_dir / "manifest.json"

    report_dir.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(exist_ok=True)

    if not args.force and (index_path.exists() or manifest_path.exists()):
        raise SystemExit(f"Report already exists: {report_dir}. Re-run with --force to overwrite scaffold files.")

    index_path.write_text(build_html(args, report_id), encoding="utf-8", newline="\n")
    manifest = {
        "report_id": report_id,
        "title": args.title,
        "status": args.status,
        "generated_at": args.generated_at,
        "repository": args.repository,
        "delivery_target": args.delivery_target,
        "ci_status": args.ci_status,
        "ci_reference": args.ci_reference,
        "index": "index.html",
        "evidence_dir": "evidence",
        "evidence": [],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(index_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
