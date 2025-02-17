Creating a Codespace
=====================
:bdg-success:`Repeat` :bdg-info:`Codespaces`

For every new branch you make in your repository, you must create a new codespace. 
This is a virtual environment that will allow you to run your code and test it before merging it into the main branch. 
It may take a few minutes to create the codespace, but once it is created, you can access it from the browser and subsequent access will be much faster.

Steps
-----

1. Open your **forked** repository in GitHub.
2. On the left side of the page select the branch you want to work on.

   .. image:: images/select-branch.png
      :alt: Screen shot showing the Demo branch is selected.

3. Click on the green Code button which will display a Local and a Codespaces tab, then click the Codespaces tab.

   .. image:: images/select-cs.png
      :alt: Screen shot showing the Codespace tab being clicked.

4. Click on the green button that says "Create codespace on".

   .. image:: images/create-cs.png
      :alt: Screen shot showing the green button that says create codespace on.

5. Wait for the codespace to be created. This may take a few minutes.
6. Once the codespace is created, you will be taken to the codespace in your browser.
   This is a browser based version of VS Code that can be used to make your changes and build the HTML pages to review your changes.
7. Enter ``CTRL + SHIFT + B`` to build the project. You can also run the build task from the Terminal menu.

   .. image:: images/run-build-task.png
      :alt: Screen shot of Terminal menu with Run Build Task selected.
      
8. The build messages will be displayed. Look to see a "build succeeded" message.
   Then a pop up will indicate an application is running. 
   
   .. image:: images/build-messages.png
      :alt: Screen shot of build messages with Open in Browser button.

9. If you click the Open in Browser button a new tab will open displaying the HTML pages you just built.

10. You can now make your changes. See the section on :doc:`/contrib/tutorials/make_rst/index`.
