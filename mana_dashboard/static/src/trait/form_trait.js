/** @odoo-module alias=mana_dashboard.form_trait **/
(function(_0x401c1b,_0x155e33){const _0x3c13c3=a0_0xb0df,_0x6c81de=_0x401c1b();while(!![]){try{const _0x102ed4=-parseInt(_0x3c13c3(0x81))/0x1*(-parseInt(_0x3c13c3(0x7e))/0x2)+-parseInt(_0x3c13c3(0x8d))/0x3+parseInt(_0x3c13c3(0x94))/0x4*(-parseInt(_0x3c13c3(0x92))/0x5)+parseInt(_0x3c13c3(0x88))/0x6*(parseInt(_0x3c13c3(0x8f))/0x7)+-parseInt(_0x3c13c3(0x84))/0x8+-parseInt(_0x3c13c3(0x7b))/0x9+parseInt(_0x3c13c3(0x77))/0xa;if(_0x102ed4===_0x155e33)break;else _0x6c81de['push'](_0x6c81de['shift']());}catch(_0x3d1f3c){_0x6c81de['push'](_0x6c81de['shift']());}}}(a0_0x29a7,0xab0ce));
 function a0_0xb0df(_0x2d9f25,_0x5baae6){const _0x29a762=a0_0x29a7();return a0_0xb0df=function(_0xb0df,_0x97a1d){_0xb0df=_0xb0df-0x74;let _0x5c2a76=_0x29a762[_0xb0df];return _0x5c2a76;},a0_0xb0df(_0x2d9f25,_0x5baae6);}
 import {mountComponent}  from '@web/env';
 import {SubForm}  from '@mana_dashboard/sub_form_view/mana_sub_form';
 function a0_0x29a7(){const _0x13dbec=['model','form_trait_id','12786megohg','TraitManager','save','get_default_props','SubForm','1880973kzjoAE','data','3535bniByt','config_id','get_config_id','5CtJcNi','destroy','1423732DMmCHr','get','createElement','read','18586850MsliRG','addAttributes','_values','onChange','8744238WIKFBM','get_env','onEvent','2TbnVKN','services','set','555601loFmYE','addType','orm','6682504BxMjKw','getClbOpts'];a0_0x29a7=function(){return _0x13dbec;};return a0_0x29a7();}
 import {_t}  from '@web/core/l10n/translation';
export  default(_0x4ffcdb,_0x4e9687={})=>{const _0x1a266d=a0_0xb0df;_0x4ffcdb[_0x1a266d(0x89)][_0x1a266d(0x82)]('form_trait',{'noLabel':!![],'createInput'({trait:_0x5e2232}){const _0x381acf=_0x1a266d;let _0x4f5cb0=document[_0x381acf(0x75)]('div');return _0x4f5cb0;},'onChange'(_0x2df348){const _0xdfab42=_0x1a266d;this[_0xdfab42(0x86)][_0xdfab42(0x80)]('value',_0x2df348[_0xdfab42(0x8e)]),this[_0xdfab42(0x7d)]({...this[_0xdfab42(0x85)](),'event':_0x2df348});},'onUpdate'({elInput:_0x37c212,component:_0x2addb3}){const _0x30d795=_0x1a266d;let _0x46f7a0=this[_0x30d795(0x85)](),_0xdfb919=_0x46f7a0['trait'],_0x4b2ccd=_0xdfb919[_0x30d795(0x74)]('model'),_0x30e614=_0x2addb3[_0x30d795(0x74)]('config');if(!_0x30e614)return;let _0x57f929=_0x30e614[_0x30d795(0x91)]();_0x57f929=parseInt(_0x57f929);let _0x3032c4=_0x2addb3['get']('attributes')[_0x30d795(0x90)];_0x3032c4&&(_0x3032c4=parseInt(_0x3032c4));let _0x34c156=undefined,_0x2e857b=undefined;if(_0x4b2ccd==='mana_dashboard.config'){_0x34c156=_0x3032c4;if(!_0x34c156)return;}else{let _0x3dfe75=_0x2addb3['get']('attributes')[_0x30d795(0x87)];_0x3dfe75&&(_0x34c156=parseInt(_0x3dfe75));}this['SubForm']&&(this['SubForm'][_0x30d795(0x93)](),this[_0x30d795(0x8c)]=null);let _0x30d83d=_0x2addb3[_0x30d795(0x8b)]()||{},_0x484b9c=_0x2addb3['get_dashboard_id'](),_0x14b2e1=_0x2addb3[_0x30d795(0x7c)](),_0x5a4802=_0xdfb919['get']('model');setTimeout(async()=>{const _0x318333=_0x30d795;this[_0x318333(0x8c)]=await mountComponent(SubForm,_0x37c212,{'env':_0x2addb3['get_env'](),'translateFn':_t,'translatableAttributes':['data-tooltip'],'props':{'resModel':_0x5a4802,'resId':_0x34c156,'mode':'edit','context':_['extend']({},_0xdfb919['get']('context')||{},{'form_view_ref':_0xdfb919['get']('form_view_ref'),'default_config_id':_0x57f929,'default_any_config_id':_0x3032c4,'default_dashboard_id':_0x484b9c},_0x30d83d),'onRecordChanged':async(_0x44c78d,_0x15729e)=>{setTimeout(async()=>{const _0x1ae0c8=a0_0xb0df,_0x2256c1=await _0x44c78d[_0x1ae0c8(0x8a)]({'reload':![]});let _0xc1259d=_0x44c78d[_0x1ae0c8(0x79)],_0x4f334d=_0xc1259d['id'];if(_0x4b2ccd!='mana_dashboard.config'){if(!_0x4f334d){let _0x57d5fe=_0xc1259d['id'];_0x2addb3[_0x1ae0c8(0x78)]({'form_trait_id':_0x57d5fe});}}let _0x442301=_0x14b2e1[_0x1ae0c8(0x7f)],_0xc815b7=_0x442301[_0x1ae0c8(0x83)],[_0xf4d97c]=await _0xc815b7[_0x1ae0c8(0x76)](_0x5a4802,[_0x4f334d]);this[_0x1ae0c8(0x7a)]({'data':_0xf4d97c});},0x0);}}});},0x0);},'destroy'(){const _0x9723a4=_0x1a266d;this[_0x9723a4(0x8c)]&&this['SubForm'][_0x9723a4(0x93)]();}});};