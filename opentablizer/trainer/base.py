from tkinter.messagebox import NO
from typing import Union, List
from opentablizer.models.base import Model


class BaseTrainer():
    """Base class for pipeline
    """
    
    def __init__(self,
                 config_file: str = None,
                 model: Union[Model, List[Model]] = None,
                 dataset=None,
                 device: str = 'gpu',
                 **kwargs) -> None:
        """_summary_

        Args:
            config_file (str, optional): _description_. Defaults to None.
            model (Union[Model, List[Model]], optional): _description_. Defaults to None.
            dataset (_type_, optional): _description_. Defaults to None.
            device (str, optional): _description_. Defaults to 'gpu'.
        """        
        pass