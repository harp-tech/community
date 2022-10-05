.. _refbinaryprotocol:

*************************************************
Harp Binary Protocol
*************************************************

Harp devices and the host computer send each other messages in order to perform their functions, such as configuring device settings or reading out data. The Harp Binary Protocol specifies how these messages should be structured so that devices can communicate with each other.

In short, devices use registers to interface with the host computer. Each register can be read from, and most can be written to, to set configurations and read datastreams. Each register has a specific function, a datatype, and a unique address. Within a register, each bit has a specific function. Devices can send messages to each other (following the message protocol) to write to or read from other devices' registers.

.. contents:: Table of Contents
  :depth: 2
  :local:

1. Registers
---------------------
Registers contain highly structured information about specific aspects of a device. For instance, one register will contain the system timestamp in seconds, and another may determine whether an LED is on. Writing to registers can set device configurations, whereas reading register values can provide information about the device or stream data.

Every Harp device must have the same 15 'Common' registers, plus additional registers specific to the device. Each register has a specific purpose, described in its Name. It also has an associated Datatype for contents of the register. Note that the Harp Binary Protocol uses Little-Endian for byte organization, meaning that the least significant value in the sequence is stored first.

The following registers are common to all Harp devices:

.. image:: ../../_static/images/common_registers.png
   :align: center

.. admonition:: Example

  The first register Name is R_WHO_AM_I. The associated datatype is U16; unsigned 16-bit. On every device, this register will contain an U16 'word' that describes which device it is. To find out the device ID, one would want to read register R_WHO_AM_I. To do so, one would use the address associated with this register, address 000. If reading address 000 returned the value 1106, one could look this up in the `list of device IDs <https://github.com/harp-tech/protocol#list-of-the-current-devices-ids-reported>`_ to find out that the device is an Input Expander.


2. Messages
--------------------------------
Information about registers, whether to configure them (write to them) or read them, are sent as messages. The available forms of message are:

* Command: Sent by the Controller to the Peripheral. Commands can change or read register content.
* Reply: Sent by the Peripheral as an answer to a Controller.
* Event: Sent by the Peripheral when an external or internal event happens. An Event carry the content of a register.

2.1 Message structure
**********************************

A Harp message sent between devices follows this structure:


== Harp Message ==
**[MessageType] [Length] [Address] [Port] [PayloadType] [Payload] [Checksum]**

Where each section corresponds to the following information:

**[MessageType]** (1 byte)
__________________________________________________________
- 1 – Read : The device requests the content of the register with address [Address]
- 2 – Write : The device is writing the content to the register with address [Address]
- 3 – Event : The device is sending the content of the register with address [Address]

**[Length]** (1 byte)
__________________________________________________________

- The number of bytes in the Harp Message still to be read, i.e., the number of bytes after
the field [Length].

**[Address]** (1 byte)
__________________________________________________________

- The address to which the Harp Message refers to.

**[Port]** (1 byte)
__________________________________________________________

- If the device is a Hub of Harp Messages, this field indicates the origin or destination of
the Harp Message.
To point to the device itself this field should be equal to 255.

**[PayloadType]** (1 byte)
__________________________________________________________

