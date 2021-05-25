import Vue from 'vue'
import Router from 'vue-router'
import Map from '@/components/Map'
import Main from "../components/Main";
import StatisticsMain from "../components/Statistics/StatisticsMain";
import TwitterPie from "../components/Statistics/TwitterPie";
import TwitterChart from "../components/Statistics/TwitterChart";
import TwitterTime from "../components/Statistics/TwitterTime";
import TwitterAge from "../components/Statistics/TwitterAge";
import TwitterIncome from "../components/Statistics/TwitterIncome";
import TwitterDensity from "../components/Statistics/TwitterDensity";
import TwitterInfo from "../components/Statistics/TwitterInfo";
import TwitterEmoji from "../components/Statistics/TwitterEmoji";
import CoverPage from "../components/CoverPage";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: CoverPage,
      name: 'CoverPage',
    },
    {
      path: '/main',
      component: Main,
      name: 'main',
      redirect: '/viewmap',
      children:
        [
        {
          path: '/viewmap',
          name: 'viewmap',
          component: Map,
        },
        {
          path: '/statisticsmain',
          name: 'StatisticsMain',
          component: StatisticsMain,
          redirect: '/twitterinfo',
          children:
            [
              {
                path: '/twitterpie',
                name: 'TwitterPie',
                component: TwitterPie,
              },
              {
                path: '/twitterchart',
                name: 'TwitterChart',
                component: TwitterChart,
              },
              {
                path: '/twittertime',
                name: 'TwitterTime',
                component: TwitterTime,
              },
              {
                path: '/twitterage',
                name: 'TwitterAge',
                component: TwitterAge,
              },
              {
                path: '/twitterincome',
                name: 'TwitterIncome',
                component: TwitterIncome,
              },
              {
                path: '/twitterdensity',
                name: 'TwitterDensity',
                component: TwitterDensity,
              },
              {
                path: '/twitterinfo',
                name: 'TwitterInfo',
                component: TwitterInfo,
              },
              {
                path: '/twitteremoji',
                name: 'TwitterEmoji',
                component: TwitterEmoji,
              },

            ]
          }
        ]
    }

  ]
})
