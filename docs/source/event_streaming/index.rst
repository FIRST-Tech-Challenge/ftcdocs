.. meta::
   :title: Event Streaming Best Practices
   :description: Best practices for livestreaming a FIRST Tech Challenge event, organized into Bronze, Silver, and Gold tiers by cost and complexity.
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, livestream, event streaming, OBS Studio, YouTube, A/V, cameras, audio, Bronze, Silver, Gold

Event Streaming Best Practices
===============================

A livestream lets families, alumni, sponsors, and teams who couldn't travel
watch an event as it happens, and it gives teams match video to review
afterward. This article describes how to put together a reliable stream for a
*FIRST* Tech Challenge event without hiring an A/V company or assigning a
:term:`volunteer <Volunteer>` to run it full time.

Who This Is For
---------------

This article is written for an Event Director or Technical Director who is
comfortable with computers but has never produced a broadcast. It covers
everything from a single-field qualifier up to a championship, using the
same building blocks at every level. If you are streaming your first event,
start with the Bronze tier.

The goal is a stream that runs on its own during :term:`matches <Match>`. Once it is set up,
the Technical Director should only need to keep an eye on it, and step in for
:term:`alliance <Alliance>` selection and the awards ceremony.

This article covers the equipment and setup needed to get a stream on the
air. It does not cover show production, such as scripting the emcee or
planning the run of show.

In This Article
---------------

If this is your first stream, read the pages in order. Each page also links to
the previous and next pages at the bottom, so you can read straight through.

- :doc:`System Overview <system_overview/system-overview>`: how cameras,
  audio, and the streaming computer connect at each tier.
- :doc:`Hardware <hardware/index>`: the physical equipment for a stream.

  - :doc:`Cameras <hardware/cameras/cameras>`: where to place cameras, and
    which cameras to use at each tier.
  - :doc:`Audio <hardware/audio/audio>`: getting clean sound from the venue or
    your own microphones.
  - :doc:`Network <hardware/network/network>`: the local camera network and
    the internet connection for the stream.
  - :doc:`Streaming Computer <hardware/streaming_computer/streaming-computer>`:
    the computer that runs OBS Studio.
  - :doc:`Video Output <hardware/video_output/video-output>`: showing the
    stream on the venue's projector.

- :doc:`Software <software/index>`: the encoder and the streaming platform.

  - :doc:`Encoders (OBS) <software/encoders_obs/encoders-obs>`: setting up OBS
    Studio.
  - :doc:`Streaming Platform <software/streaming_platform/streaming-platform>`:
    publishing the stream on YouTube.

- :doc:`Add-ons <addons/index>`: optional tools that make the stream easier to
  run or more useful to teams.

  - :doc:`OBS Plugins <addons/obs_plugins/obs-plugins>`: plugins that add
    features to OBS Studio, such as NDI camera support.
  - :doc:`Match Splitting <addons/match_splitting/index>`: one video per
    match, made live or after the event.
  - :doc:`FTC Live Integration <addons/ftc_live_integration/ftc-live-integration>`:
    showing FTC Live displays on the stream and automating scene changes.

- :doc:`Budget and Shopping List <budget/budget>`: what equipment costs at
  each tier.
- :doc:`Day-of Checklist and Troubleshooting <day_of_checklist/day-of-checklist>`:
  packing, pre-show checks, and fixing common problems.

How the Tiers Work
------------------

Each topic in this article is split into three tiers. Each tier matches a
level of event, and each one costs more and takes more work to set up than
the one before it.

Bronze: Qualifiers
   The minimum setup that produces a watchable stream: one camera on the
   field, audio from the venue's sound system, and OBS Studio running on a
   computer the event already has. If you have to buy everything, expect to
   spend about $200 per field.

Silver: Larger and Multi-Division Events
   Adds a second camera for awards and interviews, plus your own microphone
   and USB audio interface so the stream no longer depends on the venue's
   sound system. One dedicated streaming computer handles the whole event,
   separate from scoring. Usually adds a few hundred dollars to Bronze.

Gold: Regional Championships, Premier Events, and the *FIRST* Championship
   Several pan-tilt-zoom (PTZ) cameras, a mixer with wireless microphones,
   and software that uses information from FTC Live to switch scenes and
   record each match automatically. This much equipment is usually collected
   over several seasons, and much of it often belongs to individual
   volunteers.

Use the event levels as a starting point. If a qualifier can borrow a
volunteer's PTZ cameras, it should use them. You can also mix tiers; adding a
Silver microphone to an otherwise Bronze qualifier is a common first upgrade.

Borrow Before You Buy
---------------------

Most events can borrow a good part of what they need. Before spending money,
ask:

- Does the host school have an A/V club, a media class, or a theater program
  with cameras, microphones, mixers, or cables?
- Does the venue have a projector and screen, and can a laptop connect to it?
- Does the venue's sound system have a spare output you can connect to?
- Does a nearby team, league, or volunteer already own streaming equipment?

Buy equipment you'll keep using season after season, such as IP cameras and
PoE switches. Borrow anything you would use once and then store. For a first
stream, try to keep the event's own spending under about $500.

----

| **Next:** :doc:`System Overview </event_streaming/system_overview/system-overview>`

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :hidden:

   system_overview/system-overview
   hardware/index
   software/index
   addons/index
   budget/budget
   day_of_checklist/day-of-checklist
