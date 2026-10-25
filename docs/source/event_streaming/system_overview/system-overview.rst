System Overview
===============

Every tier uses the same basic signal path. Cameras and audio sources feed a
streaming computer running OBS Studio. OBS combines them into a single program
feed and sends it to the streaming platform. The same program feed can also be
shown on a projector in the venue.

.. mermaid::
   :zoom:

    flowchart LR
        subgraph Capture
            fieldCamera[Field camera]
            awardsCamera[Awards camera]
            ptz[PTZ cameras over NDI]
            venue[Venue sound system]
            mic[Your own microphones]
        end

        subgraph Processing
            usb[USB audio adapter]
            interface[USB audio interface]
            mixer[Audio mixer]
            ftclive[FTC Live]
            automation[Automation tool]
            computer[Streaming computer<br/>running OBS Studio]
        end

        subgraph Output
            platform[YouTube]
            projector[Venue projector]
            recording[Local recording]
        end

        fieldCamera --> computer
        awardsCamera --> computer
        ptz --> computer
        venue --> usb --> computer
        mic --> interface --> computer
        mic --> mixer --> computer
        ftclive -- audience display --> computer
        ftclive -- match events --> automation
        automation -- scene changes --> computer
        computer --> platform
        computer --> projector
        computer --> recording

        classDef bronze fill:#e8c39e,stroke:#8c5a2b,stroke-width:2px,color:#000
        classDef silver fill:#e6e6e6,stroke:#5f5f5f,stroke-width:2px,stroke-dasharray:6 3,color:#000
        classDef gold fill:#ffe08a,stroke:#9a7400,stroke-width:4px,color:#000

        class fieldCamera,venue,usb,computer,ftclive,platform,projector,recording bronze
        class awardsCamera,mic,interface silver
        class ptz,mixer,automation gold

The style of each box shows the tier where that piece is first added. Every
tier uses the Bronze path, and the higher tiers add to it:

- **Bronze** (tan boxes, solid border), for qualifiers: one field camera,
  audio from the venue's sound system through a USB adapter cable, and OBS
  running on the scoring computer.
- **Silver** (grey boxes, dashed border), for larger and multi-division
  events: a second camera on the awards area, your own microphones through a
  USB audio interface, and one dedicated streaming computer for the event.
- **Gold** (yellow boxes, thick border), for regional championships, Premier
  Events, and the *FIRST* Championship: several PTZ cameras on the network
  using NDI, a mixer combining all of the audio sources, and an automation
  tool connected to FTC Live that switches scenes and records each
  :term:`match <Match>`.

Plan the Layout Before Event Day
--------------------------------

Sketch the venue and mark where the field, scoring table, audience,
projector, and awards area will be. Then measure, or estimate generously,
these distances:

- From each camera position to the streaming computer or network switch.
- From the streaming computer to the projector.
- From the venue's sound system, or your mixer, to the streaming computer.

A cable that is ten feet too short is one of the most common setup-day
problems, and it's easy to avoid with a tape measure and a site visit.
