Cameras
=======

Camera placement matters more than camera price. A $60 camera mounted high
with a clear view of the whole field makes a better stream than an expensive
one at eye level behind a row of standing spectators.

Placement
---------

- Mount cameras on a stand that puts them well above head height. Light
  stands in the 7 to 13 foot range work well and cost about $40 to $65.
- Frame the whole :term:`playing field <Playing Field>`, including both
  :term:`alliance <Alliance>` stations, so viewers can tell which robots
  belong to which alliance.
- Keep the camera out of the paths that field staff, queuers, and teams walk
  during matches. Check the shot again once the audience is seated.
- Weigh down the stand's legs with sandbags, and tape down the cable so
  nobody trips on it or knocks the stand over.

Bronze Tier
-----------

Use one camera with a wide, fixed shot of the field.

A network (IP) camera is the recommended choice. Several regions use the
Amcrest IP2M-841B, a 1080p camera that costs about $60 when paired with a
low-cost PoE splitter. PoE (Power over Ethernet) carries both power and video
over one network cable, so the camera needs a single cable back to the
streaming computer or network switch. A network cable can run up to 100
meters (328 feet), which is far longer than any USB cable.

A USB webcam also works if the field is close to the streaming computer.
Passive USB 2.0 cables are limited to about 5 meters (16 feet), so longer runs
need an active USB extension cable. A smartphone running a webcam app is
another option, and it often has a better image sensor than a budget webcam.
If you use a phone, keep it plugged in to power for the whole event and turn
off its notifications and screen lock.

At a two-field event, set up one camera per field.

Silver Tier
-----------

Add a second camera aimed at the area where awards are presented and
interviews happen. Without one, viewers watch an empty field during the
awards ceremony.

The second camera can be another fixed IP camera. A PTZ (pan-tilt-zoom)
camera is a better fit, because it can be pointed at the awards area, the
emcee, or a team being interviewed without anyone climbing a ladder to move
it.

At a two-field event, the second field's camera can be re-aimed at the awards
area once matches are finished, which gives you an awards camera without
buying one.

Gold Tier
---------

Use several NDI PTZ cameras with a hardware PTZ controller. NDI is a standard
for sending video, audio, and camera control over an ordinary network. Each
camera needs only one network cable, and appears in OBS as a source once the
NDI plugin is installed (see
:doc:`OBS Plugins </event_streaming/addons/obs_plugins/obs-plugins>`).
Volunteers have paid $300 to $500 per camera and about $300 for a
controller.

Because NDI cameras are all on the same network, cameras owned by different
volunteers can be combined for championships and Premier Events. A typical Gold
setup has a camera on each field, one on the awards area, and one that an
operator can move during opening ceremonies and alliance selection.
