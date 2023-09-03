Zoom
====

Virtual zoom is described with a single dimensionless value of type
integer. Similar to the interfaces described above, virtual zoom can be
managed with these methods: 

-  setZoom(int zoom) 
-  getZoom() 
-  getMinZoom() 
-  getMaxZoom()

The Logitech C920 allows zoom values ranging from 100 to 500, although
values higher than 250-280 have no further effect on the preview image
(influenced by Vuforia).

These zoom methods are called on a PtzControl object, as described above
for exposure.