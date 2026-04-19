import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import taobaoinfoList from '../pages/taobaoinfo/list'
import taobaoinfoDetail from '../pages/taobaoinfo/detail'
import taobaoinfoAdd from '../pages/taobaoinfo/add'
import taobaoinfoforecastList from '../pages/taobaoinfoforecast/list'
import taobaoinfoforecastDetail from '../pages/taobaoinfoforecast/detail'
import taobaoinfoforecastAdd from '../pages/taobaoinfoforecast/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'taobaoinfo',
					component: taobaoinfoList
				},
				{
					path: 'taobaoinfoDetail',
					component: taobaoinfoDetail
				},
				{
					path: 'taobaoinfoAdd',
					component: taobaoinfoAdd
				},
				{
					path: 'taobaoinfoforecast',
					component: taobaoinfoforecastList
				},
				{
					path: 'taobaoinfoforecastDetail',
					component: taobaoinfoforecastDetail
				},
				{
					path: 'taobaoinfoforecastAdd',
					component: taobaoinfoforecastAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
