Encoders (Rotation Counters)
==============================


.. list-table:: Example Encoders

    * - .. figure:: images/REV-41-1291.png
            :align: center
            :width: 50%

      - .. figure:: images/REV-11-1271.png
            :align: center
            :width: 50%

An encoder is a device that measures the roatational displacement around an axis. 
All legal FTC motors contain a built in quadrature encoder that is compatible with 
a REV Hub. It is also possible to use a standalone incremental encoder like a 
REV Through Bore Enocder (shown above). An encoder works by sending out a "tick" 
per partial rotation of the shaft. More information on how many ticks are output per 
rotation can be found on the manufacturer's website. A relative encoder will only be 
able to indicate the displacement of the shaft from its starting position. An absolute 
encoder is able to indicate the displacement of the shaft from its starting position and 
the the exact angle the shaft is currently at relative to a "zero" position.


Additional Resources
---------------------

 - :ref:`Encoder Port Overview <control_hard_compon/rc_components/hub/ports/exh-ports:encoder ports>`