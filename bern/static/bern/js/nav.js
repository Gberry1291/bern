var startpat=window.location.href
let pattern=/\S*\/\/\S+?(?=\/)/
var extension=startpat.match(pattern)[0];
var newreq=""
var whattosend=""
var path=""
const csrftoken = getCookie('csrftoken');
function setreq(){
  newreq = new Request(
      path,
      {
          method: 'POST',
          headers: {'X-CSRFToken': csrftoken},
          mode: 'same-origin', // Do not send CSRF token to another domain.
          body: whattosend
      }
  );
}
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";"+"SameSite=None; Secure";
}
