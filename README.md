# neuromorphic-flow-annotator

A small desktop annotation utility for event-camera optical-flow datasets.
It provides a canvas for correcting flow vectors and exporting DSEC-style
ground-truth files. This repository is companion tooling for dataset
curation; it does not contain a model implementation.

## Usage

```bash
python annotator/app.py --dataset path/to/dsec/split
```
