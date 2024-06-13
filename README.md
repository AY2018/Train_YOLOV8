# Comment lancer un entrainement Yolo sur le calculateur




## Step 1 - Préparer l'environnement 

```bash
# Connection à Jean Zay
ssh login@jean-zay.idris.fr

# Load les bons modules 

module purge # Vide l'environnement 

module load cpuarch/amd # 

module load pytorch-gpu/py3/1.12.1 # Load version de PyTorch avec GPU support
```


## Step 2 - Préparer les fichiers 

```bash
# Clone le repo avec les scripts + dataset 
git clone https://github.com/AY2018/Train_YOLOV8.git


# Transférer les dosissiers vers le dossier $WORK de Jean Zay. 
scp -r /chemin/vers/dataset login@jean-zay.idris.fr:/chemin/vers/work/directory/
scp /chemin/vers/train.py login@jean-zay.idris.fr:/chemin/vers/work/directory/
scp /chemin/vers/dataset.yaml login@jean-zay.idris.fr:/chemin/vers/work/directory/

```

## Step 3 - Créer un Script Batch

```sh
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

module purge
module load cpuarch/amd
module load pytorch-gpu/py3/1.12.1

# Créer un environnement conda et l'activer 
conda create -n yolov8-env python=3.8 -y
source activate yolov8-env

# Installer YOLOv8 
pip install ultralytics

# Lancer le script d'entrainement
srun python -u /chemin/vers/$WORK/train.py

```


## Step 4 - Lancer le job 

```bash
sbatch /path/to/your/work/directory/train_yolov8.sh
```

## Step 5 - Monitorer le Job 

```bash
squeue -u $USER
```

## Récupérer le modèle 
À la fin de l'entraînement d'un modèle, un nouveau dossier `run` est crée avec des fichiers contenant des infos sur le déroulé de l'entrainement ainsi que les modèle. Il faut les récupérer à la fin. 

```bash
scp -r login@jean-zay.idris.fr:chemin/vers/$WORK/runs /chemin/vers/dossier/local

```



