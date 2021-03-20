const text_area = document.getElementById("paragraph");
const count_value = document.getElementById("count_value");

text_area.oninput = _=>{ 
    if (text_area.value.trim() == ""){
        var words_count = 0;
    }
    else{
        var words_count = text_area.value.trim().split(/\s+/).length;
        // var words_count = text_area.value.trim().split(' ').filter((ele)=>{return ele != "";}).length
    }
    count_value.innerText = words_count; 
}