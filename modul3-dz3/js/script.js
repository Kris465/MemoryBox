pole.addEventListener("click", function (e) {
    let poleGeo = pole.getBoundingClientRect();
  
    let myachGeo = {
      top: e.clientY - poleGeo.top - myach.clientHeight / 2,
      left: e.clientX - poleGeo.left - myach.clientWidth / 2,
    };
  
    myach.style.left = myachGeo.left + "px";
    myach.style.top = myachGeo.top + "px";
  });