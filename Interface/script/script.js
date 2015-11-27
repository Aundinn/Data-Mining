function year(){
    var d = document.articles.year;
    for(var i=2000; i <= 2015 ; i++)
    {  
        d.length++;
        d.options[d.length-1].text = i;
    }
}