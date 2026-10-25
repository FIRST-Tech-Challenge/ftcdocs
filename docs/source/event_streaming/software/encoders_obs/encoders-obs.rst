Encoders (OBS)
==============

An encoder takes the camera and audio inputs, combines them into a single
picture, compresses it, and sends it to the streaming platform. `OBS Studio
<https://obsproject.com/>`__ is the recommended encoder for FTC events at every
tier. It is free, runs on Windows, macOS, and Linux, and is widely used, so
help is easy to find.

Scenes and Sources
------------------

OBS organizes a stream into *scenes*. Each scene is a layout made up of
*sources*, such as a camera, an image, or the FTC Live audience display. The
stream shows one scene at a time, and switching scenes changes what viewers
see.

A typical FTC event uses these scenes:

- **Field**: the field camera with the FTC Live audience display or score bar
  on top. Viewers see this scene during :term:`matches <Match>`.
- **Awards**: the awards camera, used for :term:`alliance <Alliance>` selection and the awards
  ceremony (Silver and Gold).
- **Break**: a still image with the event name and the time play resumes,
  used during lunch and other breaks.

Keep overlays simple. If you can download a ready-made lower-third or overlay
template and use it as is, that's worthwhile. Designing your own graphics
usually isn't worth the time for a qualifier.

Settings Worth Changing
-----------------------

- **Output > Streaming > Video Encoder**: choose the hardware encoder (NVENC,
  AMF, or QuickSync) if one is listed. See
  :doc:`Streaming Computer </event_streaming/hardware/streaming_computer/streaming-computer>`.
- **Output > Streaming > Bitrate**: set this to no more than half of the
  venue's measured upload speed. See
  :doc:`Network </event_streaming/hardware/network/network>`.
- **Output > Recording**: record to the MKV format. If OBS or the computer
  crashes, an MKV file is still usable up to the point of the crash, while an
  MP4 file is often unreadable. After the event, use **File > Remux
  Recordings** to convert the MKV to MP4 without re-encoding it.

Record locally while you stream. The recording is your backup if the internet
connection drops, and it is the source for
:doc:`post-event match splitting </event_streaming/addons/match_splitting/post_event/post-event>`.

Once the scenes and settings are working, export them with **Scene Collection
> Export** and **Profile > Export**. The exported files can be imported on
another computer or at the next event, so the setup only has to be built once.

Bronze Tier
-----------

Use a single Field scene for matches and leave it running. Nobody needs to
operate OBS during matches. Switch to the Break scene during lunch, if you
have one.

Silver Tier
-----------

Add an Awards scene for the second camera. The Technical Director switches to
it for alliance selection and the awards ceremony, and back to the Field scene
afterward. Matches still run on the Field scene without anyone touching OBS.

An inexpensive macro keypad, such as an Elgato Stream Deck Mini, puts each
scene on its own labeled button. That's easier and less error-prone than
clicking through OBS under pressure.

Gold Tier
---------

Use an automation tool connected to FTC Live to switch scenes and start and
stop recordings for each match. OBS has a built-in WebSocket server
(**Tools > WebSocket Server Settings**) that lets outside programs control it.
Automation tools use this to switch scenes without anyone touching OBS. See
:doc:`FTC Live Integration </event_streaming/addons/ftc_live_integration/ftc-live-integration>`.
