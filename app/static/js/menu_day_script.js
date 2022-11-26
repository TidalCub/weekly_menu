function current_day(){
    var date = new Date(new Date());
    return date.toLocaleDateString("en", { weekday: 'long' });  
}

console.log(current_day())