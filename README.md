# Spatial Network Analysis of Urban Street Layouts

**Author:** Zhang Shengliang | **BUPT ID:** 2022213756
**Programme:** Information and Computational Science | **Institution:** Queen Mary School Hainan / BUPT

## Project Overview

This project develops a macro-micro dual-perspective framework for analysing street network morphology across 34 major Chinese cities. The framework resolves topological distortions in open-source street data and enables standardised batch analysis.

## Required Packages

- Python 3.9
- OSMnx v1.2.2
- GeoPandas v0.12.2
- NetworkX v2.8.8
- NumPy v1.24.3
- Matplotlib v3.7.1

## Dataset

Street network data retrieved from OpenStreetMap via OSMnx API.
Each city has its own notebook containing complete code and results.

## How to Run

1. Install required packages
2. Open any city notebook in Jupyter
3. Run all cells in sequence

## Key Findings

- Terrain is the strongest predictor of street network character
- Beijing and Xi'an retain imperial grid logic (entropy ~2.9)
- Hong Kong and Macao show near-circular rose diagrams (entropy ~3.5)
- Framework reduced pseudo-node counts by over 40%
