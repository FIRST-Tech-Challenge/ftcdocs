.. meta::
   :title: FIRST Tech Challenge Documentation
   :description: The official home of FIRST Tech Challenge Documentation.
   :keywords: FTC Control System, Control Hub, TensorFlow, PowerPlay, Blocks, OnBot Java, Android Studio, OpenCV, EasyOpenCV, AprilTags, FTC SDK, Robot Controller App, Driver Station App, Control Hub, Driver Hub, ftc-ml, IMU, Water Game

*FIRST* Tech Challenge documentation
====================================

*FIRST* Tech Challenge is a robotics program for middle and high school
students. It’s way more than building robots, see 
:doc:`About the 𝘍𝘐𝘙𝘚𝘛 Tech Challenge <overview/ftcoverview>`
to see why.

.. note::

   This project is under active development. Anything contained herein is for 
   informational purposes only; while this documentation is intended to support 
   teams and in some way provide context to game rules, the game rules supercede 
   all documentation found here. If you have feedback about this project, 
   please use our :doc:`feedback form <ftc_docs/form/form>`.

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

   manuals/game_manuals/game_manuals
   Game Q&A Forum <game_specific_resources/ftcqa/ftcqa>
   game_specific_resources/playing_field_resources/playing_field_resources
   Field Coordinate System <game_specific_resources/field_coordinate_system/field-coordinate-system>

.. toctree::
   :caption: Software Development Kit (SDK)
   :maxdepth: 1
   :hidden:

   SDK Overview <ftc_sdk/overview/index>
   Updating Components <ftc_sdk/updating/index>

.. toctree::
   :caption: Control System Resources
   :maxdepth: 1
   :hidden:

   programming_resources/shared/control_system_intro/The-FTC-Control-System 
   control_hard_compon/index
   hardware_and_software_configuration/index
   programming_resources/index

.. toctree::
   :caption: AprilTag Resources
   :maxdepth: 1
   :hidden:

   AprilTag Introduction </apriltag/vision_portal/apriltag_intro/apriltag-intro>
   VisionPortal Overview </apriltag/vision_portal/visionportal_overview/visionportal-overview>
   Understanding AprilTag Values </apriltag/understanding_apriltag_detection_values/understanding-apriltag-detection-values>
   AprilTag Test Images </apriltag/opmode_test_images/opmode-test-images>

.. toctree::
   :caption: CAD Resources
   :maxdepth: 1
   :hidden:

   Computer Aided Design (CAD) <cad_resources/index>

.. toctree::
   :caption: Additional Tools
   :maxdepth: 1
   :hidden:    
   
   ftc_ml/index
   
.. toctree::
   :caption: Team Resources
   :maxdepth: 1
   :hidden:    
   
   faq/faqs

.. toctree::
   :caption: Team Freebies and Discounts
   :maxdepth: 1
   :hidden:

   Team Complimentary Software<sponsors/software/software>
   Team Discounts<sponsors/discounts/discounts>

.. toctree::
   :caption: FTC Docs
   :maxdepth: 1
   :hidden:

   Site Feedback Form<ftc_docs/form/form>
   FTC Docs PDF<ftc_docs/pdf/pdf>
   Dark Mode<ftc_docs/dark/dark>

.. Add Contrib Section here when added

.. rst-class:: center
   
**I AM A...**

.. grid:: 1 2 2 4
   :gutter: 2 

   .. grid-item-card:: Rookie Resources
      :link: persona_pages/rookie_teams/rookie_teams
      :link-type: doc
      :class-header: sd-bg-primary font-weight-bold sd-text-white 
      :class-body: sd-text-left body

      Rookie Team 
   
      ^^^

      Rookie Teams may not know where to start. This is the way!

   .. grid-item-card:: Veteran Resources
      :link: persona_pages/veteran_teams/veteran_teams
      :link-type: doc
      :class-header: sd-bg-primary font-weight-bold sd-text-white 
      :class-body: sd-text-left

      Veteran Team 
   
      ^^^

      Veteran Teams looking for veteran resources can look here.
   
   .. grid-item-card:: Coach Resources
      :link: persona_pages/coach_admin/coach_admin
      :link-type: doc
      :class-header: sd-bg-primary font-weight-bold sd-text-white 
      :class-body: sd-text-left

      Coach (Admin)
   
      ^^^

      Coaches looking for Team Administrative Resources can 
      look here for help.

   .. grid-item-card:: Mentor Resources
      :link: persona_pages/mentor_tech/mentor_tech
      :link-type: doc
      :class-header: sd-bg-primary font-weight-bold sd-text-white 
      :class-body: sd-text-left

      Mentor (Technical)
   
      ^^^

      Technical Mentors looking for Technical Resources 
      should look here first!

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-white
      :class-body: sd-text-left 

      Programming Quick Links
   
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
      :class-header: sd-bg-secondary font-weight-bold sd-text-white
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
      :class-header: sd-bg-secondary font-weight-bold sd-text-white
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

               SDK GitHub Repository

         .. div:: col-sm pl-1 pr-1
      
            .. button-link:: https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases               
               :color: black
               :outline:
               :expand:

               SDK Releases

         .. div:: col-sm pl-1 pr-1

            .. button-link:: https://javadoc.io/doc/org.firstinspires.ftc
               :color: black
               :outline:
               :expand:

               Javadoc Documentation

   .. grid-item-card:: 
      :class-header: sd-bg-secondary font-weight-bold sd-text-white
      :class-body: sd-text-left 

      Game Manual Links
   
      ^^^

      Be sure you're following all of the rules of the competition! 
      Game Manuals and Q&A are essential documents.

      +++
 
      .. div:: container-fluid p-0

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: manuals/game_manuals/game_manuals
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Game Manuals

         .. div:: col-sm pl-1 pr-1
      
            .. button-ref:: game_specific_resources/playing_field_resources/playing_field_resources
               :ref-type: doc
               :color: black
               :outline:
               :expand:

               Field Manuals

         .. div:: col-sm pl-1 pr-1

            .. button-link:: https://ftc-qa.firstinspires.org/
               :color: black
               :outline:
               :expand:

               Game Q&A System

