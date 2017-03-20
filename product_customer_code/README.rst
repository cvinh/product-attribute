.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Product Customer Code
=====================

Provide products with customer specific codes


Installation
=============

 No external library is used.



Configuration
=============

 No configuration is required.


Usage
=====

To use this module, you need to navigate on the product variant form view and
add the customer specific codes.

Make sure your user has permissions to Manage Variants.

If you want to make a field searchable by the customer code you must pass the
partner/customer via context since the product and partner are both required in
the creation of a customer code.


e.g:
```
<field name="partner"/>
<field name="product" context="{'partner_id': partner}"/>
```


Known issues / Roadmap
======================

* None

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/product-attribute/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Vauxoo <info@vauxoo.com>
* Paul Catinean <pca@pledra.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.