# UBSN-2026-ROI-SRM-LLM-Encoding-Analysis

This repository contains the analysis code for ROI-based Shared Response Model (SRM) fitting and LLM-based encoding analyses for a naturalistic story-listening fMRI dataset.

The code is provided as reproducible notebooks/templates. Before running, replace all `CHANGE_THIS_TO_YOUR_*` placeholders with paths on your own machine.

## Repository Layout

```text
.
├── notebooks/
│   ├── 01_srm_roi_pipeline.ipynb
│   ├── 02_llm_encoding_pipeline.ipynb
│   └── 03_network_summary_and_figures.ipynb
├── scripts/
│   └── UBSN_followup_inference_template.Rmd
├── utils/
│   ├── README.md
│   └── path_config_template.py
├── data/
│   └── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Analysis Order

1. Run `notebooks/01_srm_roi_pipeline.ipynb` for one ROI/network at a time.
2. Run `notebooks/02_llm_encoding_pipeline.ipynb` for the same ROI/network.
3. After all ROIs/networks are complete, run `notebooks/03_network_summary_and_figures.ipynb`.
4. Run `scripts/UBSN_followup_inference_template.Rmd` for subject-level follow-up inference.

## Path Configuration

Search for `CHANGE_THIS_TO_YOUR_` in the notebooks/Rmd and replace the placeholders, for example:

- `CHANGE_THIS_TO_YOUR_PROJECT_DIR`: root folder where `runs/`, `encoding_runs/`, and summary outputs will be written.
- `CHANGE_THIS_TO_YOUR_BIDS_DATA_DIR`: folder containing participant fMRI data.
- `CHANGE_THIS_TO_YOUR_DATA_ROOT`: parent folder containing transcript and project-level files.
- `CHANGE_THIS_TO_YOUR_SCHAEFER400_ATLAS_NIFTI`: Schaefer-400 17-network atlas NIfTI file.
- `CHANGE_THIS_TO_YOUR_SCHAEFER2018_LABEL_TXT`: official Schaefer-400 label text file.
- `CHANGE_THIS_TO_YOUR_ROI_NAME`: ROI/network name, such as `TempPar`, `DefaultA`, or `ContA`.

## Data Not Included

No raw data, derived outputs, figures, NIfTI maps, NumPy arrays, xlsx tables, or local machine paths are included in this repository.

## Notes

- The notebooks are intentionally kept as notebooks because the original analysis was run interactively one ROI/network at a time.
- Generated output directories are ignored by Git. See `.gitignore`.
- The circular summary figure in `03_network_summary_and_figures.ipynb` is descriptive/integrative; internal lines show participant-wise gain-profile similarity, not functional connectivity.
