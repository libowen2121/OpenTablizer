NER
========

This page introduces the base model classes of the text-to-table pipeline. 

BioNER
--------

..  code-block:: python

   from opentablizer.pipelines import pipeline
   from opentablizer.postprocessor import postprocess

   # Run the pipeline
   ner = pipeline(task='ner', model='xxx', config_file='xxx')
   result_json_obj = ner(text='xxx')
   
   # Postprocess the output
   table_obj = postprocess(result_json_obj)