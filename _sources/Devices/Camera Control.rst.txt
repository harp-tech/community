.. _refcamera_control:

*************************************************
Camera Control
*************************************************

.. raw:: html

      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card card-body" >
            <div class="deviceDescription" style="margin: 0 2rem">This devices can trigger up to 2 cameras or 2 servo motors at a predetermined frequency.
            </div>
          </div>
        </div>

        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card border-light">
            <img class="card-img-top" src="../_static/images/devices/camera_control.png" alt = "Photo of device Camera Control" style="margin: 0 auto; width: 75%">
          </div>
        </div>
      </div>

      <div class="deviceFeatures">

Key Features
******************************************
- Separate sample frequency for each camera
- Alternate between camera triggering and servo motor controlling
- Each camera output can be handled as pure digital output

Use Cases
******************************************
- Experiments that require camera recordings with external control

Connectivity
******************************************
- 1x clock sync input (CLKIN) [stereo jack]
- 1x USB (for computer) [USB type B]
- 1x 5V supply out [screw terminal]
- 4x digital outputs (I/O interface for 2 cameras): CAM0 TRIG, CAM0 SYNC, CAM1 TRIG, CAM1 SYNC  [screw terminal]
- 1x digital input for general purpose or camera control (IN0) [BNC]

Software Configuration Options
******************************************
`Download software here: <https://www.google.com/url?q=https%3A%2F%2Fbitbucket.org%2Ffchampalimaud%2Fdownloads%2Fdownloads%2FHarp%2520Camera%2520Controller%2520v1.0.1.zip&sa=D&sntz=1&usg=AOvVaw37Pdw8O64-V-p5cilpQj_C>`_

- Cameras: sample frequency (up to 1KHz)
- Servo motor controller: PWM period (microseconds) and pulse period (microseconds)
- Digital input: General purpose or enable camera/motor depending on IN0 state
- Sync pulses (up to 100s)
- Event firing on: trigger and synchronism outputs, and IN0

.. raw:: html

    </div>
