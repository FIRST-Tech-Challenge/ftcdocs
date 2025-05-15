.. meta::
   :title: FIRST Tech Challenge Documentation
   :description: The official home of FIRST Tech Challenge Documentation.
   :keywords: FTC Control System, Blocks, OnBot Java, Android Studio, OpenCV, EasyOpenCV, AprilTags, FTC SDK, Robot Controller App, Driver Station App, Control Hub, Driver Hub, IMU, Water Game

*FIRST* Tech Challenge documentation
====================================

Welcome to the *FIRST®* Tech Challenge Documentation! This website contains everything you need to know to create a competition robot!
There is information and tutorials on how to use the *FIRST* Tech Challenge software and robot control system.
There is also information for coaches and mentors.

*FIRST* Tech Challenge is a robotics program for middle and high school students.
It’s way more than building robots, see :doc:`About the FIRST Tech Challenge <overview/ftcoverview>`
and :doc:`gracious_professionalism/gp` to see why.

.. toctree::
   :hidden:
   :maxdepth: 1

   /overview/ftcoverview
   gracious_professionalism/gp

.. toctree::
   :caption: Getting Started
   :maxdepth: 1
   :hidden:

   persona_pages/rookie_teams/rookie_teams
   persona_pages/veteran_teams/veteran_teams
   persona_pages/coach_admin/coach_admin
   persona_pages/mentor_tech/mentor_tech
   
.. toctree::
   :caption: Game and Season-Specific Resources
   :maxdepth: 1
   :hidden:

   game_specific_resources/blog/blog
   tech_tips/tech-tips
   ai/innovation_corner/innovation-corner
   Competition Manual <manuals/competition_manual/competition_manual>
   Game Q&A System <game_specific_resources/ftcqa/ftcqa>
   game_specific_resources/playing_field_resources/playing_field_resources
   Field Coordinate System <game_specific_resources/field_coordinate_system/field-coordinate-system>

.. toctree::
   :caption: Software Development Kit (SDK)
   :maxdepth: 1
   :hidden:

   Laptop Requirements <programming_resources/laptops/laptops>
   SDK Overview <ftc_sdk/overview/index>
   Updating Components <ftc_sdk/updating/index>

.. toctree::
   :caption: Robot Building Resources
   :maxdepth: 1
   :hidden:


.. toctree::
   :caption: Control System Resources
   :maxdepth: 1
   :hidden:

   programming_resources/shared/control_system_intro/The-FTC-Control-System 
   control_hard_compon/index
   hardware_and_software_configuration/index
   hardware_and_software_configuration/self_inspect/self-inspect
   programming_resources/index

.. toctree::
   :caption: AprilTag Resources
   :maxdepth: 1
   :hidden:

   AprilTag Introduction </apriltag/vision_portal/apriltag_intro/apriltag-intro>
   VisionPortal Overview </apriltag/vision_portal/visionportal_overview/visionportal-overview>
   Webcams for VisionPortal </apriltag/vision_portal/visionportal_webcams/visionportal-webcams>
   Understanding AprilTag Values </apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values>
   AprilTag Localization </apriltag/vision_portal/apriltag_localization/apriltag-localization>
   AprilTag Test Images </apriltag/opmode_test_images/opmode-test-images>

.. toctree::
   :caption: CAD Resources
   :maxdepth: 1
   :hidden:

   Computer Aided Design (CAD) <cad_resources/index>

.. toctree:: 
   :caption: Electrostatic Discharge
   :maxdepth: 1
   :hidden:

   Managing ESD Effects <hardware_and_software_configuration/configuring/managing_esd/managing-esd>

.. toctree::
   :caption: Manufacturing
   :maxdepth: 1
   :hidden:

   Manufacturing Methods <manufacturing/index>
   
.. toctree::
   :caption: Team Resources
   :maxdepth: 1
   :hidden:    
   
   faq/faqs
   Team Complimentary Software<sponsors/software/software>
   Team Discounts<sponsors/discounts/discounts>

