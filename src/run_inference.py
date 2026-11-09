"""Entry point for Memory-Efficient Transformer Inference via Blockwise Recomputation."""

from .blockwise import build_model


def main():
    model = build_model()
    print("ready:", model)


if __name__ == "__main__":
    main()
