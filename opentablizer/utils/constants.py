
class Tasks:
    named_entity_recognition = 'named-entity-recognition'

class Pipelines:
    """A task can be handled by different pipelines corresponding to
    different models respectively.
    
    """    
    named_entity_recognition = 'named-entity-recognition'

class Models:
    hanlp_named_entity_recognition = 'hanlp_named_entity_recognition'
    regex_named_entity_recognition = 'regex_named_entity_recognition'


DEFAULT_GROUP_NAME = 'default'
TYPE = 'type'

DEFAULT_SETUP_FOR_TASK = {
    # TaskName: (pipeline_module_name, pipeline_module)
    Tasks.named_entity_recognition: (Pipelines.named_entity_recognition,
                                     Models.hanlp_named_entity_recognition)
}