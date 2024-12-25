Switching Branches
==================
:bdg-success:`Repeat` :bdg-warning:`Local`

.. warning::
   Only complete these steps if you have chosen to develop the site locally. 
   If you are using **GitHub Codespaces** you should skip this section.

This step is necessary to change which branch you are working on. If you are working on a branch and want to switch to another branch, you can use the following command:

.. code-block:: bash

    git checkout <branch_name>

Make sure to replace ``<branch_name>`` with the name of the branch you want to switch to and that it matches the name of the branch you want to switch to that you created in the previous step.

Troubleshooting
---------------

Branch Not Found
~~~~~~~~~~~~~~~~

``error: pathspec '<branch-name>' did not match any file(s) known to git``

This error occurs when the branch you are trying to switch to does not exist. Make sure you have created the branch you are trying to switch that there are no typos. However, 
it can also occur when your local repo is not up to date with the remote repo. To fix this, you can run the following command:

.. code-block:: bash

    git fetch

This command will update your local repo with the remote repo. After running this command, try switching branches again.

Uncommitted Changes
~~~~~~~~~~~~~~~~~~~~

``error: Your local changes to the following files would be overwritten by checkout:``

This error occurs when you have uncommitted changes in your working directory. You can either commit your changes, stash them, or delete them. To commit your changes, you can use the following command:

.. code-block:: bash

    git commit -m "Your commit message"

This command will commit your changes with the message you provide.

To stash your changes, you can use the following command:

.. code-block:: bash

    git stash

Stashing allows you to save your changes for later without committing them. After stashing your changes, you can switch branches. To apply your stashed changes, you can use the following command:

.. code-block:: bash

    git stash apply

It is best to use ``git stash`` when you are not ready to commit your changes but need to switch branches.

To delete your changes, you can use the following command:

.. warning:: This command will delete all uncommitted changes in your working directory. It is not recommended to use this command unless you are sure you want to delete your changes.
.. code-block:: bash

    git reset --hard
