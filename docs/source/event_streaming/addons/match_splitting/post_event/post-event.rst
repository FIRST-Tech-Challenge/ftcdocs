Post-event
==========

Post-event match splitting uses the recording OBS made during the event. It
works at every tier, and needs no automation, only the recording and the
:term:`match <Match>` schedule. Aim to publish the matches within a day or two, while teams
are still using them to prepare for their next event.

Option 1: Chapters on the Full Video
------------------------------------

The quickest option is to leave the stream as one long video on YouTube and
add chapters. YouTube creates chapters from timestamps in the video
description. The list must start at ``0:00`` and have at least three
timestamps, each at least 10 seconds apart:

.. code-block:: text

   0:00 Opening ceremonies
   32:15 Qualification 1
   38:40 Qualification 2
   45:05 Qualification 3

Viewers can then jump straight to any match from the video's progress bar.

Option 2: Separate Videos for Each Match
----------------------------------------

Separate videos are easier to find and share, and can be added to a playlist
for the event.

#. Open the day's recording in a video editor that can cut without
   re-encoding. `LosslessCut <https://github.com/mifi/lossless-cut>`__ is free,
   runs on Windows, macOS, and Linux, and is built for exactly this job.
#. Use the match schedule to find each match. The field camera and the score
   overlay make match starts and ends easy to spot.
#. Export each match as its own file, named consistently, for example
   ``Qualification 12.mp4``.
#. Upload the files to YouTube and add them to a playlist for the event.

If you're comfortable with the command line, ``ffmpeg`` can do the same thing.
This command copies the section from 1:02:30 to 1:05:15 into a new file
without re-encoding:

.. code-block:: text

   ffmpeg -ss 01:02:30 -to 01:05:15 -i day1.mkv -c copy "Qualification 12.mp4"

Cutting without re-encoding is fast, but the cut can only land on a keyframe,
so each clip may start a second or two earlier than the exact time you asked
for. Start each cut a few seconds before the match begins.
