import argparse
from training.mnist_training import MNISTTraining
from inferences.mnist_inference import MNISTInference


def main():
    parser = argparse.ArgumentParser(
        description="Train or perform inference with the {{cookiecutter.data_set_name}} model"
    )
    parser.add_argument(
        "--mode",
        choices=["train", "inference"],
        help="Select 'train' to train the model or 'inference' to perform inference",
    )
    args = parser.parse_args()

    if args.mode == "train":
        mnist_training = MNISTTraining()
        mnist_training.train()
    elif args.mode == "inference":
        mnist_inference = MNISTInference()
        mnist_inference.infer()


if __name__ == "__main__":
    main()
