
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
        let align = this.alignment.split('~');
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
                elements.push($(`sentence[amr-id='${this.amr_id}'] [tok-id='${tok_id}']`));
            }
        }
        return elements;
    }

    test(){ return this.clean().split("~").length-1===1;}

    clean(){
        let s = this.alignment;
        if ($.trim(s).length==0)
            s = "~";
        if (s.indexOf('#') > -1)
            s = s.split('#')[0];
        s = $.trim(s);
        s = s.replace(/\s*~\s*/,' ~ ');
        s = s.replace(/\s+/,' ');
        return s;
    }

    comment(){ return this.alignment.substr(this.alignment.indexOf('#')); }

    add_left(tok_id){
        var comment = this.comment();
        comment = comment ? '   '+comment : '';
        this.alignment = this.clean().replace('~', tok_id + ' ~')+'   '+comment;
        return this.alignment;
    }

    add_right(tok_id){
        let comment = this.comment();
        comment = comment ? '   '+comment : '';
        this.alignment = this.clean() + ' ' + tok_id+'   '+comment;
        return this.alignment;
    }

    remove(tok_id){
        let comment = this.comment();
        comment = comment ? '   '+comment : '';
        let aligns = this.clean().split(' ');
        for (let i = 0; i < aligns.length; i++) {
            if (aligns[i] === tok_id) {
                aligns[i] = '';
                break;
            }
        }
        this.alignment = $.trim(aligns.join(' ')).replace('  ', ' ') + comment;
        return this.alignment;
    }
}
