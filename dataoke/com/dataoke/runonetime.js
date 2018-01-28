// https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx197c21f563166768&secret=8c8967a7ab88171ddbca4dcebb4bb208

var request = require('request');
var fs = require('fs');

access_token = "glKpu_A7a4VIIyiqVTIKFlS3s49eltxIIAr2yMDmxClmwzBwS5rJOcKcvzle8BzVdOR53YATL__Majqi7ERb53-t8SKvf3eI7_5iTQKZbjPQ0SsIC2MuBfA0TDCaGdmNUNFaAIAOHZ"

var api = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + access_token

var delete_api = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=" + access_token

var upload = "https://api.weixin.qq.com/cgi-bin/material/add_material?type=image&access_token=" + access_token

// var upload = 'https://api.weixin.qq.com/cgi-bin/media/upload?type=image&access_token=' + access_token

//创建菜单
var menu = {
    "button":[
        {
            "type": "view",
            "name": "好物集市",
            "url": "http://wyhw.banyan-data.com/h5/#/home"
        },
        {
            "type": "view",
            "name": "好物精选",
            "url": "http://wyhw.banyan-data.com/h5/#/activity"
        },
        {
            "name": "用户中心",
            "sub_button":[
                {
                    "type": "media_id",
                    "name": "客服",
                    "media_id": "oYEOry9bnSjnlN3QnIjftVJF6XaioA6uJiD3TTERkF4"
                },
                {
                    "type": "view",
                    "name": "返现说明",
                    "url":"http://c8.rrxiu.me/v/pi4a1m"
                },
                {
                    "type": "click",
                    "name": "邀请好友",
                    "key":"invite"
                },
                {
                    "type" : "click",
                    "name": "兑换规则",
                    "key": "redbag_rule"
                },
                {
             		"type": "view",
             		"name": "我的主页",
            		"url":"http://wyhw.banyan-data.com/h5/#/profile"
       			},
            ]
        }
    ]
}


//删除菜单
request.get({url:delete_api},function(err,res,body){
    if(err){
        console.log(err)
    }else {
        console.log('upload successful with res:' + body)
    } 
})



// //新增菜单
request.post({url:api,body:menu,json:true},function(err,res,body){
    if(err){
        console.log(err)
    }else {
        console.log('upload successful with res:' + body)
    }
})



