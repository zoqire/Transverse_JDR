import numpy as np
import csv
from sklearn.datasets.base import Bunch

def load_my_fancy_dataset():
    with open('fichier.csv') as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        feature_names = ['id_attaque', 'id_cible', 'damage', 'cooldown', 'efficacite']
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)
        target_names = ['damage']
            
        for i, sample in enumerate(data_file):
            data[i] = np.asarray(sample[:-1], dtype=np.int)
            target[i] = np.asarray(sample[4], dtype=np.int)

    return Bunch(data=data, target=target, feature_names=feature_names, target_names=target_names)