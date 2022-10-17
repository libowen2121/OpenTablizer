from opentablizer.pipeline.base import Pipeline


def pipeline(task: str = None,
             model: str = None,
             preprocessor=None,
             config_file: str = None,
             device: str = 'gpu',
             **kwargs) -> Pipeline:
    """Build a pipeline object

    Args:
        task (str, optional): _description_. Defaults to None.
        model (str, optional): _description_. Defaults to None.
        preprocessor (_type_, optional): _description_. Defaults to None.
        config_file (str, optional): _description_. Defaults to None.
        device (str, optional): _description_. Defaults to 'gpu'.

    Returns:
        Pipeline: _description_
    """             
    pass