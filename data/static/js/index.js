/* 后台数据图表*/
$(function(){
	var data;
	var num=7;
	var type;
	//画折线图的方法
	function dw (d,title){
			var myChart = new JSChart('chartcontainer', 'line');
			var n=parseInt(num);  
			myChart.setDataArray(d);  
			myChart.setTitle(title);
			myChart.setAxisNameX("");
			myChart.setAxisNameY("");
			// myChart.setAxisValuesSuffixX("号");
			myChart.setSize(1100,400);
			myChart.setAxisValuesNumberX(n);
			myChart.draw();
	}
	//填写表格数据
	function td (d,i){
		var obj=$(".draw .title ul").eq(i).find("li");
		var str="<tr><td>日期</td>";
		for (var i = 0; i < obj.length; i++) {
			str+="<td>"+$(obj[i]).html()+"</td>"
		};
		str+="</tr>";
		for (var i = 0; i < d.length; i++) {
			str+="<tr><td>"+d[i]["datetime"]+"</td>";
			for (var j = 0; j < obj.length; j++) {
				str+="<td>"+d[i][$(obj[j]).attr("type")]+"</td>";
			};
			str+="</tr>"
		};
		$("#table table").html(str);
	}
	//7天 15天 30天按钮
	$(".menu li").click(function(){
		$(this).css({"background":"#519BCE","color":"#fff"}).siblings().css({"background":"none","color":"#666"});
		if(num!=$(this).attr("num")){
			num=$(this).attr("num");
			$(".draw .title li").each(function(){
				if($(this).attr("type")==type){
					$(this).click();
				}
			})
		}
	})
	$(".menu li").first().click();
	//左边总的分类
	$(".bar li").click(function(){
		$(this).css('color','#519BCE').siblings().css('color','#666');
		$(".draw .title ul").eq($(this).index()).fadeIn().siblings().hide();
		var url="../"+$(this).attr('data');
		$.ajax({
			url: url,
			async:false,
			success:function(d){
				 data=JSON.parse(d);
				 data=data.json;
				 num=7;
			},
			error:function(){
				console.log("error");
			}
   		 })
		$(".draw .title ul").eq($(this).index()).children().first().click();
		td(data,$(this).index());
	})
	//上边每个小的分类
	$(".draw .title li").click(function(){
		$(this).css('color','#519BCE').siblings().css('color','#666');
		type=$(this).attr('type');
		var title=$(this).html();
		var temp=[];
		num=num>data.length?data.length:num;
		for (var i = 0; i < num; i++) {
			var time=data[i].datetime.slice(5);
			if(type=="date_aver"||type=="loss_rate"||type=="not_active_rate"||type=="loss_rate"||type=="not_active_rate"||type=="pos_aver"||type=="c_delivery"||type=="aver_position"||type=="loss_aver")
			{
				temp.unshift([time,parseFloat(data[i][type])])
			}else{
				temp.unshift([time,parseInt(data[i][type])]);
			}
		}
		dw(temp,title);
	})
	$(".bar li").first().click();
	//表格/折线图按钮
	$(".layout li").click(function(){
		$(this).css({"background":"#519BCE","color":"#fff"}).siblings().css({"background":"none","color":"#666"})
		var a=$(this).attr("for");
		if(a=="pic"){
			if($("#table").css("display")=="none")
				return;
			$("#table").css("display","none");
			$(".title").css("visibility","visible");
			$(".menu").css("display","block");
			$("#chartcontainer").css("display","block");
		}else{
			if($("#table").css("display")=="block")
				return;
			$("#table").css("display","block");
			$(".title").css("visibility","hidden");
			$(".menu").css("display","none");
			$("#chartcontainer").css("display","none");
		}
	})
})