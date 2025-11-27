let msgCount = false;

function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    let msg = "";
    let am_pm = "AM";

    // Setting time for 12 Hrs format
    if (h >= 12) {
        if (h > 12) h -= 12;
        am_pm = "PM";
    } else if (h == 0) {
        h = 12;
        am_pm = "AM";
    }
    h = checkTime(h);
    m = checkTime(m);
    s = checkTime(s);

    if (h < 12 && am_pm == "AM") {
        msg = "Good Morning, ";
    }
    if (h >= 1 && h < 4 && am_pm == "PM") {
        msg = "Good Afternoon, ";
    }
    if (h >= 5 && am_pm == "PM") {
        msg = "Good Evening, ";
    }

    if (!msgCount) {
        addGreetings(msg);
        msgCount = true;
    }

    document.getElementById('time').innerHTML = h + ":" + m + ":" + s + " " + am_pm;
    setTimeout(startTime, 1000);
}

function addGreetings(msg) {
    let x = document.getElementById('ttl').innerHTML;
    document.getElementById('ttl').innerHTML = msg + x;
}

function checkTime(i) {
    if (i < 10) { i = "0" + i };  // add zero in front of numbers < 10
    return i;
}