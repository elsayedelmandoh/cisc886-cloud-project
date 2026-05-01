"""Cloud-based Conversational Chatbot - CISC 886 Project

Entry point for running the cloud-based chatbot project.
Supports running individual sections via CLI commands.
"""
 
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.config.settings import (
    AWS_CONFIG,
    EC2_CONFIG,
    EMR_CONFIG,
    MODEL_CONFIG,
    DATASET_CONFIG,
    S3_PATHS,
    OLLAMA_CONFIG,
    OPENWEBUI_CONFIG,
)

from src.utils.helpers import (
    print_config,
    run_notebook,
    run_all_notebooks,
    list_s3_files,
    test_s3_connection,
    show_help,
)


NOTEBOOK_MAP = {
    "1": "notebooks/01-system-architecture/01-architecture.ipynb",
    "2": "notebooks/02-vpc-and-networking/01-vpc-networking.ipynb",
    "3": "notebooks/03-model-and-dataset-selection/01-model-dataset-selection.ipynb",
    "4": "notebooks/04-data-preprocessing-with-apaches-spark-on-emr/01-preprocessing.ipynb",
    "5": "notebooks/05-model-fine-tuning/01-fine-tuning.ipynb",
    "6": "notebooks/06-model-deployment-on-ec2/01-deployment.ipynb",
    "7": "notebooks/07-web-interface/01-web-interface.ipynb",
}


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "config":
        print_config(AWS_CONFIG, EC2_CONFIG, MODEL_CONFIG, EMR_CONFIG)

    elif command == "notebook":
        if len(sys.argv) < 3:
            print("Error: Specify section number (1-7)")
            print("Usage: python app.py notebook <section>")
            return
        section = sys.argv[2]
        if section not in NOTEBOOK_MAP:
            print(f"Invalid section: {section}")
            print(f"Valid sections: {', '.join(NOTEBOOK_MAP.keys())}")
            return
        notebook_path = PROJECT_ROOT / NOTEBOOK_MAP[section]
        run_notebook(str(notebook_path))

    elif command == "notebooks":
        notebook_dir = PROJECT_ROOT / "notebooks"
        run_all_notebooks(str(notebook_dir))

    elif command == "s3-list":
        print(f"Listing files in s3://{AWS_CONFIG['bucket_name']}")
        list_s3_files(AWS_CONFIG['bucket_name'])

    elif command == "s3-test":
        test_s3_connection()

    elif command == "help":
        show_help()

    else:
        print(f"Unknown command: {command}")
        print("Run 'python app.py help' for usage information")


if __name__ == "__main__":
    main()