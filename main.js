// Selectors ------------------------------------------------------------------------------------------------

function text_field(amr_id){
    return $("input[amr-id='" + amr_id + "']")
}

function amr_tok(amr_id, tok_id){
    return $("amr[amr-id='" + amr_id + "'] [tok-id='" + tok_id + "']")
}

function sent_tok(amr_id, tok_id){
    return $("sentence[amr-id='" + amr_id + "'] [tok-id='" + tok_id + "']")
}

function align_button(amr_id){
    return $("button.align[amr-id='"+amr_id+"']")
}

function color_button(amr_id, color_id){
    return $("button.color[amr-id='"+amr_id+"'][color-id='']")
}

function btn_group(amr_id){
    return $("div.btn-group[amr-id='" + amr_id + "']")
}

// Colors ---------------------------------------------------------------------------------------------------

function get_color(index) {
    colors = ["#abebc6", "#aed6f1", "#d7bde2", "#f9e79f", "#f5b7b1"];
    return colors[index % colors.length]
}

function reset_colors() {
    $("button.color").css('background-color', '#eee')
                     .attr('on', '0');
    $(".aligned").css('background-color', '')
                 .attr('on', '0');
}

function color_alignment(amr_id, alignment, color_id) {
	color = get_color(color_id);
    $(this).attr('on', '1')
           .css('background-color', color);
    // color elements
    for (let elem of parse_alignment(amr_id, alignment)) {
        elem.css('background-color', color);
    }
}

// Alignments ---------------------------------------------------------------------------------------------------

function parse_alignment(amr_id, alignment) {
    elements = [];
    align = alignment.split('~');
    // add amr elements
    amr_align = $.trim(align[0]).split(' ');
    for (let elem of amr_align) {
        if (elem) {
            tok_id = elem.replace(':', '');
            elements.push(amr_tok(amr_id,tok_id));
        }
    }
    // add sentence elements
    sent_align = $.trim(align[1]).split(' ');
    for (let elem of sent_align) {
        if (elem) {
            tok_id = elem;
            elements.push(sent_tok(amr_id,tok_id));
        }
    }
    return elements;
}

function add_alignment(amr_id, alignment) {
    text_field(amr_id).val("");
    if (alignment.includes('~')) {
        btngroup = btn_group(amr_id);
        color_id = btngroup.children().length + 1;
        button = '<button color-id="'+color_id+'" class="color" alignment="' + alignment + '" on="0">' + color_id + '</button>'
        b = $(button).on(
            {
                click: function(){
                    if($(this).attr('on') === '0'){
                        reset_colors();

                        color_alignment.bind($(this))(amr_id, alignment, color_id);
                    }
                    else {
                        reset_colors();
                    }
                },
                DOMNodeInserted: function(){
                    reset_colors();
                    color_alignment.bind($(this))(amr_id, alignment, color_id);
                },
                dblclick: function() {
                    $(this).remove();
                    reset_colors();
                }
            });
        btngroup.append(b);
    }
}

function select_element(amr_id, tok_id) {
    alignment = text_field(amr_id).val();
    if (alignment === "") {
        alignment = "~"
    }
    $(this).attr('on', '1');
    if ($(this).parents("amr").length>0) {
        alignment = alignment.replace('~', tok_id + ' ~')
    }
    else {
        alignment = alignment + ' ' + tok_id
    }
    reset_colors();
    text_field(amr_id).val(alignment);
    for (let elem of parse_alignment(amr_id, alignment)) {
        elem.css('background-color', '#eee');
        elem.attr('on', '1')
    }
}

function unselect_element(amr_id, tok_id) {
    alignment = text_field(amr_id).val();

    if ($(this).parents("amr").length>0) {
        amr_tok(amr_id, tok_id).attr('on', '0')
            .css('background-color', '#fff');
    }
    else {
        sent_tok(amr_id, tok_id).attr('on', '0')
            .css('background-color', '#fff');
    }
    aligns = alignment.split(' ');
    for (let i = 0; i < aligns.length; i++) {
        if (aligns[i] === tok_id) {
            aligns[i] = '';
            break;
        }
    }
    alignment = aligns.join(' ').replace('  ', ' ');
    text_field(amr_id).val(alignment);
}


$(document).ready(function () {
    $("input").val("");
    // Download button
    $("button.download").on("click", function(){
        aligns = {};
        $("amr").each(function(index){
            amr_id = $(this).attr("amr-id");
            aligns[amr_id] = [];
        });
        $("button.color").each(function( index ) {
            alignment = $(this).attr("alignment");
            amr_id = $(this).parents("[amr-id]").attr("amr-id");
            aligns[amr_id].push(alignment);
        });
        out = "";
        for (let amr_id in aligns){
            out += '#'+amr_id+'\n';
            out += aligns[amr_id].join('\n')+'\n';
            out += '\n';
        }
        var a = window.document.createElement('a');
        a.href = window.URL.createObjectURL(new Blob([out], {type: 'text/plain;charset=utf-8'}));
        a.download = 'amr-alignments.txt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    });
    // Show All button
    $("button.showall").on("click", function(){
        $("button.color").each(function( index ) {
            alignment = $(this).attr("alignment");
            color_id = $(this).attr("color-id");
            amr_id = $(this).parents("[amr-id]").attr("amr-id");
            color_alignment.bind($(this))(amr_id, alignment, color_id);
        });
    });
    // Add Alignment button
    $("button.align").on("click", function(){
        amr_id = $(this).attr("amr-id");
        alignment = text_field(amr_id).val();
        add_alignment(amr_id, alignment)
    });
    // elements in AMR or sentence
    $(".aligned").on({
        click: function(){
            amr_id = $(this).parents("[amr-id]").attr("amr-id");
            tok_id = $(this).attr("tok-id");

            if($(this).attr('on') === '0'){
                select_element.bind($(this))(amr_id, tok_id);
            }
            else {
                unselect_element.bind($(this))(amr_id, tok_id);
            }
        },
        dblclick: function(){
            amr_id = $(this).parents("[amr-id]").attr("amr-id");
            alignment = $("input[amr-id='" + amr_id + "']").val();
            tok_id = $(this).attr("tok-id");

            if($(this).attr('on') === '0'){
                select_element.bind($(this))(amr_id, tok_id);
            }
            add_alignment(amr_id, alignment);
        }
    }).attr("on", "0");
});


