# Clin2Path: Alzheimer's Neuropathology from Longitudinal Clinical Data

**Research code · Python/PyTorch and R · Co-first-author project**

## Overview

Clin2Path investigates whether longitudinal clinical profiles can help infer Alzheimer's disease neuropathology. The workflow compares an Elastic Net baseline with longitudinal LSTM and bidirectional LSTM approaches, then characterizes model-estimated pathological trajectories using R-based statistical analysis.

**Manuscript status:** In preparation; not yet published.

## Contributions

I served as co-first author with Qile Dai. I took primary responsibility for almost all R programming, including data preparation, predictions merging, longitudinal analysis, K-means/PCA and figures. I contributed to Python/PyTorch LSTM and BiLSTM model development jointly with Qile Dai and proposed exploring the bidirectional architecture. I also participated in writing and revising the manuscript.

## Start here: runnable standalone code

- [Synthetic BiLSTM example](examples/synthetic_bilstm_demo.py) · [Run instructions](examples/README.md)
- The example generates artificial variable-length sequences and demonstrates a PyTorch BiLSTM training loop. It is **not** the original model or a reproduction of the manuscript results.

## Research workflow and source code

| Stage | Code | Purpose |
|---|---|---|
| **S1** | [Data preparation](analysis/S1_data_preparation.ipynb) | Prepare longitudinal clinical measurements and cohort data |
| **S2** | [Elastic Net baseline](analysis/S2_elastic_net_baseline.ipynb) | Benchmark regularized cross-sectional regression |
| **S3.1** | [LSTM/BiLSTM cross-validation](analysis/) | Fit and compare neural-network models for pathology outcomes |
| **S3.2** | [Tangles model experiments](experiments/) | Explore eight outcome-combination variants |
| **S3.3** | [Out-of-fold inference](analysis/) | Generate and consolidate predictions for deceased participants |
| **S3.4** | [Final model training](analysis/S3_4_final_model_training.ipynb) | Fit selected model variants for subsequent prediction |
| **S4** | [Living-participant pathology inference](analysis/S4_5_infer_living_participants.ipynb) | Prepare and predict outcomes for living participants |
| **S5** | [R trajectory analysis](analysis/S5_2_longitudinal_trajectory_plots.Rmd), [clustering/PCA](analysis/S5_2_clustering_pca_plots.Rmd) | Study model-based longitudinal patterns |

[Analysis-stage guide](analysis/README.md) · [Archived source map](docs/CODE_MAP.md) · [Data availability and reproducibility](docs/DATA_AVAILABILITY.md)

The model-utility variants are in [src/](src/). The eight exploratory Tangles target sets are kept separate in [experiments/](experiments/).

## Interpretation and reproducibility

Inferred pathology for living participants is **model-estimated**, not directly observed neuropathology. Retrospective BiLSTM analysis is not the same as real-time forecasting. The archived scripts preserve exploratory versions and some original filenames/import paths; they are not presented as a verified end-to-end replication of the unpublished study.

**No participant-level clinical datasets, trained model weights, or notebook execution outputs are included.** See the [data-availability note](docs/DATA_AVAILABILITY.md) for information about what is and is not distributed.

## Acknowledgment

This research was carried out collaboratively with Qile Dai under Jingjing Yang's supervision. The author confirms that code sharing was discussed with and permitted by the supervising researcher.
