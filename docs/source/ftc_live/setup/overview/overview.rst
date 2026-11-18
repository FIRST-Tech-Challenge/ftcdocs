.. meta::
   :title: FTC Live Overview
   :description: An overview of the FIRST Tech Challenge event systems, the scoring server, and what is new in FTC Live this season.
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, FTC Live, scoring system, Event Portal, scoring server, source of truth

FTC Live Overview
=================

The Three Event Systems
-----------------------

*FIRST* Event Portal
   The Event Portal (``event-portal.firstinspires.org``) is a private cloud
   interface. Program Delivery Partners and administrators use it to create
   leagues and events, manage advancement, and run season and team reports.
   Teams use it to upload portfolios, upload avatars, and (for remote
   judging only) take part in judging.

FTC Live
   FTC Live is the local software that runs at the event. It handles event
   logistics, match schedule generation, match play, alliance selection, and
   displays. It uploads event data to the cloud so the public can see it.
   This software is the focus of this guide.

FTC Events
   The public website (``ftc.events``) shows region and event information,
   match results, awards, team information and history, and league rankings.

What Is the Scoring Server?
---------------------------

The *scoring server* is the primary event laptop running FTC Live. It must be
the laptop that runs the Match Control page at the event. All other devices
connect to it, including Head Referee tablets, Official Scorer tablets,
Inspector tablets, and displays.

The Technical Director, or the Field Technical Advisor (FTA) if the event has
no Technical Director, administers the scoring server laptop. The Scorekeeper
operates it.

When FTC Live Becomes the Source of Truth
-----------------------------------------

When the event data in the Event Portal is final, an authorized user transfers
it to FTC Live. See :doc:`/ftc_live/setup/transfer_event_data/transfer-event-data`
for when and how.

.. important::

   Once the scoring server has the event data, it is the *source of truth*: the
   one place where all data is considered accurate and up to date. Later
   changes in the Event Portal, such as changing the teams at an event or a
   team's home region, are ignored. Judging results can be imported in a
   separate process.

   Make any changes needed after the transfer locally in FTC Live. The
   Scorekeeper or another authorized user makes them.

Who Uses Each System
--------------------

The Event Portal is used for event administration before event day, and by
some volunteers on event day. There are several user roles with different
levels of access. A roles and responsibilities chart is in the *FIRST* Event
Portal Region Management Guide.

The Scorekeeper keeps the scoring server and the whole FTC Live system running
at an event, and should follow this guide in order. The other FTC Live roles
depend on the size of the event and the plan for user tablets and features.
Ask the Event Director, FTA, or Technical Director which users need access to
FTC Live tablets.

What's New This Season
----------------------

Practice Matches
   Events can now run optional practice matches. FTC Live includes a schedule
   builder for them.

Awards
   The Awards Manager has a new interface. The Present Awards button on the
   Match Control page shows which awards to give at each awards break.
   Warnings help make sure the correct number of awards is given and that no
   award has duplicate winners. The event scripts are also editable.
