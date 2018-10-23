



var mode = 'amr-text';
$(document).ready(function () {
    $('button.choice').attr('on','0');
    // Download button
    $("button.amr-text").on("click", function(){
        $('button.choice').attr('on','0');
        $(this).attr('on','1');
        mode = 'amr-text';
        $("[name='description']").html(
            'The <b>AMR-Sentence</b> tool is for aligning AMRs with natural text.'
        )
    });
    // Select AMR-AMR Alignment
    $("button.amr-ccg").on("click", function(){
        $('button.choice').attr('on','0');
        $(this).attr('on','1');
        mode = 'amr-ccg';
        $("[name='description']").html(
            'The <b>AMR-CCG</b> tool is for assigning AMR semantics to CCG lexical entries.'
        )
    });
    // Select AMR-UD Alignment
    $("button.amr-ud").on("click", function(){
        $('button.choice').attr('on','0');
        $(this).attr('on','1');
        mode = 'amr-ud';
        $("[name='description']").html(
            'The <b>AMR-UD</b> tool is for structurally aligning AMRs and Universal Dependencies.'
        )
    });
    // Select AMR-AMR Alignment
    $("button.amr-amr").on("click", function(){
        $('button.choice').attr('on','0');
        $(this).attr('on','1');
        mode = 'amr-amr';
        $("[name='description']").html(
            'The <b>AMR-AMR</b> tool is for aligning AMRs, such as for coreference, multiligual AMRs, etc.'
        )
    });
    // Load AMR Data
    // $("button.amr-upload").on("click", amr_upload);
    // // Load Other Data
    // $("button.any-upload").on("click", any_upload);
    // Launch button
    $("button.launch").on("click", function(){

    });
});