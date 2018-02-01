Properties Registry
===================

This page list the standard properties that can be attached to ``underworlds``
nodes. These properties have **fixed semantics** and clients who set or read
them MUST adhere to these semantics.

New properties can be added to this registry by `opening a new issue
<https://github.com/severin-lemaignan/underworlds/issues>`_ with the proposed
name, the type of node the property applies to, the datatype of the property
value, and the accurate description of its semantics.

Clients are free to use other, non-listed properties for their own use-cases.
The use of non-standard properties should however be limited in order to ensure
interoperability.

Properties Specification
------------------------

Required vs optional properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Properties can be either *required* or *optional*. ``underworlds`` clients can
always assume that a *required* property is present and set, however conformant
clients should always check whether an *optional* property is set before using
it.


Syntax and Datatypes
~~~~~~~~~~~~~~~~~~~~


- Properties names MUST be string only using characters in ``[a-zA-Z0-9_]``.
- Properties names MUST start with ``[a-zA-Z_]``.
- Properties values MUST be of one of the following types: ``bool``, ``int``,
  ``float``, ``string``, ``id`` (a unique identifier for another ``underwords``
  object) or a list of such values, as long as all the list elements have the
  same type.
- Properties MUST either:
    - be marked as ``REQUIRED``
    - be marked as ``OPTIONAL``
    - provide a default value. In this case, they are implicitely marked as ``REQUIRED``
- Properties values MUST NOT be None/null/nil as this value is reserved for
  non-set properties.

Registry
--------

Properties common for all node types (including MESH, CAMERA, ENTITY)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``parent`` [``id``, OPTIONAL]: the parent of the node. Always non-empty,
  except for the root node
- ``children`` [``list<id>``, OPTIONAL]: the children of this node, if any
- ``transformation`` [``list<float>``, REQUIRED, default: identity
  (1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1)]: the 6-D transform of the node wrt to the
  parent, row major.

Properties for MESH nodes
~~~~~~~~~~~~~~~~~~~~~~~~~

- ``mesh_ids`` [``list<string>``, REQUIRED]: handle(s) to the actual mesh data
- ``aabb`` [``list<float>``, OPTIONAL]: the axis-aligned bounding-box of the
  mesh, excluding possible children, as (x1, y1, z1, x2, y2, z2). The order of the
  points is not guaranteed.
- ``physics`` [``bool``, REQUIRED, default:true]: whether the node should
  take part to physics calculation (including collision checking)
- ``transparent`` [``bool``, REQUIRED, default:false]: whether the node should
  be considered transparent when performing visibility calculations


Properties for CAMERA nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``aspect`` [``float``, REQUIRED]: the aspect ratio of the camera
- ``horizontalfov`` [``float``, REQUIRED]: the horizontal field of view (in degrees)
- ``clipplanenear`` [``float``, OPTIONAL]: the near clipping plane of the camera (in metres)
- ``clipplanefar`` [``float``, OPTIONAL]: the far clipping plane of the camera (in metres)


Properties common for all temporal types (including EVENT, SITUATION)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- ``start`` [``float``, REQUIRED]: the start time of the temporal object, as a
  timestamp in seconds. The special value 0 means that the event/situation has
  not started yet.

Properties for SITUATION
~~~~~~~~~~~~~~~~~~~~~~~~

- ``end`` [``float``, REQUIRED]: the end time of the temporal object, as a
  timestamp in seconds. The special value 0 means that the situation has
  not ended yet.

