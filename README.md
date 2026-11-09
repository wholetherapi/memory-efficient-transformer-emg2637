# Memory-Efficient Transformer Inference via Blockwise Recomputation

Reference implementation accompanying the paper *Memory-Efficient Transformer Inference via Blockwise Recomputation*.

Utilities for activation checkpointing and blockwise recomputation during inference.

## Installation

```bash
git clone https://github.com/wholetherapi/memory-efficient-transformer-emg2637.git
cd memory-efficient-transformer-emg2637
pip install -r requirements.txt
```

## Repository layout

- `src/run_inference.py` — training / evaluation entry point
- `src/blockwise.py` — core implementation
- `tests/` — unit tests
