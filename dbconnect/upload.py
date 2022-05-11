import  yaml
import os
from azure.storage.blob import _container_client, ContainerClient


def load_config():
    dir_root=os.path.dirname(os.path.abspath(__file__))
    with open(dir_root + "/config.yaml", "r")as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)


def get_file(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startswith('.'):
                yield entry

def upload(files, connection_string, container_name):
    container_client= ContainerClient.from_connection_string(connection_string, container_name)
    for file in files:
        blob_client= container_client.get_blob_client(file.name)
        with open(file.path, "rb")as data:
            blob_client.upload_blob(data)
config =load_config()
excel= get_file(config["source_folder"])
upload(excel, config["azure_storage_connectionstring"], config["container_name"])


