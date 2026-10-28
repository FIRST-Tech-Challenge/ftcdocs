OBS Plugins
===========

Plugins add features to OBS Studio. Only install the plugins your setup
actually uses. Plugins are built for specific OBS versions, and a major OBS
update can break one, so after every OBS update, test the stream before the
next event.

GStreamer Plugin (Bronze and Silver)
------------------------------------

Most IP cameras send video using RTSP. OBS can open an RTSP feed with its
built-in Media Source, but the picture often lags a second or more behind real
time. The free `OBS GStreamer plugin <https://github.com/fzwoch/obs-gstreamer>`__
opens the same feed with much less delay. This matters when the stream is
also shown on the venue projector, where the audience can see the lag.

DistroAV (Gold)
---------------

NDI cameras and NDI decoders need the `DistroAV plugin
<https://github.com/DistroAV/DistroAV>`__ (formerly called OBS-NDI). With it
installed, NDI cameras on the network appear as sources in OBS, and OBS can
send its program output back out as an NDI feed for remote displays.

Stream Deck Integration (Silver and Gold)
-----------------------------------------

The Elgato Stream Deck software connects to OBS directly, so each button can
switch to a scene, start or stop recording, or mute a microphone. This is the
simplest way to give the Technical Director reliable scene switching without
learning OBS.

Automatic Scene Switching (Gold)
--------------------------------

Automatic scene switching doesn't use a traditional OBS plugin. Instead, an
outside tool reads match information from FTC Live and controls OBS through
OBS's built-in WebSocket server. See
:doc:`FTC Live Integration </event_streaming/addons/ftc_live_integration/ftc-live-integration>`.
