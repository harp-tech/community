:notoc:

.. _refdeviceregistersandoperation:
*************************************************
Harp device common registers and operation
*************************************************

.. contents:: Table of Contents
  :depth: 3
  :local:


Introduction
------------------------------------------------
This page lists the registers and operation modes that must be present in any Harp device. These allow Harp devices to be identified and easily combined. Additional optional registers and functionalities are also presented.

Common Registers:
****************************************************

Summary description of each register can be found below.

Application Registers are the registers which differ from device to device according the device purpose. It is up to the developer to set the names and types of each Application Register. The addresses of Application Registers should be equal to 32 or higher.

Operation Modes:
****************************************************

The Harp Device, when acting as a Peripheral, should implement the following Operation Modes:

- **Standby Mode** (mandatory): Replies to Controller commands. Events are disabled and must not be sent.
- **Active Mode** (mandatory): Replies to Controller commands. Events are enabled and sent to Controller whenever the Peripheral decides.
- **Speed Mode** (optional): Allows the implementation of a different and specific communication protocol. In this mode, the Harp Binary Protocol is no longer used. The specific protocol designed must implement the possibility to leave this mode.

The mandatory Operation Modes are the Standby Mode and Active Mode. The Speed Mode is optional and, in many of the applications, is not needed.

It is strongly recommended that a Harp Device acting as a Peripheral should continuously check if the communication with the Controller is active and healthy. If this doesn’t happen over the last 3 seconds, the Harp Device should go to Standby Mode and flush/destroy its TX buffer.

Registers
------------------------------------------------

Common Registers
****************************************************

List of all Common Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <body>
      <table border="1" cellpadding="2" cellspacing="0" style = "text-align: center;">
      <tbody>
        <tr style="font-weight: bold; font-size: 0.8rem; background-color: #aaa">
        <th>Name</th><th>Volatile</th><th>Read Only</th><th>Type</th><th>Add.</th><th>Default</th><th>Brief Description</th><th>Mandatory</th>
        </tr>
        <tr style="background-color: #f0f0f0">
        <td>R_WHO_AM_I</td><td>-</td><td>Yes</td><td>U16</td><td>000</td><td>a)</td><td>Who am I</td><td>Yes</td>
        </tr>
        <tr style="background-color: #ffffff">
        <td>R_HW_VERSION_H</td><td>-</td><td>Yes</td><td>U8</td><td>001</td><td>a)</td><td>Major Hardware version</td><td>Yes</td>
        </tr>
        <tr style="background-color: #f0f0f0">
        <td>R_HW_VERSION_L</td><td>-</td><td>Yes</td><td>U8</td><td>002</td><td>a)</td><td>Minor Hardware version</td><td>Yes</td>
        </tr>
        <tr style="background-color: #ffffff">
        <td>R_ASSEMBLY_VERSION</td><td>-</td><td>Yes</td><td>U8</td><td>003</td><td>a)</td><td>Version of the assembled components</td><td>Optional</td>
        </tr>
        <tr style="background-color: #f0f0f0">
        <td>R_HARP_VERSION_H</td><td>-</td><td>Yes</td><td>U8</td><td>004</td><td>a)</td><td>Major HARP version</td><td>Optional</td>
        </tr>
        <tr style="background-color: #ffffff">
        <td>R_HARP_VERSION_L</td><td>-</td><td>Yes</td><td>U8</td><td>005</td><td>a)</td><td>Minor HARP version</td><td>Optional</td>
        </tr>
        <tr style="background-color: #f0f0f0">
        <td>R_FW_VERSION_H</td><td>-</td><td>Yes</td><td>U8</td><td>006</td><td>a)</td><td>Major Firmware version of the application</td><td>Yes</td>
        </tr>
        <tr style="background-color: #ffffff">
        <td>R_FW_VERSION_L</td><td>-</td><td>Yes</td><td>U8</td><td>007</td><td>a)</td><td>Minor Firmware version of the application</td><td>Yes</td>
        </tr>
        <tr style="background-color: #f0f0f0">
        <td>R_TIMESTAMP_SECOND</td><td>Yes</td><td>No</td><td>U32</td><td>008</td><td>0</td><td>System timestamp: seconds</td><td>Yes</td>
        </tr>
        <tr style="background-color: #ffffff">
        <td>R_TIMESTAMP_MICRO</td><td>Yes</td><td>Yes</td><td>U16</td><td>009</td><td>0</td><td>System timestamp: microseconds</td><td>Optional</td>
        </tr>
        <tr style="background-color: #f0f0f0">
        <td>R_OPERATION_CTRL</td><td>No</td><td>No</td><td>U8</td><td>010</td><td>b)</td><td>Configuration of the operation mode</td><td>c)</td>
        </tr>
        <tr style="background-color: #ffffff">
        <td>R_RESET_DEV</td><td>No</td><td>No</td><td>U8</td><td>011</td><td>b)</td><td>Reset device and save non-volatile registers</td><td>Optional</td>
        </tr>
        <tr style="background-color: #f0f0f0">
        <td>R_DEVICE_NAME</td><td>No</td><td>No</td><td>U8</td><td>012</td><td>b)</td><td>Name of the device given by the user</td><td>Optional</td>
        </tr>
        <tr style="background-color: #ffffff">
        <td>R_SERIAL_NUMBER</td><td>No</td><td>No</td><td>U16</td><td>013</td><td>b)</td><td>Unique serial number of the device</td><td>Optional</td>
        </tr>
        <tr style="background-color: #f0f0f0">
        <td>R_CLOCK_CONFIG</td><td>No</td><td>No</td><td>U8</td><td>014</td><td>b)</td><td>Synchronization clock configuration</td><td>Optional</td>
        </tr>
      </tbody>
    </table>

