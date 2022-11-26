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

function menu_id(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const menuid =  urlParams.get('menuid')
    return menuid
}

function set_menu_planner_link(){
    var link = document.getElementById("menu-planner-link")
    li = "/menu/menu-planner?menuid=" + menu_id() + "&wdc=none"
    link.href = li
}

expand_current_day()
set_menu_planner_link()