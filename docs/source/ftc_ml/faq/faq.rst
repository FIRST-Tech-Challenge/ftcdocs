FAQ
====

Why is TensorFlow called “TensorFlow”?
----------------------------------------

   -  The name TensorFlow is derived from the single- and
      multi-dimensional arrays that neural networks perform operations
      on, known as “\ *tensors”*. Data in a neural network “flows”
      through the network as its being classified, passing through
      weighted nodes. Hence TensorFlow. There were apparently multiple
      projects known as “TensorFlow” that sprung up at the same time.

How many frames of our object is enough to ensure a good model?
----------------------------------------------------------------

   -  That’s going to be completely dependent upon the object, poses
      you’re trying to account for, backgrounds, and lighting
      conditions. Adding novel objects on top of pre-trained models
      doesn’t require thousands of training frames, but it does require
      the RIGHT training frames to create a general “description” of the
      object. Exceeding 1,000 frames for a single object is likely
      overkill.

How do I know if my model is trained well?
-------------------------------------------
   -  There are a number of :ref:`metrics<ftc_ml/managing_tool/model_metrics/model-metrics:understanding model metrics>`
      that can help you determine when a model begins to converge (where additional
      training will likely lead to no benefit). Pay special attention to
      mAP metrics and Loss metrics, you should see those metrics
      generally settle by around 100 epochs.

Why does my team only get 240 minutes of model training time?
-----------------------------------------------------------------

   -  Training in the Google TensorFlow network on GPU resources is not
      free. Each team is allocated an amount of time based on the costs
      of using the fixed cloud resources. Our hope is that a team who is
      congnizant of their training time should be able to get 2-3 models
      and additional training time on one model with that allocation.

   -  It is not possible for a team to “purchase” additional training
      time for their account. We’re hoping teams will give us feedback
      on what they feel a reasonable amount of time could be (and let us
      figure out how to allocate those resources). However, teams who
      have the capability and resources to clone the open-source `fmltc
      repository <https://github.com/FIRST-Tech-Challenge/fmltc>`__ that
      ftc-ml is based on can run their own “instance” of this tool in
      their own Google Cloud Project. However, swim at your own risk.

Why can’t I seem to get a 100% object detection prediction?
--------------------------------------------------------------

   -  Model predictions are never perfect, and attempting to strive for
      that makes for a really specific and non-generic model. If object
      detection probability is really high (in the 90-99% range), it
      might be pointing out that your model may not be as generic as it
      could be, or is overtrained; it depends on the datasets and what
      you’re trying to do. Generally after training if your model is
      predicting all objects above 50% all the time you’re actually
      doing really well.

I read somewhere about a parameter I can tweak…
-------------------------------------------------

   -  There are no parameters tweakable in ftc-ml, sorry. It was
      designed to be simple and easy to use. If you want, feel free to
      clone your own `fmltc
      repository <https://github.com/FIRST-Tech-Challenge/fmltc>`__,
      modify the code, and deploy it to your own Google Cloud Project
      instance! However, swim at your own risk.

Can object bounding boxes overlap?
--------------------------------------

   -  Sure, but if you have “blocks” in front of a “ball” such that
      objects are obscuring each other, just label the parts that are
      not obscured. Don’t include areas in your bounding box where
      “there would be the rest of the ball here if it wasn’t obscured by
      these blocks”

What are the limitations imposed within the ftc-ml tool? (PER TEAM)
---------------------------------------------------------------------

   -  Max # of Datasets: 20 (you can delete datasets to make more)

   -  Max # of Videos: 50 (you can delete videos to upload more)

   -  Max # of Videos performing tracking at once: 3 (for multiple
      logins doing tracking)

   -  Max # Bounding Boxes per frame: 10

   -  Max Video Limits: 2 Minutes, 1000 frames, 3840 x 2160 resolution,
      100MB