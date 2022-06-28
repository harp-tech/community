.. _behaviorDevice:

*************************************************
Behavior
*************************************************

.. raw:: html

      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card card-body" >
            <div class="deviceDescription">This is a multi-purpose device tailored to behavioral experiments. It allows control of pokes, RGB LEDs, LEDs, cameras, servo motors and a quadrature counter.
            </div>
          </div>
        </div>

        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card border-light">
            <img class="card-img-top" src="../_static/images/devices/alldevices\behaviorDevice.png" alt = "Photo of device Behavior" style="margin: 0 auto; width: 75%">
          </div>
        </div>
      </div>

      <div class="deviceFeatures">

Key Features
******************************************
- Enable pulse and configure duration for each output
- Support for PWM configuration (frequency up to 10KHz and duty cycle)
- LED current (up to 100mA) and maximum nominal current configuration
- Up to 2 cameras controlling (DO0 and DO1)
- Up to 2 servo motors (DO2 and DO3)
- Up to 1 quadrature counter (Port2) (Note: Port0 and Port1 can also act as quadrature counters but this is a request feature)

Use Cases
******************************************
- Behavioral experiments


Connectivity
******************************************
- 1x clock sync input (CLKIN) [stereo jack]
- 1x USB (for computer) [USB type B]
- 1x 12V supply [barrel connector jack]
- 3x poke connectors (LED+12V valve) (Poke0, Poke1, Poke2) [RJ45]
- 2x LEDs outputs (5V) (LED0, LED1) [screw terminal]
- 2x RGB LEDs outputs (5V) (RGB0, RGB1) [flick lock 3x male pins]
- 4x general purpose digital outputs with PWM (5V) (DO0-DO3) [screw terminal]
- 1x ADC (5V) [screw terminal]

Software Configuration Options
******************************************
`Download software here: <https://www.google.com/url?q=https%3A%2F%2Fbitbucket.org%2Ffchampalimaud%2Fdownloads%2Fdownloads%2FHarp%2520Behavior%2520v2.0.0.zip&sa=D&sntz=1&usg=AOvVaw1HGd7wVYA0V_2_2wDvRWE7>`_

- Outputs: pulse duration, PWM (frequency and duty cycle)
- LEDs: RGB values, current, and maximum nominal current
- Extended features: cameras, servo motors, and quadrature counter
- Event firing on:  Digital DIs from Ports / Infrared beams from Pokes, Digital DIOs from Ports, Data (includes Analog Input and Encoder), When send a trigger to camera on DO 0, When send a trigger to camera on DO 1

.. raw:: html

    </div>
