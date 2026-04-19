<template>
	<div class="home-preview">




		<!-- 商品推荐 -->
		<div id="animate_recommendtaobaoinfo" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">淘宝男鞋推荐</span>
				<span class="recommend_subhead">{{'taobaoinfo'.toUpperCase()}} RECOMMEND</span>
			</div>
			<!-- 样式八 -->
			<div class="list list8 index-pv1">
				<div class="list-body-left">
					<div v-if="taobaoinfoRecommend.length>0" @click="toDetail('taobaoinfoDetail', taobaoinfoRecommend[0])" class="list-item1 animation-box">
						<img v-if="preHttp(taobaoinfoRecommend[0].imgurl)" :src="taobaoinfoRecommend[0].imgurl.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (taobaoinfoRecommend[0].imgurl?taobaoinfoRecommend[0].imgurl.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{taobaoinfoRecommend[0].prosheng}}</div>
							<div class="name">{{taobaoinfoRecommend[0].procity}}</div>
							<div class="name">{{taobaoinfoRecommend[0].title}}</div>
							<div class="name">{{taobaoinfoRecommend[0].jiage}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{taobaoinfoRecommend[0].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{taobaoinfoRecommend[0].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{taobaoinfoRecommend[0].storeupnum}}</span>
							</div>
						</div>
					</div>
					<div v-if="taobaoinfoRecommend.length>1" @click="toDetail('taobaoinfoDetail', taobaoinfoRecommend[1])" class="list-item2 animation-box">
						<img v-if="preHttp(taobaoinfoRecommend[1].imgurl)" :src="taobaoinfoRecommend[1].imgurl.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (taobaoinfoRecommend[1].imgurl?taobaoinfoRecommend[1].imgurl.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{taobaoinfoRecommend[1].prosheng}}</div>
							<div class="name">{{taobaoinfoRecommend[1].procity}}</div>
							<div class="name">{{taobaoinfoRecommend[1].title}}</div>
							<div class="name">{{taobaoinfoRecommend[1].jiage}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{taobaoinfoRecommend[1].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{taobaoinfoRecommend[1].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{taobaoinfoRecommend[1].storeupnum}}</span>
							</div>
						</div>
					</div>
					<div v-if="taobaoinfoRecommend.length>2" @click="toDetail('taobaoinfoDetail', taobaoinfoRecommend[2])" class="list-item3 animation-box">
						<img v-if="preHttp(taobaoinfoRecommend[2].imgurl)" :src="taobaoinfoRecommend[2].imgurl.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (taobaoinfoRecommend[2].imgurl?taobaoinfoRecommend[2].imgurl.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{taobaoinfoRecommend[2].prosheng}}</div>
							<div class="name">{{taobaoinfoRecommend[2].procity}}</div>
							<div class="name">{{taobaoinfoRecommend[2].title}}</div>
							<div class="name">{{taobaoinfoRecommend[2].jiage}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{taobaoinfoRecommend[2].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{taobaoinfoRecommend[2].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{taobaoinfoRecommend[2].storeupnum}}</span>
							</div>
						</div>
					</div>
				</div>
				<div class="list-body-right">
					<div v-if="taobaoinfoRecommend.length>3" @click="toDetail('taobaoinfoDetail', taobaoinfoRecommend[3])" class="list-item1 animation-box">
						<img v-if="preHttp(taobaoinfoRecommend[3].imgurl)" :src="taobaoinfoRecommend[3].imgurl.split(',')[0]" alt="" />
						<img v-else :src="baseUrl +  (taobaoinfoRecommend[3].imgurl?taobaoinfoRecommend[3].imgurl.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{taobaoinfoRecommend[3].prosheng}}</div>
							<div class="name">{{taobaoinfoRecommend[3].procity}}</div>
							<div class="name">{{taobaoinfoRecommend[3].title}}</div>
							<div class="name">{{taobaoinfoRecommend[3].jiage}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{taobaoinfoRecommend[3].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{taobaoinfoRecommend[3].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{taobaoinfoRecommend[3].storeupnum}}</span>
							</div>
						</div>
					</div>
					<div v-if="taobaoinfoRecommend.length>4" @click="toDetail('taobaoinfoDetail', taobaoinfoRecommend[4])" class="list-item2 animation-box">
						<img v-if="preHttp(taobaoinfoRecommend[4].imgurl)" :src="taobaoinfoRecommend[4].imgurl.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (taobaoinfoRecommend[4].imgurl?taobaoinfoRecommend[4].imgurl.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{taobaoinfoRecommend[4].prosheng}}</div>
							<div class="name">{{taobaoinfoRecommend[4].procity}}</div>
							<div class="name">{{taobaoinfoRecommend[4].title}}</div>
							<div class="name">{{taobaoinfoRecommend[4].jiage}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{taobaoinfoRecommend[4].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{taobaoinfoRecommend[4].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{taobaoinfoRecommend[4].storeupnum}}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('taobaoinfo')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				newsList: [],
				taobaoinfoRecommend: [],





			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		computed: {
			username() {
				return localStorage.getItem('username')
			}
		},
		//方法集合
		methods: {
			swiperChanges() {
				setTimeout(()=>{
				},750)
			},

			listIndexClick18(index, name) {
				this['listIndex18' + name] = index[this['listColumn18' + name]]
				this.getList()
			},

			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendtaobaoinfo',css:'animate__'},
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
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "taobaoinfo/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "taobaoinfo/autoSort2";
				}
				data = {
					page: 1,
					limit: 6,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.taobaoinfoRecommend = res.data.data.list;
					}
				});
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id, storeupType: 1}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		padding: 0;
		margin: 0 auto;
		overflow: hidden;
		display: flex;
		width: 100%;
		justify-content: space-between;
		flex-wrap: wrap;
		.recommend {
			padding: 0 10%;
			margin: 0 auto 0;
			background: none;
			width: 100%;
			position: relative;
			order: 1;
			.recommend_title_box {
				padding: 0;
				margin: 20px auto;
				background: none;
				display: flex;
				width: 100%;
				justify-content: center;
				flex-wrap: wrap;
				height: auto;
				.recommend_title {
					padding: 0;
					color: #000000;
					background: url(http://codegen.caihongy.cn/20251216/01df11827f544c1cb3e1d2e19e43b803.png) no-repeat right center ;
					font-weight: 600;
					display: block;
					letter-spacing: 10px;
					width: auto;
					font-size: 30px;
					line-height: 94px;
					text-align: center;
					height: 94px;
				}
				.recommend_subhead {
					margin: 0;
					color: #CBCBCB;
					font-weight: 500;
					display: none;
					width: auto;
					font-size: 20px;
					line-height: 30px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, -4px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list8 {
				padding: 10px 0;
				color: #fff;
				background: none;
				display: flex;
				width: 100%;
				font-size: 14px;
				justify-content: space-between;
				flex-wrap: wrap;
				height: auto;
				.list-body-left {
					display: flex;
					width: calc(50% - 10px);
					flex-wrap: wrap;
					height: auto;
					order: 4;
					.list-item1 {
						cursor: pointer;
						margin: 0 10px 0 0;
						width: calc(50% - 10px);
						position: relative;
						height: auto;
						order: 3;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 200px;
						}
						.infoBox {
							padding: 10px 0;
							align-content: center;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							display: flex;
							width: 100%;
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 26px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								width: 100%;
								font-size: 16px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
					.list-item2 {
						cursor: pointer;
						margin: 0 0 0 10px;
						width: calc(50% - 10px);
						position: relative;
						height: auto;
						order: 4;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 200px;
						}
						.infoBox {
							padding: 10px 0;
							align-content: center;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							display: flex;
							width: 100%;
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 26px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								width: 100%;
								font-size: 16px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
					.list-item3 {
						cursor: pointer;
						margin: 0 0 20px;
						width: 100%;
						position: relative;
						height: auto;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 300px;
						}
						.infoBox {
							padding: 10px 0;
							align-content: center;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							display: flex;
							width: 100%;
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 26px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								width: 100%;
								font-size: 16px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
				}
				.list-body-right {
					margin: 0;
					display: flex;
					width: calc(50% - 10px);
					flex-wrap: wrap;
					height: auto;
					.list-item1 {
						cursor: pointer;
						margin: 0;
						width: 100%;
						position: relative;
						height: auto;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 300px;
						}
						.infoBox {
							padding: 10px 0;
							align-content: center;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							display: flex;
							width: 100%;
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 26px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								width: 100%;
								font-size: 16px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
					.list-item2 {
						cursor: pointer;
						margin: 20px 0 0;
						width: 100%;
						position: relative;
						height: auto;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 200px;
						}
						.infoBox {
							padding: 10px 0;
							align-content: center;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							display: flex;
							width: 100%;
							align-items: center;
							position: absolute;
							flex-wrap: wrap;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 26px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								width: 100%;
								font-size: 16px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #ddd;
				cursor: pointer;
				margin: 0px auto;
				display: none;
				line-height: 40px;
				right: 10%;
				border-radius: 0px;
				top: 50px;
				background: #6aac5a;
				width: 120px;
				justify-content: center;
				position: absolute;
				text-align: center;
				.text {
					margin: 0 5px 0 0;
					color: #fff;
					font-size: 16px;
					order: 2;
				}
				.icon {
					margin: 0 10px 0 0;
					color: #fff;
					display: none;
					width: auto;
					font-size: 18px;
					height: 7px;
				}
			}
		}
	}
</style>
