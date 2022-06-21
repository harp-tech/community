:notoc:

*************************************************
How HARP works
*************************************************

.. _whyharp:
Why HARP was developed
-------------------------------------------------

Current Neuroscience experiments rely on multiple parallel streams of data, acquired from different devices, to examine how neural circuit activity relates to animal behaviours. This requires precise timestamping of experimental events, so that neural and behavioural data can be accurately ordered in time. Temporally aligning different streams of data, often acquired at different frequencies, rapidly becomes more difficult as setups increase in complexity.

Harp is a family of high-performance devices that make it easy for scientists to synchronize and extend the functionality of their setups. Harp devices can configure, control, & track a wide range of peripheral devices such as cameras, LEDs, nosepokes, & motors. Connecting an extra HARP device is a straightforward way to add extra functionality to a setup. All HARP devices can be connected to a shared clock line, self-synchronizing to a precision of tens of microseconds. This means that all experimental events are timestamped on the same clock and no post-hoc alignment of timing is necessary.

From an engineering perspective, extending the functionality of a setup can also be difficult, if this requires developing a new device, including how this device will communicates with a computer, and how users will interact with the device. By agreeing beforehand how the entire family of devices will communicate, engineers do not have to reinvent or attune protocols each time they wish to develop a new device. This leads to faster, cheaper, and more robust development.

What is HARP
-------------------------------------------------

HARP describes a communication protocol and architecture, as well as specific devices that implement these structures.

:ref:`The binary protocol is described here.<refbinaryprotocol>`
