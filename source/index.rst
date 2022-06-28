:notoc:

.. image:: _static/images/harplogo.png
  :scale: 30%
  :align: center

**Date**: |today|


.. raw:: html

  <div class="row">
    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex" style="margin-top: 0em!important">
      <div class="card border-light">


Neuroscience experiments often rely on multiple parallel datastreams, acquired from different devices at different frequencies. As setups increase in complexity, temporally aligning these datastreams  rapidly becomes more difficult.

|

Harp is a family of devices that configure, control, & track a wide range of peripheral devices such as cameras, LEDs, nosepokes, & motors. Combining Harp devices is an easy way to extend experimental setup functionality with integrated timestamp synchronisation across devices.

:ref:`More about why Harp was developed <whyharp>`

|

See here for a list of existing devices. Don't see what you're looking for? Harp protocols were designed so that new devices can be developed that will interact seamlessly with existing tools.

:ref:`More about Harp protocols <refprotocols>`

.. raw:: html

      </div>
    </div>
    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex" style="margin-top: 0em!important">
      <div class="card border-light">
      <img class="card-img-top" src="_static/images/devices/behaviour_peripherals.jpg" style="align: right; scale: 30%">
      </div>
    </div>
  </div>

.. raw:: html

  <div class="row">
    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex" style="margin-top: 0em!important">
      <div class="card border-light">
        <h5 class="card-title text-center">Using Harp Devices</h5>
        <img class="card-img-top" src="_static/images/harp_features_overview.png" alt="Infographic showcasing HARP" style="margin: auto">
      </div>
    </div>
    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 d-flex" style="margin-top: 0em!important">
      <div class="card border-light">
      <h5 class="card-title text-center">Key Specifications</h5>
        <div class="card-body" >
          <p class="card-text">

**Communication protocol and architecture standardized across devices**

  *Streamlined communication when adding new devices to setup, and reduces time and effort of developing new devices*
**Integrated hardware synchronization**

  *Eliminates need for extra inter-device synchronization TTLs or post-hoc timestamp alignment*
**Intuitive graphical tools for device configuration**

  *Easy to choose the settings your setup requires*
**Event-based protocol**

  *Smaller file sizes as data is transmitted when changes occur, rather than at set frequencies like in traditional hardware*

**Bonsai, Matlab, LabVIEW, and Python compatible**

  *Easily integrate synchronized data into existing analysis pipelines*


.. raw:: html

            </div>
          </div>
        </div>
      </div>


.. raw:: html

    <h2 style = "text-align: center"> Getting Started </h2>

    <div class="container">
      <div class="row row-cols-lg-3 row-cols-md-3 row-cols-sm-1 row-cols-xs-1">
        <div class="col mb-4">
          <div class="card h-100 text-center intro-card shadow">
            <a href = "Devices/device_list.html">
              <img src="_static/images/noun_macbook.svg" class="card-img-top" height="160">
              <div class="card-body flex-fill">
                <p class="card-reference">Harp device list</p>
              </div>
            </a>
          </div>
        </div>
        <div class="col mb-4">
          <div class="card h-100 text-center intro-card shadow">
            <a href = About/Using-HARP/index.html>
              <img src="_static/images/noun_screwdriver.svg" class="card-img-top" height="160">
              <div class="card-body flex-fill">
                <p class="card-reference">How Harp works</p>
              </div>
            </a>
          </div>
        </div>
        <div class="col mb-4">
          <div class="card h-100 text-center intro-card shadow">
            <a href = About/How-HARP-works/index.html>
              <img src="_static/images/noun_books.svg" class="card-img-top" height="160">
              <div class="card-body flex-fill">
                <p class="card-reference">Harp Protocols</p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>

License
#################################################

This work is licensed under CC BY-SA 4.0.

To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/

.. toctree::
    :hidden:
    :titlesonly:

    About/index
    Devices/device_list
    About/Using-HARP/index
    About/How-HARP-works/index
