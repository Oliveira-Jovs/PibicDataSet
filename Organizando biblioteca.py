import os
from PIL import Image
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms
import shutil

# Definindo constantes
N_CLASSES = 14
CLASS_NAMES = [
    'Atelectasis', 'Cardiomegaly', 'Effusion', 'Infiltration', 'Mass', 'Nodule', 'Pneumonia',
    'Pneumothorax', 'Consolidation', 'Edema', 'Emphysema', 'Fibrosis', 'Pleural_Thickening', 'Hernia'
]
DATA_DIR = "images"
TEST_IMAGE_LIST = 'val_list.txt'
BATCH_SIZE = 4
OUTPUT_DIR = 'DataSetDoencasPulmonares'

class ChestXrayDataSet(Dataset):
    def __init__(self, data_dir, image_list_file, transform=None):
        """
        Args:
            data_dir: caminho para o diretório de imagens.
            image_list_file: caminho para o arquivo contendo os nomes das imagens e seus respectivos rótulos.
            transform: transformação opcional a ser aplicada em uma amostra.
        """
        image_names = []
        labels = []
        with open(image_list_file, "r") as f:
            for line in f:
                items = line.split()
                image_name = items[0]
                label = items[1:]
                label = [int(i) for i in label]
                found = False
                for i in range(1, 13):
                    name = os.path.join(data_dir, f"images_{i:03d}/images", image_name)
                    if os.path.exists(name):
                        image_name = name
                        found = True
                        break
                if not found:
                    print(f"Imagem {image_name} não encontrada em nenhum dos diretórios esperados.")
                    continue
                image_names.append(image_name)
                labels.append(label)

        self.image_names = image_names
        self.labels = labels
        self.transform = transform

    def __getitem__(self, index):
        """
        Args:
            index: o índice do item
        Retorna:
            imagem e seus rótulos
        """
        image_name = self.image_names[index]
        image = Image.open(image_name).convert('RGB')
        label = self.labels[index]
        if self.transform is not None:
            image = self.transform(image)
        return image, torch.FloatTensor(label), image_name  # Retornar o nome da imagem também

    def __len__(self):
        return len(self.image_names)

# Definir qualquer transformação, se necessário
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Criar o conjunto de dados de teste
test_dataset = ChestXrayDataSet(data_dir=DATA_DIR, image_list_file=TEST_IMAGE_LIST, transform=transform)

# Função para mapear rótulos para nomes de classes
def map_labels_to_class_names(labels):
    class_names = [CLASS_NAMES[i] for i, label in enumerate(labels) if label == 1]
    return class_names

# Função para criar pastas para cada doença, se não existirem
def create_disease_folders(output_dir, class_names):
    for class_name in class_names:
        class_folder = os.path.join(output_dir, class_name)
        os.makedirs(class_folder, exist_ok=True)

# Criar pastas para cada doença
create_disease_folders(OUTPUT_DIR, CLASS_NAMES)

# Iterar sobre o conjunto de dados de teste e mover as imagens para as pastas correspondentes
for i in range(len(test_dataset)):
    try:
        image, label, image_name = test_dataset[i]
        cont = i + 1
        class_names = map_labels_to_class_names(label)
        for class_name in class_names:
            dest_folder = os.path.join(OUTPUT_DIR, class_name)
            dest_path = os.path.join(dest_folder, os.path.basename(image_name))
            shutil.move(image_name, dest_path)
            print(f"Imagem {image_name} movida para {dest_path}")
    except FileNotFoundError as e:
        print(f"Erro ao mover {image_name}: {e}")

print("Processo concluído.")
