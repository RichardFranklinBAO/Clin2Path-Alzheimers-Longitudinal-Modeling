# Clin2Path research-code navigation

These are archived analyses arranged by the study's original S1–S5 flow. Notebook outputs and execution counts were removed prior to upload. The original restricted ROS/MAP datasets and trained model weights are **not** included.

| Stage | Script(s) | Purpose |
|---|---|---|
| S1 | `S1_data_preparation.ipynb` | Longitudinal cohort construction |
| S2 | `S2_elastic_net_baseline.ipynb` | Cross-sectional Elastic Net benchmarks |
| S3.1 | `S3_1_bilstm_amyloid_cv.py`, `S3_1_bilstm_nia_cv.py`, `S3_1_lstm_tangles_cv.py`, `S3_1_lstm_relu_global_cv.py` | Main architecture and CV experiments |
| S3.2 | [`../experiments/`](../experiments/) | Eight alternative tangles target sets |
| S3.3 | `S3_3_oof_*.ipynb`, `S3_3_combine_oof_predictions.Rmd` | Decedent cross-validation predictions and merging |
| S3.4 | `S3_4_final_model_training.ipynb` | Selected-model fitting |
| S4 | `S4_NIA_coding_checks.Rmd`, `S4_data_table_assembly.Rmd`, `S4_living_participant_checks.Rmd`, `S4_5_infer_living_participants.ipynb` | Cohort checks, classification, living-person inference |
| S5 | `S5_1_combine_group_predictions.Rmd`, `S5_2_longitudinal_trajectory_plots.Rmd`, `S5_2_clustering_pca_plots.Rmd` | Model-based trajectories, K-means, PCA and visualizations |

**The script organization is for portfolio readability, not end-to-end reproducibility.** Several scripts import utilities under their old names or expect original relative directory locations. Model/CV result comparisons must be checked against each original version. No code in this archive is asserted to validate pathologies for living participants.

For a data-free, independently runnable PyTorch example, see [synthetic_bilstm_demo.py](../examples/synthetic_bilstm_demo.py).
