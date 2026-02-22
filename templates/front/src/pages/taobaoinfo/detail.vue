<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'/'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/taobaoinfo?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item3"><a href="javascript:void(0);">详情</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-fanhui01"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="detail-preview">
			<div class="attr">
				<div class="info">
					<div class="title-item">
						<div class="detail-title">
							{{detail.prosheng}}
						</div>
						<div class="colectBtn" @click="storeup(1)" v-show="!isStoreup">
							<i class="icon iconfont icon-shoucang10"></i>
							<span class="text">收藏({{detail.storeupnum}})</span>
						</div>
						<div class="colectBtnActive" @click="storeup(-1)" v-show="isStoreup">
							<i class="icon iconfont icon-shoucang12"></i>
							<span class="text">已收藏({{detail.storeupnum}})</span>
						</div>
					</div>
					<div class="item">
						<div class="lable">市</div>
						<div class="text "  >{{detail.procity}}</div>
					</div>
					<div class="item">
						<div class="lable">标题</div>
						<div class="text "  >{{detail.title}}</div>
					</div>
					<div class="item">
						<div class="lable">价格</div>
						<div class="text "  >{{detail.jiage}}</div>
					</div>
					<div class="item">
						<div class="lable">销售量</div>
						<div class="text "  >{{detail.salesnum}}</div>
					</div>
					<div class="item">
						<div class="lable">标签</div>
						<div class="text "  >{{detail.shoptag}}</div>
					</div>
					<div class="item">
						<div class="lable">包邮</div>
						<div class="text "  >{{detail.baoyounew}}</div>
					</div>
					<div class="item">
						<div class="lable">参数1</div>
						<div class="text "  >{{detail.property1}}</div>
					</div>
					<div class="item">
						<div class="lable">参数2</div>
						<div class="text "  >{{detail.property2}}</div>
					</div>
					<div class="item">
						<div class="lable">参数3</div>
						<div class="text "  >{{detail.property3}}</div>
					</div>
					<div class="item">
						<div class="lable">商家账号</div>
						<div class="text "  >{{detail.nickname}}</div>
					</div>
					<div class="item">
						<div class="lable">商家名称</div>
						<div class="text "  >{{detail.shopname}}</div>
					</div>
					<div class="item">
						<div class="lable">详情地址</div>
						<div class="text  link"  @click="linkOthers(detail.detailurl)">{{detail.detailurl}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('taobaoinfo','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('taobaoinfo','删除')" @click="delClick">删除</el-button>
						<el-button class="editBtn" @click="allchapterClick()" type="warning" v-if="btnAuth('taobaoinfo','章节管理')">章节管理</el-button>
					</div>
				</div>
			</div>
		
			<el-carousel v-if="detailBanner.length" trigger="click" indicator-position="inside" arrow="always" type="default" direction="horizontal" height="480px" :autoplay="false" :interval="3000" :loop="true">
				<el-carousel-item v-for="item in detailBanner" :key="item.id">
					<img :preview-src-list="[item]" v-if="item.substr(0,4)=='http'" :src="item" class="image">
					<img :preview-src-list="[baseUrl + item]" v-else :src="baseUrl + item" class="image">
				</el-carousel-item>
			</el-carousel>

			<div class="zancai">
				<div v-if="!isThumbsupnum && !isCrazilynum" class="zan" @click="thumbsupOrCrazily(21)">
					<i class="icon iconfont icon-zan07"></i>
					<span class="text">赞一下({{detail.thumbsupnum}})</span>
				</div>
				<div v-if="!isThumbsupnum && !isCrazilynum" class="cai" @click="thumbsupOrCrazily(22)">
					<i class="icon iconfont icon-cai01"></i>
					<span class="text">踩一下({{detail.crazilynum}})</span>
				</div>
				<div v-if="isThumbsupnum" class="zanActive" @click="cancelThumbsupOrCrazily(21)">
					<i class="icon iconfont icon-zan11"></i>
					<span class="text">已赞({{detail.thumbsupnum}})</span>
				</div>
				<div v-if="isCrazilynum" class="caiActive" @click="cancelThumbsupOrCrazily(22)">
					<i  class="icon iconfont icon-cai16"></i>
					<span class="text">已踩({{detail.crazilynum}})</span>
				</div>
			</div>


			<el-tabs class="detail-tabs" v-model="activeName" type="border-card" v-if="tabsNum>0" >
			</el-tabs>

		</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import Swiper from "swiper";
	export default {
		//数据集合
		data() {
			return {
				tablename: 'taobaoinfo',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '淘宝男鞋'
					}
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				tabsNum: 0,
				activeName: '1',
				storeupParams: {
					name: '',
					picture: '',
					refid: 0,
					tablename: 'taobaoinfo',
					userid: Number(localStorage.getItem('frontUserid'))
				},
				isStoreup: false,
				storeupInfo: {},
				isCrazilynum: false,
				isThumbsupnum: false,
				thumbsupOrCrazilyInfo: {},
				buynumber: 1,
				centerType: false,
				storeupType: false,
			}
		},
		created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0) {
				this.centerType = true
			}
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			
			this.init();
		},
		mounted() {
		},
		computed: {
			username() {
				return localStorage.getItem('username')
			}
		},
		//方法集合
		methods: {
			init() {
				this.id = this.$route.query.id
				this.baseUrl = this.$config.baseUrl;
				this.$http.get(this.tablename + '/detail/'  + this.id, {}).then(async res => {
					if (res.data.code == 0) {
						this.detail = res.data.data;
						this.title = this.detail.prosheng;
						if(this.detail.imgurl) {
							this.detailBanner = this.detail.imgurl.split(",w").length>1?[this.detail.imgurl]:this.detail.imgurl.split(',');
						}
						this.$forceUpdate();
						if(localStorage.getItem('frontToken')){
							this.getStoreupStatus();
							this.getThumbsupOrCrazilyStatus();
						}

					}
				});
			},
			linkOthers(url) {
				window.open(url);//打开一个新的标签页
			},
			storeup(type) {
				if (type == 1 && !this.isStoreup) {
					this.storeupParams.name = this.title;
					this.storeupParams.picture = this.detailBanner[0];
					this.storeupParams.refid = this.detail.id;
					this.storeupParams.type = String(type);
					this.$http.post('storeup/add', this.storeupParams).then(res => {
						if (res.data.code == 0) {
							this.isStoreup = true;
							this.detail.storeupnum++
							this.$http.post('taobaoinfo/update', this.detail).then(res => {});
							this.$message({
								type: 'success',
								message: '收藏成功!',
								duration: 1500,
							});
						}
					});
				}
				if (type == -1 && this.isStoreup) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '1', refid: this.detail.id, tablename: 'taobaoinfo', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isStoreup = true;
							this.storeupInfo = res.data.data.list[0];
							let delIds = new Array();
							delIds.push(this.storeupInfo.id);
							this.$http.post('storeup/delete', delIds).then(res => {
								if (res.data.code == 0) {
									this.isStoreup = false;
									this.detail.storeupnum--
									this.$http.post('taobaoinfo/update', this.detail).then(res => {});
									this.$message({
										type: 'success',
										message: '取消成功!',
										duration: 1500,
									});
								}
							});
						}
					});
				}
			},
			getStoreupStatus(){
				if(localStorage.getItem("frontToken")) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '1', refid: this.detail.id, tablename: 'taobaoinfo', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isStoreup = true;
							this.storeupInfo = res.data.data.list[0];
						}
					});
				}
			},
			async thumbsupOrCrazily(type) {
				this.storeupParams.name = this.title;
				this.storeupParams.picture = this.detailBanner[0];
				this.storeupParams.refid = this.detail.id;
				this.storeupParams.type = String(type);
				await this.$http.post('storeup/add', this.storeupParams).then(res => {
					if (res.data.code == 0) {
						let detail = JSON.parse(JSON.stringify(this.detail))
						if (type == 21) detail.thumbsupnum = Number(detail.thumbsupnum) + 1;
						if (type == 22) detail.crazilynum = Number(detail.crazilynum) + 1;
						this.$http.post('taobaoinfo/update', detail).then(res => {
							this.detail = detail
						});
						this.getThumbsupOrCrazilyStatus();
						this.$message({
							type: 'success',
							message: '操作成功!',
							duration: 1500,
						});
						
					}
				});
				
			},
			async cancelThumbsupOrCrazily(type) {
				let delIds = new Array();
				delIds.push(this.thumbsupOrCrazilyInfo.id);
				await this.$http.post('storeup/delete', delIds).then(res => {
					if (res.data.code == 0) {
						let detail = JSON.parse(JSON.stringify(this.detail))
						if (type == 21) detail.thumbsupnum -= 1;
						if (type == 22) detail.crazilynum -= 1;
						this.$http.post('taobaoinfo/update', detail).then(res => {
							this.detail = detail
						});
						this.isThumbsupnum = false;
						this.isCrazilynum = false;
						this.$message({
							type: 'success',
							message: '取消成功!',
							duration: 1500,
						});
					}
				});
				
			},
			getThumbsupOrCrazilyStatus() {
				if(localStorage.getItem("frontToken")) {
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '21', refid: this.detail.id, tablename: 'taobaoinfo', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isThumbsupnum = true;
							this.thumbsupOrCrazilyInfo = res.data.data.list[0];
						}
					});
					this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: '22', refid: this.detail.id, tablename: 'taobaoinfo', userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
						if (res.data.code == 0 && res.data.data.list.length > 0) {
							this.isCrazilynum = true;
							this.thumbsupOrCrazilyInfo = res.data.data.list[0];
						}
					});
				}
			},
			curChange(page) {
				this.getDiscussList(page);
			},
			prevClick(page) {
				this.getDiscussList(page);
			},
			nextClick(page) {
				this.getDiscussList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getDiscussList(1);
			},
			// 返回按钮
			backClick(){
				if(this.storeupType){
					history.back()
				}else{
					let params = {}
					if(this.centerType){
						params.centerType = 1
					}
					this.$router.push({path: '/index/taobaoinfo', query: params});
				}
			},
			// 下载
			download(file ){
				if(!file) {
					this.$message({
						type: 'error',
						message: '文件不存在',
						duration: 1500,
					});
					return;
				}
				let arr = file.replace(new RegExp('upload/', "g"), "")
				axios.get(this.baseUrl + 'file/download?fileName=' + arr, {
					headers: {
						token: localStorage.getItem("frontToken")
					},
					responseType: "blob"
				}).then(({
					data
				}) => {
					const binaryData = [];
					binaryData.push(data);
					const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
						type: 'application/pdf;chartset=UTF-8'
					}))
					const a = document.createElement('a')
					a.href = objectUrl
					a.download = arr
					// a.click()
					// 下面这个写法兼容火狐
					a.dispatchEvent(new MouseEvent('click', {
						bubbles: true,
						cancelable: true,
						view: window
					}))
					window.URL.revokeObjectURL(data)
				},err=>{
					axios.get((location.href.split(this.$config.name).length>1 ? location.href.split(this.$config.name)[0] :'') + this.$config.name + 'file/download?fileName=' + arr, {
						headers: {
							token: localStorage.getItem("frontToken")
						},
						responseType: "blob"
					}).then(({
						data
					}) => {
						const binaryData = [];
						binaryData.push(data);
						const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
							type: 'application/pdf;chartset=UTF-8'
						}))
						const a = document.createElement('a')
						a.href = objectUrl
						a.download = arr
						// a.click()
						// 下面这个写法兼容火狐
						a.dispatchEvent(new MouseEvent('click', {
							bubbles: true,
							cancelable: true,
							view: window
						}))
						window.URL.revokeObjectURL(data)
					})
				})
			},


			// 权限判断
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			// 修改
			editClick(){
				this.$router.push(`/index/taobaoinfoAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此淘宝男鞋？') .then(_ => {
					this.$http.post('taobaoinfo/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$http.get('storeup/list',{params:{
								page: 1,
								limit: 100,
								refid: this.detail.id,
								tablename: 'taobaoinfo',
							}}).then(async obj=>{
								if(obj.data&&obj.data.code==0){
									let arr = []
									for(let x in obj.data.data.list){
										arr.push(obj.data.data.list[x].id)
									}
									if(arr.length){
										await this.$http.post('storeup/delete',arr).then(()=>{})
									}
									this.$message({
										type: 'success',
										message: '删除成功!',
										duration: 1500,
										onClose: () => {
											history.back()
										}
									});
								}
							})
						}
					});
				}).catch(_ => {});
			},
			allchapterClick (){
				let params = {
					refid: this.detail.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/chaptertaobaoinfo', query: params});
			},
			// 获取uuid
			getUUID() {
				return new Date().getTime();
			},
		},
		components: {
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.detail-preview {
		padding: 0 10%;
		margin: 10px auto;
		display: flex;
		width: 100%;
		position: relative;
		flex-wrap: wrap;
		.attr {
			padding: 0px;
			margin: 0 0 20px;
			background: none;
			flex: 1;
			display: flex;
			position: relative;
			order: 2;
			.info {
				border-radius: 8px;
				padding: 10px;
				margin: 0;
				background: #fff;
				flex: 1;
				.title-item {
					padding: 10px;
					margin: 0 0 0px 0;
					background: none;
					display: flex;
					border-color: rgba(5, 135, 71,0.3);
					border-width: 0 0 1px;
					justify-content: space-between;
					align-items: center;
					border-style: solid;
					.detail-title {
						padding: 0;
						color: #333;
						font-weight: 600;
						font-size: 18px;
						border-color: #009899;
						border-width: 0 0 0 0px;
						line-height: 1;
						border-style: solid;
					}
					.colectBtn {
						cursor: pointer;
						border: 0px solid #eee;
						border-radius: 4px;
						padding: 5px 15px;
						background: none;
						.icon {
							color: #666;
							font-size: 16px;
						}
						.text {
							color: #000;
							font-size: 16px;
						}
					}
					.colectBtnActive {
						background: #058747;
						border-color: #058747;
						.icon {
							color: #fff;
							font-size: 16px;
						}
						.text {
							color: #fff;
							font-size: 16px;
						}
					}
					.colectBtn:hover {
						background: #058747;
						border-color: #058747;
						.icon {
							color: #fff;
						}
						.text {
							color: #fff;
						}
					}
					.colectBtnActive:hover {
						background: #058747;
						border-color: #058747;
						.icon {
							color: #fff;
						}
						.text {
							color: #fff;
						}
					}
				}
				.item {
					padding: 5px 10px;
					margin: 0 0 0px 0;
					background: none;
					display: flex;
					border-color: rgba(5, 135, 71,0.3);
					border-width: 0 0 1px;
					justify-content: spaceBetween;
					border-style: solid;
					.lable {
						padding: 0 10px 0 0;
						color: #333;
						white-space: nowrap;
						font-weight: 500;
						width: auto;
						font-size: 16px;
						line-height: 24px;
						text-align: right;
						height: auto;
					}
					.text {
						padding: 0 10px;
						color: #666;
						word-break: break-all;
						flex: 1;
						font-size: 14px;
						line-height: 24px;
						height: auto;
					}
					.price {
						color: #f00;
					}
					.bold {
						font-weight: bold;
					}
					.link {
						cursor: pointer;
						text-decoration: underline;
					}
				}
				.btn_box {
					padding: 10px 0;
					display: flex;
					flex-wrap: wrap;
				}
				.editBtn {
					border: 1px solid #46AC2E;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 10px;
					margin: 0 0 0 10px;
					outline: none;
					color: #fff;
					background: #46AC2E;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.editBtn:hover {
					opacity: 0.7;
				}
				.delBtn {
					border: 1px solid #46AC2E;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 10px;
					margin: 0 0 0 10px;
					outline: none;
					color: #fff;
					background: #46AC2E;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.delBtn:hover {
					opacity: 0.7;
				}
			}
		}
		.el-carousel {
			margin: 0 0 0 20px;
			width: 480px;
			height: 480px;
			order: 1;
			/deep/ .el-carousel__indicator button {
				width: 0;
				height: 0;
				display: none;
			}
			/deep/ .el-carousel__container {
				.el-carousel__arrow--left {
					width: 36px;
					font-size: 12px;
					height: 36px;
				}
				.el-carousel__arrow--left:hover {
					background: red;
				}
				.el-carousel__arrow--right {
					width: 36px;
					font-size: 12px;
					height: 36px;
				}
				.el-carousel__arrow--right:hover {
					background: red;
				}
				.el-carousel__item {
					border-radius: 10px;
					width: 100%;
					height: 100%;
					img {
						object-fit: cover;
						width: 100%;
						height: 100%;
					}
				}
			}
		
			/deep/ .el-carousel__indicators {
				padding: 0;
				margin: 0;
				z-index: 2;
				position: absolute;
				list-style: none;
				li {
					padding: 0;
					margin: 0 4px;
					background: #fff;
					display: inline-block;
					width: 12px;
					opacity: 0.4;
					transition: 0.3s;
					height: 12px;
				}
				li:hover {
					padding: 0;
					margin: 0 4px;
					background: #fff;
					display: inline-block;
					width: 24px;
					opacity: 0.7;
					height: 12px;
				}
				li.is-active {
					padding: 0;
					margin: 0 4px;
					background: #fff;
					display: inline-block;
					width: 24px;
					opacity: 1;
					height: 12px;
				}
			}
		}
		.zancai {
			padding: 0;
			margin: 0px auto 20px;
			background: none;
			display: flex;
			width: 100%;
			justify-content: center;
			order: 3;
			.zan {
				cursor: pointer;
				border: 1px solid #000000;
				border-radius: 4px;
				padding: 10px 40px;
				margin: 0 100px 0 0;
				background: none;
				display: flex;
				width: auto;
				justify-content: center;
				align-items: center;
				.icon {
					margin: 0 3px;
					color: #666;
					font-size: 14px;
				}
				.text {
					margin: 0 3px;
					color: #666;
					font-size: 16px;
				}
			}
			.zan:hover {
				background: #058747;
				border-color: #058747;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.zanActive {
				cursor: pointer;
				border-radius: 4px;
				padding: 10px 20px;
				margin: 0 20px 0 0;
				background: #ff6f3d;
				display: flex;
				width: auto;
				border-color: #ff6f3d;
				justify-content: center;
				align-items: center;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.zanActive:hover {
				background: #058747;
				border-color: #058747;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			
			.cai {
				cursor: pointer;
				border: 1px solid #000000;
				border-radius: 4px;
				padding: 10px 40px;
				margin: 0;
				background: none;
				display: flex;
				width: auto;
				justify-content: center;
				align-items: center;
				.icon {
					margin: 0 3px;
					color: #666;
					font-size: 14px;
				}
				.text {
					margin: 0 3px;
					color: #666;
					font-size: 16px;
				}
			}
			.cai:hover {
				background: rgb(70, 172, 46);
				border-color: rgb(70, 172, 46);
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.caiActive {
				background: #ff6f3d;
				border-color: #ff6f3d;
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
			.caiActive:hover {
				background: rgb(70, 172, 46);
				border-color: rgb(70, 172, 46);
				.icon {
					color: #fff;
				}
				.text {
					color: #fff;
				}
			}
		}
		.detail-tabs {
			border: 0px solid #DCDFE6;
			box-shadow: none;
			padding: 0;
			margin: 20px auto;
			background: none;
			width: 100%;
			order: 5;
			& /deep/ .el-tabs__header .el-tabs__nav-wrap {
				margin-bottom: 0;
			}
			/deep/ .el-tabs__header {
				padding: 10px 0;
				background: none;
				display: block;
				width: 100%;
				border-color: #707070;
				border-width: 0;
				line-height: 1.5;
				border-style: solid;
				text-align: center;
			}
			
			/deep/ .el-tabs__header .el-tabs__item {
				border: 0;
				padding: 0 62px 0 20px;
				margin: 20px;
				color: #000;
				font-weight: 500;
				display: inline-block;
				font-size: 18px;
				border-color: transparent;
				line-height: 40px;
				box-shadow: 0px 10px 30px 1px rgba(0,0,0,0.16);
				background: url(http://codegen.caihongy.cn/20251216/46953773c99f46e9a99d376cdc9e83bb.png) no-repeat right center / 42px 24px;
				border-width: 0;
				position: relative;
				border-style: solid;
				list-style: none;
				height: 40px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item:hover {
				border: 0;
				padding: 0 62px 0 20px;
				margin: 0 30px 0 0;
				color: #000;
				font-weight: 500;
				display: inline-block;
				font-size: 18px;
				border-color: transparent;
				line-height: 40px;
				box-shadow: 0px 10px 30px 1px rgba(0,0,0,0.16);
				background: url(http://codegen.caihongy.cn/20251216/cf8d7c447abc4afe867bb6ba0e7b2683.png) no-repeat right center / 42px 24px;
				border-width: 0;
				position: relative;
				border-style: solid;
				list-style: none;
				height: 40px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				border: 0;
				padding: 0 62px 0 20px;
				margin: 0 30px 0 0;
				color: #000;
				font-weight: 500;
				display: inline-block;
				font-size: 18px;
				border-color: transparent;
				line-height: 40px;
				box-shadow: 0px 10px 30px 1px rgba(0,0,0,0.16);
				background: url(http://codegen.caihongy.cn/20251216/cf8d7c447abc4afe867bb6ba0e7b2683.png) no-repeat right center / 42px 24px;
				border-width: 0;
				position: relative;
				border-style: solid;
				list-style: none;
				height: 40px;
			}
			
			/deep/ .el-tabs__content {
				padding: 15px 5px;
				color: #333;
				background: #fff;
				width: 100%;
				font-size: 16px;
			}
		}
	}
</style>
