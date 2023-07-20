
d3.json("/get-data").then(
  function(d){
    console.log(d);
    document.getElementById("d3-write-here").innerHTML = d;
  })
    

  
// function metaTable(sample) {
//     //  git the url from api 
//     d3.json("http/localhost:5000/electric_cars").then((data) => {
//       console.log(data)
//       let metadata = data.metadata;
//       console.log(metadata);
//       let metaArry = metadata.filter(sampleObj => sampleObj.id == sample)
//       let metaResult = metaArry[0]
  
//       let metaTableData = d3.select("#sample-metadata")
//       metaTableData.html("")
//       for (key in metaResult) {
//         metaTableData.append('h6').text(`${key.toUpperCase()}: ${metaResult[key]}`)
//       }
//     })
//   }

// // get how many cars
// car.length;
// ///loob and print ou all the prices of cars
    
   
    