/** @odoo-module alias=mana_dashboard.gauge_chart **/
const a0_0x146c88=a0_0x40f5;(function(_0xe84bd,_0x3740c2){const _0x2a35c5=a0_0x40f5,_0x2715a5=_0xe84bd();while(!![]){try{const _0x4e4950=parseInt(_0x2a35c5(0x10a))/0x1*(parseInt(_0x2a35c5(0xf4))/0x2)+parseInt(_0x2a35c5(0xf5))/0x3+-parseInt(_0x2a35c5(0x10e))/0x4+-parseInt(_0x2a35c5(0xfa))/0x5*(-parseInt(_0x2a35c5(0xf1))/0x6)+parseInt(_0x2a35c5(0xfc))/0x7*(-parseInt(_0x2a35c5(0x109))/0x8)+parseInt(_0x2a35c5(0x110))/0x9+parseInt(_0x2a35c5(0xfb))/0xa*(-parseInt(_0x2a35c5(0xf3))/0xb);if(_0x4e4950===_0x3740c2)break;else _0x2715a5['push'](_0x2715a5['shift']());}catch(_0x31d61a){_0x2715a5['push'](_0x2715a5['shift']());}}}(a0_0x63bb,0x7ecb3));
 function a0_0x40f5(_0x28cf44,_0x21153b){const _0x63bb1c=a0_0x63bb();return a0_0x40f5=function(_0x40f550,_0x91c449){_0x40f550=_0x40f550-0xec;let _0x26bf21=_0x63bb1c[_0x40f550];return _0x26bf21;},a0_0x40f5(_0x28cf44,_0x21153b);}
 import {renderToString}  from '@web/core/utils/render';
 import {BlockRegistry}  from '@mana_dashboard_base/mana_block_registry';
 import {icons}  from '@mana_dashboard_base/utils/mana_icons';
 import {BlockBase}  from '@mana_dashboard_base/mana_block_base';
 function a0_0x63bb(){const _0x19bc91=['render','set','statistics','365edApeR','20HtkgBI','7RFMqPl','innerHTML','apply','_onchange_res_model_id','get_widget','BaseView','prototype','extend','res_model_id','then','_rpc','template','get_template_id','6247448mnfeZl','641101frqQVD','listenTo','_onchange_config','_onchange_template','3036856qNqORD','classList','1394892nfXGgp','addAttributes','init','addType','add','getTrait','model','DomComponents','28794Qhfzlm','get','607739ZrzOFZ','2djDBlA','3070722Jrisil','save_config'];a0_0x63bb=function(){return _0x19bc91;};return a0_0x63bb();}
 import {_t}  from '@web/core/l10n/translation';const BaseModel=BlockBase['BaseModel'],BaseView=BlockBase[a0_0x146c88(0x101)];
 function builder(_0x49305c,_0x1b3d00){const _0xcc412e=a0_0x146c88,_0x2fcb6c=_0x49305c[_0xcc412e(0xf0)];_0x49305c['BlockManager'][_0xcc412e(0xed)]('field_statistics',{'label':_t('Field Statistics'),'category':_t('Statistics'),'select':!![],'render':()=>{const _0xb9291c=_0xcc412e;return'<div\x20class=\x22d-flex\x20flex-column\x20align-items-center\x20justify-content-center\x22><div\x20class=\x22chart-icon\x22>'+icons[_0xb9291c(0xf9)]+'</div><div\x20class=\x27anita-block-label\x27>Field\x20Statistics</div></div>';},'content':{'type':'field_statistics'}}),_0x2fcb6c[_0xcc412e(0xec)]('field_statistics',{'model':BaseModel[_0xcc412e(0x103)]({'defaults':{...BaseModel[_0xcc412e(0x102)]['defaults'],'name':_t('Field Statistics'),'classes':['field_statistics'],'attributes':{},'traits':[{'name':'res_model_id','type':'many2one','res_model':'ir.model'},{'name':'field_id','type':'many2one','res_model':'ir.model.fields','domain':[]},{'name':'statistics','type':'select','options':[{'value':'count','name':'Count'},{'value':'sum','name':'Sum'},{'value':'avg','name':'Average'},{'value':'min','name':'Min'},{'value':'max','name':'Max'}]},{'name':'template','type':'text','changeProp':0x1}]},'initialize'(){const _0x7ba2d=_0xcc412e;BaseModel[_0x7ba2d(0x102)]['initialize'][_0x7ba2d(0xfe)](this,arguments);let _0x1a0ad7=this[_0x7ba2d(0xf2)]('attributes')[_0x7ba2d(0x104)];_0x1a0ad7&&this[_0x7ba2d(0xee)]('field_id')[_0x7ba2d(0xf8)]('domain',[['model_id','=',_0x1a0ad7]]);},'get_custom_props'(){const _0x2ae28f=_0xcc412e;return{'template':this[_0x2ae28f(0xf2)]('template')};},'parse_custom_props'(_0xfb2a53){const _0x47ff0a=_0xcc412e;_0xfb2a53=JSON['parse'](_0xfb2a53||'{}'),this[_0x47ff0a(0xf8)]('template',_0xfb2a53[_0x47ff0a(0x107)]);}},{'isComponent':_0x1941ea=>{const _0x1b470f=_0xcc412e;if(_0x1941ea&&_0x1941ea[_0x1b470f(0x10f)]&&_0x1941ea[_0x1b470f(0x10f)]['contains']('field_statistics'))return{'type':'field_statistics'};}}),'view':BaseView[_0xcc412e(0x103)]({'tagName':'span','events':{},'init'(){const _0x3550c0=_0xcc412e;BaseView['prototype'][_0x3550c0(0x112)][_0x3550c0(0xfe)](this,arguments),this['listenTo'](this[_0x3550c0(0xef)],'change:attributes:res_model_id',this[_0x3550c0(0xff)]),this[_0x3550c0(0x10b)](this[_0x3550c0(0xef)],'change:attributes:field_id',this['_onchange_config']),this['listenTo'](this[_0x3550c0(0xef)],'change:attributes:statistics',this[_0x3550c0(0x10c)]),this[_0x3550c0(0x10b)](this[_0x3550c0(0xef)],'change:template',this[_0x3550c0(0x10d)]),this['listenTo'](this[_0x3550c0(0xef)],'change:val',this[_0x3550c0(0xf7)]),this[_0x3550c0(0x10c)](![]);},'_onchange_template'(){const _0x2530a8=_0xcc412e;this[_0x2530a8(0xef)][_0x2530a8(0xf6)](),this['render']();},'_onchange_res_model_id'(){const _0x5a2af1=_0xcc412e;let _0x365e6d=this[_0x5a2af1(0xef)][_0x5a2af1(0xf2)]('attributes')[_0x5a2af1(0x104)],_0xa19d76=this['model'][_0x5a2af1(0xf2)]('attributes')['field_id'];_0x365e6d?this['model'][_0x5a2af1(0xee)]('field_id')[_0x5a2af1(0xf8)]('domain',[['model_id','=',_0x365e6d]]):this['model'][_0x5a2af1(0xee)]('field_id')[_0x5a2af1(0xf8)]('domain',[['model_id','=',0x0]]),this[_0x5a2af1(0xef)][_0x5a2af1(0x111)]({'field_id':null}),_0xa19d76&&_0x365e6d&&this[_0x5a2af1(0x10c)]();},'_onchange_config'(_0x5d6fad=!![]){const _0x3aff94=_0xcc412e;let _0x31e587=this[_0x3aff94(0xef)][_0x3aff94(0xf2)]('attributes')['res_model_id'],_0xa51d4e=this[_0x3aff94(0xef)][_0x3aff94(0xf2)]('attributes')['field_id'],_0x31db76=this[_0x3aff94(0xef)][_0x3aff94(0xf2)]('attributes')[_0x3aff94(0xf9)];if(_0x31e587&&_0xa51d4e&&_0x31db76){_0x5d6fad&&this['model']['save_config']();let _0x4ff039=this[_0x3aff94(0x100)]();_0x4ff039[_0x3aff94(0x106)]({'model':'mana_dashboard.dashboard','method':'get_model_field_statistics','args':[_0x31e587,_0xa51d4e,_0x31db76]})[_0x3aff94(0x105)](_0x476a76=>{const _0xe88d58=_0x3aff94;this[_0xe88d58(0xef)]['set']('val',_0x476a76);});}},'render'(..._0x1375be){const _0x127b36=_0xcc412e;BaseView[_0x127b36(0x102)][_0x127b36(0xf7)][_0x127b36(0xfe)](this,_0x1375be);let _0x41df2a=this['model'][_0x127b36(0xf2)]('val'),_0x5c5094=this['model'][_0x127b36(0xf2)]('template');if(_0x41df2a){this['update_template']();let _0x3d7c3b=qweb[_0x127b36(0xf7)](this[_0x127b36(0x108)](),{'val':_0x41df2a,'view':this});this['el']['innerHTML']=_0x3d7c3b;}else this['el'][_0x127b36(0xfd)]='null';return this;}})});};BlockRegistry[a0_0x146c88(0xed)]('field_statistics',builder);