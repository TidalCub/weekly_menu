function week_number(){
    currentDate = new Date();
    startDate = new Date(currentDate.getFullYear(), 0, 1);
    var days = Math.floor((currentDate - startDate) /
        (24 * 60 * 60 * 1000));
          
    var weekNumber = Math.ceil(days / 7);
    return weekNumber
}

function url_args(){
    var url = url.href
    console.log(url)
}
console.log(week_number())

window.onload = url_args() 