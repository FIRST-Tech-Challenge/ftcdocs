Day-of Checklist and Troubleshooting
====================================

Most stream problems can be found and fixed before the doors open. This page
covers packing the equipment, checking the stream before it goes live,
watching it during the event, and fixing the most common problems.

Packing an Event Kit
--------------------

Regions that run many streams keep each field's equipment in its own rolling
tote, with a printed packing list taped inside the lid. One tote holds the
camera, stand, network switch, cables, microphones, and adapters for one
field; a two-field event takes two totes. This makes it easy to hand a kit to
a different volunteer and know nothing is missing.

- Label both ends of every cable with what it connects to.
- Pack spare network cables, a spare audio-to-USB adapter, a power strip, and
  gaffer tape.
- Coil cables using the over-under method. Alternate one normal loop with
  one loop twisted the opposite way. The cable then lies flat, uncoils
  without tangling, and doesn't develop kinks. Never wrap a cable around
  your elbow.

Before the Event
----------------

- Install OBS, plugin, and operating system updates at least a few days
  before the event, then run a test stream. Don't update on event day.
- Confirm the scheduled stream exists in YouTube Studio and the stream key in
  OBS matches it.
- Confirm with the venue that the streaming computer can reach YouTube. See
  :doc:`Network </event_streaming/hardware/network/network>`.

Before Going Live
-----------------

- Start a short test stream set to *Unlisted* and watch it on a phone, with
  headphones. Check that video, game sounds, and the emcee microphone all
  come through.
- Check audio levels with the emcee talking and game sounds playing at the
  same time. Levels that look fine when the room is quiet can clip once the
  emcee starts.
- Check each camera's framing with the audience seated and field staff in
  position.
- Open the OBS **Stats** dock and confirm it shows no skipped or dropped
  frames.
- Start the local recording in OBS.

During the Event
----------------

- Watch the venue projector, if it shows the program output. It is the
  fastest way to spot a bumped camera.
- Glance at the OBS Stats dock between matches.
- Switch to the Awards scene for alliance selection and the awards ceremony,
  and back to the Field scene afterward (Silver).
- If the event will run past 12 hours, end the stream and start a new one at
  a break. See
  :doc:`Streaming Platform </event_streaming/software/streaming_platform/streaming-platform>`.

After the Event
---------------

- Stop the stream, then stop the recording.
- Remux the recording to MP4 (**File > Remux Recordings**) and copy it off the
  streaming computer before packing up.
- Split the matches and publish them. See
  :doc:`Match Splitting </event_streaming/addons/match_splitting/index>`.
- Restock the tote and note anything that broke or ran out.

Common Problems
---------------

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Problem
     - Likely Cause
     - What to Try
   * - No audio on the stream
     - OBS is listening to the wrong device, or a USB adapter was unplugged
       and reconnected
     - In OBS, open the audio source's properties and select the correct
       device again.
   * - Audio is distorted
     - The level is too high before it reaches the computer
     - Turn down the venue mixer's output or the audio interface's gain, not
       just the level in OBS.
   * - Stream is choppy or keeps buffering
     - Upload bandwidth is too low or is shared with other devices
     - Lower the bitrate in OBS. If the Stats dock shows dropped frames,
       move the streaming computer to a wired connection.
   * - Stream stutters and the Stats dock shows skipped frames
     - The computer can't keep up with encoding
     - Switch to a hardware encoder, lower the resolution to 720p, or close
       other programs.
   * - An IP or NDI camera shows black
     - The camera lost power or network
     - Check the PoE switch's port lights and reseat the camera's network
       cable before assuming the camera has failed.
   * - Projector shows nothing from a fiber HDMI cable
     - The cable is connected backward, or the fiber is damaged
     - Check that the *Source* end is at the computer. Then try a short HDMI
       cable to rule out the projector.
