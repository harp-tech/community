*************************************************
Device List
*************************************************

.. raw:: html

    <body>

    <div id="myBtnContainer">
      <button class="btn clicked" onclick="filterSelection('all')"> Show all</button>
          <button class="btn" onclick="filterSelection('Digital Interface')">Digital Interface</button>
    <button class="btn" onclick="filterSelection('Sound')">Sound</button>
    <button class="btn" onclick="filterSelection('Sensor Interface')">Sensor Interface</button>
    <button class="btn" onclick="filterSelection('Poke')">Poke</button>
    <button class="btn" onclick="filterSelection('Multipurpose')">Multipurpose</button>
    <button class="btn" onclick="filterSelection('Analog Interface')">Analog Interface</button>
    <button class="btn" onclick="filterSelection('Timestamp Generators')">Timestamp Generators</button>

    </div>

    <div class="container">

      <div class="row row-cols-1 row-cols-md-3 g-4">

          <div class="col filterDiv Multipurpose">
      <div class="card device h-100">
        <a href = alldevices/behaviorDevice.html>
        <img src="../_static/images/devices/behaviorDevice.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Behavior</h5>
          <p class="card-text">At the heart of a behavioural setup, this device is used to configure and track peripherals such as pokes, LEDs, motors, cameras etc. </p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sensor Interface">
      <div class="card device h-100">
        <a href = alldevices/wearBasestation.html>
        <img src="../_static/images/devices/wearBasestation.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">WEAR Basestation</h5>
          <p class="card-text">This device is the basestation for the Wired and Wireless sensor devices. The devices can be configured using the Harp Wear software.</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Digital Interface">
      <div class="card device h-100">
        <a href = alldevices/cameraTriggerControl.html>
        <img src="../_static/images/devices/cameraTriggerControl.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Camera trigger control</h5>
          <p class="card-text">Allows up to 2 cameras to be triggered at a predefined frequency</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sensor Interface">
      <div class="card device h-100">
        <a href = alldevices/RFIDreader.html>
        <img src="../_static/images/devices/RFIDreader.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">RFID Reader</h5>
          <p class="card-text"></p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sensor Interface">
      <div class="card device h-100">
        <a href = alldevices/wearWirelessSensor.html>
        <img src="../_static/images/devices/wearWirelessSensor.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Wear Wireless Motion Sensor</h5>
          <p class="card-text">Wireless low weight 9-axis motion sensor</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sensor Interface">
      <div class="card device h-100">
        <a href = alldevices/loadCellsReader.html>
        <img src="../_static/images/devices/loadCellsReader.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Load Cells Reader</h5>
          <p class="card-text">Analog interface for 4 load cells sensors</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sensor Interface">
      <div class="card device h-100">
        <a href = alldevices/loadCellsInterface.html>
        <img src="../_static/images/devices/loadCellsInterface.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Load Cells Interface</h5>
          <p class="card-text">Board for interfacing with up two load cells boards</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sensor Interface">
      <div class="card device h-100">
        <a href = alldevices/LEDArrayInterface.html>
        <img src="../_static/images/devices/LEDArrayInterface.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">LED Array Interface</h5>
          <p class="card-text">LED array controller for optostimulation experiments</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sensor Interface">
      <div class="card device h-100">
        <a href = alldevices/RGBController.html>
        <img src="../_static/images/devices/RGBController.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">RGB Controller</h5>
          <p class="card-text">Strips of RGB LEDs (up tp 32) can be controlled with this board</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sensor Interface">
      <div class="card device h-100">
        <a href = alldevices/syringePump.html>
        <img src="../_static/images/devices/syringePump.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Syringe Pump</h5>
          <p class="card-text"></p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sound">
      <div class="card device h-100">
        <a href = alldevices/audioSwitch.html>
        <img src="../_static/images/devices/audioSwitch.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Audio Switch</h5>
          <p class="card-text">Configurable multiple audio switch</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sound">
      <div class="card device h-100">
        <a href = alldevices/soundBoard.html>
        <img src="../_static/images/devices/soundBoard.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Sound Board</h5>
          <p class="card-text">High performance sound card</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Sound">
      <div class="card device h-100">
        <a href = alldevices/audioAmplifier.html>
        <img src="../_static/images/devices/audioAmplifier.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Audio Amplifier</h5>
          <p class="card-text">High bandwidth audio amplifier with low distortion and no signal loss over frequency</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Analog Interface">
      <div class="card device h-100">
        <a href = alldevices/analogInput.html>
        <img src="../_static/images/devices/analogInput.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Analog Input</h5>
          <p class="card-text">Multiple analog input converter board</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Digital Interface">
      <div class="card device h-100">
        <a href = alldevices/pwmGenerator.html>
        <img src="../_static/images/devices/pwmGenerator.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Multi PWM generator</h5>
          <p class="card-text">This board provides 4 independent PWM outputs that can be triggered by four different input triggers or all at the same time.</p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Digital Interface">
      <div class="card device h-100">
        <a href = alldevices/synchronizer.html>
        <img src="../_static/images/devices/synchronizer.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Synchronizer</h5>
          <p class="card-text"></p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Digital Interface">
      <div class="card device h-100">
        <a href = alldevices/inputExpander.html>
        <img src="../_static/images/devices/inputExpander.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Input Expander</h5>
          <p class="card-text"></p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Digital Interface">
      <div class="card device h-100">
        <a href = alldevices/outputExpander.html>
        <img src="../_static/images/devices/outputExpander.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Output Expander</h5>
          <p class="card-text"></p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Multipurpose">
      <div class="card device h-100">
        <a href = alldevices/ibldevice.html>
        <img src="../_static/images/devices/ibldevice.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">IBL Behavior Control</h5>
          <p class="card-text"></p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Timestamp Generators">
      <div class="card device h-100">
        <a href = alldevices/clockSynchronizer.html>
        <img src="../_static/images/devices/clockSynchronizer.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">Clock synchronizer</h5>
          <p class="card-text"></p>
        </div>
       </a>
      </div>
    </div>
    <div class="col filterDiv Digital Interface Poke">
      <div class="card device h-100">
        <a href = alldevices/testDevice.html>
        <img src="../_static/images/devices/testDevice.png" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">test device</h5>
          <p class="card-text"></p>
        </div>
       </a>
      </div>
    </div>



      </div>
    </div>

    <script>
    filterSelection("all")
    function filterSelection(c) {
      var x, i;
      x = document.getElementsByClassName("filterDiv");
      if (c == "all") c = "";
      for (i = 0; i < x.length; i++) {
        w3RemoveClass(x[i], "show");
        if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
      }
    }

    function w3AddClass(element, name) {
      var i, arr1, arr2;
      arr1 = element.className.split(" ");
      arr2 = name.split(" ");
      for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
      }
    }

    function w3RemoveClass(element, name) {
      var i, arr1, arr2;
      arr1 = element.className.split(" ");
      arr2 = name.split(" ");
      for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
          arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
      }
      element.className = arr1.join(" ");
    }

    // Add active class to the current button (highlight it)
    var btnContainer = document.getElementById("myBtnContainer");
    var btns = btnContainer.getElementsByClassName("btn");
    for (var i = 0; i < btns.length; i++) {
      btns[i].addEventListener("click", function(){
        var current = document.getElementsByClassName("clicked");
        current[0].className = current[0].className.replace(" clicked", "");
        this.className += " clicked";
      });
    }
    </script>

    </body>
    </html>
