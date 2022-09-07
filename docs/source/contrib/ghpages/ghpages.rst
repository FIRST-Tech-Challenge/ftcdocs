Deploying to Github Pages
===========================

At the moment, the official *First* Tech Challenge Documentation deploys to Github Pages. 
This is done using a custom Github Action that builds the site in a specific way. The best 
way to ensure that your content will be rendered correctly is to use the same build process. 
Since it is hard to do this locally the best way to do this is to deploy this to Github Pages 
yourself.

Preparation
------------

- Github Account
- Fork of this repository

Deployment
------------

Deploying to Github Pages is as simple as enablng workflows in your forked repository as outlined in the 
`Github Docs <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#managing-github-actions-permissions-for-your-repository>`_.
This will then generate a site at ``https://<USERNAME>.github.io/<FORK-NAME>``. Replace ``<USERNAME>`` 
with your Github username and ``<FORK-NAME>`` with the name of your forked repository. This will generate a 
site based on the ``main`` branch of your forked repository. Every time you push to the ``main`` branch 
this site will automatically update. Keep in mind that these updates are not instant take around 5 minutes though 
it can very easily take longer.

Deploy from different branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deploying from a different branch can be done quite simply. Do this by going to ``https://github.com/<USERNAME>/<FORK-NAME>/actions/workflows/publish.yaml``.
Replace ``<USERNAME>`` with your Github username and ``<FORK-NAME>`` with the name of your forked repository. Then click ``Run Workflow``. From this drop 
down change ``Branch: main`` to the branch you want to deploy from. Then click ``Run Workflow`` again. This will generate a site based on the branch you selected. 
While it is also possible to edit the workflow file to deploy from a different branch this is not recommended as it will make it harder to update your forked branch and 
to merge PRs to upstream.
