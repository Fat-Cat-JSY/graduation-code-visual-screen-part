<template>
	<div class="home-content" :style="{'backgroundImage': indexBgUrl?`url(${$base.url + indexBgUrl})`:''}">
		<!-- title -->
		<div id="home-title" class="home-title animate__animated">
			<div class="titles" >
				<span>欢迎使用</span>
				{{this.$project.projectName}}
			</div>
		</div>
		<!-- statis -->
		<div class="statis-box">
			<div id="statis1" class="statis1 animate__animated" v-if="isAuth('yonghu','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-touxiang04"></span>
				</div>
				<div class="right">
					<div class="num">{{yonghuCount}}</div>
					<div class="name">用户总数</div>
				</div>
			</div>
			<div id="statis2" class="statis2 animate__animated" v-if="isAuth('taobaoinfo','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-liulan12"></span>
				</div>
				<div class="right">
					<div class="num">{{taobaoinfoCount}}</div>
					<div class="name">淘宝男鞋总数</div>
				</div>
			</div>
		</div>
		<!-- statis -->
	
		<!-- echarts -->
		<!-- 9 -->
		<div class="type9">
			<div class="echarts1 animate__animated" v-if="isAuth('yonghu','首页统计',2)">
				<div id="yonghuChart1" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts2 animate__animated" v-if="isAuth('yonghu','首页统计',2)">
				<div id="yonghuChart2" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts3 animate__animated" v-if="isAuth('taobaoinfo','首页统计',2)">
				<el-select
					v-if="changeStatQuery(['users'])"
					v-model="taobaoinfochartQuery1.title" placeholder="标题" @change="taobaoinfoChat1" clearable>
					<el-option v-for="item in taobaoinfoChartOptions1" :label="item" :value="item"></el-option>
				</el-select>
				<div id="taobaoinfoChart1" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts4 animate__animated" v-if="isAuth('taobaoinfo','首页统计',2)">
				<el-select
					v-if="changeStatQuery(['users'])"
					v-model="taobaoinfochartQuery2.title" placeholder="标题" @change="taobaoinfoChat2" clearable>
					<el-option v-for="item in taobaoinfoChartOptions2" :label="item" :value="item"></el-option>
				</el-select>
				<div id="taobaoinfoChart2" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts5 animate__animated" v-if="isAuth('taobaoinfo','首页统计',2)">
				<el-select
					v-if="changeStatQuery(['users'])"
					v-model="taobaoinfochartQuery3.title" placeholder="标题" @change="taobaoinfoChat3" clearable>
					<el-option v-for="item in taobaoinfoChartOptions3" :label="item" :value="item"></el-option>
				</el-select>
				<div id="taobaoinfoChart3" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts6 animate__animated" v-if="isAuth('taobaoinfo','首页统计',2)">
				<el-select
					v-if="changeStatQuery(['users'])"
					v-model="taobaoinfochartQuery4.title" placeholder="标题" @change="taobaoinfoChat4" clearable>
					<el-option v-for="item in taobaoinfoChartOptions4" :label="item" :value="item"></el-option>
				</el-select>
				<div id="taobaoinfoChart4" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts7 animate__animated" v-if="isAuth('taobaoinfo','首页统计',2)">
				<el-select
					v-if="changeStatQuery(['users'])"
					v-model="taobaoinfochartQuery5.title" placeholder="标题" @change="taobaoinfoChat5" clearable>
					<el-option v-for="item in taobaoinfoChartOptions5" :label="item" :value="item"></el-option>
				</el-select>
				<div id="taobaoinfoChart5" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts8 animate__animated" v-if="isAuth('taobaoinfo','首页统计',2)">
				<el-select
					v-if="changeStatQuery(['users'])"
					v-model="taobaoinfochartQuery6.title" placeholder="标题" @change="taobaoinfoChat6" clearable>
					<el-option v-for="item in taobaoinfoChartOptions6" :label="item" :value="item"></el-option>
				</el-select>
				<div id="taobaoinfoChart6" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts9 animate__animated" v-if="isAuth('taobaoinfo','首页统计',2)">
				<el-select
					v-if="changeStatQuery(['users'])"
					v-model="taobaoinfochartQuery7.title" placeholder="标题" @change="taobaoinfoChat7" clearable>
					<el-option v-for="item in taobaoinfoChartOptions7" :label="item" :value="item"></el-option>
				</el-select>
				<div id="taobaoinfoChart7" style="width: 100%;height: 100%"></div>
			</div>
		</div>
		<!-- echarts -->
	</div>
