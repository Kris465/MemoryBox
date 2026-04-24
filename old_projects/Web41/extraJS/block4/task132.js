function isTrainAtPlatform(a, b, c, d, n, m) {
    const arrival = a * 60 + b;
    const departure = c * 60 + d;
    const passenger = n * 60 + m;
  
    return passenger >= arrival && passenger <= departure;
  }
  
  const a = 10; 
  const b = 30; 
  const c = 11;
  const d = 15; 
  const n = 10; 
  const m = 45; 
  
  if (isTrainAtPlatform(a, b, c, d, n, m)) {
    console.log("Поезд стоит на платформе.");
  } else {
    console.log("Поезда нет на платформе.");
  }