.. toctree::
   :caption: FTC Docs
   :maxdepth: 1
   :hidden:

   Booklets<booklets/index>
   Archive <https://ftc-docs.firstinspires.org/projects/ftcdocs-archive/en/latest/index.html>
   Site Feedback Form<ftc_docs/form/form>
   Contributing to FTC Docs<contrib/index>

.. Add Contrib Section here when added

**I am a...**

- :doc:`New Team <persona_pages/rookie_teams/rookie_teams>` - New Teams may not know where to start. This is the way!

- :doc:`Returning Team <persona_pages/veteran_teams/veteran_teams>` - Returning Teams looking for resources can look here.

- :doc:`Coach <persona_pages/coach_admin/coach_admin>` - Coaches looking for help or Team Administrative Resources can look here.

- :doc:`Mentor <persona_pages/mentor_tech/mentor_tech>` - Technical Mentors looking for Technical Resources should look here first!

The main menu contains links to the top level content. The following are quick links organized by topic.

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-black
      :class-body: sd-text-left 

      Programming Links
   
      ^^^

      Quick Links for Programming Language Resources 

      +++

      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1

            .. button-ref:: programming_resources/blocks/Blocks-Tutorial
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Blocks
      
         .. div:: col-sm pl-1 pr-1

            .. button-ref:: programming_resources/onbot_java/OnBot-Java-Tutorial
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               OnBot Java
         
         .. div:: col-sm pl-1 pr-1
 
            .. button-ref:: programming_resources/android_studio_java/Android-Studio-Tutorial
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Android Studio

         .. div:: col-sm pl-1 pr-1

            .. button-ref:: ../../apriltag/vision_portal/apriltag_intro/apriltag-intro
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               AprilTags

         .. div:: col-sm pl-1 pr-1
 
            .. button-ref:: programming_resources/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               All Resources

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-black
      :class-body: sd-text-left 

      Control System Links
   
      ^^^

      Let's get to know the *FIRST* Tech Challenge Control System! 

      +++

      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: control_hard_compon/ds_components/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Driver Station

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: control_hard_compon/rc_components/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Robot Controller

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: hardware_and_software_configuration/connecting_devices/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Device Connections

         .. div:: col-sm pl-1 pr-1

            .. button-ref:: hardware_and_software_configuration/configuring/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Hardware Configuration

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-black
      :class-body: sd-text-left 

      Software Development Kit (SDK)
   
      ^^^

      The Software Development Kit (SDK) is the collection of tools for
      developing software and executing it on the robot. 

      +++
 
      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1

            .. button-ref:: ftc_sdk/overview/index
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               About the SDK

         .. div:: col-sm pl-1 pr-1
      
            .. button-link:: https://github.com/FIRST-Tech-Challenge/FtcRobotController/              
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               SDK GitHub Repository (external)

         .. div:: col-sm pl-1 pr-1
      
            .. button-link:: https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases               
               :color: black
               :outline:
               :expand:

               SDK Releases (external)

         .. div:: col-sm pl-1 pr-1

            .. button-link:: https://javadoc.io/doc/org.firstinspires.ftc
               :color: black
               :outline:
               :expand:

               Javadoc Documentation (external)

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-black
      :class-body: sd-text-left 

      Game Links
   
      ^^^

      Be sure you're following all of the rules of the competition! 
      The Competition Manual is an essential document.

      +++
 
      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: manuals/competition_manual/competition_manual
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Competition Manual

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: game_specific_resources/playing_field_resources/playing_field_resources
               :ref-type: doc
               :color: black
               :outline:
               :expand:

         .. div:: col-sm pl-1 pr-1

            .. button-link:: https://ftc-qa.firstinspires.org/
               :color: black
               :outline:
               :expand:

               Game Question and Answer System (external)

.. note::

   This project is under active development. Anything contained herein is for 
   informational purposes only; while this documentation is intended to support 
   teams and in some way provide context to game rules, the game rules supercede 
   all documentation found here. If you have feedback about this project, 
   please use our :doc:`feedback form <ftc_docs/form/form>`.

