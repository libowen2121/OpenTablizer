.. Open Tablizer documentation master file, created by
   sphinx-quickstart on Tue Oct 11 17:07:15 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Open Tablizer's documentation
=========================================


Getting Started
---------------


..  code-block:: python

   from opentablizer.pipelines import pipeline

   # Run the pipeline from the third-party off-the-shelf tools
   ner_pipeline = pipeline(task='named-entity-recognition',
                           model='hanlp_named_entity_recognition',
                           model_source='from_off_the_shelf')
   result_obj = ner_pipeline({'text': '2021年测试高血压是138，时间是午饭后2点45，低血压是44'})
   print(result_obj)

   # >>> [
   # >>>    ('2021年', 'DATE', 0, 1), 
   # >>>    ('138', 'INTEGER', 4, 5), 
   # >>>    ('2点45', 'TIME', 10, 11), 
   # >>>    ('44', 'INTEGER', 14, 15)
   # >>>    ]

   # Run the pipeline from rules

   # Run the pipeline from pretrained models (CPM & OpenDelta)
   
   

.. toctree::
   :glob:
   :maxdepth: 3
   :caption: Package Reference

   modules/pipeline
   modules/trainer
   modules/model


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