</template>
<script>
import 'animate.css'
//9
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
			yonghuCount: 0,
			taobaoinfoCount: 0,
			taobaoinfochartQuery1: {},
			taobaoinfoChartOptions1: [],
			taobaoinfochartQuery2: {},
			taobaoinfoChartOptions2: [],
			taobaoinfochartQuery3: {},
			taobaoinfoChartOptions3: [],
			taobaoinfochartQuery4: {},
			taobaoinfoChartOptions4: [],
			taobaoinfochartQuery5: {},
			taobaoinfoChartOptions5: [],
			taobaoinfochartQuery6: {},
			taobaoinfoChartOptions6: [],
			taobaoinfochartQuery7: {},
			taobaoinfoChartOptions7: [],
			line: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":10,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"interval":0,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"showSymbol":true,"symbol":"arrow","symbolSize":12},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"}},
			bar: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":12,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":10,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"interval":0,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"right":"20","top":"60","left":"20","bottom":"20","containLabel":true},"series":{"barWidth":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"barBorderRadius":[5,5,5,5],"borderWidth":0,"opacity":1,"shadowColor":"#000"},"colorBy":"data","barCategoryGap":"40%"},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"subtext":"","shadowBlur":0,"bottom":"auto","show":true,"right":"auto","subtextStyle":{"padding":[5,0,0,0],"borderColor":"red","color":"red","borderWidth":10},"top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"base":{"animate":false,"interval":2000}},
			pie: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"title":{"borderType":"solid","padding":[5,0,0,0],"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":14,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":[5,0,0,0],"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":0,"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#eee","color":"inherit","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","formatter":"{b}: ({d}%)","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#666","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false}}},
			funnel: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"title":{"borderType":"solid","padding":2,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"center","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#666","textShadowColor":"transparent","fontSize":14,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false}}},
			boardBase: {"funnelNum":8,"lineNum":8,"radarNum":8,"gaugeNum":8,"barNum":8,"pieNum":8},
			gauge: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"title":{"top":"top","left":"left","textStyle":{"fontSize":14,"lineHeight":24,"color":"#333","fontWeight":600}},"series":{"pointer":{"offsetCenter":[0,"10%"],"icon":"path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z","width":8,"length":"80%"},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"opacity":0.5,"shadowBlur":1,"shadowColor":"#000"},"roundCap":true},"anchor":{"show":true,"itemStyle":{"color":"inherit"},"size":18,"showAbove":true},"emphasis":{"disabled":false},"progress":{"show":true,"roundCap":true,"overlap":true},"splitNumber":25,"detail":{"formatter":"{value}","backgroundColor":"inherit","color":"#fff","borderRadius":3,"width":20,"fontSize":12,"height":10},"title":{"fontSize":14},"animation":true}},
			radar: {"backgroundColor":"transparent","radar":{"shape":"circle"},"color":["#365E77","#DF308C","#0CB906","#7690cb","#49ada0","#5BBAEC","#a68a28","#EE142F","#FFE9E9"],"legend":{"padding":5,"itemGap":5,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":4,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"auto","itemWidth":4,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#7987FD"}},"title":{"top":"top","left":"left","textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":14,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#666","textShadowBlur":0}}},
			indexBgUrl: '',
			indexLogoUrl: '',
		};
	},
	mounted(){
		this.init();
		this.getyonghuCount();
		if(this.isAuth('yonghu','首页统计',2)){
			this.yonghuChat1();
		}
		if(this.isAuth('yonghu','首页统计',2)){
			this.yonghuChat2();
		}
		this.gettaobaoinfoCount();
		if(this.isAuth('taobaoinfo','首页统计',2)){
			this.gettaobaoinfotitleOptions1()
			this.taobaoinfoChat1();
		}
		if(this.isAuth('taobaoinfo','首页统计',2)){
			this.gettaobaoinfotitleOptions2()
			this.taobaoinfoChat2();
		}
		if(this.isAuth('taobaoinfo','首页统计',2)){
			this.gettaobaoinfotitleOptions3()
			this.taobaoinfoChat3();
		}
		if(this.isAuth('taobaoinfo','首页统计',2)){
			this.gettaobaoinfotitleOptions4()
			this.taobaoinfoChat4();
		}
		if(this.isAuth('taobaoinfo','首页统计',2)){
			this.gettaobaoinfotitleOptions5()
			this.taobaoinfoChat5();
		}
		if(this.isAuth('taobaoinfo','首页统计',2)){
			this.gettaobaoinfotitleOptions6()
			this.taobaoinfoChat6();
		}
		if(this.isAuth('taobaoinfo','首页统计',2)){
			this.gettaobaoinfotitleOptions7()
			this.taobaoinfoChat7();
		}
		window.addEventListener('scroll', this.handleScroll)
		setTimeout(()=>{
			this.handleScroll()
		},100)
	},
	created() {
		this.$http.get('config/info?name=bIndexBackgroundImg',).then(rs=>{this.indexBgUrl = rs.data.data?rs.data.data.value:''})
		this.$http.get('config/info?name=bHomeLogo',).then(rs=>{this.indexLogoUrl = rs.data.data?rs.data.data.value:''})
	},
	computed: {
		sessionForm() {
			return JSON.parse(this.$storage.getObj('userForm'))
		},
		avatar(){
			return this.$storage.get('headportrait')?this.$storage.get('headportrait'):''
		},
	},
	methods:{
		handleScroll() {
			let arr = [
				{id:'home-title',css:'animate__'},
				{id:'statis1',css:'animate__'},
				{id:'statis2',css:'animate__'},
				{id:'yonghuChart1',css:'animate__'},
				{id:'yonghuChart2',css:'animate__'},
				{id:'taobaoinfoChart1',css:'animate__'},
				{id:'taobaoinfoChart2',css:'animate__'},
				{id:'taobaoinfoChart3',css:'animate__'},
				{id:'taobaoinfoChart4',css:'animate__'},
				{id:'taobaoinfoChart5',css:'animate__'},
				{id:'taobaoinfoChart6',css:'animate__'},
				{id:'taobaoinfoChart7',css:'animate__'},
			]
			
			for (let i in arr) {
				let doc = document.getElementById(arr[i].id)
				if (doc) {
					let top = doc.offsetTop
					let win_top = window.innerHeight + window.pageYOffset
					// console.log(top,win_top)
					if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
						// console.log(doc)
						doc.classList.add(arr[i].css)
					}
				}
			}
		},
		// 统计图动画
		myChartInterval(type, xAxisData, seriesData, myChart) {
			this.$nextTick(() => {
				setInterval(() => {
					let xAxis = xAxisData.shift()
					xAxisData.push(xAxis)
					let series = seriesData.shift()
					seriesData.push(series)
				
					if (type == 1) {
						myChart.setOption({
							xAxis: [{
								data: xAxisData
							}],
							series: [{
								data: seriesData
							}]
						});
					}
					if (type == 2) {
						myChart.setOption({
							yAxis: [{
								data: xAxisData
							}],
							series: [{
								data: seriesData
							}]
						});
					}
				}, $template2.back.board.bar.base.interval);
			})
		},
		changeStatQuery(arr) {
			if(arr.length==1) {
				if(arr[0] == 'users'&&this.$storage.get("sessionTable")=='users') {
					return true
				}
			}
			let role = this.$storage.get('role')
			for(let x in arr) {
				if(arr[x] == role) {
					return true
				}
			}
			return false
		},
		init(){
			if(this.$storage.get('Token')){
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code != 0) {
						router.push({ name: 'login' })
					}
				});
			}else{
				router.push({ name: 'login' })
			}
		},
		getyonghuCount() {
			this.$http({
				url: `yonghu/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.yonghuCount = data.data
				}
			})
		},
		yonghuChat1(e=null) {
			this.$nextTick(()=>{
				var yonghuChart1 = echarts.init(document.getElementById("yonghuChart1"),'macarons');
				let params = {
				}
				this.$http({
					url: `yonghu/value/yonghuxingming/nianling`,
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.lineNum){
								break;
							}
							xAxis.push(res[i].yonghuxingming);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].yonghuxingming
							})
						}
						var option = {};
						let titleObj = this.line.title
						titleObj.text = '年龄统计'
						
						const legendObj = this.line.legend
						let tooltipObj = { trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
						let xAxisObj = this.line.xAxis
						xAxisObj.type = 'category'
						xAxisObj.data = xAxis
						
						let yAxisObj = this.line.yAxis
						yAxisObj.type = 'value'
						const gridObj = this.line.grid
						
						let seriesObj = {
							data: yAxis,
							type: 'line',
						}
						seriesObj = Object.assign(seriesObj , this.line.series)
						option = {
							backgroundColor: this.line.backgroundColor,
							color: this.line.color,
							title: titleObj,
							legend: legendObj,
							grid: gridObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj]
						};
						// 使用刚指定的配置项和数据显示图表。
						yonghuChart1.setOption(option);
				
						//根据窗口的大小变动图表
						window.onresize = function() {
							yonghuChart1.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		yonghuChat2(e=null) {
			this.$nextTick(()=>{

				var yonghuChart2 = echarts.init(document.getElementById("yonghuChart2"),'macarons');
				let params = {
				}
				this.$http({
					url: "yonghu/group/xingbie",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.pieNum){
								break;
							}
							xAxis.push(res[i].xingbie);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].xingbie
							})
						}
						var option = {};
						let titleObj = this.pie.title
						titleObj.text = '用户统计'
						
						const legendObj = this.pie.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
						tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
						
						let seriesObj = {
							type: 'pie',
							radius: '55%',
							center: ['50%', '60%'],
							data: pArray,
							emphasis: {
								itemStyle: {
									shadowBlur: 10,
									shadowOffsetX: 0,
									shadowColor: 'rgba(0, 0, 0, 0.5)'
								}
							}
						}
						seriesObj = Object.assign(seriesObj , this.pie.series)
						const gridObj = this.pie.grid
						option = {
							backgroundColor: this.pie.backgroundColor,
							color: this.pie.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						yonghuChart2.setOption(option);
				
						//根据窗口的大小变动图表
						window.onresize = function() {
							yonghuChart2.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		gettaobaoinfoCount() {
			this.$http({
				url: `taobaoinfo/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.taobaoinfoCount = data.data
				}
			})
		},
		gettaobaoinfotitleOptions1() {
			this.$http.get('option/taobaoinfo/title',
			).then(rs=>{
				this.taobaoinfoChartOptions1 = rs.data.data
			})
		},
		taobaoinfoChat1(e=null) {
			if(this.changeStatQuery(['users'])) {
				document.getElementById('taobaoinfoChart1').setAttribute('style','width: 100%;height: calc(100% - 50px)')
			}
			this.$nextTick(()=>{
				var taobaoinfoChart1 = echarts.init(document.getElementById("taobaoinfoChart1"),'macarons');
				let params = {
				}
				if(this.taobaoinfochartQuery1.title) {
					params.conditionColumn = 'title'
					params.conditionValue = this.taobaoinfochartQuery1.title
				}
				this.$http({
					url: `taobaoinfo/value/title/jiage`,
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.lineNum){
								break;
							}
							xAxis.push(res[i].title);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].title
							})
						}
						var option = {};
						let titleObj = this.line.title
						titleObj.text = '价格统计'
						
						const legendObj = this.line.legend
						let tooltipObj = { trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
						let xAxisObj = this.line.xAxis
						xAxisObj.type = 'category'
						xAxisObj.data = xAxis
						
						let yAxisObj = this.line.yAxis
						yAxisObj.type = 'value'
						const gridObj = this.line.grid
						
						let seriesObj = {
							data: yAxis,
							type: 'line',
							areaStyle: {}
						}
						seriesObj = Object.assign(seriesObj , this.line.series)
						option = {
							backgroundColor: this.line.backgroundColor,
							color: this.line.color,
							title: titleObj,
							legend: legendObj,
							grid: gridObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj]
						};
						// 使用刚指定的配置项和数据显示图表。
						taobaoinfoChart1.setOption(option);
				
						//根据窗口的大小变动图表
						window.onresize = function() {
							taobaoinfoChart1.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		gettaobaoinfotitleOptions2() {
			this.$http.get('option/taobaoinfo/title',
			).then(rs=>{
				this.taobaoinfoChartOptions2 = rs.data.data
			})
		},
		taobaoinfoChat2(e=null) {
			if(this.changeStatQuery(['users'])) {
				document.getElementById('taobaoinfoChart2').setAttribute('style','width: 100%;height: calc(100% - 50px)')
			}
			this.$nextTick(()=>{

				var taobaoinfoChart2 = echarts.init(document.getElementById("taobaoinfoChart2"),'macarons');
				let params = {
				}
				if(this.taobaoinfochartQuery2.title) {
					params.conditionColumn = 'title'
					params.conditionValue = this.taobaoinfochartQuery2.title
				}
				this.$http({
					url: `taobaoinfo/value/title/salesnum`,
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.barNum){
								break;
							}
							xAxis.push(res[i].title);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].title
							})
						}
						var option = {};
						let titleObj = this.bar.title
						titleObj.text = '销售量统计'
						
						const legendObj = this.bar.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
				
						let xAxisObj = this.bar.xAxis
						xAxisObj.type = 'value'
						
						let yAxisObj = this.bar.yAxis
						yAxisObj.type = 'category'
						yAxisObj.data = xAxis
						let seriesObj = {
							data: yAxis,
							type: 'bar',
						}
						seriesObj = Object.assign(seriesObj , this.bar.series)
						const gridObj = this.bar.grid

						option = {
							backgroundColor: this.bar.backgroundColor,
							color: this.bar.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						taobaoinfoChart2.setOption(option);
				
						//根据窗口的大小变动图表
						window.onresize = function() {
							taobaoinfoChart2.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		gettaobaoinfotitleOptions3() {
			this.$http.get('option/taobaoinfo/title',
			).then(rs=>{
				this.taobaoinfoChartOptions3 = rs.data.data
			})
		},
		taobaoinfoChat3(e=null) {
			if(this.changeStatQuery(['users'])) {
				document.getElementById('taobaoinfoChart3').setAttribute('style','width: 100%;height: calc(100% - 50px)')
			}
			this.$nextTick(()=>{

				var taobaoinfoChart3 = echarts.init(document.getElementById("taobaoinfoChart3"),'macarons');
				let params = {
				}
				if(this.taobaoinfochartQuery3.title) {
					params.conditionColumn = 'title'
					params.conditionValue = this.taobaoinfochartQuery3.title
				}
				this.$http({
					url: "taobaoinfo/group/shoptag",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.pieNum){
								break;
							}
							xAxis.push(res[i].shoptag);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].shoptag
							})
						}
						var option = {};
						let titleObj = this.pie.title
						titleObj.text = '标签统计'
						
						const legendObj = this.pie.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
						tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
						
						let seriesObj = {
							type: 'pie',
							radius: '55%',
							center: ['50%', '60%'],
							data: pArray,
							emphasis: {
								itemStyle: {
									shadowBlur: 10,
									shadowOffsetX: 0,
									shadowColor: 'rgba(0, 0, 0, 0.5)'
								}
							}
						}
						seriesObj = Object.assign(seriesObj , this.pie.series)
						const gridObj = this.pie.grid
						
						option = {
							backgroundColor: this.pie.backgroundColor,
							color: this.pie.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						taobaoinfoChart3.setOption(option);
						//根据窗口的大小变动图表
						window.onresize = function() {
							taobaoinfoChart3.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
		gettaobaoinfotitleOptions4() {
			this.$http.get('option/taobaoinfo/title',
			).then(rs=>{
				this.taobaoinfoChartOptions4 = rs.data.data
			})
		},
		taobaoinfoChat4(e=null) {
			if(this.changeStatQuery(['users'])) {
				document.getElementById('taobaoinfoChart4').setAttribute('style','width: 100%;height: calc(100% - 50px)')
			}
			this.$nextTick(()=>{

				var taobaoinfoChart4 = echarts.init(document.getElementById("taobaoinfoChart4"),'macarons');
				let params = {
				}
				if(this.taobaoinfochartQuery4.title) {
					params.conditionColumn = 'title'
					params.conditionValue = this.taobaoinfochartQuery4.title
				}
				this.$http({
					url: "taobaoinfo/group/property1",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.funnelNum){
								break;
							}
							xAxis.push(res[i].property1);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].property1
							})
						}
						var option = {};
						let titleObj = this.funnel.title
						titleObj.text = '参数1统计'
						
						let legendObj = {
							data: xAxis,
						}
						legendObj = Object.assign(legendObj , this.funnel.legend)
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.funnel.tooltip?this.funnel.tooltip:{})
						let seriesObj = {
							name: '参数1统计',
							data: pArray,
							type: 'funnel',
							left: '10%',
							top: 60,
							bottom: 60,
							width: '80%',
							minSize: '0%',
							maxSize: '100%',
						}
						seriesObj = Object.assign(seriesObj , this.funnel.series)
						const gridObj = this.funnel.grid
						option = {
							backgroundColor: this.funnel.backgroundColor,
							color: this.funnel.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							series: seriesObj,
							grid: gridObj
						}
						// 使用刚指定的配置项和数据显示图表。
						taobaoinfoChart4.setOption(option);

						//根据窗口的大小变动图表
						window.onresize = function() {
							taobaoinfoChart4.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
		gettaobaoinfotitleOptions5() {
			this.$http.get('option/taobaoinfo/title',
			).then(rs=>{
				this.taobaoinfoChartOptions5 = rs.data.data
			})
		},
		taobaoinfoChat5(e=null) {
			if(this.changeStatQuery(['users'])) {
				document.getElementById('taobaoinfoChart5').setAttribute('style','width: 100%;height: calc(100% - 50px)')
			}
			this.$nextTick(()=>{

				var taobaoinfoChart5 = echarts.init(document.getElementById("taobaoinfoChart5"),'macarons');
				let params = {
				}
				if(this.taobaoinfochartQuery5.title) {
					params.conditionColumn = 'title'
					params.conditionValue = this.taobaoinfochartQuery5.title
				}
				this.$http({
					url: "taobaoinfo/group/property2",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.pieNum){
								break;
							}
							xAxis.push(res[i].property2);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].property2
							})
						}
						var option = {};
						let titleObj = this.pie.title
						titleObj.text = '参数2统计'
						
						const legendObj = this.pie.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
						tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
						
						let seriesObj = {
							type: 'pie',
							radius: ['25%', '55%'],
							center: ['50%', '60%'],
							data: pArray,
							emphasis: {
								itemStyle: {
									shadowBlur: 10,
									shadowOffsetX: 0,
									shadowColor: 'rgba(0, 0, 0, 0.5)'
								}
							}
						}
						seriesObj = Object.assign(seriesObj , this.pie.series)
						const gridObj = this.pie.grid
						option = {
							backgroundColor: this.pie.backgroundColor,
							color: this.pie.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						taobaoinfoChart5.setOption(option);
						//根据窗口的大小变动图表
						window.onresize = function() {
							taobaoinfoChart5.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
		gettaobaoinfotitleOptions6() {
			this.$http.get('option/taobaoinfo/title',
			).then(rs=>{
				this.taobaoinfoChartOptions6 = rs.data.data
			})
		},
		taobaoinfoChat6(e=null) {
			if(this.changeStatQuery(['users'])) {
				document.getElementById('taobaoinfoChart6').setAttribute('style','width: 100%;height: calc(100% - 50px)')
			}
			this.$nextTick(()=>{

				var taobaoinfoChart6 = echarts.init(document.getElementById("taobaoinfoChart6"),'macarons');
				let params = {
				}
				if(this.taobaoinfochartQuery6.title) {
					params.conditionColumn = 'title'
					params.conditionValue = this.taobaoinfochartQuery6.title
				}
				this.$http({
					url: "taobaoinfo/group/property3",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.barNum){
								break;
							}
							xAxis.push(res[i].property3);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].property3
							})
						}
						var option = {};
						let titleObj = this.bar.title
						titleObj.text = '参数3统计'
						
						const legendObj = this.bar.legend
						
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
				
						let seriesObj = {
							data: yAxis,
							type: 'bar',
							coordinateSystem: 'polar',
							label: {
								show: true,
								position: 'middle',
								formatter: '{b}: {c}'
							}
						}
						seriesObj = Object.assign(seriesObj , this.bar.series)
						const gridObj = this.bar.grid
						option = {
							backgroundColor: this.bar.backgroundColor,
							color: this.bar.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							polar: {
								radius: [0, '80%']
							},
							angleAxis: {
								// max: 'auto',
								startAngle: 75
							},
							radiusAxis: {
								type: 'category',
								data: xAxis
							},
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						taobaoinfoChart6.setOption(option);
						//根据窗口的大小变动图表
						window.onresize = function() {
							taobaoinfoChart6.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
		gettaobaoinfotitleOptions7() {
			this.$http.get('option/taobaoinfo/title',
			).then(rs=>{
				this.taobaoinfoChartOptions7 = rs.data.data
			})
		},
		taobaoinfoChat7(e=null) {
			if(this.changeStatQuery(['users'])) {
				document.getElementById('taobaoinfoChart7').setAttribute('style','width: 100%;height: calc(100% - 50px)')
			}
			this.$nextTick(()=>{

				var taobaoinfoChart7 = echarts.init(document.getElementById("taobaoinfoChart7"),'macarons');
				let params = {
				}
				if(this.taobaoinfochartQuery7.title) {
					params.conditionColumn = 'title'
					params.conditionValue = this.taobaoinfochartQuery7.title
				}
				this.$http({
					url: "taobaoinfo/group/prosheng",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.barNum){
								break;
							}
							xAxis.push(res[i].prosheng);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].prosheng
							})
						}
						var option = {};
						let titleObj = this.bar.title
						titleObj.text = '省份统计'
						
						const legendObj = this.bar.legend
						
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
						let xAxisObj = this.bar.xAxis
						xAxisObj.type = 'category'
						xAxisObj.data = xAxis
						
						let yAxisObj = this.bar.yAxis
						yAxisObj.type = 'value'
				
						let seriesObj = {
							data: yAxis,
							type: 'bar',
						}
						seriesObj = Object.assign(seriesObj , this.bar.series)
						const gridObj = this.bar.grid
						option = {
							backgroundColor: this.bar.backgroundColor,
							color: this.bar.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						taobaoinfoChart7.setOption(option);
						//根据窗口的大小变动图表
						window.onresize = function() {
							taobaoinfoChart7.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
	}
};
</script>
<style lang="scss" scoped>
	.home-content {
		padding: 0 30px 30px;
		background: url(http://codegen.caihongy.cn/20251223/e2a842fdcb8b40f29998f525fbbcd669.png) no-repeat center top / cover;
		display: flex;
		width: 100%;
		min-height: 100vh;
		flex-wrap: wrap;
		height: auto;
		.home-title {
			padding: 10px 0 0;
			box-shadow: none;
			margin: 10px 0 0;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			transition: 0.3s;
			.titles {
				padding: 0;
				color: #333;
				font-size: 30px;
				line-height: 60px;
				span {
				}
			}
		}
		.home-title:hover {
			transform: translate3d(0, 0px, 0);
		}
		.statis-box {
			margin: 20px 0;
			background: none;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			flex-wrap: wrap;
			.statis1 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 40px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: 600;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis1:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis2 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis2:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis3 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis3:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis4 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis4:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis5 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis5:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis6 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis6:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis7 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis7:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis8 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis8:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis9 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis9:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis10 {
				border: 1px solid #e7e9ec;
				border-radius: 10px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: none;
					display: flex;
					width: 30%;
					align-items: center;
					height: 48px;
					.iconfont {
						border-radius: 100%;
						padding: 0;
						color: #318be3;
						background: #318be315;
						font-weight: 500;
						width: 48px;
						font-size: 32px;
						line-height: 48px;
						text-align: center;
						height: 48px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: center;
					.num {
						margin: 5px 0;
						color: #555;
						font-weight: bold;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #816f77;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis10:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
		}
		// echarts9
		.type9 {
			padding: 0;
			align-content: flex-start;
			background: none;
			display: flex;
			width: 100%;
			justify-content: space-between;
			flex-wrap: wrap;
			height: auto;
			.echarts1 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts1:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts2 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts2:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts3 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts3:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts4 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts4:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts5 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(100% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts5:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts6 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts6:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts7 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts7:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts8 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts8:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts9 {
				border: 1px solid #e7e9ec;
				border-radius: 8px;
				padding: 20px;
				box-shadow: 0 3px 6px rgba(0,0,0,.06);
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts9:hover {
				box-shadow: 0 3px 9px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
		}
	}
	
	.echarts-flag-2 {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		padding: 10px 20px;
		background: rebeccapurple;
	
		&>div {
			width: 32%;
			height: 300px;
			margin: 10px 0;
			background: rgba(255,255,255,.1);
			border-radius: 8px;
			padding: 10px 20px;
		}
	}
	.animate__animated {
		animation-fill-mode: none;
	}
</style>
