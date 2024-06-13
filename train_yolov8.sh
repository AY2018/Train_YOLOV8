#!/bin/bash
#SBATCH --job-name=YoloV8Training
#SBATCH --output=YoloV8Training%j.out
#SBATCH --error=YoloV8Training%j.err
#SBATCH --partition=gpu_p4
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --gres=gpu:8
#SBATCH --cpus-per-task=8
#SBATCH --time=01:00:00
#SBATCH --qos=qos_gpu-t4
#SBATCH --account=your_account_name

# Load necessary modules
module purge
module load cpuarch/amd
module load pytorch-gpu/py3/1.12.1

# Create and activate the conda environment
conda create -n yolov8-env python=3.8 -y
source activate yolov8-env

# Install YOLOv8 dependencies
pip install ultralytics

# Run your YOLOv8 training script
srun python -u /chemin/train.py
