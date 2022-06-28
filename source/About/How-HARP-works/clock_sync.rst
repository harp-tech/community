:notoc:

.. _refclocksync:
*************************************************
Synchronization Clock
*************************************************

.. contents:: Table of Contents
  :depth: 2
  :local:

One of the most important features of Harp is the ability of all Harp devices to share the same clock. Because any registered event is timestamped on the same clock, the temporal sequence of events is accurately determined even if events are detected by different devices.

1. Introduction
------------------------------------------
The Harp Synchronization Clock is a bus that disseminates the actual current time to Harp devices.
It’s a serial communication containing the time information. Each device uses the last byte of the
transmission to align themselves with the current time.

2. Serial configuration
------------------------------------------
Baud rate used is 100 kbps.

The last byte starts **exactly** 672 us before the elapse of the current second (picture below).

The packet is composed of 6 bytes (header[2] and timestamp_s[4])
- header[2] = {0xAA, 0xAF)
- The timestamp_s is of type uint32 little-endian and contains the current second

.. warning:: IMPORTANT

    Since there's no checksum to validate the packet, the sender must make sure that, if the header sequence is present in the, the packet is not sent.

3. Example code
------------------------------------------
Example of a microcontroller C code: ::

  ISR(TCD0_OVF_vect, ISR_NAKED)
      {
          if ((*timestamp_byte0 == 0xAA) && (*timestamp_byte1 == 0xAF)) reti();
          if ((*timestamp_byte1 == 0xAA) && (*timestamp_byte2 == 0xAF)) reti();
          if ((*timestamp_byte2 == 0xAA) && (*timestamp_byte3 == 0xAF)) reti();

          switch (timestamp_tx_counter)
      {
          case 1:
              USARTD1_DATA = 0xAA;
              break;
          case 2:
              USARTD1_DATA = 0xAF;
              break;
          case 4:
              USARTD1_DATA = *timestamp_byte0;
              break;
          case 6:
              USARTD1_DATA = *timestamp_byte1;
              break;
          case 7:
              USARTD1_DATA = *timestamp_byte2;
              break;
          case 1998:
              USARTD1_DATA = *timestamp_byte3;
              break;
      }

4. Physical connection
------------------------------------------

The physical connection is made by a simple audio cable.

The connector used is from Switchcraft Inc. and has the part number 35RASMT2BHNTRX
