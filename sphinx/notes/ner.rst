NER
========

This page introduces the base model classes of the text-to-table pipeline. 

BioNER
--------

..  code-block:: python

   from opentablizer.pipelines import pipeline
   from opentablizer.postprocessor import postprocess

   # Run the pipeline from third-party off-the-shelf tools
   ner_pipeline = pipeline(task='named-entity-recognition',
                           model='hanlp_named_entity_recognition',
                           model_source='from_off_the_shelf')
   print(ner_pipeline({'text': '2021年测试高血压是138，时间是午饭后2点45，低血压是44'}))

   # >>> [
   # >>>    ('2021年', 'DATE', 0, 1), 
   # >>>    ('138', 'INTEGER', 4, 5), 
   # >>>    ('2点45', 'TIME', 10, 11), 
   # >>>    ('44', 'INTEGER', 14, 15)
   # >>>    ]
   
   # Postprocess the output
   table_obj = postprocess(result_json_obj)