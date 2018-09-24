document.onreadystatechange = () => {
  if (document.readyState === 'complete') {
    var countDownDate = new Date("November 24, 2018 23:23:59").getTime();
    var x = setInterval(function() {
    var now = new Date().getTime();
    var distance = countDownDate - now;
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    if (days<0) {
      var textcount = "SEE THE SCHEDULE!";
    }
    else if (days==0) { 
      if (hours==0) {
        if (minutes==0) {
          var textcount = "ONLY "+seconds+" SECONDS LEFT!";
        }
        else{
          var textcount = "ONLY "+minutes+" MINUTES LEFT!";
        }
      }
      else{
        var textcount = "ONLY "+hours+" HOURS LEFT!";
      }
    }
    else{
      var textcount = "ONLY "+days+" DAYS LEFT!";
    }
    document.getElementById("countdown").innerHTML = textcount;
    }, 1000);
  }
};
