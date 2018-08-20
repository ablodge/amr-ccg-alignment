
function color(index){
	colors = ["#abebc6", "#aed6f1", "#d7bde2", "#f5b7b1", "#f9e79f"]
	return colors[index%colors.length]
}

$(document).ready(function(){
//    $(".sentence").click(function(){
//        id = $(this).attr('id')
//        $(".amr-"+id).toggle();
//    });
    $("button").click(function(){
		clr = $(this).attr('id');
		id = $(this).attr('class').replace('button-','tok-');
		sent_id = id.split('-')[1]
		$(".tok").css('background-color',"white");
		$("button").css('background-color','#eee')
		$(this).css('background-color',color(clr));
        $("span."+id).css('background-color',color(clr));
    });
});