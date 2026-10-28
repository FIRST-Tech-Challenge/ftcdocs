Streaming Computer
==================

The streaming computer runs OBS Studio, which decodes the camera feeds,
combines them, encodes the result, and sends it to the platform. Most events
need only one streaming computer, however many fields or divisions they have:
the stream is a single program feed, and OBS switches between fields within
it. How powerful that computer needs to be, and whether an event needs more
than one, depends on how much decoding and encoding work it has to do.

What Makes the Computer Work Harder
-----------------------------------

- **Each camera.** IP and NDI cameras send compressed video, and OBS has to
  decode every one of them while it is connected, not only the one on screen.
  Each camera you add increases the load.
- **Resolution and frame rate.** A 1080p stream at 60 frames per second takes
  about twice the work of one at 30 frames per second. 1080p at 30 frames per
  second is plenty for an FTC event.
- **Each separate encode.** The stream, a local recording, per-match
  recordings, and an NDI output to remote displays can each need their own
  encode. In OBS's simple output mode, setting the recording quality to
  **Same as stream** reuses the stream's encode instead of making a second
  one.
- **Browser sources.** The FTC Live audience display is a web page, and OBS
  renders it like a browser would.

How Many Computers
------------------

Plan on one streaming computer for each separate stream. A running copy of
OBS produces one program feed, so an event that streams all of its fields or
divisions as a single feed needs one computer.

Championships that stream each division as its own feed need a separate
encode for each one. That is usually more than one computer can handle well,
so plan on one streaming computer per division stream.

Choosing a Computer
-------------------

- **Use a hardware encoder if the computer has one.** Most computers with a
  recent NVIDIA, AMD, or Intel graphics chip include one, and OBS lists it in
  the encoder setting as NVENC, AMF, or QuickSync. A hardware encoder takes
  the encoding work off the processor, which leaves room for decoding cameras
  and running everything else.
- **Plug it into wall power.** Laptops often slow down on battery.
- **Turn off sleep, screen savers, and automatic updates** for the day of the
  event. An operating system update that restarts the computer in the middle
  of a :term:`match <Match>` ends the stream.

Test the computer with the full setup before the event: every camera
connected, the audience display open, and the stream and recording both
running. During the test and the event, open OBS's **Stats** dock (**Docks >
Stats**). It shows how many frames are being skipped because the computer
can't keep up, and how many are being dropped because the network can't keep
up. If skipped frames climb steadily, reduce the load: lower the resolution or
frame rate, share the recording encode with the stream, or remove a camera.

Bronze Tier
-----------

One camera and one stream is a light load. At a qualifier, the scoring
computer can usually run OBS alongside FTC Live. If the test shows skipped
frames, lower the stream to 720p or borrow a second computer for streaming.

Silver Tier
-----------

Use one dedicated streaming computer for the whole event, separate from the
scoring computer, so a problem with the stream can't affect scoring. Even with
two fields or two divisions, one computer is enough as long as the event is
streamed as a single feed. Run the full-load test described above with every
camera connected before relying on it.

To show a laptop's screen or another HDMI source on the stream, use a USB HDMI
capture card. Cards that cost about $27 work well, but they get hot; keep them
somewhere with airflow rather than buried under cables.

Gold Tier
---------

Gold setups put the most load on the streaming computer: several NDI cameras,
automatic scene switching, per-match recordings, and often an NDI output for
remote displays. A small form factor mini PC with a strong hardware encoder
(about $640) can run FTC Live, OBS, and the digital audio routing for an
event, and is easier to transport and set up than a desktop tower.

If each division has its own stream, give each stream its own streaming
computer.
