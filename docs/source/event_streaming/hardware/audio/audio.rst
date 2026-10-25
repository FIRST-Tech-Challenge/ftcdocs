Audio
=====

Viewers will put up with a soft picture far longer than they will put up with
bad sound. If the stream's audio is distorted, echoing, or buried in crowd
noise, consider streaming with no audio at all until you can fix it.

Audio is also where Bronze and Silver differ the most. A Bronze stream relies
on the venue's sound system, so its quality depends on the venue. A Silver
stream brings its own microphone and interface, so it sounds the same
everywhere.

What the Stream Needs to Hear
-----------------------------

- **Game sounds.** These tell viewers when a :term:`match <Match>` starts, when the
  :term:`TELEOP` period begins, and when the match ends.
- **The emcee.** The emcee introduces teams and explains what is happening.
- **Music,** if the event plays any. Read `Music and Copyright`_ before
  putting music on the stream.

Bronze Tier
-----------

Take a feed from the venue's sound system. Most gym and auditorium mixers
have a spare output, often labeled AUX, REC, or MON, and many powered speakers
have an XLR "thru" output. Connect that output to the streaming computer with
an audio-to-USB adapter cable (about $20). OBS treats the adapter as a
microphone input.

Test the feed before the event, with someone talking into the emcee
microphone while game sounds play:

- If the level in OBS is too low, raise the gain on that source in OBS.
- If the sound is distorted, ask the venue to turn its output down. Distortion
  that happens before the signal reaches the computer can't be removed
  afterward.

This feed carries everything the venue plays, including music. Only use it if
the event's music is cleared for streaming, or if the event plays no music.

Silver Tier
-----------

Bring your own microphone and audio interface so the stream no longer depends
on the venue.

- **Wireless microphones.** Several regions use the Phenyx Pro PTU-71-2H, a
  two-microphone kit that costs about $135.
- **A small USB audio interface,** such as a Focusrite Scarlett Solo or a MOTU
  M2. Connect the microphone receiver to one input and the game sound output
  of the computer playing them to the other. The interface connects to the
  streaming computer over USB, and you mix the inputs in OBS.
- **A powered speaker,** if the venue has no usable sound system. A compact
  speaker with a small built-in mixer, such as the Mackie SRM150 (about $300),
  fills most gyms and can take the microphone and game sounds directly.

In OBS, add a Limiter filter to each audio source so a shouting emcee or a
loud buzzer doesn't clip the stream, and use headphones on the streaming
computer to listen to what viewers actually hear.

Gold Tier
---------

Use a dedicated mixer to combine several wireless microphones, game sounds,
and music. An 8-channel analog mixer (about $220) covers most events. Larger
events use a digital mixer such as the Behringer X Air XR18 (about $500),
sometimes with a physical control surface.

- Send the mixer's main output into the venue's sound system through a
  spare XLR or AUX input. The room and the stream then hear the same mix, and
  you don't have to bring large speakers.
- Send a separate output from the mixer to the streaming computer, so you can
  set the stream's level without changing what the room hears.
- Give the emcee in-ear monitors so they can hear themselves over the crowd.
- For venues where audio has to reach several places, such as a pit area on
  the other side of the building, an audio-over-network system such as Dante
  sends audio anywhere on the network without running more cable. Dante
  adapters cost about $160 to $200 each.

Music and Copyright
-------------------

YouTube automatically detects copyrighted music in livestreams and mutes or
blocks the affected part of the stream. Plan for this before the event:

- Play music from a library that is licensed for streaming, such as
  `Epidemic Sound <https://www.epidemicsound.com/>`__.
- Or keep music in the room and off the stream. This only works if the
  stream's audio comes from your own microphones rather than the venue's
  sound system, which is one reason to move to Silver.
