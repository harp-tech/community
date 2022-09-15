.. _synchronizer:

*************************************************
Synchronizer
*************************************************

.. raw:: html

      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card card-body border-light" >
            <div class="deviceDescription">Used to synchronize and align the different apparatus and devices present in a complex setup.
 
 It timestamps each rising or falling edge of the 9 digital input signals. The sampling of the inputs can also be configured to use a ﬁxed sampling frequency.
            </div>
          </div>
        </div>

        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 d-flex">
          <div class="card border-light" style = "text-align: center">
            <img class="card-img-top" src="../../_static/images/devices/synchronizer.png" alt = "Photo of device Synchronizer" style="margin: 0 auto; width: 75%">
            
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
Receives and timestamps up to 9 digital input signals
 
 Sampling on signal transitions or fixed sampling frequency up to 2 KHz

Use Cases
******************************************
Setups requiring signal alignment

Connectivity
******************************************
- 1x clock sync input (CLKIN) [stereo jack]
 - 1x USB (for computer) [USB type B]
 - 9x digital inputs (DIN0 to DIN5) [BNC], (DIN6 to DIN8) [screw terminal]
 - 1x digital output (DOUT0) [screw terminal]

Software Configuration Options
******************************************
`Download software here: <https://bitbucket.org/fchampalimaud/downloads/downloads/Harp%20Synchronizer%20v1.2.0.zip>`_

- Input read trigger: SW only, any input changes, Rise/Fall edge of DIN0, Frequency of 100, 250, 500, 1000, or 2000 Hz
 - Output Pin Mode: toggle when a read occur, equal to DIN0, pulses of 1, 2, or 5 ms, pulses of 250, or 500 us

.. raw:: html

    </div>
