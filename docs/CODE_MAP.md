# Source code provenance and study-stage map

Research source scripts have been organized from the original study archive into `analysis/`, `src/` and `experiments/`. Saved Jupyter outputs and execution counters were cleared.

| Stage | Files |
|---|---|
| S1 | `analysis/S1_data_preparation.ipynb` |
| S2 | `analysis/S2_elastic_net_baseline.ipynb` |
| S3.1 | Four CV model variants under `analysis/S3_1_*.py` |
| S3.2 | Eight exploratory target combinations under `experiments/` |
| S3.3 | Four out-of-fold model notebooks and `S3_3_combine_oof_predictions.Rmd` |
| S3.4 | `analysis/S3_4_final_model_training.ipynb` |
| S4 | NIA coding, data assembly, living-participant checks and inference |
| S5 | Predicted-trajectory combination, longitudinal plots, clustering and PCA |
| Utilities | Historical LSTM/BiLSTM variants under `src/` |

Some original imports and filenames differ from the new directory layout; these historical scripts document the computational research but are not guaranteed to run unmodified without the authorized research environment.

The separate [synthetic BiLSTM demonstration](../examples/synthetic_bilstm_demo.py) runs without clinical data. No actual participant data files are included.
