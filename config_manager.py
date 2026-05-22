import json
from pathlib import Path

config_file=Path("config.json")

def load_config():
    default_config={"last_source":"", "zip_default": False}
    
    if not config_file.exists():
        return default_config
    
    with config_file.open("r") as f:
        return json.load(f)
    
def save_config(config_data):
    with config_file.open("w") as f:
        json.dump(config_data,f,indent=4)
        