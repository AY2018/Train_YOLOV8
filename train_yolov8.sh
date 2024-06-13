#!/bin/bash
#SBATCH --job-name=YoloV8Training  # Nom du job
#SBATCH --output=YoloV8Training%j.out  # Fichier de sortie (%j est remplacé par l'ID du job)
#SBATCH --error=YoloV8Training%j.err  # Fichier d'erreur (%j est remplacé par l'ID du job)
#SBATCH --partition=gpu_p4  # Partition spécifiée pour utiliser les GPU A100
#SBATCH --nodes=1  # Réserver un nœud
#SBATCH --ntasks=8  # Réserver 8 tâches (ou processus)
#SBATCH --gres=gpu:8  # Réserver 8 GPU
#SBATCH --cpus-per-task=8  # Réserver 8 CPU par tâche (et mémoire associée)
#SBATCH --time=01:00:00  # Temps maximal d'allocation (HH:MM:SS)
#SBATCH --qos=qos_gpu-t4  # Qualité de service (QoS) pour la réservation
#SBATCH --account=your_account_name  # Nom du compte pour la comptabilité

module purge  # Nettoyer les modules chargés par défaut

module load cpuarch/amd  # Charger les optimisations pour les CPU AMD

module load pytorch-gpu/py3/1.12.1  # Charger PyTorch avec support GPU

# Créer et activer un environnement conda
conda create -n yolov8-env python=3.8 -y  Python 3.8
source activate yolov8-env  

# Installer les dépendances de YOLOv8
pip install ultralytics  

# Exécuter votre script de formation YOLOv8
srun python -u /path/to/your/work/directory/train.py  
