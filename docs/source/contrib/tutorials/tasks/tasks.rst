Intro to VS Code Tasks
=======================
:bdg-secondary:`Information` 

In order to simplify the process of building and running FTC Docs we have created a set of tasks for Visual Studio Code. 
These tasks are defined in the `.vscode/tasks.json` file and can be run via the `Terminal` -> `Run Task...` menu. 

Tasks
-----

``make-setup``
~~~~~~~~~~~~~~
This task will install the necessary dependencies for building FTC Docs. This task should only need to be run once.

``make-html``
~~~~~~~~~~~~~
This task will build the HTML version of the FTC Docs. The output will be placed in the `html` directory. This 
will not automatically create a local server to view the output. In most cases we would instead recommend using 
the `make-autobuild` task.

``make-latexpdf``
~~~~~~~~~~~~~~~~~
This task will build the PDF version of the FTC Docs. The output will be placed in the `latex` directory. In the 
backend it generates the LaTeX files and then runs `pdflatex` to generate the PDF. This build functionality is 
not supported in this tutorial though Codespace users can use this task. The PDF output is stored as ``docs/build/latex/ftcdocs.pdf``. Note that 
this task takes a long time to run and is not recommended for frequent use.

``make-autobuild``
~~~~~~~~~~~~~~~~~~~
This task will build the HTML version of the FTC Docs and then start a local server to view the output. It will also
automatically rebuild the HTML version of the FTC Docs whenever a file is changed. This is the recommended way to 
view the FTC Docs while working on them. It is also hotkeyed to `Ctrl+Shift+B` for easy access. You can stop this 
task by pressing `Ctrl+C` in the terminal.

``make-clean``
~~~~~~~~~~~~~~~
This task will remove all of the build artifacts. This is useful if you want to start from a clean slate. 
This is sometimes necessary if you are not seeing your changes reflected in the output as will sometimes happen 
with images and other static files.