- Indicates the type of data available on the [Payload]. The [Payload] can contain:

  * An element T
  * Or a timestamped element Timestamped<T>

  If the Type is **Timestamped<T>**, the first 6 bytes contains the time information and is
  divided into [TimestampSeconds] (4 bytes) and [TimestampMicroseconds] (2 bytes).

  - [TimestampSeconds] - Unsigned 32 bits containing the seconds.
  - [TimestampMicroseconds] - Unsigned 16 bits containing the microseconds divided by 32.


  The time information can be retrieved using the formula:

  - Timestamp(s) = [TimestampSeconds] + [TimestampMicroseconds] * 32 * 10-6

  .. raw:: html

    <details closed><summary> List of all available types of [Payload]:
    </summary>

    <table>
        <thead>
            <tr>
                <th colspan="2"></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1 - T U8 :</td>
                <td>Unsigned 8 bits</td>
            </tr>
            <tr>
                <td>2 - T U16 :</td>
                <td>Unsigned 16 bits</td>
            </tr>
            <tr>
                <td>4 - T U32 :</td>
                <td>Unsigned 32 bits</td>
            </tr>
            <tr>
                <td>8 - T U64 :</td>
                <td>Unsigned 64 bits</td>
            </tr>
            <tr>
                <td>129 - T I8 :</td>
                <td>Signed 8 bits</td>
            </tr>
            <tr>
                <td>130 - T I16 :</td>
                <td>Signed 16 bits</td>
            </tr>
            <tr>
                <td>132 - T I32 :</td>
                <td>Signed 32 bits</td>
            </tr>
            <tr>
                <td>136 - T I64 :</td>
                <td>Signed 64 bits</td>
            </tr>
            <tr>
                <td>68 - T Float :</td>
                <td>Single-precision floating-point 32 bits</td>
            </tr>
            <tr>
                <td>16 - Timestamped<> :</td>
                <td>Time information only</td>
            </tr>
            <tr>
                <td>17 - Timestamped<T> U8:</td>
                <td>Timestamped unsigned 8 bits</td>
            </tr>
            <tr>
                <td>18 - Timestamped<T> U16:</td>
                <td>Timestamped unsigned 16 bits</td>
            </tr>
            <tr>
                <td>20 - Timestamped<T> U32:</td>
                <td>Timestamped unsigned 32 bits</td>
            </tr>
            <tr>
                <td>24 - Timestamped<T> U64:</td>
                <td>Timestamped unsigned 64 bits</td>
            </tr>
            <tr>
                <td>145 - Timestamped<T> I8:</td>
                <td>Timestamped signed 8 bits</td>
            </tr>
            <tr>
                <td>146 - Timestamped<T> I16:</td>
                <td>Timestamped signed 16 bits</td>
            </tr>
            <tr>
                <td>148 - Timestamped<T> I32:</td>
                <td>Timestamped signed 32 bits</td>
            </tr>
            <tr>
                <td>152 - Timestamped<T> I64:</td>
                <td>Timestamped signed 64 bits</td>
            </tr>
            <tr>
                <td>84 - Timestamped<T> Float:</td>
                <td>Timestamped Single-precision floating-point 32 bits</td>
            </tr>

        </tbody>
    </table>
    </div>
    </details>



**[Payload]** (? byte(s))
_____________________________

The content.

**[Checksum]** (1 byte)
_____________________________

The U8 (unsigned 8 bits) sum of all bytes of the Harp Data.
The receiver of the package should compute himself this checksum and compare with the one
present on the Harp Message. The Harp Message should be discarded if both do not match.

2.2 Features and Code Examples
******************************************

Some of the fields described on the previous chapter have special features:

**[MessageType]** (1 byte)
_____________________________

The field [Command] has an Error flag on the 4th least significant bit. When this bit is
set it means that an error occur.
Examples of possible errors cane be a) when Controller tries to read a register that doesn’t
exist, b) Controller tries to write unacceptable data to a certain register, c) [PayloadType]
doesn’t match with the register [Address] type, etc.
A simple code in C to check for error will be::

    int errorMask = 0x08;

    if (Command & errorMask)
    {
      printf(“Error detected.\n”);
    }

**[Length]** (1 byte)
_____________________________

If one byte is not enough to express the length of the Harp Message, use [Length] equal to
255 and add after an unsigned 16 bits word with the Harp Message length.

Replace the [Length] with:

  [255] (1 byte) [ExtendedLength] (2 bytes)

**[PayloadType]** (1 byte)
_____________________________

