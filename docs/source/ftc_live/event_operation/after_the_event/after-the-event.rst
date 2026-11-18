After the Event and Server Management
=====================================

This page covers the final steps on event day, how to find the database and log
files that technical support may ask for, and how to add or remove events on the
server.

Print the Advancement Report
----------------------------

Once all matches have concluded and the Head Referee and Event Director have
verified them, go to the Event Dashboard and print the Advancement Report.

Before you finish:

- The Judge Advisor must review that the awards were entered correctly and that
  the teams are listed correctly on the Advancement Report.
- Verify the correct number of advancing teams with the Event Director.

.. note::

   The event results are published with **Send Results to FIRST**, and the
   awards then appear on the FTC Events website.

Send Results to *FIRST*
-----------------------

The final step for event day is to go to the Event Dashboard and select **Send
Results to FIRST**. This starts the sync to the official *FIRST* Tech Challenge
results page on the FTC Events website.

If the laptop doesn't have an internet connection at the event, do this within
2-3 days, when the laptop is online again.

Access the Database Files and Logs
----------------------------------

The FTC Live splash screen has links to the database (``db``) files and the
logs. Use them to review an issue, or to get the files if technical support
asks for them.

Add or Remove Events on the Server
----------------------------------

FTC Live was designed so that each event's data is downloaded just a few days
before the event. Region advancement is tracked in the cloud and updates locally
only when an individual event is downloaded. Those updates are needed to
calculate the correct advancement outcomes shown at the end of each event.
Downloading all the event data at once skips them, which can cause mismatches
and errors between the local and cloud advancement data. There may be other
reasons to add or remove events.

To make sure the advancement information for upcoming events is up to date:

#. Log in as ``local``, the FTC Live Event Admin login.
#. At the top left, next to the *FIRST* Tech Challenge logo, open the **Event
   Admin** menu.
#. Select **Manage Server** to open the options for adding and removing events.

   .. image:: images/manage-server-menu.png
      :alt: The FTC Live header with the Event Admin menu open. The Event Admin menu and its Manage Server item are marked 1 and 2.

#. On the Manage Server page, find the third group, **Event Hiding / Reload**.

   .. image:: images/event-hiding.png
      :alt: The Event Hiding / Reload group on the Manage Server page, with a select event drop-down.

#. In the selector, choose the event code of an event you have not played yet,
   then select the red **Hide** button.
#. FTC Live asks you to type the event code to confirm. Type it in to confirm.

Hiding an event:

- Removes it from the list of events on the main page. Pages for that event
  become unavailable.
- Makes it possible to download the event again with updated data when
  appropriate.

After Hiding Old Event Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Log in to the Event Portal. For the next upcoming events:

- Verify that each event is set up correctly, and that all teams are added and
  show the correct eligibility. See the "Pre-event Day Responsibilities"
  section of the Region Administrator Guide, page 7.
- Verify that Automated Advancement is configured. See the Automated
  Advancement Guide.
