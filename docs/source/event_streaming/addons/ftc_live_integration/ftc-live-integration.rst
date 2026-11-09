FTC Live Integration
====================

FTC Live is the software that runs scoring at FTC events. Its displays are web
pages, so OBS can show them on the stream, and outside tools can follow what
is happening in each :term:`match <Match>`.

Showing the Audience Display (All Tiers)
----------------------------------------

The FTC Live audience display shows the match timer, score, and rankings.
Showing it on the stream gives viewers the same information as the audience
in the room.

#. In FTC Live, open the audience display and copy its address from the
   browser's address bar.
#. In OBS, add a **Browser** source to the Field scene and paste the address.
#. Set the source's width and height to match the stream resolution, for
   example 1920 by 1080.

The streaming computer must be able to reach the FTC Live server over the
network. If OBS and FTC Live run on the same computer, this is automatic.

Automating OBS from FTC Live (Gold)
-----------------------------------

Automation tools connect to two things at once: FTC Live, to learn when each
match starts and ends, and OBS's WebSocket server, to switch scenes and start
or stop recordings. With one running, the stream switches to the field for
each match, records each match into its own file, and needs no one at the
controls during matches. See
:doc:`Live Match Splitting </event_streaming/addons/match_splitting/live/live>`.

Volunteers have built a tool for this, available at `obs.vens.co
<https://obs.vens.co>`__. Follow the setup instructions on that site.

These tools run alongside FTC Live, not inside it. FTC Live doesn't need to be
changed or configured to support them, and if an automation tool stops
working, scoring keeps working. Keep it that way: don't install anything onto
the FTC Live server to support the stream.
