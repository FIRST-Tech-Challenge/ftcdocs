Live
====

Live match splitting produces a separate recording for each :term:`match <Match>` while the
event is running, so match videos can be uploaded the same day. It is a
Gold-tier add-on.

How It Works
------------

An automation tool watches FTC Live for match events, such as a match being
started, ending, or having its score posted. When a match starts, the tool
tells OBS to switch to the field scene and start recording. When the match
ends and the score is shown, it stops the recording. Each match ends up in its
own file.

At least one tool built by FTC :term:`volunteers <Volunteer>` already does
this. See
:doc:`FTC Live Integration </event_streaming/addons/ftc_live_integration/ftc-live-integration>`
for how these tools connect to FTC Live and OBS.

What You Need
-------------

- OBS Studio with the WebSocket server turned on (**Tools > WebSocket Server
  Settings**).
- A network connection between the computer running the automation tool,
  the FTC Live server, and the streaming computer. If all three run on the
  same computer, this is automatic.
- Enough free disk space on the streaming computer for a full day of match
  recordings.

Before the Event
----------------

Run a few practice matches in FTC Live with the automation tool connected.
Check that a recording starts and stops for each one, and that the files are
named so you can tell which match is which. Problems with the automation are
much easier to fix before the first qualification match than during it.

Keep OBS recording the whole day as well, separately from the per-match
recordings. If the automation misses a match, you can still cut it from the
full recording using the
:doc:`post-event method <../post_event/post-event>`.
