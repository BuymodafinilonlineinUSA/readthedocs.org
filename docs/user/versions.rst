Versioned documentation
=======================

Read the Docs supports multiple versions of your repository.
On initial import,
we will create a ``latest`` version.
This will point at the default branch defined in your VCS control
(by default, ``main`` on Git and ``default`` in Mercurial).

If your project has any tags or branches with a name following `semantic versioning <https://semver.org/>`_,
we also create a ``stable`` version, tracking your most recent release.
If you want a custom ``stable`` version,
create either a tag or branch in your project with that name.

When you have :doc:`/integrations` configured for your repository,
we will automatically build each version when you push a commit.

How we envision versions working
--------------------------------

In the normal case,
the ``latest`` version will always point to the most up to date development code.
If you develop on a branch that is different than the default for your VCS,
you should set the **Default Branch** to that branch.

You should push a **tag** for each version of your project.
These tags should be numbered in a way that is consistent with semantic versioning.
This will map to your ``stable`` branch by default.

.. note::
    We in fact are parsing your tag names against the rules given by
    `PEP 440`_. This spec allows "normal" version numbers like ``1.4.2`` as
    well as pre-releases. An alpha version or a release candidate are examples
    of pre-releases and they look like this: ``2.0a1``.

    We only consider non pre-releases for the ``stable`` version of your
    documentation.

If you have documentation changes on a **long-lived branch**,
you can build those too.
This will allow you to see how the new docs will be built in this branch of the code.
Generally you won't have more than 1 active branch over a long period of time.
The main exception here would be **release branches**,
which are branches that are maintained over time for a specific release number.

.. _PEP 440: https://www.python.org/dev/peps/pep-0440/

Version states
--------------

States define the visibility of a version across the site.
You can change the states of a version from the :guilabel:`Versions` tab of your project.

Active
~~~~~~

- **Active**

  - Docs for this version are visible
  - Builds can be triggered for this version

- **Inactive**

  - Docs for this version aren't visible
  - Builds can't be triggered for this version

When you deactivate a version, its docs are removed.

Hidden
~~~~~~

- **Not hidden and Active**

  - This version is listed on the :term:`flyout menu` on the docs site
  - This version is shown in search results on the docs site

- **Hidden and Active**

  - This version isn't listed on the :term:`flyout menu` on the docs site
  - This version isn't shown in search results from another version on the docs site
    (like on search results from a superproject)

Hiding a version doesn't make it private,
any user with a link to its docs would be able to see it.
This is useful when:

- You no longer support a version, but you don't want to remove its docs.
- You have a work in progress version and don't want to publish its docs just yet.

.. note::

   Active versions that are hidden will be listed as ``Disallow: /path/to/version/``
   in the default `robots.txt file <https://www.robotstxt.org/>`__ created by Read the Docs.

Privacy levels
--------------

.. note::

   Privacy levels are only supported on :doc:`/commercial/index`.

Public
~~~~~~

It means that everything is available to be seen by everyone.

Private
~~~~~~~

Private versions are available only to people who have permissions to see them.
They will not display on any list view, and will 404 when you link them to others.
If you want to share your docs temporarily, see :doc:`/commercial/sharing`.

In addition, if you want other users to view the build page of your public versions,
you'll need to the set the :doc:`privacy level of your project </commercial/privacy-level>` to public.

Logging out
'''''''''''

When you log in to a documentation site, you will be logged in until close your browser.
To log out, click on the :guilabel:`Log out` link in your documentation's :term:`flyout menu`.
This is usually located in the bottom right or bottom left, depending on the theme design.
This will log you out from the current domain,
but not end any other session that you have active.

.. figure:: /_static/images/logout-button.png
   :align: center

Tags and branches
-----------------

Read the Docs supports two workflows for versioning: based on tags or branches.
If you have at least one tag,
tags will take preference over branches when selecting the stable version.

Version Control Support Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+------------+-----------+------------+-----------+
|            |    git     |    hg     |   bzr      |     svn   |
+============+============+===========+============+===========+
| Tags       |    Yes     |    Yes    |   Yes      |    No     |
+------------+------------+-----------+------------+-----------+
| Branches   |    Yes     |    Yes    |   Yes      |    No     |
+------------+------------+-----------+------------+-----------+
| Default    |    master  |   default |            |    trunk  |
+------------+------------+-----------+------------+-----------+

Version warning
---------------

A banner can be automatically displayed to notify viewers that there may be
a more stable version of the documentation available. Specifically:

- When the ``latest`` version is being shown, and there's also a ``stable`` version active and not hidden,
  then the banner will remind the viewer that some of the documented features may not yet be
  available, and suggest that the viewer switch to the ``stable`` version.
- When a version is being shown that is not the ``stable`` version, and there's a ``stable``
  version available, then the banner will suggest that the viewer switch to the ``stable`` version
  to see the newest documentation.


This feature is enabled by default on projects using the new beta addons.
The beta addons can be enabled by using ``build.commands`` config key or via the new beta dashboard (https://beta.readthedocs.org) going to the admin section of your docs (:guilabel:`Admin` > :guilabel:`Advanced Settings`)

.. note::

   An older version of this feature is currently only available to projects that have already enabled it.
   When the updated feature development is finished the toggle setting will be enabled for all projects.

Redirects on root URLs
----------------------

When a user hits the root URL for your documentation,
for example ``https://pip.readthedocs.io/``,
they will be redirected to the **Default version**.
This defaults to **latest**,
but could also point to your latest released version.
