# Spatial Network Analysis of Urban Street Layouts
**Author:** Zhang Shengliang | **BUPT ID:** 2022213756  
**Programme:** Information and Computational Science | **Institution:** Queen Mary School Hainan / BUPT

---

## Project Overview
This project develops a macro-micro dual-perspective framework for analysing street network morphology across 34 major Chinese cities, including municipalities, provincial capitals, and autonomous region capitals. The framework resolves topological distortions in open-source street data and enables standardised batch analysis across cities with diverse terrains and historical backgrounds.

---

## Required Packages and Dependencies
- Python 3.9
- OSMnx v1.2.2
- GeoPandas v0.12.2
- NetworkX v2.8.8
- NumPy v1.24.3
- Matplotlib v3.7.1
- Jupyter Notebook

Install all dependencies:
pip install osmnx==1.2.2 geopandas==0.12.2 networkx==2.8.8 numpy==1.24.3 matplotlib==3.7.1

---

## Code Structure
/pilot_study
  haikou_pilot.ipynb        — Haikou pilot analysis and method validation

/batch_analysis
  batch_34cities.ipynb      — Full 34-city batch processing

/results
  /network_maps             — Street network maps for all 34 cities
  /rose_diagrams            — Orientation rose diagrams for all 34 cities
  core_indicators_34cities.csv  — Complete indicator dataset

---

## Dataset
Street network data was retrieved from OpenStreetMap via the OSMnx API.
Data source: https://www.openstreetmap.org
Administrative boundary data: National Geomatics Centre of China Public Service Platform

The dataset is self-generated through the provided code. Raw data files are not included as they are publicly available and can be retrieved by running the notebooks.

---

## How to Run
1. Install all required packages listed above
2. Open Jupyter Notebook
3. Run haikou_pilot.ipynb first to validate the method
4. Run batch_34cities.ipynb for the full 34-city analysis
5. Results will be saved automatically to the /results folder

---

## Key Findings
- Terrain is the strongest predictor of street network character
- Ancient planned cities (Xi'an, Beijing) retain imperial grid logic
- Hong Kong and Macao produce near-circular orientation rose diagrams, closest to organic European cities in Boeing's global dataset
- The macro-micro framework reduced pseudo-node counts by over 40% and brought core indicator errors below 3%
