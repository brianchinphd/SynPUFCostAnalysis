# AI-Assisted PMPM Review Copilot

This project demonstrates a simple workflow for converting validated PMPM trend outputs into a standardized business-facing memo for cost-of-care review.

## Purpose
The goal is to speed interpretation and communication of PMPM findings after the underlying analysis has already been completed and validated.

## Input
- `PMPM_Summary_CT0809.csv`: summary metrics from the Connecticut 2008-2009 SynPUF PMPM trend analysis

## Workflow
1. Calculate and validate PMPM trend metrics in the main analysis notebook.
2. Export key findings to a compact summary file.
3. Generate a concise memo covering:
   - Executive Summary
   - QA / Interpretation Warning
   - Key Trend Drivers
   - Recommended Follow-Up

## Output
- `sample_memo.md`: example memo generated from the summary metrics

## Local Dashboard

This project also includes a simple Streamlit dashboard (`app.py`) that reads the summary metrics file and presents:
- top-line PMPM trend metrics
- service-line and utilization follow-up signals
- QA flag review
- a generated draft summary for stakeholder communication

Example screenshots:
- `dashboard1.png`
- `dashboard2.png`

## Why this matters
Analysts often spend time translating validated findings into stakeholder-ready language. This workflow shows one way to standardize that step while keeping the underlying analytical logic separate from the memo-generation layer.
