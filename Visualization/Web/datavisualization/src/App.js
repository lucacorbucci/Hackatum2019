import React, { useEffect, useState } from 'react';
import './App.css';
import Chart from "react-apexcharts";


function App() {
  let XAXISRANGE = 4
  const optionsGraph = {
    chart: {
      id: 'realtime',
      animations: {
        enabled: true,
        easing: 'linear',
        dynamicAnimation: {
          speed: 4000
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
      text: 'Dynamic Updating Chart',
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
      setInterval(() => {

        fetch('http://localhost:8000', options)
          .then(function (response) {
            return _parseJSON(response)
          }).then(function (data) {
            if (data !== {}) {
              var array = []
              for (var i = 0; i < data['raw_data'].length; i++) {
                array.push({ x: data['raw_data'][i][0], y: data['raw_data'][i][1] })
              }
              var n = array.length
              if (100 > n)
                setAccelerationX([{ data: array.slice(0, n) }]);
              else
                setAccelerationX([{ data: array.slice(n - 100, n) }]);

              if (accelerationX[0]['data'] !== undefined)
                console.log(accelerationX[0]['data'].length)
            }

          });

      }, 4000);
    } catch (e) {
      console.log(e);
    }
  })




  return (
    <div>
      <div id="chart">
        <Chart options={optionsGraph} series={accelerationX} type="line" height="350" />
      </div>
    </div>
  );
}

export default App;
