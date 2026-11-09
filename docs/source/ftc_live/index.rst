.. meta::
   :title: FTC Live Setup Guide
   :description: How to set up and run FTC Live, the local scoring and event management software for FIRST Tech Challenge events.
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, FTC Live, scoring system, scorekeeper, Event Portal, scoring server, match control

FTC Live Setup Guide
====================

*FIRST*\ ® Tech Challenge event management is split across three systems: the
cloud-based *FIRST* Event Portal, the local software that runs on event day
(FTC Live), and a public website. This guide covers the system requirements
and a step-by-step process for using FTC Live at an event. Most optional
features are covered in their own pages.

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
it to FTC Live. See :doc:`/ftc_live/transfer_event_data/transfer-event-data`
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

In This Guide
-------------

Work through the pages in this order:

#. :doc:`Hardware and Network Requirements </ftc_live/hardware_and_network/hardware-and-network>`:
   what to bring and how to lay out the system.
#. :doc:`Install FTC Live and Log In </ftc_live/install_and_login/install-and-login>`:
   download, install, and sign in.
#. :doc:`Transfer Event Data </ftc_live/transfer_event_data/transfer-event-data>`:
   move the event from the Event Portal to FTC Live.
#. :doc:`Event Preparation </ftc_live/event_preparation/event-preparation>`:
   check schedules and teams, print documents, and set up users, sponsors,
   and inspection.
#. :doc:`Match Control </ftc_live/match_control/match-control>`: run test,
   practice, and qualification matches.
#. :doc:`Alliance Selection and Playoffs </ftc_live/alliance_selection_and_playoffs/alliance-selection-and-playoffs>`:
   run alliance selection and the playoff matches.
#. :doc:`Awards </ftc_live/awards/awards>`: enter and present awards.
#. :doc:`After the Event </ftc_live/after_the_event/after-the-event>`: print
   the advancement report, send results, and manage the server.

Optional and special-case topics:

- :doc:`Audience Displays </ftc_live/audience_displays/audience-displays>`
- :doc:`Inspection Tools </ftc_live/inspection_tools/inspection-tools>`
- :doc:`Dual Division Events </ftc_live/dual_division/dual-division>`
- :doc:`Paper Scoring </ftc_live/paper_scoring/paper-scoring>`

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :hidden:

   hardware_and_network/hardware-and-network
   install_and_login/install-and-login
   transfer_event_data/transfer-event-data
   event_preparation/event-preparation
   match_control/match-control
   alliance_selection_and_playoffs/alliance-selection-and-playoffs
   awards/awards
   after_the_event/after-the-event
   audience_displays/audience-displays
   inspection_tools/inspection-tools
   dual_division/dual-division
   paper_scoring/paper-scoring
