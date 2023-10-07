$(function() {
    var INDEX = 0; 
    $("#chat-submit").click(async function(e) {
        e.preventDefault();
        var msg = $("#chat-input").val(); 

        if(msg.trim() == ''){
            return false;
        }
        
        generate_message(msg, 'self');
        var buttons = [
            {
            name: 'Existing User',
            value: 'existing'
            },
            {
            name: 'New User',
            value: 'new'
            }
        ];

        $.ajax({
            url: "http://127.0.0.1:8080/bot_query",
            method: "POST",
            contentType: "application/x-www-form-urlencoded", 
            data: {"query": msg},
            success: function(reply) {
                if(reply){
                    //generate message con la respuesta respuesta (msg,self) 
                    var init = reply.response 
                    var s = 'bot'
                    generate_message(init,s)
                } else {

                }
            }
        }); 
    })
    
    function generate_message(msg, type) {
        INDEX++;
        var str="";
        str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
        str += "          <div class=\"cm-msg-text\">";
        str += msg;
        str += "          <\/div>";
        str += "        <\/div>";
        $(".chat-logs").append(str);
        $("#cm-msg-"+INDEX).hide().fadeIn(300);
        if(type == 'self'){
            $("#chat-input").val(''); 
        }    
        $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);    
    }  
    
    function generate_button_message(msg, buttons){    
        /* Buttons should be object array 
        [
            {
            name: 'Existing User',
            value: 'existing'
            },
            {
            name: 'New User',
            value: 'new'
            }
        ]
        */
        INDEX++;
        var btn_obj = buttons.map(function(button) {
        return  "              <li class=\"button\"><a href=\"javascript:;\" class=\"btn btn-primary chat-btn\" chat-value=\""+button.value+"\">"+button.name+"<\/a><\/li>";
        }).join('');
        var str="";
        str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg user\">";
        str += "          <div class=\"cm-msg-text\">";
        str += msg;
        str += "          <\/div>";
        str += "          <div class=\"cm-msg-button\">";
        str += "            <ul>";   
        str += btn_obj;
        str += "            <\/ul>";
        str += "          <\/div>";
        str += "        <\/div>";
        $(".chat-logs").append(str);
        $("#cm-msg-"+INDEX).hide().fadeIn(300);   
        $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);
        $("#chat-input").attr("disabled", true);
    }
    
    $(document).delegate(".chat-btn", "click", function() {
        var value = $(this).attr("chat-value");
        var name = $(this).html();
        $("#chat-input").attr("disabled", false);
        generate_message(name, 'self');
    })
    
    $("#chat-circle").click(function() {   
        //HERE
        //funcion llamada init_bot
        $.ajax({
            url: "http://127.0.0.1:8080/init_bot",
            method: "POST",
            success: function(reply) {
                if(reply){
                    //generate message con la respuesta respuesta (msg,self) 
                    var init = reply.response 
                    var s = 'bot'
                    generate_message(init,s)
                } else {

                }
            }
        }); 
        //generate message con la respuesta respuesta (msg,self)
        $("#chat-circle").toggle('scale');
        $(".chat-box").toggle('scale');
    })
    
    $(".chat-box-toggle").click(function() {
        $("#chat-circle").toggle('scale');
        $(".chat-box").toggle('scale');
    })
    
})