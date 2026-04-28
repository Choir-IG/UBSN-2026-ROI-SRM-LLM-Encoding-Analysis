"""Template path configuration for the UBSN ROI analysis.

Copy this file to a local, untracked config file if you want to centralize paths.
Do not commit machine-specific paths to GitHub.
"""

from pathlib import Path

PROJECT_DIR = Path(r"CHANGE_THIS_TO_YOUR_PROJECT_DIR")
BIDS_DATA_DIR = Path(r"CHANGE_THIS_TO_YOUR_BIDS_DATA_DIR")
DATA_ROOT = Path(r"CHANGE_THIS_TO_YOUR_DATA_ROOT")
SCHAEFER400_ATLAS_NIFTI = Path(r"CHANGE_THIS_TO_YOUR_SCHAEFER400_ATLAS_NIFTI")
SCHAEFER2018_LABEL_TXT = Path(r"CHANGE_THIS_TO_YOUR_SCHAEFER2018_LABEL_TXT")
ROI_NAME = "CHANGE_THIS_TO_YOUR_ROI_NAME"