For the definition of the [PayloadType] types, a C# code is presented.
Note that the time information can appear without an element **Timestamp<>**. ::

    int isUnsigned = 0x00;
    int isSigned = 0x80;
    int isFloat = 0x40;
    int hasTimestamp = 0x10;

    enum PayloadType
    {
        U8 = (isUnsigned | 1),
        S8 = (isSigned | 1),
        U16 = (isUnsigned | 2),
        S16 = (isSigned | 2),
        U32 = (isUnsigned | 4),
        S32 = (isSigned | 4),
        U64 = (isUnsigned | 8),
        S64 = (isSigned | 8),
        Float = (isFloat | 4),
        Timestamp = hasTimestamp,
        TimestampedU8 = (hasTimestamp | U8),
        TimestampedS8 = (hasTimestamp | S8),
        TimestampedU16 = (hasTimestamp | U16),
        TimestampedS16 = (hasTimestamp | S16),
        TimestampedU32 = (hasTimestamp | U32),
        TimestampedS32 = (hasTimestamp | S32),
        TimestampedU64 = (hasTimestamp | U64),
        TimestampedS64 = (hasTimestamp | S64),
        TimestampedFloat = (hasTimestamp | Float)
    }

**[PayloadType]** (1 byte)
_____________________________

The field **[PayloadType]** has a flag on the 5th least significant bit that indicates if the
time information is available on the Harp Message. For some reasons, the time information
may not make sense to appear on the Harp Message.
A simple code in C to check if the time information is available will be: ::

  int hasTimestamp = 0x10;
  if (PayloadType & hasTimestamp )
  {
  printf(“The time information is available on the Harp Message’s Payload.\n”);
  }

**[Checksum]** (1 byte)
____________________________

Example on how to calculate the **[Checksum]** in C language. ::

  unsigned char Checksum = 0;
  int i = 0;
  for (; i < Length + 1; i++ )
  {
      Checksum += HarpMessage(i);
  }

2.2 Payload and Arrays
***************************************
The [payload]’s element can contain a single value or an array of values. To find the amount of values a simple
code can be applied using the information contained on the [Length] and the [PayloadType].
Example to calculate the number of values on the [Payload]’s element in C language: ::

  int arrayLength;
  int hasTimestamp = 0x10;
  int sizeMask = 0x0F;

  if (PayloadType & hasTimestamp )
  {
      /* Harp Message has time information
      arrayLength = (Length – 10) / (PayloadType & sizeMask )
  }
  else
  {
      /* Harp Message doesn’t have time information
      arrayLength = (Length – 4) / (PayloadType & sizeMask )
  }


3. Typical Usage
--------------------------------

.. role:: red
.. role:: blue
.. role:: green

3.1 Commands
************************************
Usually the Peripheral device that runs this protocol receives Write and Read commands from the Controller and sends Events to the Controller.
Some Harp Messages are shown here to demonstrate the typical usage. Note that, from the Controller to the Peripheral, the time information is not added to the Harp Message since this information is not necessary.

Note: [CMD] is a Command, [RPL] is a Reply and [EVT] is an Event.

== WRITE ==
____________________________

From Controller to Peripheral. Peripheral replies.

- [CMD] Controller: 2 :blue:`Length Address Port` :green:`PayloadType` :red:`T` Checksum
- [RPL] Peripheral: 2 :blue:`Length Address Port`  :green:`PayloadType` :red:`Timestamp<T>` Checksum OK
- [RPL] Peripheral: 10 :blue:`Length Address Port`  :green:`PayloadType` :red:`Timestamp<T>` Checksum ERROR

The time information contains the time when the register with Address was updated.

== READ ==
____________________________

From Controller to Peripheral. Peripheral replies.

- [CMD] Controller: 1 :blue:`4 Address Port`  :green:`PayloadType` Checksum
- [RPL] Peripheral: 1 :blue:`Length Address Port` :green:`PayloadType` :red:`Timestamp<T>` Checksum OK
- [RPL] Peripheral: 9 :blue:`10 Address Port` :green:`PayloadType` :red:`Timestamp<>` Checksum ERROR

The time information contains the time when the register with Address was read.

== EVENT ==
____________________________

Always from Peripheral to Controller.

- [EVT] Peripheral: 3 :blue:`Length Address Port` :green:`PayloadType` :red:`Timestamp<T>` Checksum

The time information contains the time when the register with Address was read.
