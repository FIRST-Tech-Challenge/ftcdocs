Choosing a Wi-Fi Band for Your Robot
====================================

Started in the 2023-2024 season, Tech Tips are segments released in the
*FIRST* Tech Challenge `Team E-mail Blast
<https://www.firstinspires.org/resource-library/ftc/team-blast-archive>`__.
Sometimes the Tech Tips are included in whole in the email blast, but sometimes
there is more content than is reasonable in the email blast so partial content
is included in the blast with the rest of the content here.

.. _wifibands:

Hopefully "Bandwidth of Robots" will be your new favorite way to refer to
groups of wireless robots. This Tech Tip covers Wi-Fi bands and why you might
be shooting yourself in the foot by not selecting (and designing your robots
for) the right Wi-Fi band. And at the end of the day how do you truly know
which band you should be using?

If you're anything like the average team, Wi-Fi bands are something nebulous
that you don't really understand or even give a second thought to. At least,
until "bad things" start happening and you're grasping at straws trying to
resolve them. So let's start this discussion by talking about radio
frequency bands and then the two Wi-Fi bands we have access to, 2.4GHz and
5GHz.

.. _wifibands1:

Frequencies and Wavelengths
---------------------------

What are the important properties of Wi-Fi frequencies we should know? To
explain Wi-Fi frequencies, let's look at something most of us might already
be more familiar with - AM and FM radio frequency bands (which share similar
behaviors, ignoring modulation differences).

AM radio stations are assigned carrier radio frequencies between
540kHz-1600kHz. For example WGHM 900 AM out of Nashua, NH, is licensed to
broadcast at 900kHz. AM radio station signals travel very far very easily
mostly because the frequencies in AM radio have very large wavelengths -
900kHz, for example, has a full wavelength of 333m (just over one fifth of a
mile) - and because of this they can bend around obstacles very easily
(buildings, mountains, curvature of the earth, etc). However, long
wavelength AM radio is more susceptible to interference and static than
shorter wavelength transmissions, like FM.

FM radio stations are assigned frequencies between 88.1MHz-108.1MHz. For
example, WEVS 88.3 FM also in Nashua, NH broadcasts at 88.3MHz. FM radio
frequencies are higher frequency, and have a shorter wavelength - 88.3MHz is
about 3.4m (about 11 feet) in wavelength - and cannot bend around obstacles
as easily. Shorter wavelength frequencies also tend to be absorbed/reflected
(comparatively) much easier by obstacles as well.

Hence when driving through the mountains and forests of NH I am more apt to
be able to cleanly listen to the AM station uninterrupted but not the FM
station, even though they're broadcasting at roughly the same power and from
very similar locations.

Frequency bands used for Wi-Fi share very similar characteristics, but
because the frequencies for Wi-Fi are much higher some characteristics are
more exaggerated. As an analogy, for the purposes of this discussion, we can
say that 2.4GHz is to 5GHz as AM is to FM. 2.4GHz frequencies have a longer
wavelength (starting at ~0.125m or ~5 inches) than 5GHz frequencies
(starting at ~0.05m or ~2 inches), and because of that 2.4GHz radio waves
can bend around objects better than 5GHz ones but are much more susceptible
to interference than 5GHz. Similarly 5GHz frequencies will also tend to be
reflected/absorbed much easier by solid objects, and so 5GHz tends to
perform better with an unobstructed line of sight between antennas.

.. _wifibands2:

Sources of Interference
-----------------------

Unlike AM and FM radio, Wi-Fi doesn't have dedicated frequency space. This can
cause legitimate issues due to the number of existing devices and services that
already use frequencies that Wi-Fi has to share.

You might have realized this, but wireless devices are all the rage. The FCC
(in the USA) doesn't just let any device broadcast on any frequency they
want. Instead, there are licensed and unlicensed radio frequency bands. Some
frequencies are uniquely licensed to private operators, for example radio
stations pay a lot of money to the FCC for the exclusive rights to broadcast
on specific frequencies. HAM radio operators undergo special training to be
allowed to broadcast on a range of licensed frequencies (some reserved only
for HAM radio, some not). The FCC also sets aside frequencies that are
unlicensed, meaning the operators themselves (like you, your neighbor, or
the kid down the street) don't need training or licensing to operate devices
that broadcast on those frequencies. The devices themselves must adhere to
specific regulations, but those requirements are generally easy to meet.