a) These values are stored during factory process and are persistent, i.e., they cannot be changed by the user.
b) Check register notes on the specific register explanation
c) Only parts of the functionality is mandatory. Check register notes on the explanation.

R_WHO_AM_I – Who Am I
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <body>
      <div class="table-container">
           <div class="table-item">Address: 000</div>
           <div class="table-item first">WHO_AM_I [15:0]</div>
      </div>
    </body>

Used to verify the identity of the device.

A list of devices can be found at https://github.com/harp-tech/protocol. To reserve a range or certain IDs for your project or company, please send an e-mail to filipe@oeps.tech.
If the device doesn’t have a pre-allocated ID on the IDs list, this register should be read as 0.

R_TIMESTAMP_SECOND – System timestamp: seconds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <body>
      <div class="table-container">
           <div class="table-item">Address: 008</div>
           <div class="table-item first">SECONDS [31:0]</div>
      </div>
    </body>

Contains the current system timestamp in seconds. The default value is 0 (ZERO) and will increment one unit for each second.

R_TIMESTAMP_MICRO – System timestamp: microseconds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <body>
      <div class="table-container">
           <div class="table-item">Address: 009</div>
           <div class="table-item first">USECONDS [15:0]</div>
      </div>
    </body>

Contains the microseconds count within each second. Each LSB corresponds to 32 μseconds. The maximum
value is 31249.

R_OPERATION_CTRL – Configuration the operation mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <table cellpadding="1" cellspacing="0" width = "100%"  align = "center" style = "text-align: center; table-layout: fixed; font-size: 0.8rem">

      <caption></caption>
      <tbody>
        <tr style= "border: 0px">
          <th>Bit</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th><th>0</th>
        </tr>

        <tr style="border: 0px">
          <th>Address: 010</th><th class = "highlight">ALIVE_EN</th><th class = "highlight">OPLEDEN</th><th class = "highlight">VISUALEN</th>
          <th class = "highlight">MUTE_RPL</th><th class = "highlight">DUMP</th><th class = "highlight" >-</th><th colspan="2" class = "highlight">OP_MODE [1:0] </th>
        </tr>

        <tr style= "border: 0px">
          <th>Default (Mandatory)</th><th>1 (Optional)</th><th>1 (Optional)</th><th>1 (Optional)</th><th>0 (Optional)</th><th>0 (Optional)</th><th>0 -</th><th  colspan="2" >0 a)</th>
        </tr>

      </tbody>
    </table>

