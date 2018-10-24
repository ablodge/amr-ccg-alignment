
class AMR_Alignment{
    constructor(amr_id, alignment) {
        this.amr_id = amr_id;
        this.alignment = alignment;
    }

    get(){ return this.alignment; }

    color(my_color) {
        // color elements
        for (let elem of this.parse()) {
            if (elem.attr('colors')==="0"){
                elem.attr('colors','1');
                elem.css('background-color', my_color);
            }
            else if (elem.attr('colors')==="1"){
                elem.attr('colors','2');
                let color1 = elem.css('background-color');
                let color2 = my_color;
                let gradient = `repeating-linear-gradient( to right, ${color1}, ${color1} 10px, ${color2} 10px, ${color2} 20px)`;
                elem.css('background',gradient);
            }
            else {
                elem.attr('colors','3+');
                elem.css('border', 'solid 3px '+my_color);
            }
        }
    }

    parse() {
        let elements = [];
        let align = this.clean().split('~');
        // add amr elements
        let amr_align = $.trim(align[1]).split(' ');
        for (let elem of amr_align) {
            if (elem) {
                let tok_id = elem.replace(':', '');
                elements.push($(`amr[amr-id='${this.amr_id}'] [tok-id='${tok_id}']`));
            }
        }
        // add sentence elements
        let sent_align = $.trim(align[0]).split(' ');
        for (let elem of sent_align) {
            if (elem) {
                let tok_id = elem;
                elements.push($(`anything[amr-id='${this.amr_id}'] [tok-id='${tok_id}']`));
            }
        }
        return elements;
    }

    test(){ return this.clean().split("~").length-1===1;}

    clean(){
        let s = this.alignment;
        if (!$.trim(s))
            s = "~";
        if (s.indexOf('#') > -1)
            s = s.split('#')[0];
        s = $.trim(s);
        s = s.replace(/\s*~\s*/,' ~ ');
        s = s.replace(/\s+/,' ');
        return s;
    }

    comment(){
        let c = '';
        if (this.alignment.indexOf('#')>-1)
            c = this.alignment.substr(this.alignment.indexOf('#'));
        if (!this.is_connected())
            c += '# ✘disconnected ';
        let type = $(`anything[amr-id='${this.amr_id}']`).attr('class');
        if (type==='CCG' && this.is_isomorphic())
            c += '# ✓sem args = syn args ';
        return '     '+c;
    }

    add_left(tok_id){
        this.alignment = this.clean().replace('~', tok_id + ' ~');
        this.alignment += this.comment();
        return this.alignment;
    }

    add_right(tok_id){
        this.alignment = this.clean() + ' ' + tok_id;
        this.alignment += this.comment();
        return this.alignment;
    }

    remove(tok_id){
        let aligns = this.clean().split(' ');
        for (let i = 0; i < aligns.length; i++) {
            if (aligns[i] === tok_id) {
                aligns[i] = '';
                break;
            }
        }
        this.alignment = $.trim(aligns.join(' ')).replace('  ', ' ');
        this.alignment += this.comment();
        return this.alignment;
    }

    is_connected(){
        let elements = [];
        let align = this.alignment.split('~');
        let amr_align = $.trim(align[1]).split(' ');
        if (amr_align.length<=1)
            return true;
        let nodes = [];
        let edges = [];
        for (let elem of amr_align){
            if (elem.includes('_'))
                edges.push(elem);
            else
                nodes.push(elem)
        }
        // every node is connected to an edge
        let test1 = nodes.every(
            (n)=>edges.some(
                (e)=>e.split('_').indexOf(n) > -1
            )
        );
        // every edge is connected to a node
        if (!test1)
            return false;
        let test2 = edges.every(
            (e)=>nodes.some(
                (n)=>e.split('_').indexOf(n) > -1
            )
        );
        return test2;
    }

    is_isomorphic(){
        // number of semantic args equals the number of syntactic args
        if(!$.trim(this.clean().split('~')[0]) || !$.trim(this.clean().split('~')[1]))
            return false;

        let sem_count = 0;
        let syn_count = 0;
        let align = this.clean().split('~');
        let amr_align = $.trim(align[1]).split(' ');
        let sent_align = $.trim(align[0]).split(' ');
        // get nodes and edges
        let nodes = [];
        let edges = [];
        for (let elem of amr_align){
            if (elem.includes('_'))
                edges.push(elem);
            else
                nodes.push(elem)
        }
        // get number of semantic args
        let sem_args = [];
        for (let e of edges){
            let a = e.split('_')[0];
            let b = e.split('_')[2];
            sem_args.push(a);
            sem_args.push(b);
        }
        sem_args = new Set(sem_args);
        for (let n of sem_args){
            if (nodes.indexOf(n)===-1)
                sem_count += 1;
        }
        // get number of syntactic args
        for (let w of sent_align){
            let selector = $(`anything[amr-id='${this.amr_id}'] [tok-id='${w}'] args`);
            if (selector.length>0)
                syn_count += parseInt(selector.html());
        }
        return sem_count===syn_count;
    }

