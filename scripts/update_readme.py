#!/usr/bin/env python3
"""Fetch recent PRs and update the profile README."""

import json
import os
import subprocess
import re
from datetime import datetime


USERNAME = "acisseJZhong"
REPOS = [
    ("pytorch", "torchtitan"),
    ("pytorch", "pytorch"),
    ("vllm-project", "vllm"),
    ("meta-pytorch", "torchtune"),
]
MAX_PRS_PER_REPO = 10

# PRs with these titles are noise — skip them
SKIP_TITLES = {"test", "fix", "update", "rebase main", "rebase"}


def fetch_prs(owner, repo):
    """Fetch recent PRs by the user for a given repo."""
    query = f"author:{USERNAME}+type:pr+repo:{owner}/{repo}"
    result = subprocess.run(
        [
            "gh", "api",
            f"search/issues?q={query}&sort=created&order=desc&per_page={MAX_PRS_PER_REPO}",
        ],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Error fetching PRs for {owner}/{repo}: {result.stderr}")
        return []

    data = json.loads(result.stdout)
    prs = []
    for item in data.get("items", []):
        title = item["title"].strip()
        if title.lower() in SKIP_TITLES:
            continue

        # Extract a short summary from the body
        body = item.get("body") or ""
        summary = extract_summary(body, title)

        prs.append({
            "number": item["number"],
            "title": title,
            "state": item["state"],
            "date": item["created_at"][:10],
            "summary": summary,
            "url": f"https://github.com/{owner}/{repo}/pull/{item['number']}",
        })
    return prs


def extract_summary(body, title):
    """Extract a concise summary from the PR body."""
    if not body:
        return title

    # Clean up the body
    body = body.replace("\r\n", "\n")

    # Try to find a "Summary" section
    summary_match = re.search(
        r"(?:\*\*Summary\*\*|## Summary|# Summary)[:\s]*\n?(.*?)(?:\n\n|\n#|\n\*\*|$)",
        body, re.IGNORECASE | re.DOTALL,
    )
    if summary_match:
        text = summary_match.group(1).strip()
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # strip links
        text = text.strip("- ").strip()
        if len(text) > 20:
            return text[:150].strip()

    # Try "Motivation" section
    motivation_match = re.search(
        r"(?:\*\*Motivation\*\*|## Motivation|# Motivation)[:\s]*\n?(.*?)(?:\n\n|\n#|\n\*\*|$)",
        body, re.IGNORECASE | re.DOTALL,
    )
    if motivation_match:
        text = motivation_match.group(1).strip()
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = text.strip("- ").strip()
        if len(text) > 20:
            return text[:150].strip()

    # Try first meaningful line
    for line in body.split("\n"):
        line = line.strip().strip("-").strip()
        if (
            len(line) > 20
            and not line.startswith("#")
            and not line.startswith("Stack from")
            and not line.startswith("#### Context")
            and not line.startswith("[")
            and "ghstack" not in line
        ):
            line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
            return line[:150].strip()

    return title


def generate_pr_section():
    """Generate the Recent Contributions markdown section."""
    lines = ["### Recent Contributions", ""]
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    for owner, repo in REPOS:
        prs = fetch_prs(owner, repo)
        lines.append(f"#### [{owner}/{repo}](https://github.com/{owner}/{repo})")
        lines.append("")

        if not prs:
            lines.append("_No recent PRs_")
            lines.append("")
            continue

        lines.append("| Date | PR | Summary |")
        lines.append("|------|-----|---------|")
        for pr in prs:
            summary = pr["summary"].replace("|", "\\|")
            lines.append(
                f"| {pr['date']} | [#{pr['number']}]({pr['url']}) | **{pr['title']}** — {summary} |"
            )
        lines.append("")
        all_prs_url = f"https://github.com/{owner}/{repo}/pulls?q=is%3Apr+author%3A{USERNAME}"
        lines.append(f"[View all my PRs in {owner}/{repo} &rarr;]({all_prs_url})")
        lines.append("")

    lines.append(f"_Last updated: {now}_")
    return "\n".join(lines)


def main():
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    readme_path = os.path.normpath(readme_path)

    if not os.path.exists(readme_path):
        # If run from repo root
        readme_path = "README.md"

    with open(readme_path, "r") as f:
        content = f.read()

    pr_section = generate_pr_section()

    # Replace everything between the markers
    start_marker = "<!-- RECENT_CONTRIBUTIONS_START -->"
    end_marker = "<!-- RECENT_CONTRIBUTIONS_END -->"

    if start_marker in content:
        pattern = re.escape(start_marker) + r".*?" + re.escape(end_marker)
        new_content = re.sub(
            pattern,
            f"{start_marker}\n{pr_section}\n{end_marker}",
            content,
            flags=re.DOTALL,
        )
    else:
        new_content = content + f"\n{start_marker}\n{pr_section}\n{end_marker}\n"

    with open(readme_path, "w") as f:
        f.write(new_content)

    print("README updated successfully.")


if __name__ == "__main__":
    main()
