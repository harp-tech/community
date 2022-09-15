.. _pwmGenerator:

*************************************************
Multi PWM generator
*************************************************

.. raw:: html

      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card card-body border-light" >
            <div class="deviceDescription">This board provides 4 independent PWM outputs that can be triggered by four different input triggers or all at the same time. Also four output synchronization signals are available. The PWM signal generation is configured in software.
            </div>
          </div>
        </div>

        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card border-light" style = "text-align: center">
            <img class="card-img-top" src="../../_static/images/devices/pwmGenerator.png" alt = "Photo of device Multi PWM generator" style="margin: 0 auto; width: 75%">
            
                    <a href="REPOLINK">
        <button class = "button repo">
        <i class="fab fa-bitbucket"></i> Design Files
        </button>
        </a>

          </div>
        </div>
      </div>

      <div class="deviceFeatures">

Key Features
******************************************
- PWM output generation
- Configurable frequency and duty cycle
- Frequency up to 32 KHz
- Enabling mechanisms by software or hardware to prevent erroneous triggerings
- Start and stop triggers (also by software)
- Infinite or configured number of pulses
- Complete trigger mechanisms

Use Cases
******************************************
- Camera triggering
- Laser control

Connectivity
******************************************
- 1x clock sync input (CLKIN) [stereo jack]
- 1x USB (for computer) [USB type B]
- 1x 12V supply [barrel connector jack]
- 5x Digital input triggers: CH0 to CH3, ALL [BNC]
- 4x Digital output PWM signals: CH0 to CH3 [BNC]
- 5x Digital output sync signals: CH0 to CH3, ALL [BNC]

Software Configuration Options
******************************************
`Download software here: <https://www.google.com/url?q=https%3A%2F%2Fbitbucket.org%2Ffchampalimaud%2Fdownloads%2Fdownloads%2FHarp%2520Multi%2520Pwm%2520Generator%2520v2.1.0.zip&sa=D&sntz=1&usg=AOvVaw2Wg0b379x9WilnpYdOI8wc>`_

- PWM outputs: Frequency, duty cycle, number of pulses, Mode (count pulses or infinite)
- Triggers: mask and mode (start or start and stop)
- Event firing on: start and stop of each PWM burst

.. raw:: html

    </div>
