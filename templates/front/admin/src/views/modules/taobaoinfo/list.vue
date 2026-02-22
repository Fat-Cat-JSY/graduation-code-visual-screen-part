  
<template>
	<div class="main-content" :style='{"width":"100%","padding":"20px 30px 30px"}'>
		<!-- 列表页 -->
		<template v-if="showFlag ">
			<el-form class="center-form-pv" :style='{"border":"1px solid #e7e9ec","padding":"20px 20px 0","boxShadow":"0 3px 6px rgba(0,0,0,.06)","margin":"0 0 20px","borderRadius":"10px","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","justifyContent":"space-between"}' :inline="true" :model="searchForm">
				<el-row :style='{"padding":"0px","boxShadow":"none","borderRadius":"10px","flexWrap":"wrap","display":"flex","width":"auto","position":"relative"}' >
					<div  :style='{"margin":"0 10px 20px 0","display":"flex"}'>
						<label :style='{"margin":"0 10px 0 0","whiteSpace":"nowrap","color":"#666","display":"inline-block","lineHeight":"40px","fontSize":"16px","fontWeight":"500","height":"40px"}' class="item-label">省</label>
						<el-input v-model="searchForm.prosheng" placeholder="省" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div  :style='{"margin":"0 10px 20px 0","display":"flex"}'>
						<label :style='{"margin":"0 10px 0 0","whiteSpace":"nowrap","color":"#666","display":"inline-block","lineHeight":"40px","fontSize":"16px","fontWeight":"500","height":"40px"}' class="item-label">市</label>
						<el-input v-model="searchForm.procity" placeholder="市" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div  :style='{"margin":"0 10px 20px 0","display":"flex"}'>
						<label :style='{"margin":"0 10px 0 0","whiteSpace":"nowrap","color":"#666","display":"inline-block","lineHeight":"40px","fontSize":"16px","fontWeight":"500","height":"40px"}' class="item-label">标题</label>
						<el-input v-model="searchForm.title" placeholder="标题" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<el-button class="search" type="success" @click="search()">
						<span class="icon iconfont icon-fangdajing01" :style='{"margin":"0 0px","fontSize":"16px","color":"#fff","height":"40px"}'></span>
						查询
					</el-button>
				</el-row>

				<el-row class="actions" :style='{"width":"auto","margin":"0px 0 20px -4px","flexWrap":"wrap","display":"flex"}'>
					<el-button class="add" v-if="isAuth('taobaoinfo','新增')" type="success" @click="addOrUpdateHandler()">
						<span class="icon iconfont icon-tianjia16" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						添加
					</el-button>
					<el-button class="del" v-if="isAuth('taobaoinfo','删除')" :disabled="dataListSelections.length?false:true" type="danger" @click="deleteHandler()">
						<span class="icon iconfont icon-shanchu6" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						删除
					</el-button>


					<el-button class="btn18" v-if="isAuth('taobaoinfo','爬取数据')" type="success" @click="spider()">
						<span class="icon iconfont icon-shuju17" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						爬取数据
					</el-button>
					<el-button class="btn18" type="success" @click="cleanClick()">
						<span class="icon iconfont icon-shuju17" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						数据清洗
					</el-button>
					<el-button v-if="isAuth('taobaoinfo','训练模型')" class="btn18" type="success" @click="dlRecomClick()">
						<span class="icon iconfont icon-shuju17" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						训练模型					</el-button>
					<el-button class="btn18" v-if="isAuth('taobaoinfo','价格统计')" type="success" @click="chartDialogShow1">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						价格统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('taobaoinfo','销售量统计')" type="success" @click="chartDialogShow2">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						销售量统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('taobaoinfo','标签统计')" type="success" @click="chartDialogShow3">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						标签统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('taobaoinfo','参数1统计')" type="success" @click="chartDialogShow4">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						参数1统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('taobaoinfo','参数2统计')" type="success" @click="chartDialogShow5">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						参数2统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('taobaoinfo','参数3统计')" type="success" @click="chartDialogShow6">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						参数3统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('taobaoinfo','省份统计')" type="success" @click="chartDialogShow7">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"auto"}'></span>
						省份统计
					</el-button>
				</el-row>
			</el-form>
			<div :style='{"border":"1px solid #e7e9ec","width":"100%","padding":"0px","boxShadow":"0 3px 6px rgba(0,0,0,.06)","borderRadius":"10px","background":"#fff"}'>
				<el-table class="tables"
					:stripe='false'
					:style='{"padding":"0","borderColor":"#e7e8fc","borderRadius":"10px","borderWidth":"0px 0 0 0px","background":"#fff","width":"100%","borderStyle":"solid"}' 
					:border='false'
					v-if="isAuth('taobaoinfo','查看')"
					:data="dataList"
					v-loading="dataListLoading"
					@selection-change="selectionChangeHandler">
					<el-table-column :resizable='true' type="selection" align="center" width="50"></el-table-column>
					<el-table-column :resizable='true' :sortable='true' label="序号" type="index" width="50" />
					<el-table-column :resizable='true' :sortable='true'
												prop="prosheng"
						label="省">
						<template slot-scope="scope">
							{{scope.row.prosheng}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="procity"
						label="市">
						<template slot-scope="scope">
							{{scope.row.procity}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="title"
						label="标题">
						<template slot-scope="scope">
							{{scope.row.title}}
						</template>
					</el-table-column>
					<el-table-column  :resizable='true' prop="imgurl" width="200" label="图片">
						<template slot-scope="scope">
							<div v-if="scope.row.imgurl">
								<img v-if="scope.row.imgurl.substring(0,4)=='http'&&scope.row.imgurl.split(',w').length>1" :src="scope.row.imgurl" width="100" height="100" style="object-fit: cover" @click="imgPreView(scope.row.imgurl)">
								<img v-else-if="scope.row.imgurl.substring(0,4)=='http'" :src="scope.row.imgurl.split(',')[0]" width="100" height="100" style="object-fit: cover" @click="imgPreView(scope.row.imgurl.split(',')[0])">
								<img v-else :src="$base.url+scope.row.imgurl.split(',')[0]" width="100" height="100" style="object-fit: cover" @click="imgPreView($base.url+scope.row.imgurl.split(',')[0])">
							</div>
							<div v-else>无图片</div>
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="jiage"
						label="价格">
						<template slot-scope="scope">
							{{scope.row.jiage}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="salesnum"
						label="销售量">
						<template slot-scope="scope">
							{{scope.row.salesnum}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="shoptag"
						label="标签">
						<template slot-scope="scope">
							{{scope.row.shoptag}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="baoyounew"
						label="包邮">
						<template slot-scope="scope">
							{{scope.row.baoyounew}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="property1"
						label="参数1">
						<template slot-scope="scope">
							{{scope.row.property1}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="property2"
						label="参数2">
						<template slot-scope="scope">
							{{scope.row.property2}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="property3"
						label="参数3">
						<template slot-scope="scope">
							{{scope.row.property3}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="nickname"
						label="商家账号">
						<template slot-scope="scope">
							{{scope.row.nickname}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="shopname"
						label="商家名称">
						<template slot-scope="scope">
							{{scope.row.shopname}}
						</template>
					</el-table-column>
					<el-table-column :resizable='true' :sortable='true'
												prop="storeupnum"
						label="收藏数">
						<template slot-scope="scope">
							{{scope.row.storeupnum}}
						</template>
					</el-table-column>
					<el-table-column width="300" label="操作">
						<template slot-scope="scope">
							<el-button class="view" v-if=" isAuth('taobaoinfo','查看')" type="success" @click="addOrUpdateHandler(scope.row.id,'info')">
								<span class="icon iconfont icon-chakan2" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"40px"}'></span>
								查看
							</el-button>
							<el-button class="edit" v-if=" isAuth('taobaoinfo','修改') " type="success" @click="addOrUpdateHandler(scope.row.id)">
								<span class="icon iconfont icon-xiugai1" :style='{"margin":"0 0px","fontSize":"16px","color":"inherit","height":"40px"}'></span>
								修改
							</el-button>




							<el-button class="del" v-if="isAuth('taobaoinfo','删除')" type="primary" @click="deleteHandler(scope.row.id)">
								<span class="icon iconfont icon-shanchu6" :style='{"margin":"0 0px","fontSize":"14px","color":"inherit","height":"40px"}'></span>
								删除
							</el-button>
						</template>
					</el-table-column>
				</el-table>
			</div>
			<el-pagination
				@size-change="sizeChangeHandle"
				@current-change="currentChangeHandle"
				:current-page="pageIndex"
				background
				:page-sizes="[10, 50, 100, 200]"
				:page-size="pageSize"
				:layout="layouts.join()"
				:total="totalPage"
				prev-text="< "
				next-text="> "
				:hide-on-single-page="false"
				:style='{"padding":"0","margin":"20px 0 0","whiteSpace":"nowrap","color":"#333","textAlign":"center","width":"100%","fontWeight":"500"}'
			></el-pagination>
		</template>
		
		<!-- 添加/修改页面  将父组件的search方法传递给子组件-->
		<add-or-update v-if="addOrUpdateFlag" :parent="this" ref="addOrUpdate"></add-or-update>




		<el-dialog
			class="chartDialog"
			:visible.sync="chartVisiable1"
			width="800">
			<div v-if="changeStatQuery(['users'])" style="display: flex;width: 100%;align-items: center;margin: 0 0 20px;">
				<div style="padding: 0 10px;">标题</div>
				<el-select v-model="chartQuery1.title" placeholder="请选择" @change="chartDialog1" clearable>
					<el-option v-for="item in titleChartOptions1" :label="item" :value="item"></el-option>
				</el-select>
			</div>
			<div id="jiageChart1" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartVisiable1 = false">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			class="chartDialog"
			:visible.sync="chartVisiable2"
			width="800">
			<div v-if="changeStatQuery(['users'])" style="display: flex;width: 100%;align-items: center;margin: 0 0 20px;">
				<div style="padding: 0 10px;">标题</div>
				<el-select v-model="chartQuery2.title" placeholder="请选择" @change="chartDialog2" clearable>
					<el-option v-for="item in titleChartOptions2" :label="item" :value="item"></el-option>
				</el-select>
			</div>
			<div id="salesnumChart2" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartVisiable2 = false">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			class="chartDialog"
			:visible.sync="chartVisiable3"
			width="800">
			<div v-if="changeStatQuery(['users'])" style="display: flex;width: 100%;align-items: center;margin: 0 0 20px;">
				<div style="padding: 0 10px;">标题</div>
				<el-select v-model="chartQuery3.title" placeholder="请选择" @change="chartDialog3" clearable>
					<el-option v-for="item in titleChartOptions3" :label="item" :value="item"></el-option>
				</el-select>
			</div>
			<div id="shoptagChart3" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartVisiable3 = false">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			class="chartDialog"
			:visible.sync="chartVisiable4"
			width="800">
			<div v-if="changeStatQuery(['users'])" style="display: flex;width: 100%;align-items: center;margin: 0 0 20px;">
				<div style="padding: 0 10px;">标题</div>
				<el-select v-model="chartQuery4.title" placeholder="请选择" @change="chartDialog4" clearable>
					<el-option v-for="item in titleChartOptions4" :label="item" :value="item"></el-option>
				</el-select>
			</div>
			<div id="property1Chart4" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartVisiable4 = false">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			class="chartDialog"
			:visible.sync="chartVisiable5"
			width="800">
			<div v-if="changeStatQuery(['users'])" style="display: flex;width: 100%;align-items: center;margin: 0 0 20px;">
				<div style="padding: 0 10px;">标题</div>
				<el-select v-model="chartQuery5.title" placeholder="请选择" @change="chartDialog5" clearable>
					<el-option v-for="item in titleChartOptions5" :label="item" :value="item"></el-option>
				</el-select>
			</div>
			<div id="property2Chart5" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartVisiable5 = false">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			class="chartDialog"
			:visible.sync="chartVisiable6"
			width="800">
			<div v-if="changeStatQuery(['users'])" style="display: flex;width: 100%;align-items: center;margin: 0 0 20px;">
				<div style="padding: 0 10px;">标题</div>
				<el-select v-model="chartQuery6.title" placeholder="请选择" @change="chartDialog6" clearable>
					<el-option v-for="item in titleChartOptions6" :label="item" :value="item"></el-option>
				</el-select>
			</div>
			<div id="property3Chart6" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartVisiable6 = false">返回</el-button>
			</span>
		</el-dialog>
		<el-dialog
			class="chartDialog"
			:visible.sync="chartVisiable7"
			width="800">
			<div v-if="changeStatQuery(['users'])" style="display: flex;width: 100%;align-items: center;margin: 0 0 20px;">
				<div style="padding: 0 10px;">标题</div>
				<el-select v-model="chartQuery7.title" placeholder="请选择" @change="chartDialog7" clearable>
					<el-option v-for="item in titleChartOptions7" :label="item" :value="item"></el-option>
				</el-select>
			</div>
			<div id="proshengChart7" style="width:100%;height:600px;"></div>
			<span slot="footer" class="dialog-footer">
				<el-button @click="chartVisiable7 = false">返回</el-button>
			</span>
		</el-dialog>

		<el-dialog title="预览图" :visible.sync="previewVisible" width="50%">
			<img :src="previewImg" alt="" style="width: 100%;">
		</el-dialog>
	</div>
</template>

<script>
	import * as echarts from 'echarts'
	import chinaJson from "@/components/echarts/china.json";
	import axios from 'axios';
	import AddOrUpdate from "./add-or-update";
	import {
		Loading
	} from 'element-ui';
	export default {
		data() {
			return {
				indexQueryCondition: '',
				searchForm: {
					key: ""
				},
				form:{},
				dataList: [],
				pageIndex: 1,
				pageSize: 10,
				totalPage: 0,
				dataListLoading: false,
				dataListSelections: [],
				showFlag: true,
				line: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":10,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"interval":0,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"showSymbol":true,"symbol":"arrow","symbolSize":12},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"}},
				bar: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":12,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":10,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"interval":0,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"right":"20","top":"60","left":"20","bottom":"20","containLabel":true},"series":{"barWidth":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"barBorderRadius":[5,5,5,5],"borderWidth":0,"opacity":1,"shadowColor":"#000"},"colorBy":"data","barCategoryGap":"40%"},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"subtext":"","shadowBlur":0,"bottom":"auto","show":true,"right":"auto","subtextStyle":{"padding":[5,0,0,0],"borderColor":"red","color":"red","borderWidth":10},"top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"base":{"animate":false,"interval":2000}},
				pie: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"title":{"borderType":"solid","padding":[5,0,0,0],"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":14,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":[5,0,0,0],"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":0,"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#eee","color":"inherit","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","formatter":"{b}: ({d}%)","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#666","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false}}},
				funnel: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"title":{"borderType":"solid","padding":2,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"center","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#666","textShadowColor":"transparent","fontSize":14,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false}}},
				boardBase: {"funnelNum":8,"lineNum":8,"radarNum":8,"gaugeNum":8,"barNum":8,"pieNum":8},
				gauge: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#8ebc74","#6ad2ff","#89e6d8","#73ded4","#73c0de","#3ba272","#4495ac","#4479ac","#ea7ccc"],"title":{"top":"top","left":"left","textStyle":{"fontSize":14,"lineHeight":24,"color":"#333","fontWeight":600}},"series":{"pointer":{"offsetCenter":[0,"10%"],"icon":"path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z","width":8,"length":"80%"},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"opacity":0.5,"shadowBlur":1,"shadowColor":"#000"},"roundCap":true},"anchor":{"show":true,"itemStyle":{"color":"inherit"},"size":18,"showAbove":true},"emphasis":{"disabled":false},"progress":{"show":true,"roundCap":true,"overlap":true},"splitNumber":25,"detail":{"formatter":"{value}","backgroundColor":"inherit","color":"#fff","borderRadius":3,"width":20,"fontSize":12,"height":10},"title":{"fontSize":14},"animation":true}},
				radar: {"backgroundColor":"transparent","radar":{"shape":"circle"},"color":["#365E77","#DF308C","#0CB906","#7690cb","#49ada0","#5BBAEC","#a68a28","#EE142F","#FFE9E9"],"legend":{"padding":5,"itemGap":5,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":4,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"auto","itemWidth":4,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#7987FD"}},"title":{"top":"top","left":"left","textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":14,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#666","textShadowBlur":0}}},
				titleChartOptions1: [],
				chartQuery1: {},
				chartVisiable1: false,
				titleChartOptions2: [],
				chartQuery2: {},
				chartVisiable2: false,
				titleChartOptions3: [],
				chartQuery3: {},
				chartVisiable3: false,
				titleChartOptions4: [],
				chartQuery4: {},
				chartVisiable4: false,
				titleChartOptions5: [],
				chartQuery5: {},
				chartVisiable5: false,
				titleChartOptions6: [],
				chartQuery6: {},
				chartVisiable6: false,
				titleChartOptions7: [],
				chartQuery7: {},
				chartVisiable7: false,
				addOrUpdateFlag:false,
				layouts: ["total","prev","pager","next","sizes","jumper"],
				previewImg: '',
				previewVisible: false,
			};
		},
		created() {
			if(this.statType) {
				return false
			}
			this.init();
			this.getDataList();
		},
		mounted() {
		},
		watch: {
		},
		filters: {
			htmlfilter: function (val) {
				return val.replace(/<[^>]*>/g).replace(/undefined/g,'');
			}
		},
		computed: {
			tablename(){
				return this.$storage.get('sessionTable')
			},
			role(){
				return this.$storage.get('role')
			},
		},
		components: {
			AddOrUpdate,
		},
		methods: {
			queryChange(arr){
				for(let x in arr) {
					if(arr[x] == this.role) {
						return true
					}
				}
				return false
			},
			imgPreView(url){
				this.previewImg = url
				this.previewVisible = true
				
			},
			linkOthers(url) {
				window.open(url);//打开一个新的标签页
			},
			changeStatQuery(arr) {
				if(arr.length==1) {
					if(arr[0] == 'users'&&this.$storage.get("sessionTable")=='users') {
						return true
					}
				}
				for(let x in arr) {
					if(arr[x] == this.role) {
						return true
					}
				}
				return false
			},
			chartDialogShow1() {
				this.chartVisiable1 = true
				this.$http.get('option/taobaoinfo/title',
				).then(rs=>{
					this.titleChartOptions1 = rs.data.data
				})
				this.chartDialog1()
			},
			// 统计接口1
			chartDialog1() {
				this.$nextTick(()=>{
					var jiageChart1 = echarts.init(document.getElementById("jiageChart1"),'macarons');
					let params = {}
					if(this.chartQuery1.title) {
						params.conditionColumn = 'title'
						params.conditionValue = this.chartQuery1.title
					}
					this.$http({
						url: "taobaoinfo/value/title/jiage",
						method: "get",
						params
					}).then(({data})=>{
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
							jiageChart1.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								jiageChart1.resize();
							};
						}
					})
				})
			},
			chartDialogShow2() {
				this.chartVisiable2 = true
				this.$http.get('option/taobaoinfo/title',
				).then(rs=>{
					this.titleChartOptions2 = rs.data.data
				})
				this.chartDialog2()
			},
			// 统计接口2
			chartDialog2() {
				this.$nextTick(()=>{
					var salesnumChart2 = echarts.init(document.getElementById("salesnumChart2"),'macarons');
					let params = {}
					if(this.chartQuery2.title) {
						params.conditionColumn = 'title'
						params.conditionValue = this.chartQuery2.title
					}
					this.$http({
						url: "taobaoinfo/value/title/salesnum",
						method: "get",
						params
					}).then(({data})=>{
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
								grid: gridObj,
								tooltip: tooltipObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							salesnumChart2.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								salesnumChart2.resize();
							};
						}
					})
				})
			},
			chartDialogShow3() {
				this.chartVisiable3 = true
				this.$http.get('option/taobaoinfo/title',
				).then(rs=>{
					this.titleChartOptions3 = rs.data.data
				})
				this.chartDialog3()
			},
			// 统计接口3
			chartDialog3() {
				this.$nextTick(()=>{
					var shoptagChart3 = echarts.init(document.getElementById("shoptagChart3"),'macarons');
					let params = {}
					if(this.chartQuery3.title) {
						params.conditionColumn = 'title'
						params.conditionValue = this.chartQuery3.title
					}
					this.$http({
						url: "taobaoinfo/group/shoptag",
						method: "get",
						params
					}).then(({data})=>{
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
								grid: gridObj,
								tooltip: tooltipObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							shoptagChart3.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								shoptagChart3.resize();
							};
						}
					})
				})
			},
			chartDialogShow4() {
				this.chartVisiable4 = true
				this.$http.get('option/taobaoinfo/title',
				).then(rs=>{
					this.titleChartOptions4 = rs.data.data
				})
				this.chartDialog4()
			},
			// 统计接口4
			chartDialog4() {
				this.$nextTick(()=>{
					var property1Chart4 = echarts.init(document.getElementById("property1Chart4"),'macarons');
					let params = {}
					if(this.chartQuery4.title) {
						params.conditionColumn = 'title'
						params.conditionValue = this.chartQuery4.title
					}
					this.$http({
						url: "taobaoinfo/group/property1",
						method: "get",
						params
					}).then(({data})=>{
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
							property1Chart4.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								property1Chart4.resize();
							};
						}
					})
				})
			},
			chartDialogShow5() {
				this.chartVisiable5 = true
				this.$http.get('option/taobaoinfo/title',
				).then(rs=>{
					this.titleChartOptions5 = rs.data.data
				})
				this.chartDialog5()
			},
			// 统计接口5
			chartDialog5() {
				this.$nextTick(()=>{
					var property2Chart5 = echarts.init(document.getElementById("property2Chart5"),'macarons');
					let params = {}
					if(this.chartQuery5.title) {
						params.conditionColumn = 'title'
						params.conditionValue = this.chartQuery5.title
					}
					this.$http({
						url: "taobaoinfo/group/property2",
						method: "get",
						params
					}).then(({data})=>{
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
								grid: gridObj,
								tooltip: tooltipObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							property2Chart5.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								property2Chart5.resize();
							};
						}
					})
				})
			},
			chartDialogShow6() {
				this.chartVisiable6 = true
				this.$http.get('option/taobaoinfo/title',
				).then(rs=>{
					this.titleChartOptions6 = rs.data.data
				})
				this.chartDialog6()
			},
			// 统计接口6
			chartDialog6() {
				this.$nextTick(()=>{
					var property3Chart6 = echarts.init(document.getElementById("property3Chart6"),'macarons');
					let params = {}
					if(this.chartQuery6.title) {
						params.conditionColumn = 'title'
						params.conditionValue = this.chartQuery6.title
					}
					this.$http({
						url: "taobaoinfo/group/property3",
						method: "get",
						params
					}).then(({data})=>{
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
								grid: gridObj,
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
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							property3Chart6.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								property3Chart6.resize();
							};
						}
					})
				})
			},
			chartDialogShow7() {
				this.chartVisiable7 = true
				this.$http.get('option/taobaoinfo/title',
				).then(rs=>{
					this.titleChartOptions7 = rs.data.data
				})
				this.chartDialog7()
			},
			// 统计接口7
			chartDialog7() {
				this.$nextTick(()=>{
					var proshengChart7 = echarts.init(document.getElementById("proshengChart7"),'macarons');
					let params = {}
					if(this.chartQuery7.title) {
						params.conditionColumn = 'title'
						params.conditionValue = this.chartQuery7.title
					}
					this.$http({
						url: "taobaoinfo/group/prosheng",
						method: "get",
						params
					}).then(({data})=>{
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
								grid: gridObj,
								tooltip: tooltipObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							proshengChart7.setOption(option);
							  //根据窗口的大小变动图表
							window.onresize = function() {
								proshengChart7.resize();
							};
						}
					})
				})
			},
			init () {
			},
			search() {
				this.pageIndex = 1;
				this.getDataList();
			},

			// 获取数据列表
			getDataList() {
				this.dataListLoading = true;
				let params = {
					page: this.pageIndex,
					limit: this.pageSize,
					sort: 'id',
					order: 'desc',
				}
				if(this.searchForm.prosheng!='' && this.searchForm.prosheng!=undefined){
					params['prosheng'] = '%' + this.searchForm.prosheng + '%'
				}
				if(this.searchForm.procity!='' && this.searchForm.procity!=undefined){
					params['procity'] = '%' + this.searchForm.procity + '%'
				}
				if(this.searchForm.title!='' && this.searchForm.title!=undefined){
					params['title'] = '%' + this.searchForm.title + '%'
				}
				let user = JSON.parse(this.$storage.getObj('userForm'))
				this.$http({
					url: "taobaoinfo/page",
					method: "get",
					params: params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.dataList = data.data.list;
						this.totalPage = data.data.total;
					} else {
						this.dataList = [];
						this.totalPage = 0;
					}
					this.dataListLoading = false;
				});
			},
			// 每页数
			sizeChangeHandle(val) {
				this.pageSize = val;
				this.pageIndex = 1;
				this.getDataList();
			},
			// 当前页
			currentChangeHandle(val) {
				this.pageIndex = val;
				this.getDataList();
			},
			// 多选
			selectionChangeHandler(val) {
				this.dataListSelections = val;
			},
			// 添加/修改
			addOrUpdateHandler(id,type) {
				this.showFlag = false;
				this.addOrUpdateFlag = true;
				this.crossAddOrUpdateFlag = false;
				if(type!='info'&&type!='msg'){
					type = 'else';
				}
				this.$nextTick(() => {
					this.$refs.addOrUpdate.init(id,type );
				});
			},
			// 删除
			async deleteHandler(id ) {
				var ids = id? [Number(id)]: this.dataListSelections.map(item => {
					return Number(item.id);
				});
				await this.$confirm(`确定进行[${id ? "删除" : "批量删除"}]操作?`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(async () => {
					await this.$http({
						url: "taobaoinfo/delete",
						method: "post",
						data: ids
					}).then(async ({ data }) => {
						if (data && data.code === 0) {
							for(let x in ids){
								await this.$http.get('storeup/list',{params: {
									page: 1,
									limit: 100,
									refid: ids[x],
									tablename: 'taobaoinfo'
								}}).then(async obj=>{
									if(obj.data&&obj.data.code==0){
										if(obj.data.data.list.length){
											let arr = []
											for(let i in obj.data.data.list){
												arr.push(obj.data.data.list[i].id)
											}
											await this.$http.post('storeup/delete',arr).then(()=>{})
										}
									}
								})
							}
							this.$message({
								message: "操作成功",
								type: "success",
								duration: 1500,
								onClose: () => {
									this.search();
								}
							});
			
						} else {
							this.$message.error(data.msg);
						}
					});
				});
			},

			spider() {
				this.$message({
					message: "数据爬取中...",
					type: "success",
					duration: 3000,
					onClose: () => {
						this.search();
					}
				});
				this.$http({
					url: "spider/taobaoinfo",
					method: "get",
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.$message({
							message: "爬取完成",
							type: "success",
							duration: 1500,
							onClose: () => {
								this.getDataList(this.roleName);
							}
						});
					} else {
						this.$alert(data.msg)
					}
				});
			},

			cleanClick() {
				this.$confirm(`是否进行数据清洗?`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(()=>{
					let loading = null
					loading = Loading.service({
						target: this.$refs['roleMenuBox'],
						fullscreen: false,
						text: '数据清洗中...'
					})
					this.$http({
						url: 'taobaoinfo/cleanse',
						method: 'get'
					}).then(res=>{
						if(res.data&&res.data.code==0){
							if (loading) loading.close()
							this.$message({
								message: "数据清洗完成！",
								type: "success",
								duration: 1500,
								onClose: () => {
									this.getDataList()
								}
							});
						}
					})
				})
			},
			dlRecomClick() {
				this.$confirm(`是否进行模型训练？`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(()=>{
					let loading = null
					loading = Loading.service({
						target: this.$refs['roleMenuBox'],
						fullscreen: false,
						text: '训练中...'
					})
					this.$http({
						url: 'taobaoinfo/trainRecommend',
						method: 'get'
					}).then(res=>{
						if(res.data&&res.data.code==0){
							if (loading) loading.close()
							this.$message({
								message: res.data.msg,
								type: "success",
								duration: 1500,
								onClose: () => {
									this.getDataList()
								}
							});
						}
					})
				})
			},
		}

	};
