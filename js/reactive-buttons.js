class OnOffButton {

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