    readible(){
        let r = '';
        let align = this.clean().split('~');

        // add sentence elements
        let sent_align = $.trim(align[0]).split(' ');
        for (let a of sent_align) {
            if (!a) continue;
            let tok_id = a;
            let selector = $(`anything[amr-id='${this.amr_id}'] word[tok-id='${tok_id}']`);
            for (let elem of selector.toArray())
                r += $(elem).html()
                            .replace(/<tok>.*?<\/tok>/g,'')
                            .replace(/<.*?>/g,'')+' ';

        }
        r += '~ ';
        // add amr elements
        let amr_align = $.trim(align[1]).split(' ');
        for (let a of amr_align) {
            if (!a) continue;
            let tok_id = a.replace(':','');
            let selector = $(`amr[amr-id='${this.amr_id}'] [tok-id='${tok_id}']`);
            for (let elem of selector.toArray())
                r += $(elem).html().replace(/<.*?>/,'')+' ';
        }
        return r;
    }
}
class CmdLine {
    constructor(elem) {
        this.random_id = Math.floor(Math.random() * 1000000)
        $(elem).attr('id',this.random_id)
        this.me = $(`input:text.cmdline#${this.random_id}`);
    }

    select(){ return this.me; }

    set(text){ this.me.val(text); }

    get(){ return this.me.val(); }

    clear(){ this.set(''); }

    parse(regex){ return regex.exec(this.get()); }

    add(text){
        let a = this.get();
        this.set(a+text);
    }

    clean(f){
        let a = this.get();
        this.set(f(a));
    }

    static create(){
        return `<input type="text" class="cmdline"/>`
    }
}class OnOffButton {

    constructor(elem, on_behavior, off_behavior, colors) {
        this.on_behavior = on_behavior;
        this.off_behavior = off_behavior;
        this.colors = colors;
        this.random_id = Math.floor(Math.random() * 1000000)
        $(elem).attr('id',this.random_id)
        this.me = $(`button.reactive-onoff#${this.random_id}`);
    }

    select(){ return this.me }

    turn_on(){
        this.on_behavior();
        this.me.attr('on','1');
        if ('on' in this.colors)
            this.select().css('background-color', this.colors['on']);
        else
            this.select().css('background-color', '#eee');
    }

    turn_off(){
        this.off_behavior();
        this.me.attr('on','0');
        if ('off' in this.colors)
            this.select().css('background-color', this.colors['off']);
        else
            this.select().css('background-color', '#eee');
    }

    flip(){
        if (this.me.attr('on')==='0')
            this.turn_on();
        else
            this.turn_off();
    }

    static create(name){
        return '<button class="reactive-onoff" on="0">' + name + '</button>';
    }
}

// Colors ---------------------------------------------------------------------------------------------------

function get_color(index) {
    colors = ["#abebc6", "#aed6f1", "#d7bde2", "#f9e79f", "#f5b7b1"];
    return colors[index % colors.length]
}

function reset_colors() {
    $("button.reactive-onoff").css('background-color', '#eee')
                     .attr('on', '0');
    $(".aligned").css({'background': '', 'border': ''})
                 .attr({'on': '0', 'colors':'0'})
                 .removeClass('selected');

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
        amr_alignment = new AMR_Alignment(amr_id,alignment);
        for (let elem of amr_alignment.parse()) {
            $(elem).attr('on', '1')
                .addClass('covered');
        }
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
            .addClass('selected');
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
            .addClass('selected')
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

    let comment_out = function(string){
        string = string.replace(/<.*?>/g,'');
        string = $.trim(string);
        split = string.split('\n');
        comment = '';
        for (let s of split)
            comment += '# '+s+'\n'
        return comment;
    };

    let out = "";
    for (let amr_id in aligns){
        let amr = $(`amr[amr-id='${amr_id}']`).html()
            .replace(/<.*?>/g,'');
        amr = comment_out(amr);
        let sent = $(`anything[amr-id='${amr_id}']`).html()
            .replace(/<sub>/g,'[')
            .replace(/<\/sub>/g,']')
            .replace(/<tr class="expand".*?<\/tr>/g,'')
            .replace(/<button .*?<\/button>/g,'')
            .replace(/<.*?>/g,'')
            .replace(/ /g,'\t');
        sent = comment_out(sent);
        let sent_type = $(`anything[amr-id='${amr_id}']`).attr('class');
        out += '#'+amr_id+'\n';
        out += '# AMR:\n'+amr;
        out += `# ${sent_type}:\n`+sent;
        out += '# Alignments:\n';
        for (let align of aligns[amr_id]){
            let amr_alignment = new AMR_Alignment(amr_id, align);
            out += '# '+amr_alignment.readible()+'\n';
        }
        for (let align of aligns[amr_id]){
            out += align+'\n';
        }
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
        text = text.replace(/\r/g,'').replace(/\n\n+/g,'\n\n');
        text = text.split('\n\n');
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
                let align = $.trim(line);
                add_alignment(amr_id, align);
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
    $(document).keydown(function (e) {
            if (e.ctrlKey && e.key === 'x') {
                showall()
            }
    });
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
            select_element.bind($(this))();

            let amr_id = $(this).parents("[amr-id]").first().attr("amr-id");
            let alignment = $("input[amr-id='" + amr_id + "']").val();
            add_alignment(amr_id,alignment);
        }
    }).attr("on", "0");
    $("button.expand").on({
        click:function(){
            let amr_id = $(this).parents("[amr-id]").first().attr("amr-id");
            let elem = $(`anything[amr-id='${amr_id}'] tr.expand`);
            if (elem.css('display')==='none'){
                elem.css('display','');
                $(this).text('CCG parse ▼');
            }
            else {
                elem.css('display','none');
                $(this).text('CCG parse ▲');
            }
        }
    });
    $('tr.expand').css('display','none');
});