a) Standby Mode and Active Mode are mandatory. Speed Mode is optional.

How each Bit is used:
############################

- **Bits 1:0 – OP_MODE [1:0]: Operation Mode**

    These bits define the operation mode of the device.
    Note that, if Speed Mode is selected, the device will no longer reply to the HARP commands, only to its
    specific Speed Mode commands.

- **Bit 3 – DUMP**

    When written to 1, the device adds the content of all registers to the streaming buffer.
    This bit is always read as 0.

- **Bit 4 – MUTE_RPL**

    If equal to 1, the Replies to all the Commands are muted, i.e., will not be sent by the device.

- **Bit 5 – VISUALEN**

    If equal to 1, the visual indications, typically LEDs, available on the device will operate. If equals to 0, all the visual indications should turn off.

- **Bit 6 – OPLEDEN**

    If equal to 1, the LED present on the device will indicate the Operation Mode selected.


.. raw:: html

    <table border="1" cellpadding="2" cellspacing="0" width = 75% align = center style = "text-align: center;">
    <caption>Table 2-2. Operation Mode</caption>
    <tbody><tr style="font-weight: bold; background-color: #aaa">
      <th>OP_MODE[0:1]</th><th>Configuration</th>
      </tr>
      <tr style="background-color: #f0f0f0">
      <td>0</td><td>Standby Mode. The device has all Events turned off.</td>
      </tr>
      <tr style="background-color: #ffffff">
      <td>1</td><td>Active Mode. The device turns ON Event detection. Only enabled Events will be operating.</td>
      </tr>
      <tr style="background-color: #f0f0f0">
      <td>2</td><td>Reserved.</td>
      </tr>
      <tr style="background-color: #ffffff">
      <td>3</td><td>Speed Mode. The device enters Speed Mode.</td>
      </tr>
    </table>


.. raw:: html

    <table border="1" cellpadding="2" cellspacing="0" width = 75% align = center style = "text-align: center;">
    <caption>Table 2-2. LED toggle indication</caption>
    <tbody><tr style="font-weight: bold; background-color: #aaa">
      <th>Interval in Seconds</th><th>Operation Mode</th>
      </tr>
      <tr style="background-color: #f0f0f0">
      <td>4</td><td>Standby Mode.</td>
      </tr>
      <tr style="background-color: #ffffff">
      <td>2</td><td>Active Mode.</td>
      </tr>
      <tr style="background-color: #f0f0f0">
      <td>1</td><td>Speed Mode.</td>
      </tr>
      <tr style="background-color: #ffffff">
      <td>0.1</td><td>A critical error occurred. Only a hardware reset or a new power up can remove the device from this Mode.</td>
      </tr>
    </table>

- **Bit 7 – ALIVE_EN**

    If equal to 1, the device sends an Event with the R_TIMESTAMP_SECONDS content each second. This allows the
    Controller and/or the user to check that the device is alive. Although this is an optional feature, it’s strongly suggested that the device should implement it.

R_RESET_DEV – Reset device and save non-volatile registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <table cellpadding="1" cellspacing="0" width = "100%"  align = "center" style = "text-align: center; table-layout: fixed; font-size: 0.8rem">

    <caption></caption>
    <tbody>
    <tr>
      <th>Bit</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th><th>0</th>
    </tr>

    <tr>
      <th style= "background-color: white">Address: 011</th><th class = "highlight">BOOT_EE</th><th class = "highlight">BOOT_DEF</th><th class = "highlight">-</th><th class = "highlight">-</th>
      <th class = "highlight">-</th><th class = "highlight">SAVE</th><th class = "highlight">RST_EE</th><th class = "highlight">RST_DEF</th>
    </tr>

    </tbody>
    </table>

How each Bit is used:
############################

- **Bits 0 – RST_DEF**

    If this bit is written to 1, the device resets and boots with all the registers, both Common and Application
    registers, with the default values. EEPROM will be erased and the default values will be the permanent boot
    option.
    This bit is always read as 0.

