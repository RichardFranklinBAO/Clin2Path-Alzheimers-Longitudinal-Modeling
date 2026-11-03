# Data availability and reproducibility

The original Clin2Path analysis uses research data from the ROS/MAP cohorts. This portfolio intentionally excludes the underlying participant-level clinical datasets, identifiable records, trained model weights, and subject-level intermediate predictions. Filenames and cohort-variable names in code are necessary to document data inputs and should not be interpreted as shared participant records.

The original research scripts reflect a multi-stage analysis and include different exploratory model variants. They depend on research datasets, data paths and utility imports that are not distributed as a turnkey pipeline. Independent readers can run the self-contained [synthetic BiLSTM example](../examples/synthetic_bilstm_demo.py), which does not use ROS/MAP participants.

The code-sharing permission was confirmed by the repository owner with the supervising researcher. This does not change the access conditions governing the underlying cohort data.

**Analytic distinction:** Model-inferred pathology for living participants should not be presented as directly measured neuropathology; some BiLSTM models use retrospective complete sequence information.
