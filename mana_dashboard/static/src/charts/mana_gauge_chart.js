/** @odoo-module alias=mana_dashboard.gauge_chart **/
var a0_0x3755d2=a0_0x212b;(function(_0x5ce2ff,_0x4f25e6){var _0x17947a=a0_0x212b,_0x3ed2a1=_0x5ce2ff();while(!![]){try{var _0x5aafba=parseInt(_0x17947a(0x187))/0x1*(-parseInt(_0x17947a(0x182))/0x2)+parseInt(_0x17947a(0x184))/0x3+-parseInt(_0x17947a(0x189))/0x4+parseInt(_0x17947a(0x185))/0x5*(parseInt(_0x17947a(0x188))/0x6)+-parseInt(_0x17947a(0x18b))/0x7*(-parseInt(_0x17947a(0x18a))/0x8)+-parseInt(_0x17947a(0x183))/0x9+parseInt(_0x17947a(0x18c))/0xa;if(_0x5aafba===_0x4f25e6)break;else _0x3ed2a1['push'](_0x3ed2a1['shift']());}catch(_0x1b5358){_0x3ed2a1['push'](_0x3ed2a1['shift']());}}}(a0_0x3acc,0x894a6));
 function a0_0x3acc(){var _0x1eca7f=['371ayzmyQ','4328900ojbrRF','classList','571322OxZmty','1334781LUYDrz','1356588YVAmAa','3158310UXQfJe','add','3eSRhNK','6OWpzwJ','1756184iKWUvV','73952czdfcI'];a0_0x3acc=function(){return _0x1eca7f;};return a0_0x3acc();}
 import {BlockRegistry}  from '@mana_dashboard_base/mana_block_registry';
 import {builder}  from '@mana_dashboard_base/charts/mana_chart_builder';
 import {icons}  from '@mana_dashboard_base/utils/mana_icons';
 import {_t}  from '@web/core/l10n/translation';
 import {render_block,default_chart_trait}  from '@mana_dashboard_base/charts/mana_chart_util';
 function a0_0x212b(_0x3966b2,_0xc938b1){var _0x3acca1=a0_0x3acc();return a0_0x212b=function(_0x212b53,_0x404300){_0x212b53=_0x212b53-0x182;var _0x2fd3be=_0x3acca1[_0x212b53];return _0x2fd3be;},a0_0x212b(_0x3966b2,_0xc938b1);}BlockRegistry[a0_0x3755d2(0x186)]('gauge_chart',builder({'name':_t('Gauge Chart'),'chart_type':'gauge_chart','render':render_block('Gauge Chart',icons['gauge_chart_svg']),'default_option':{'series':[{'type':'gauge','progress':{'show':!![],'width':0x12},'axisLine':{'lineStyle':{'width':0x12}},'axisTick':{'show':![]},'splitLine':{'length':0xf,'lineStyle':{'width':0x2,'color':'#999'}},'axisLabel':{'distance':0x19,'color':'#999','fontSize':0x14},'anchor':{'show':!![],'showAbove':!![],'size':0x19,'itemStyle':{'borderWidth':0xa}},'title':{'show':![]},'detail':{'valueAnimation':!![],'fontSize':0x50,'offsetCenter':[0x0,'70%']},'data':[{'value':0x46}]}]},'traits':default_chart_trait,'content':{'type':'gauge_chart'},'category':_t('Chart'),'isComponent'(_0x9b9607){var _0x5a0c46=a0_0x3755d2;if(_0x9b9607[_0x5a0c46(0x18d)]&&_0x9b9607[_0x5a0c46(0x18d)]['contains']('gauge_chart'))return{'type':'gauge_chart'};},'default_template':'mana_dashboard.template_simple_gauge_chart','template_category':'chart','template_type':'gauge chart','search_sensitive':!![],'enable_drill_down':![]}));