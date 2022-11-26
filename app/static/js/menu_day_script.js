function current_day(){
    var date = new Date(new Date());
    return date.toLocaleDateString("en", { weekday: 'long' });  
}

function expand_current_day(){
    var day = current_day()
    var body =document.getElementById(day) 
    body.classList.add("active-day");
    
}

function clicked_day_check(day){
    remove_active_day()
    var day_box = document.getElementById(day) 
    day_box.classList.add("active-day");
}

function remove_active_day(){
    var day_arr = document.getElementsByClassName("active-day")
    Array.from(day_arr).forEach((day_arr) => {
        day_arr.classList.remove("active-day")
    })
}

expand_current_day()