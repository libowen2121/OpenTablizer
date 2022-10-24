from opentablizer.pipelines.base import Pipeline
from opentablizer.models.base import Model
from opentablizer.utils.config import ConfigDict
from opentablizer.utils.constants import DEFAULT_SETUP_FOR_TASK, Tasks, Pipelines
from opentablizer.utils.register import build_from_cfg, registers


def pipeline(task: str = None,
             pipeline: str = None,
             model: str = None,
            #  preprocessor=None,
             config_file: str = None,
             model_source: str = 'from_pretrained',
             device: str = 'gpu',
             **extra_kwargs) -> Pipeline:
    """The method to create a pipeline for a given task.

    Args:
        task (str, optional): task name. Defaults to None.
        pipeline (str, optional): pipeline name. Defaults to None.
        model (str, optional): model name. Defaults to None.
        config_file (str, optional): _description_. Defaults to None.
        model_source (str, optional): model resource [from_pretrained, from_off_the_shelf, from_rules]. Defaults to 'from_pretrained'.
        device (str, optional): device. Defaults to 'gpu'.

    Raises:
        ValueError: _description_

    Returns:
        Pipeline: _description_
    """    
    
    if task is None:
        raise ValueError('task is required')

    assert isinstance(model, (type(None), str, list)), \
        f'model should be either None, str, List[str], or List[Model], but got {type(model)}'
    
    if pipeline is None:
        # get default pipeline and default model for this task
        pipeline, default_model = get_default_pipeline_info(task)
    if model is None:
        model = default_model 
    
    cfg = ConfigDict(task=task, type=pipeline, model=model, 
                     model_source=model_source, device=device)  # default type is pipeline
    if extra_kwargs:
        cfg.update(extra_kwargs)

    # TODO
    # if preprocessor is not None:
    #     cfg.preprocessor = preprocessor

    return build_from_cfg(cfg, registers.pipelines, group_key=task)


def get_default_pipeline_info(task):
    """ Get default info for a given task.

    Args:
        task (str): task name.

    Return:
        A tuple: first element is pipeline name, second element
            is model name.
    """
    default_pipeline, default_model = DEFAULT_SETUP_FOR_TASK[task]
    return default_pipeline, default_model