- **Bits 1 – RST_EE**

    If this bit is written to 1, the device resets and boots with all his registers, both Common and Application
    registers, with the values saved on the non-volatile memory, usually an EEPROM. The EEPROM values will be
    the permanent boot option.

    Should not be possible to write to this bit if the non-volatile memory is empty.

    This bit is always read as 0.

- **Bits 2 – SAVE**

    If this bit is written to 1, the device saves all the non-volatile registers (Common and Application) to the
    internal non-volatile memory and boots. The non-volatile memory should be the permanent boot option.

    This bit is always read as 0.

- **Bits 3 – NAME_TO_DEFAULT**

    If this bit is written to 1, the device boots with the default name.

    This bit is always read as 0.

- **Bits 6 – BOOT_DEF**

    It is a state bit (read only). Indicates that the device booted with the default register values.

- **Bits 7 – BOOT_EE**

    It is a state bit (read only). Indicates that the device booted with the register values saved on the EEPROM.

.. note::
  To avoid unexpected behaviors, one bit at a time should be written to register R_RESET_DEV.

R_DEVICE_NAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
An array of 25 bytes that should contain the device name.
The last byte and the bytes not used must be equal to 0.
This register is non-volatile. The device will reset if this register is written.

R_SERIAL_NUMBER – Device’s serial number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <body>
      <div class="table-container">
           <div class="table-item">Address: 013</div>
           <div class="table-item first">SERIAL_NUMBER [15:0]</div>
      </div>
    </body>

This number should be unique for each unit of the same Device ID.

To write to this register a two-step write command is needed. First, write the value 0xFFFF, and then the
desired serial number. The device will reset after the second write command is sent.

R_CLOCK_CONFIG – Synchronization clock configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <table cellpadding="1" cellspacing="0" width = "100%"  align = "center" style = "text-align: center; table-layout: fixed; font-size: 0.8rem">

      <tbody>
        <tr>
          <th>Bit</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th><th>0</th>
        </tr>

        <tr>
          <th>Address: 014</th><th class = "highlight">CLK_LOCK</th><th class = "highlight" style = "font-size: 0.8rem">CLK_UNLOCK</th><th class = "highlight">-</th><th class = "highlight">GEN_ABLE</th>
          <th class = "highlight">REP_ABLE</th><th class = "highlight">-</th><th class = "highlight">CLK_GEN</th><th class = "highlight">CLK_REP</th>
        </tr>

      </tbody>
    </table>

How each Bit is used:
#############################

- **Bits 0 – CLK_REP**

    If this bit is written t to 1, the device will repeat the Harp Synchronization Clock to the Clock Output
    connector, if available. It will act has a daisy-chain by repeating the Clock Input into Clock Output.
    Writing 1 to this bit also unlocks the Harp Synchronization Clock.
    This bit is read as 1 if the device is repeating the Harp Synchronization Clock.

- **Bits 1 – CLK_GEN**

    If this bit is written to 1, the device resets will generate the Harp Synchronization Clock in the Clock Output
    connector, if available. The Clock Input is ignored.
    This bit is read as 1 if the device is generating the Harp Synchronization Clock.

- **Bits 3 – REP_ABLE**

    This is a read only bit. Written to this bit will not have any effect.
    The bit is equal to 1 if the device can repeat the Harp Timestamp Clock.

- **Bits 4 – GEN_ABLE**

    This is a read only bit. Written to this bit will not have any effect.
    The bit is equal to 1 if the device can generate the Harp Timestamp Clock.

- **Bits 6 – CLK_UNCLOCK**

    If this bit is written to 1, the device will unlock the timestamp register counter (register
    R_TIMESTAMP_SECOND) and will accept new timestamp values.
    This bit is read as 1 if the timestamp register is unlocked.

- **Bits 7 – CLK_LOCK**

    If this bit is written to 1, the device will lock the current timestamp counter (register R_TIMESTAMP_SECOND)
    and will not be able to accept new timestamp values.
    This bit is read as 1 if the timestamp register is locked.

.. note::
  The device always wakes up in the unlock state.
