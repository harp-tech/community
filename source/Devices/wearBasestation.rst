.. _REFDEVICE:

*************************************************
WEAR Basestation
*************************************************

.. raw:: html

      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card card-body" >
            <div class="deviceDescription">This device is the basestation for the Wired and Wireless sensor devices. The devices can be configured using the Harp Wear software.
            </div>
          </div>
        </div>

        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card border-light">
            <img class="card-img-top" src="../_static/images/devices/wearBasestation.png" alt = "Photo of device WEAR Basestation" style="margin: 0 auto; width: 75%">
          </div>
        </div>
      </div>

      <div class="deviceFeatures">

Key Features
******************************************
- Sample rate up to 500 Hz
- LED optical stimulation
- Start & Stop through pin or software
- Output pulse for valves
- Accelerometer, Gyroscope, and Magnetometer
- Wired or Wireless communication

Use Cases
******************************************
- Use this device to configure the settings of the WEAR wired or wireless sensor devices (light motion sensors with electrostimulation capabilities)

Connectivity
******************************************
- 1x clock sync input (CLKIN) [stereo jack]
- 1x clock sync output(CLKOUT) [stereo jack]
- 1x USB (for computer) [USB type B]
- 1x 5V supply [barrel connector jack]
- 2x Digital inputs DI0 [BNC], DI1  [screw terminal]
- 2x Digital outputs: DO0 [BNC], DO1  [screw terminal]
- 1x Analog input: AI0  [screw terminal]
- 2x Cameras triggering: CAM0 [flick lock], CAM1 [screw terminal]
- 2x Servo motor controllers:  CAM0 [flick lock], CAM1 [screw terminal]

Software Configuration Options
******************************************
`Download software here: <https://www.google.com/url?q=https%3A%2F%2Fbitbucket.org%2Ffchampalimaud%2Fdownloads%2Fdownloads%2FHarp%2520Wear%2520v1.3.4.zip&sa=D&sntz=1&usg=AOvVaw1AFYY-Pa3m_w9ZNoSqKxZa>`_

- Sensors: sample frequency, accelerometer range, gyroscope range
- Sensor device wireless settings: device ID, IR LEDs ON period, TX power, and prioritization
- Stimulation: trigger mode (SW-only or input signal dependent), ON/OFF periods, number of cycle repetitions, and current
- I/O: input trigger mode and output behavior
- Cameras: sample frequency
- Servo motors: PWM and pulse periods
- Event firing on: Acquisition status, Data arrives from sensor, Any of the inputs is read, Camera is triggered, DO0 each second and pulse ending on output DO1, Sensor metadata, HW and SW Versions of both sensor and receiver

.. raw:: html

    </div>
