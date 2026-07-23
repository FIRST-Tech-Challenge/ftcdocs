Printer Choice
==============

This section will focus on printers from each budget range that could be useful for FTC teams.
As you compare features and drawbacks across each budget range, there is one must-have feature no team should buy a printer without, along with a few other important guidelines to keep in mind:

**Product Recalls**: It is important to check if the printer you intend on buying has had any product recalls or other known safety issues.

This is important to check for safety reasons, as well as to make sure you are not buying a printer that has a known issue that could cause it to break down or pose a safety hazard.

Early model Bambu Lab A1 printers (**manufactured and sold before Jan 30, 2024**) had `a recall <https://blog.bambulab.com/a1-recall-update/>`_ due to a fire hazard from the heatbed cable.

There are also reports of `NTC thermistors melting <https://all3dp.com/4/bambu-lab-confirms-a1-components-on-older-machines-can-burn-out/>`_ on certain Bambu Lab A1 models as well, which could cause the printer plastic to melt.

Bambu Lab has fixed the issue in Q3 2025, but if you have an older model, it is important to check if your printer has the affected components and to contact Bambu Lab for a replacement if it does.

**Thermal Runaway Protection**: This is a feature where if a thermistor on the printer disagrees with the heater input
and temperature trends don't make sense, the 3D printer will shut itself down. This is essential to prevent possible
fires and teams should not buy 3D printers without this feature.

Most 3D printers you buy today will have this due to firmware updates, despite the age of the printer, but **it should still be checked (especially pre-2020 Ender 3 models)**.

Please search up whether the printer model you intend on buying has this feature. If you search up Ender 3s,
you will find some results that say it does not, but this is dated information and not true, as newer (after 2020) Ender 3s are 
now shipped with that enabled in the firmware by default. **However, on older Ender 3 models, this needs to be checked and enabled by the user, as it is not enabled by default.**

All other printers that we list in our sections below are modern enough to have this feature as well.

**Obsolete Products**: 3D printing technology moves at a fast pace, and it is important to check if the printer you intend on buying is not obsolete or discontinued by the manufacturer.
This is important to check for a few reasons.

1. Obsolete printers can be hard to find, and prices may be overinflated.
2. It may be more difficult to find replacement parts or to get support from the manufacturer if you run into issues with the printer.
3. Newer printers have extra features, better performance, and/or more easy to use software, so you may be missing out on a better experience by buying an obsolete printer.
4. It may be more difficult to find software updates or firmware updates for the printer, which could lead to compatibility issues with newer software or hardware.

However, if your team is on a tight budget, buying last generation printers that are now discontinued may be a good option, as long as you check that they have the features listed above, reasonable spare parts availability, and are aware of any potential issues that may arise from buying a discontinued printer.

**Multicolour Printing**:

This feature lets a printer use multiple filament colours in one print, either with a multi-extruder setup or a filament switching system (built-in, such as on the Centauri Carbon 2, or separate, such as the Bambu Lab AMS series).
For FTC teams, multicolour is mostly useful for team branding or decorative parts rather than functional robot components, so consider whether the added cost and complexity are worthwhile for your team's needs.

General considerations:

* Some systems (e.g. Bambu Lab AMS, Prusa MMU3, Elegoo Centauri Carbon 2) can also serve as a filament library for single-colour prints, letting you quickly switch between materials without manually swapping spools.
* Some systems can automatically switch to another spool if one runs out—useful for long prints or large batches of identical parts.
* Remote filament load/unload can be convenient for team members monitoring prints from across the room or remotely.
* On some brands, multiple units can be chained together for more colour/material options, but this adds cost and may require additional accessories.
* Multicolour systems waste significant filament during colour changes, so tune slicer settings and use multicolour only when needed.
* Some printers use purge ("poop") chutes during colour changes; if not set up properly, these can create significant waste and mess.

If you are purchasing a Bambu Lab printer, buying an AMS 2 Pro/AMS HT/AMS/AMS Lite with the printer (usually the "Combo" version) is generally better value than buying it separately.

Bambu Lab AMS notes:

* The AMS series only works with Bambu Lab printers.
* The AMS/AMS HT/AMS 2 Pro doubles as filament storage, helping keep filament dry in humid environments.
* The AMS 2 Pro can actively dry filament, but you may still need an AMS HT for higher-temperature materials (e.g. carbon fibre filaments).
* The AMS Lite is only compatible with A1 series printers and lacks active drying and enclosed storage.
* Only one AMS Lite can be used per A1 series printer, and it cannot be combined with other AMS models.
* You can mix AMS 2 Pro/AMS HT/AMS units together on compatible printers.
* Replace or reheat the desiccant periodically. Avoid blue indicating silica gel (contains toxic cobalt chloride) or calcium chloride desiccant (can leak water and damage the AMS). Use orange-to-green indicating silica gel instead.
* An AMS Hub, external power supply, or other accessories may be needed for certain setups; refer to Bambu Lab documentation for details.
* For detailed information, refer to the `Bambu Lab AMS documentation <https://wiki.bambulab.com/en/ams-series>`_.

If you are purchasing a different brand, check multiple reputable reviews to confirm the multicolour system is reliable and does not create excessive waste. Some implementations are poorly executed and can be more trouble than they are worth.

With dual/multi-nozzle systems, you may need to stock multiple nozzle types and handle additional maintenance; refer to the manufacturer's documentation for model-specific guidance.

The list of printers below is not exhaustive, but it is a good starting point for teams to compare different printers from different brands across different price ranges and to get an idea of what features are available at each price point.

.. toctree::
    :maxdepth: 1

    Budget Printers (Under $400 USD) <budget_printers/budget_printers>
    Mid-Range Printers ($300-$800 USD) <mid_range_printers/mid_range_printers>
    High-End Printers ($800+ USD) <high_end_printers/high_end_printers>
    Discontinued 3D Printers <discontinued_printers/discontinued_printers>