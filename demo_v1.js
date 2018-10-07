
function get_color(index){
	colors = ["#abebc6", "#aed6f1", "#d7bde2", "#f5b7b1", "#f9e79f"]
	return colors[index%colors.length]
}

function get_div_id(elem){
	var x = $(elem).parents("div.aligner");
	return x.attr("id")
}

function reset_colors(){
	$("button.color").css('background-color','#eee');
	$("button.color").attr('on','0');
	$(".aligned").css('background-color','');
    $(".aligned").attr('on','0');
}

function parse_alignment(align){
	elements = []
	// add amr elements
	amr_align = $.trim(align.split('~')[0]).split(' ')
	for (let elem of amr_align) {
		if (elem.length>0) {
			elements.push($("amr."+div_id+" ."+elem.replace(':','')));
		}
	}
	// add sentence elements
	sent_align = $.trim(align.split('~')[1]).split(' ')
	for (let elem of sent_align) {
		if (elem.length>0) {
			elements.push($("sentence."+div_id+" word."+elem));
		}
	}
	return elements;
}

function align_button(){
	div_id = get_div_id(this);
	alignment = $("input."+div_id).val();
	$("input."+div_id).val("");
	if (alignment.includes('~')){
		i = $("div#"+div_id+" .btn-group").children().length + 1;
		var b = $('<button color_id="'+i+'" class="color" alignment="'+alignment+'" on="0">'+i+'</button>').on(
			{click: color_button2, DOMNodeInserted: color_button1});
		$("div#"+div_id+" .btn-group").append(b);
	}
}

function color_button1(){
	div_id = get_div_id(this);
	color_id = $(this).attr('color_id');
	alignment = $(this).attr('alignment');
	// color button
	color = get_color(color_id);
	reset_colors();
	$(this).attr('on', '1');
	$(this).css('background-color', color);
	// color elements
	for (let elem of parse_alignment(alignment)){
		elem.css('background-color', color);
	}
}	

function color_button2(){
	div_id = get_div_id(this);
	color_id = $(this).attr('color_id');
	alignment = $(this).attr('alignment');
	// color button
	color = get_color(color_id);
	if ($(this).attr('on')=='1') {
		reset_colors();
	}
	else {
		reset_colors();
		$(this).attr('on', '1');
		$(this).css('background-color', color);
		// color elements
		for (let elem of parse_alignment(alignment)){
			elem.css('background-color', color);
		}
	}
}	

function click_element(){
	element_id = $(this).attr('class').replace('aligned ','');
	div_id = get_div_id(this);
	alignment = $("input."+div_id).val();
	if (alignment=="") {
		alignment = "~"
	}
	if ($(this).attr('on')=='1') {
		$(this).attr('on','0');
		aligns = alignment.replace('~',' ~ ').split(' ');
		for (let i=0; i<aligns.length; i++){
			if (aligns[i]==element_id){
				aligns[i] = '';
				break;
			}
		}
		alignment = aligns.join(' ').replace('  ', ' ');
		$("input."+div_id).val(alignment)
	}
	else{
		$(this).attr('on','1')
		if ($(this).parent().parent().is('amr')){
			$("input."+div_id).val(alignment.replace('~',element_id+' ~'))
		}
		else {
			$("input."+div_id).val(alignment+' '+element_id)
		}
	}
	reset_colors();
	alignment = $("input."+div_id).val();
	for (let elem of parse_alignment(alignment)){
		elem.css('background-color', '#eee');
		elem.attr('on','1')
	}
}

$(document).ready(function(){
	$("button.align").on("click", align_button);
	$(".aligned").on("click", click_element);
	$("input").val("");
	$(".aligned").attr("on","0");
});
