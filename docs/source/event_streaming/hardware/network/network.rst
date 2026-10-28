Network
=======

A stream needs two network connections: a local network that connects the
cameras to the streaming computer, and an internet connection that carries the
stream to the platform. Test both at the venue before event day if you can.

Internet Connection
-------------------

Streaming depends on *upload* speed. Run a speed test from the streaming
computer, on the same connection it will use during the event, and note the
upload number. Set the video bitrate in OBS to no more than about half of that
number, so the stream still has headroom when other devices on the network
get busy. YouTube's `live encoder settings page
<https://support.google.com/youtube/answer/2853702>`__ lists the bitrates it
recommends for each resolution.

Connect the streaming computer to the internet with a network cable whenever
possible. Avoid running the stream through a phone hotspot near the field: a
hotspot adds another Wi-Fi network on the channels robots use. See the
:doc:`/control_system_troubleshooting/index` for how other Wi-Fi traffic
affects robots.

School Networks
---------------

School networks often block streaming sites. Contact the school's IT staff at
least a week before the event and ask:

- Whether the streaming computer can use a staff network or a wired port with
  fewer restrictions than the guest network.
- Whether outbound connections to YouTube's ingest servers are allowed. Stream
  ingest is often allowed even when browsing to youtube.com is blocked.
- If the standard RTMP port (1935) is blocked, whether RTMPS over port 443
  works. OBS can use YouTube's RTMPS servers, and port 443 is the same port
  used for ordinary secure web traffic.

Bronze Tier
-----------

A Bronze setup with a single USB webcam doesn't need a local camera network.
If you use one IP camera, connect it with a PoE splitter and a network cable,
either straight to the streaming computer or to a small switch.

Silver Tier
-----------

With two or more IP cameras, use a small PoE switch to power and connect them.
Several regions use 5-port Gigabit PoE switches that cost about $26. Managed
versions cost little more than unmanaged ones and are worth buying, because
they let you see which ports are powered and which devices are connected.

Give each camera a fixed IP address, either set on the camera or reserved on
the router. That way the camera addresses saved in OBS keep working at every
event.

Gold Tier
---------

NDI cameras find each other and OBS automatically, but that discovery usually
only works when everything is on the same local network. Venue networks often
block it. Put NDI cameras, the streaming computer, and any Dante audio
equipment on their own switch rather than the venue's network, and connect
the streaming computer to the internet separately.
