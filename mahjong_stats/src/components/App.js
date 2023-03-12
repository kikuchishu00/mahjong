import React, {useState, useEffect} from 'react';
import axios from "axios";
import {  Line } from 'react-chartjs-2';
import { Chart, registerables } from "chart.js"
Chart.register(...registerables)

export default function Graph(){
  const [stats, setStats] = useState([]);
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/stats')
    .then(res => {
        setStats(res.data)
    })
    },[]);
  const statslength = stats.length;
  for(let i=0;i<statslength;i++){
    stats[i].id=i;
  };
  function MakeTotalArray(stats){
    TotalArray=[];
    for(let i=0;i<statslength;i++){
      if(i==0){
        TotalArray.push(Number(stats[i].points));
      } else{
        var last = TotalArray[TotalArray.length-1];
        TotalArray.push(Number(stats[i].points)+last);
      };
    };
    return TotalArray;
  };
  function HandlePointsChange(e,num) {
    setStats((stats) =>
    stats.map((obj) => (obj.id === num ? { id: num, points: e.target.value,date:obj.date } : obj))
    );
  };

  function MakeDateArray(stats){
    DateArray=[];
    for(let i=0;i<statslength;i++){
      DateArray.push(stats[i].date);
    };
    return DateArray;
  };
  let DateArray = MakeDateArray(stats);
  let TotalArray = MakeTotalArray(stats)
  const data={
    labels:DateArray,
    datasets:[{
      label: "totalpoint",
      data:TotalArray,
    },
   ],
  };

  return(
    <>
    <div >
      {stats.map((data) => (
            <label className="form">
            date:{data.date} / point:
            <input
              value={data.points}
              onChange={e=>HandlePointsChange(e,data.id)}
            />
          </label>
        ))}
    </div>
    <div>
    <Line data={data}/>
    </div>
    </>
  );
}

