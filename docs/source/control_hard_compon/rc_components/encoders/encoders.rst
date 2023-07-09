Encoders (Rotation Counters)
==============================

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      REV HD Hex Motor 

      ^^^

      .. figure:: images/REV-41-1291.png
         :align: center
         :width: 50%

      +++

      Built-in Encoder in the REV HD Hex Motor

   .. grid-item-card::
      :class-header: sd-bg-dark font-weight-bold sd-text-white
      :class-body: sd-text-left body

      REV Through Bore Encoder

      ^^^

      .. figure:: images/REV-11-1271.png
         :align: center
         :width: 50%

      +++

      REV Through Bore Encoder, in incremental mode.

An encoder is a device that measures the rotational displacement around an
axis.  Most legal *FIRST* Tech Challenge motors contain a built in quadrature
encoder that is compatible with a REV Hub. It is also possible to use a
standalone incremental encoder like a REV Through Bore Encoder (shown above).
An incremental encoder works by sending out a "tick" per partial rotation of
the shaft. More information on how many ticks are output per rotation can be
found on the manufacturer's website. An absolute encoder is able to indicate
the displacement of the shaft from its starting position and the the exact
angle the shaft is currently at relative to a "zero" position.


Additional Resources
---------------------

 - :ref:`Encoder Port Overview <control_hard_compon/rc_components/hub/ports/exh-ports:encoder ports>`
