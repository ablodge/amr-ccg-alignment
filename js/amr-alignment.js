
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
                elements.push($(`sentence[amr-id='${this.amr_id}'] [tok-id='${tok_id}']`));
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
        let type = $(`sentence[amr-id='${this.amr_id}']`).attr('class');
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
            let selector = $(`sentence[amr-id='${this.amr_id}'] [tok-id='${w}'] args`);
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
            let selector = $(`sentence[amr-id='${this.amr_id}'] word[tok-id='${tok_id}']`);
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
