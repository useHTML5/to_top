to_top
------

Add link to up page top top.

Install
-------
requirements.in:

git+https://github.com/useHTML5/to_top.git@0.1#egg=to_top


INSTALLED_APPS = {
  'to_top',
}

Needs jquery sekizai css and js blocks in code.

@import "design/import";

usage
_____


In base.html:

{% include 'to_top.html' %}

