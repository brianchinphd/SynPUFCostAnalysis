# SynPUFCostAnalysis

This repository contains payer-style healthcare analytics case studies built with the CMS Medicare Synthetic Public Use Files (SynPUF, Sample 13). The portfolio is designed to show how claims-style data can be translated into decision support for cost of care, risk stratification, and PMPM trend validation.

## What This Portfolio Demonstrates

- Claims-based healthcare analytics using Python and SQL-style workflows
- Cost-of-care and utilization analysis across large administrative datasets
- Risk stratification, cohort segmentation, and trend decomposition
- Reproducible, decision-facing analytics that connect findings to action

## Project Directory

### 1. High-Cost Tail Simulation: Outpatient Spend Concentration

**Business question**  
Which outpatient member segment is driving disproportionate spend, and where would targeted intervention be most actionable?

**Approach**  
Using SynPUF claims data, this project identifies the highest-cost outpatient member segment and simulates condition-focused cost-reduction scenarios across service lines.

**Key result**  
The top 1.25% of members accounted for 14% of outpatient spend. Intervention scenarios were then modeled to compare expected savings and identify the most actionable targets.

**Why it matters**  
This project provides a scalable high-cost tail framework that helps cost-of-care teams focus on the small segment driving disproportionate spend and prioritize interventions with the strongest projected impact.

### 2. Sleep and CVD Predictors: Risk Signal Modeling

**Business question**  
Can diagnosis-based signals identify members at elevated risk for higher ED utilization and total medical cost?

**Approach**  
Using CMS SynPUF claims data, this project builds a claims-based risk stratification workflow using sleep-disorder and cardiovascular diagnosis flags linked to ED utilization and total cost.

**Key result**  
Members with both sleep and cardiovascular flags showed the highest ED use. Both signals were also associated with higher ED utilization and higher total medical cost compared with members without those flags.

**Why it matters**  
This project demonstrates a scalable claims-based risk signal framework that can support targeted care management, high-risk member identification, and cost-containment strategy.

### 3. PMPM Trending Prototype: Coverage-Mix Distortion Audit

**Business question**  
Does observed PMPM movement reflect true medical trend, or is it being distorted by denominator mix effects?

**Approach**  
This project uses Connecticut SynPUF data to build a reproducible PMPM trend framework that compares aggregate results with a stable full-year cohort to test for coverage-duration mix distortion.

**Key result**  
Raw market PMPM declined 15.5% from 2008 to 2009, but the 12-month stable cohort showed a 5.4% increase. This divergence suggested that coverage-duration mix was masking the underlying cost trend.

**Why it matters**  
This project provides a defensible PMPM audit workflow that separates population-mix artifacts from underlying trend and improves confidence in cost trend interpretation before action is taken. A lightweight dashboard and memo-generation extension also show how validated trend outputs can be packaged for repeat review and stakeholder communication.

## Notes

- All analyses use synthetic CMS SynPUF data and are intended to demonstrate analytic logic and workflow design rather than real market conditions.
- These projects are decision-support prototypes with emphasis on the business framing, analytic reasoning, and reproducible workflow.
