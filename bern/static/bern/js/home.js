document.getElementById("switchevent").addEventListener("click",function(){
  document.getElementById("switchhouse").classList.toggle("houseon")
  document.getElementById("switch").classList.toggle("switchoff")
})


document.getElementById("subbutton").addEventListener("click",senddata)
function senddata(){

  let daydic={
    "name":document.getElementById("nameinput").value,
    "patientname":document.getElementById("patientname").value,
    "patientage":document.getElementById("patientage").value,
    "patientdes":document.getElementById("patientdes").value,
  }

  path=extension+"/"
  whattosend=JSON.stringify(daydic)

  setreq()
  fetch(newreq).then(function(response) {
    return response.json()
  }).then(function(x) {
    alert(x["message"])
  });
}
