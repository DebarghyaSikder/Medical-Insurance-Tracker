import os
from typing import Optional
from Insurance.entity.config_entity import MODEL_FILE_NAME, TRANSFORMER_OBJECT_FILE_NAME, TARGET_ENCODER_OBJECT_FILE_NAME

# FOlder created for new data(new model saved)
# Compare new model with old model by Checking accuracy 
# If new has better accuracy accept it or else keep the old model deployed

# save model ->0->1->2->3

class ModelResolver:
    def __init__(self, model_registry:str="saved_models",
                 transformer_dir_name="transformer",
                 target_encoder_dir_name="target_encoder",
                 model_dir_name="model"):
        
        self.model_registry = model_registry
        os.makedirs(self.model_registry, exist_ok=True)
        self.transformer_dir_name = transformer_dir_name
        self.model_dir_name = model_dir_name
        self.target_encoder_dir_name = target_encoder_dir_name
        
        
    def get_latest_dir_path(self):
        """
        Get the latest directory path from the model registry.
        """
        try:
            dir_name= os.listdir(self.model_registry)
            if len(dir_name) == 0:
                return None
            
            dir_name=list(map(int,dir_name))
            latest_dir = max(dir_name)
            return os.path.join(self.model_registry, f"{latest_dir}")
        
        except Exception as e:
            raise e
        
    def get_latest_model_path(self): 
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception("Model is not available")
            
            return os.path.join(latest_dir, self.model_dir_name, MODEL_FILE_NAME)
        except Exception as e:
            raise e
    
    def get_latest_transformer_path(self):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception("Transform data is not available")
            return os.path.join(latest_dir, self.target_encoder_dir_name, TARGET_ENCODER_OBJECT_FILE_NAME)
        except Exception as e:
            raise e
    
    def get_latest_target_encoder_path(self):
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception("Target encoder data is not available")
            return os.path.join(latest_dir, self.transformer_dir_name, TRANSFORMER_OBJECT_FILE_NAME)

        except Exception as e:
            raise e 
        
    def get_latest_save_dir_path(self):
        """
        Get the latest save directory path from the model registry.
        """
        try:
            latest_dir=self.get_latest_dir_path()
            if latest_dir is None:
                return os.path.join(self.model_registry, f"{0}")
            
            latest_dir_num=int(os.path.basename(self.get_latest_dir_path()))
            return os.path.join(self.model_registry, f"{latest_dir_num}")
        except Exception as e:
            raise e    
        
    def get_latest_save_model_path(self):
        
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir, self.model_dir_name, MODEL_FILE_NAME) # pkl
        except Exception as e:
            raise e    
        
    def get_latest_save_transformer_path(self):
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir, self.transformer_dir_name, TRANSFORMER_OBJECT_FILE_NAME) # transform.pkl       
        except Exception as e:
            raise e
        
    def get_latest_save_target_encoder_path(self):
        try:
            latest_dir=self.get_latest_save_dir_path()
            return os.path.join(latest_dir, self.target_encoder_dir_name, TARGET_ENCODER_OBJECT_FILE_NAME) # target_encoder.pkl
        except Exception as e:
            raise e
                