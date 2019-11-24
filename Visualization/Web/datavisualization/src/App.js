import React, { useEffect, useState } from 'react';
import './App.css';
import Chart from "react-apexcharts";


function App() {
  let XAXISRANGE = 4
  const optionsGraphAcc = {
    chart: {
      id: 'realtime',
      animations: {
        enabled: true,
        easing: 'linear',
        dynamicAnimation: {
          speed: 2000
        }
      },
      toolbar: {
        show: false
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },

    title: {
      text: 'Acceleration',
      align: 'left'
    },
    markers: {
      size: 0
    },
    xaxis: {
      type: 'datetime',
      range: XAXISRANGE,
    },
    yaxis: {
      max: 25000
    },
    legend: {
      show: false
    }
  }

  const optionsGraphGyro = {
    chart: {
      id: 'realtime',
      animations: {
        enabled: true,
        easing: 'linear',
        dynamicAnimation: {
          speed: 2000
        }
      },
      toolbar: {
        show: false
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },

    title: {
      text: 'Gyro',
      align: 'left'
    },
    markers: {
      size: 0
    },
    xaxis: {
      type: 'datetime',
      range: XAXISRANGE,
    },
    yaxis: {
      max: 35000
    },
    legend: {
      show: false
    }
  }

  const optionsGraphTempt = {
    chart: {
      id: 'realtime',
      animations: {
        enabled: true,
        easing: 'linear',
        dynamicAnimation: {
          speed: 2000
        }
      },
      toolbar: {
        show: false
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },

    title: {
      text: 'Temperature',
      align: 'left'
    },
    markers: {
      size: 0
    },
    xaxis: {
      type: 'datetime',
      range: XAXISRANGE,
    },
    yaxis: {
      max: 25000
    },
    legend: {
      show: false
    }
  }

  // const [data, setData] = useState([]);
  const [accelerationX, setAccelerationX] = useState([{}]);
  const [temperature, setTemperature] = useState([{}]);
  const [GyroX, setGyro] = useState([{}]);

  const options = {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json;charset=UTF-8'
    }
  };

  function _parseJSON(response) {
    return response.text().then(function (text) {
      try {
        return text ? JSON.parse(text) : {}
      }
      catch (e) {
        return {}
      }
    })
  }


  useEffect(() => {
    try {

      fetch('http://localhost:8000', options)
        .then(function (response) {
          console.log("fetch")
          return _parseJSON(response)
        }).then(function (data) {
          if (data !== {} && data !== undefined) {
            var array = []
            var arrayy = []
            var arrayz = []
            var arraya = []
            var arrayb = []
            var arrayc = []
            var temperature = []
            try {
              for (var i = 0; i < data['raw_data'].length; i++) {
                array.push({ x: data['raw_data'][i][0], y: data['raw_data'][i][1] })
                arrayy.push({ x: data['raw_data'][i][0], y: data['raw_data'][i][2] })
                arrayz.push({ x: data['raw_data'][i][0], y: data['raw_data'][i][3] })

                temperature.push({ x: data['raw_data'][i][0], y: data['raw_data'][i][4] })

                arraya.push({ x: data['raw_data'][i][0], y: data['raw_data'][i][5] })
                arrayb.push({ x: data['raw_data'][i][0], y: data['raw_data'][i][6] })
                arrayc.push({ x: data['raw_data'][i][0], y: data['raw_data'][i][7] })

              }
              setTimeout(function () { //Start the timer

                setAccelerationX([{ data: array }, { data: arrayy }, { data: arrayz }]);
                setTemperature([{ data: temperature }])
                setGyro([{ data: arraya }, { data: arrayb }, { data: array }])
              }, 900)


              if (accelerationX[0]['data'] !== undefined)
                console.log(accelerationX[0]['data'].length)
            } catch (e) {
              setAccelerationX([{ data: accelerationX[0]['data'] }, { data: accelerationX[1]['data'] }, { data: accelerationX[2]['data'] }])
              setTemperature([{ data: temperature }])
            }

          }
          else {
            setAccelerationX([{ data: accelerationX[0]['data'] }, { data: accelerationX[1]['data'] }, { data: accelerationX[2]['data'] }])
            setTemperature([{ data: temperature[0]['data'] }])
            setGyro([{ data: GyroX[0]['data'] }, { data: GyroX[1]['data'] }, { data: GyroX[2]['data'] }])
          }
        });

    } catch (e) {
      setAccelerationX([{ data: accelerationX[0]['data'] }, { data: accelerationX[1]['data'] }, { data: accelerationX[2]['data'] }])
      setTemperature([{ data: temperature[1]['data'] }])
      setGyro([{ data: GyroX[0]['data'] }, { data: GyroX[1]['data'] }, { data: GyroX[2]['data'] }])
    }
  })




  return (
    <div>
      <div id="chart">
        <Chart options={optionsGraphAcc} series={accelerationX} type="line" height="350" />
      </div>
      <div id="chart">
        <Chart options={optionsGraphTempt} series={temperature} type="line" height="350" />
      </div>
      <div id="chart">
        <Chart options={optionsGraphGyro} series={GyroX} type="line" height="350" />
      </div>
    </div>
  );
}

export default App;
