
// Colors ---------------------------------------------------------------------------------------------------

function get_color(index) {
    colors = ["#abebc6", "#aed6f1", "#d7bde2", "#f9e79f", "#f5b7b1"];
    return colors[index % colors.length]
}

function reset_colors() {
    $("button.reactive-onoff").css('background-color', '#eee')
                     .attr('on', '0');
    $(".aligned").css({'background': '', 'border': ''})
                 .attr({'on': '0', 'colors':'0'});
}

// Alignments --------------------------------------------------------------------------------------------------------

function add_alignment(amr_id, alignment) {
    let amr_align = new AMR_Alignment(amr_id,alignment);
    let cmd_line = new CmdLine(`input:text[amr-id='${amr_id}']`);
    cmd_line.clear();

    if (amr_align.test()) {
        let btngroup = $(`.btn-group[amr-id='${amr_id}']`);
        let color_id = (btngroup.children().length!==0) ?
            (parseInt(btngroup.children().last().attr('color-id'))+1).toString() : 1;
        let color = get_color(color_id);

        let on_behavior = function(){
            reset_colors();
            amr_align.color(color);
        };
        let off_behavior = function(){
            reset_colors();
        };
        btngroup.append(OnOffButton.create(color_id));
        let b = btngroup.children().last();
        let onoff = new OnOffButton(b,
            on_behavior,
            off_behavior,
            {'on' : color}
        );
        onoff.select().attr({
            'alignment': alignment,
            'color-id':color_id,
            'amr-id': amr_id
        });

        onoff.select().on({
            click: function(){onoff.flip()},
            dblclick: function() {
                $(this).remove();
                reset_colors();
            }
        });
        onoff.turn_on();
    }
}

function select_element() {
    let amr_id = $(this).parents("[amr-id]").first().attr("amr-id");
    let tok_id = $(this).attr("tok-id");

    let cmd_line = new CmdLine(`input:text[amr-id='${amr_id}']`);
    let alignment = cmd_line.get();
    let amr_alignment = new AMR_Alignment(amr_id, alignment);

    $(this).attr('on', '1');
    if ($(this).parents("amr").length>0)
        alignment = amr_alignment.add_right(tok_id);
    else
        alignment = amr_alignment.add_left(tok_id);

    reset_colors();
    cmd_line.set(alignment);
    amr_alignment = new AMR_Alignment(amr_id,alignment);
    for (let elem of amr_alignment.parse()) {
        $(elem).attr('on', '1')
            .css('background-color', '#eee');
    }
}

function unselect_element() {
    let amr_id = $(this).parents("[amr-id]").first().attr("amr-id");
    let tok_id = $(this).attr("tok-id");

    let cmd_line = new CmdLine(`input:text[amr-id='${amr_id}']`);
    let alignment = cmd_line.get();
    let amr_alignment = new AMR_Alignment(amr_id,alignment);

    alignment = amr_alignment.remove(tok_id);
    cmd_line.set(alignment);

    reset_colors();
    amr_alignment = new AMR_Alignment(amr_id, alignment);
    for (let elem of amr_alignment.parse()) {
        $(elem).attr('on', '1')
            .css('background-color', '#eee');
    }
}

// Options --------------------------------------------------------------------------------------

function download(){
    let aligns = {};
    $("amr").each(function(index){
        amr_id = $(this).attr("amr-id");
        aligns[amr_id] = [];
    });
    $("button.reactive-onoff").each(function( index ) {
        alignment = $(this).attr("alignment");
        amr_id = $(this).parents("[amr-id]").first().attr("amr-id");
        aligns[amr_id].push(alignment);
    });
    let out = "";
    for (let amr_id in aligns){
        out += '#'+amr_id+'\n';
        out += aligns[amr_id].join('\n')+'\n';
        out += '\n';
    }
    let a = window.document.createElement('a');
    a.href = window.URL.createObjectURL(new Blob([out], {type: 'text/plain;charset=utf-8'}));
    a.download = 'amr-alignments.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

function load(){
    let file = $('input:file').prop('files')[0];
    let f = new FileReader();
    f.onload = function(e) {
        let text = e.target.result;
        text = text.replace('\r','');
        text = text.split(/\n\n+/);
        for (let t of text){
            t = $.trim(t);
            let amr_id = /^#[0-9]+/.exec(t)[0];
            amr_id = amr_id.replace('#','');
            let lines = t.split('\n');
            for (let line of lines){
                if (!line)
                    continue;
                if ($.trim(line).startsWith('#'))
                    continue;
                align = line;
                add_alignment(amr_id,align);
            }
        }
    };
    f.readAsText(file);
}

function showall(){
    reset_colors();
    $("button.reactive-onoff").each(function( index ) {
        let alignment = $(this).attr("alignment");
        let color_id = $(this).attr("color-id");
        let color = get_color(color_id);
        let amr_id = $(this).parents("[amr-id]").first().attr("amr-id");
        let amr_alignment = new AMR_Alignment(amr_id,alignment);
        $(this).css('background-color',color)
            .attr('on','1');
        amr_alignment.color(color);
    });
}

$(document).ready(function () {
    $("input").val("");
    // Download button
    $("button.download").on("click", download);
    // Load button
    $("button.load").on("click", load);
    // Show All button
    $("button.showall").on("click", showall);
    // Add Alignment button
    $("button.align").on("click", function(){
        let amr_id = $(this).attr("amr-id");
        let cmd_line = new CmdLine(`input:text[amr-id='${amr_id}']`);
        let alignment = cmd_line.get();
        add_alignment(amr_id, alignment);
    });
    // elements in AMR or sentence
    $(".aligned").on({
        click: function(){
            if($(this).attr('on') === '0')
                select_element.bind($(this))();
            else
                unselect_element.bind($(this))();
        },
        dblclick: function(){
            let amr_id = $(this).parents("[amr-id]").first().attr("amr-id");
            let alignment = $("input[amr-id='" + amr_id + "']").val();

            if($(this).attr('on') === '0'){
                select_element.bind($(this))();
            }
            add_alignment(amr_id,alignment);
        }
    }).attr("on", "0");
});

