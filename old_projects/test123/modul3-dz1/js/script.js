inputname.addEventListener("input", function (e) {
    let alphavit = /[A-Za-zА-Яа-яЁё -]/;
    let simbols = e.target.value.split("");
    let simb = simbols.pop();
    if (!alphavit.test(simb)) {
      e.target.value = simbols.join("");
    }
  });