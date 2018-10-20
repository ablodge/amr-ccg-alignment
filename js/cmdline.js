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
}