</script>
<style lang="scss" scoped>
	
	.center-form-pv {
		.el-date-editor.el-input {
			width: auto;
		}
	}
	
	.el-input {
		width: auto;
	}
	
	// form
	.center-form-pv .el-input {
		width: 100%;
	}
	.center-form-pv .el-input /deep/ .el-input__inner {
		border: 1px solid #eee;
		border-radius: 6px;
		padding: 0 12px;
		box-shadow: none;
		outline: none;
		color: #333;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 36px;
	}
	.center-form-pv .el-select {
		width: 100%;
	}
	.center-form-pv .el-select /deep/ .el-input__inner {
		border: 1px solid #eee;
		border-radius: 6px;
		padding: 0 10px;
		box-shadow: none;
		outline: none;
		color: #333;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 36px;
	}
	.center-form-pv .el-date-editor {
		width: 100%;
	}
	
	.center-form-pv .el-date-editor /deep/ .el-input__inner {
		border: 1px solid #eee;
		border-radius: 6px;
		padding: 0 10px 0 30px;
		box-shadow: none;
		outline: none;
		color: #333;
		background: #fff;
		width: 100%;
		font-size: 16px;
		height: 36px;
	}
	
	.center-form-pv .search {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 12px 0 10px;
		outline: none;
		color: #fff;
		background: #0f79f1;
		width: auto;
		font-size: 16px;
		height: 36px;
	}
	
	.center-form-pv .search:hover {
		opacity: 0.8;
	}
	
	.center-form-pv .actions .add {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 10px;
		margin: 4px;
		outline: none;
		color: #fff;
		background: #0f79f1;
		width: auto;
		font-size: 14px;
		height: 36px;
	}
	
	.center-form-pv .actions .add:hover {
		opacity: 0.8;
	}
	
	.center-form-pv .actions .del {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 10px;
		margin: 4px;
		outline: none;
		color: #fff;
		background: #db562d;
		width: auto;
		font-size: 14px;
		height: 36px;
	}
	
	.center-form-pv .actions .del:hover {
		opacity: 0.8;
	}
	
	.center-form-pv .actions .statis {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 10px;
		margin: 4px;
		outline: none;
		color: #fff;
		background: #6ba54a;
		width: auto;
		font-size: 14px;
		height: 36px;
	}
	
	.center-form-pv .actions .statis:hover {
		opacity: 0.8;
	}
	
	.center-form-pv .actions .btn18 {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 10px;
		margin: 4px;
		outline: none;
		color: #fff;
		background: #666;
		width: auto;
		font-size: 14px;
		height: 36px;
	}
	
	.center-form-pv .actions .btn18:hover {
		opacity: 0.8;
	}
	
	// table
	.el-table /deep/ .el-table__header-wrapper thead {
		color: #999;
		font-weight: 500;
		width: 100%;
	}
	
	.el-table /deep/ .el-table__header-wrapper thead tr {
		background: none;
	}
	
	.el-table /deep/ .el-table__header-wrapper thead tr th {
		padding: 12px 0;
		background: #f9f9fa;
		border-color: #f6f6f6;
		border-width: 0 0px 1px 0;
		border-style: solid;
		text-align: center;
	}

	.el-table /deep/ .el-table__header-wrapper thead tr th .cell {
		padding: 0 0 0 5px;
		word-wrap: normal;
		color: #333;
		white-space: normal;
		font-weight: bold;
		display: flex;
		vertical-align: middle;
		font-size: 14px;
		line-height: 24px;
		text-overflow: ellipsis;
		word-break: break-all;
		width: 100%;
		justify-content: flex-start;
		align-items: center;
		position: relative;
		min-width: 110px;
	}

	.el-table /deep/ .el-table__body-wrapper {
		position: relative;
	}
	.el-table /deep/ .el-table__body-wrapper tbody {
		width: 100%;
	}

	.el-table /deep/ .el-table__body-wrapper tbody tr {
		background: #fff;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
		padding: 4px 0;
		color: #333;
		background: none;
		border-color: #f6f6f6;
		border-width: 0 0px 1px 0;
		border-style: solid;
		text-align: left;
	}
	
		
	.el-table /deep/ .el-table__body-wrapper tbody tr:hover td {
		padding: 4px 0;
		color: #333;
		background: #f9f9fb;
		border-color: #f6f6f6;
		border-width: 0 0px 1px 0;
		border-style: solid;
		text-align: left;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
		padding: 4px 0;
		color: #333;
		background: none;
		border-color: #f6f6f6;
		border-width: 0 0px 1px 0;
		border-style: solid;
		text-align: left;
	}

	.el-table /deep/ .el-table__body-wrapper tbody tr td .cell {
		padding: 0 0 0 5px;
		overflow: hidden;
		word-break: break-all;
		white-space: normal;
		font-size: inherit;
		line-height: 24px;
		text-overflow: ellipsis;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .view {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 0px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #0f79f1;
		background: none;
		width: auto;
		font-size: 14px;
		height: 32px;
		order: 3;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .view:hover {
		opacity: 0.8;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .add {
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .add:hover {
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .edit {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 0px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #8ebc74;
		background: none;
		width: auto;
		font-size: 14px;
		height: 32px;
		order: -1;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .edit:hover {
		opacity: 0.8;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .del {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 0px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #e56060;
		background: none;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .del:hover {
		opacity: 0.8;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .btn8 {
		border: 0;
		cursor: pointer;
		border-radius: 6px;
		padding: 0 0px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #333;
		background: none;
		width: auto;
		font-size: 14px;
		height: 32px;
		order: 5;
	}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .btn8:hover {
		opacity: 0.8;
	}
	
	// pagination
	.main-content .el-pagination /deep/ .el-pagination__total {
		margin: 0 auto 0 0;
		color: #666;
		font-weight: 400;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		line-height: 28px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .btn-prev {
		border: 1px solid #e7e9ec;
		border-radius: 2px;
		padding: 0;
		margin: 0 5px;
		color: #666;
		background: #fff;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		line-height: 28px;
		min-width: 35px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .btn-next {
		border: 1px solid #e7e9ec;
		border-radius: 2px;
		padding: 0;
		margin: 0 5px;
		color: #666;
		background: #fff;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		line-height: 28px;
		min-width: 35px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .btn-prev:disabled {
		border: 1px solid #e7e9ec;
		cursor: not-allowed;
		border-radius: 2px;
		padding: 0;
		margin: 0 5px;
		color: #666;
		background: #eee;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		line-height: 28px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .btn-next:disabled {
		border: 1px solid #e7e9ec;
		cursor: not-allowed;
		border-radius: 2px;
		padding: 0;
		margin: 0 5px;
		color: #666;
		background: #eee;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		line-height: 28px;
		height: 28px;
	}

	.main-content .el-pagination /deep/ .el-pager {
		padding: 0;
		margin: 0;
		display: inline-block;
		vertical-align: top;
	}

	.main-content .el-pagination /deep/ .el-pager .number {
		cursor: pointer;
		border: 1px solid #e7e9ec;
		padding: 0 4px;
		margin: 0 5px;
		color: #666;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		line-height: 28px;
		border-radius: 2px;
		background: #fff;
		text-align: center;
		min-width: 30px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pager .number:hover {
		cursor: pointer;
		padding: 0 4px;
		margin: 0 5px;
		color: #fff;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		border-color: #fbd35a;
		line-height: 28px;
		border-radius: 2px;
		background: #0f79f1;
		text-align: center;
		min-width: 30px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pager .number.active {
		cursor: default;
		padding: 0 4px;
		margin: 0 5px;
		color: #fff;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		border-color: #fbd35a;
		line-height: 28px;
		border-radius: 2px;
		background: #0f79f1;
		text-align: center;
		min-width: 30px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes {
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		line-height: 28px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input {
		margin: 0 5px;
		width: 100px;
		position: relative;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input .el-input__inner {
		border: 1px solid #e7e9ec;
		cursor: pointer;
		padding: 0 25px 0 8px;
		color: #606266;
		display: inline-block;
		font-size: 15px;
		line-height: 28px;
		border-radius: 3px;
		outline: 0;
		background: #FFF;
		width: 100%;
		text-align: center;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input span.el-input__suffix {
		top: 0;
		position: absolute;
		right: 0;
		height: 100%;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input .el-input__suffix .el-select__caret {
		cursor: pointer;
		color: #C0C4CC;
		width: 25px;
		font-size: 15px;
		line-height: 28px;
		text-align: center;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__jump {
		margin: 0 0 0 24px;
		color: #606266;
		display: inline-block;
		vertical-align: top;
		font-size: 15px;
		line-height: 28px;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__jump .el-input {
		border-radius: 3px;
		padding: 0 2px;
		margin: 0 2px;
		display: inline-block;
		width: 50px;
		font-size: 15px;
		line-height: 18px;
		position: relative;
		text-align: center;
		height: 28px;
	}
	
	.main-content .el-pagination /deep/ .el-pagination__jump .el-input .el-input__inner {
		border: 1px solid #e7e9ec;
		cursor: pointer;
		padding: 0 3px;
		color: #606266;
		display: inline-block;
		font-size: 15px;
		line-height: 28px;
		border-radius: 3px;
		outline: 0;
		background: #FFF;
		width: 100%;
		text-align: center;
		height: 28px;
	}
	
	// list one
	.one .list1-view {
		border: 0;
		cursor: pointer;
		border-radius: 4px;
		padding: 0 10px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #fff;
		background: #6d96ff;
		width: auto;
		font-size: 14px;
		height: 32px;
		order: 3;
	}
	
	.one .list1-view:hover {
		opacity: 0.8;
	}
	
	.one .list1-edit {
		border: 0;
		cursor: pointer;
		border-radius: 4px;
		padding: 0 10px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #4f7df5;
		background: #edf2ff;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.one .list1-edit:hover {
		opacity: 0.8;
	}
	
	.one .list1-del {
		border: 0;
		cursor: pointer;
		border-radius: 4px;
		padding: 0 10px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #f00;
		background: #ffefed;
		width: auto;
		font-size: 14px;
		height: 32px;
	}
	
	.one .list1-del:hover {
		opacity: 0.8;
	}
	
	.one .list1-btn8 {
		border: 0;
		cursor: pointer;
		border-radius: 4px;
		padding: 0 10px;
		margin: 0 5px 5px 0;
		outline: none;
		color: #fff;
		background: #3bcfbf;
		width: auto;
		font-size: 14px;
		height: 32px;
		order: 11;
	}
	
	.one .list1-btn8:hover {
		opacity: 0.8;
	}
	
	.main-content .el-table .el-switch {
		display: inline-flex;
		vertical-align: middle;
		line-height: 30px;
		position: relative;
		align-items: center;
		height: 30px;
	}
	.main-content .el-table .el-switch /deep/ .el-switch__label--left {
		cursor: pointer;
		margin: 0 10px 0 0;
		color: #333;
		font-weight: 500;
		display: none;
		vertical-align: middle;
		font-size: 16px;
		transition: .2s;
		height: 30px;
	}
	.main-content .el-table .el-switch /deep/ .el-switch__label--right {
		cursor: pointer;
		margin: 0 0 0 10px;
		color: #333;
		font-weight: 500;
		display: none;
		vertical-align: middle;
		font-size: 16px;
		transition: .2s;
		height: 30px;
	}
	.main-content .el-table .el-switch /deep/ .el-switch__core {
		border: 1px solid #ff8b00;
		cursor: pointer;
		border-radius: 15px;
		margin: 0;
		outline: 0;
		background: #ff8b00;
		display: inline-block;
		width: 36px;
		box-sizing: border-box;
		transition: border-color .3s,background-color .3s;
		height: 18px;
	}
	.main-content .el-table .el-switch /deep/ .el-switch__core::after {
		border-radius: 100%;
		top: 1px;
		left: 2px;
		background: #FFF;
		width: 14px;
		position: absolute;
		transition: all .3s;
		height: 14px;
	}
	.main-content .el-table .el-switch.is-checked /deep/ .el-switch__core::after {
		margin: 0 0 0 -16px;
		left: 100%;
	}
	
	.main-content .el-table .el-rate /deep/ .el-rate__item {
		cursor: pointer;
		display: inline-block;
		vertical-align: middle;
		font-size: 0;
		position: relative;
	}
	.main-content .el-table .el-rate /deep/ .el-rate__item .el-rate__icon {
		margin: 0 3px;
		display: inline-block;
		font-size: 18px;
		position: relative;
		transition: .3s;
	}

	.chartDialog /deep/ .el-dialog {
		background: #fff;
	}
</style>