Wi-Fi uses portions of the radio frequency spectrum designated as unlicensed
- remember that these frequencies are available to the general public to use
- so anyone can broadcast signals over it. And boy howdy do they. The
2.4GHz frequency band was opened to the public in 1985, and devices
began using that frequency for use. Wi-Fi emerged in the late 1990's.
The 2.4GHz frequency band became extremely crowded, and by devices using
different protocols - think about trying to have a conversation with a
friend in a crowded room, but some people are talking "normally", some
are using air horns, and others are mimicking nails on a chalkboard. The
resource was very narrow, but at least interference was just a matter of
distance - though not everyone lives in the deserts of Arizona where
they can carry out their conversations in relative peace.

By the turn of the 20th century, the 5GHz space was opened up for unlicensed
use. This required different hardware, as the 2.4GHz devices couldn't simply
just start using 5GHz. The 5GHz band was much larger, and it took longer for
it to become crowded as more devices came onto the market that could use it.
5GHz already had a bunch of legacy systems that used portions of it, and so
the FCC grandfathered those systems and made special regulations for using
those frequencies (most manufacturers designed their devices to only use the
portions of the 5GHz band with the least rules and regulations). Some uses
of 2.4GHz could not move to 5GHz because of the frequency wave propagation
behaviors (that we talked about previously, e.g. reflections and wave
bending), but many systems like Wi-Fi found the greatest use in 5GHz. The
number of channels and the frequency space was much larger in 5GHz, and 5GHz
Wi-Fi technologies learned to use the 5GHz space more efficiently and
robustly.

When you consider which frequency you should use, you have to consider many
factors. How obstructed is the path from the radio to the receiver?  How
crowded might the frequency space be that you're trying to use? Has the
event organizer worked with the venue to clear specific channels for robots
to use? What advanced technologies might the device you're using be capable
of utilizing on specific frequency bands?

.. _wifibands3:

Robot Design and Choosing Your Band
-----------------------------------

Robot design - and more aptly "Control Hub placement" - is THE critical
factor in influencing the Wi-Fi frequency/band you should be using. Remember
Wi-Fi is a line-of-sight technology, that means Wi-Fi does best when there's
a straight unobstructed path from the antenna on the Control Hub to the
antenna on the Driver Hub. Where is the antenna in a Control Hub? It's right
under the plastic on the "face" of the hub on the logo side. If the Control
Hub can be mounted so that its antenna is generally not
covered/surrounded/blocked by metal, 5GHz should be your target band.
However, if your Control Hub is buried deep inside the robot and surrounded
by metal, the 2.4GHz band may be your only option (remember, the lower
frequencies of 2.4GHz might be able to "bend around" metal obstacles
slightly better). Unfortunately exposing the "back side" of the Control Hub
instead of the "front side" of the hub is not going to yield similar
results, as there is a PCB with metal traces between the antenna and the
"back side" of the Hub that will block/reflect/absorb signals.

Does that mean your Control Hub needs to be mounted unprotected on the
outside of the robot in order to get good signal reception? Not necessarily,
fortunately not all materials are the same. Plastics are generally the most
"invisible" to Wi-Fi frequencies, or at least their
absorption/blocking/reflection (also known as attenuation) is generally
minimal enough to not sufficiently matter. Wood, especially thin birch
commonly used in many robot designs, is slightly more attenuating but
definitely still a great option. Metals, however, will greatly attenuate
Wi-Fi frequencies and are the worst materials for Wi-Fi transmission. Yes,
I'm looking at YOU teams who use hook-and-loop to mount your robot battery
to the top of the Control Hub - stop doing that! And for those looking for
inspiration in this upcoming season, water is also an incredibly poor medium
for transmission of Wi-Fi frequencies.

But how do you know for sure how well your robot's Wi-Fi is performing? You
can monitor the Wi-Fi signal's strength through the Driver Station App. Check
out :ref:`Monitoring Your Robot's Wi-Fi Connection
<tech_tips/tech-tips/tech-tip-wifi-monitoring/tech-tip-wifi-monitoring:Monitoring Your Robot's Wi-Fi Connection>`
for info on how to view and understand Wi-Fi Signal Strength. If your signal
is strong when using 5GHz at maximum field range (from the Driver Hub) and
in all robot orientations, you should be good to go on 5GHz! Feel free to
compare the performance on 5GHz and 2.4GHz, and if they're comparable you
should stick with 5GHz for better interference reduction.

In summary, the vast majority of robots should be using 5GHz as this is the
optimal channel in terms of interference reduction, device crowding, and
channel utilization by the Wi-Fi standards. Robot design - specifically
Control Hub placement - might necessitate the use of 2.4GHz if the
line-of-sight path to the Control Hub antenna in the robot is too greatly
obstructed by metal, especially motors. By monitoring the robot's Wi-Fi
signal strength, you can determine which frequency band yields the best
Wi-Fi signal performance for your robot.

Got any questions about Wi-Fi bands? Come start or join the conversation on
the `FTC Community Forums <https://ftc-community.firstinspires.org/>`__!
