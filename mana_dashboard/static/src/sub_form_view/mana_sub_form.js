/** @odoo-module alias=mana_dashboard.sub_form_view **/
const a0_0x11fcbc=a0_0x8798;(function(_0xa25bb9,_0x24c3d6){const _0x55796c=a0_0x8798,_0x26765b=_0xa25bb9();while(!![]){try{const _0x4882ea=-parseInt(_0x55796c(0x17a))/0x1+parseInt(_0x55796c(0x17f))/0x2*(parseInt(_0x55796c(0x193))/0x3)+parseInt(_0x55796c(0x17b))/0x4*(-parseInt(_0x55796c(0x192))/0x5)+parseInt(_0x55796c(0x197))/0x6*(parseInt(_0x55796c(0x198))/0x7)+-parseInt(_0x55796c(0x182))/0x8*(-parseInt(_0x55796c(0x194))/0x9)+parseInt(_0x55796c(0x17d))/0xa*(parseInt(_0x55796c(0x18b))/0xb)+-parseInt(_0x55796c(0x190))/0xc*(parseInt(_0x55796c(0x180))/0xd);if(_0x4882ea===_0x24c3d6)break;else _0x26765b['push'](_0x26765b['shift']());}catch(_0x242fd7){_0x26765b['push'](_0x26765b['shift']());}}}(a0_0x49df,0x78e68));
 import {useChildRef}  from '@web/core/utils/hooks';
 import {View}  from '@web/views/view';
 import {_t}  from '@web/core/l10n/translation';
 function a0_0x49df(){const _0x2ea61a=['defaultProps','145dFJLfI','1176726TQqbid','1179RTJmlN','discardRecord','onRecordDiscarded','42vdGIic','227304EBEdyh','viewProps','preventCreate','removeRecord','455955cEqEXN','17472xgGGMK','includes','40pogpeX','resId','2GZIFoO','11870391mrkeCk','context','27520xxtukY','viewId','onRecordSaved','modalRef','mode','components','resModel','setup','preventEdit','2532079OkagzQ','bind','save','template','props','12xfwDKa'];a0_0x49df=function(){return _0x2ea61a;};return a0_0x49df();}
 import {ManaView}  from './mana_view';
 import {Component,onMounted,useSubEnv}  from '@odoo/owl';
export  class SubForm extends Component{[a0_0x11fcbc(0x189)](){const _0x1750d3=a0_0x11fcbc;super['setup'](),this[_0x1750d3(0x185)]=useChildRef(),this[_0x1750d3(0x177)]={'type':'form','context':this['props'][_0x1750d3(0x181)]||{},'display':{'controlPanel':![]},'mode':this[_0x1750d3(0x18f)][_0x1750d3(0x186)]||'edit','resId':this[_0x1750d3(0x18f)][_0x1750d3(0x17e)]||![],'resModel':this[_0x1750d3(0x18f)][_0x1750d3(0x188)],'viewId':this['props'][_0x1750d3(0x183)]||![],'preventCreate':this[_0x1750d3(0x18f)][_0x1750d3(0x178)],'preventEdit':this['props'][_0x1750d3(0x18a)],'discardRecord':this[_0x1750d3(0x195)][_0x1750d3(0x18c)](this),'saveRecord':async(_0x7d3f59,{saveAndNew:_0x586cf7})=>{const _0x372490=_0x1750d3,_0x178462=await _0x7d3f59[_0x372490(0x18d)]({'reload':![]});return _0x178462&&await this[_0x372490(0x18f)]['onRecordSaved'](_0x7d3f59),_0x178462;}},this[_0x1750d3(0x18f)][_0x1750d3(0x179)]&&(this[_0x1750d3(0x177)][_0x1750d3(0x179)]=async()=>{const _0xec0b6a=_0x1750d3;await this[_0xec0b6a(0x18f)][_0xec0b6a(0x179)]();}),useSubEnv({'config':{'onRecordChanged':this[_0x1750d3(0x18f)]['onRecordChanged'],'onRecordSaved':this[_0x1750d3(0x18f)][_0x1750d3(0x184)]}});}async[a0_0x11fcbc(0x195)](){const _0x12d7ee=a0_0x11fcbc;this[_0x12d7ee(0x18f)][_0x12d7ee(0x196)]&&await this[_0x12d7ee(0x18f)][_0x12d7ee(0x196)]();}};
 function a0_0x8798(_0xfbefa3,_0x330c62){const _0x49df06=a0_0x49df();return a0_0x8798=function(_0x87982e,_0x414f37){_0x87982e=_0x87982e-0x177;let _0x24d75d=_0x49df06[_0x87982e];return _0x24d75d;},a0_0x8798(_0xfbefa3,_0x330c62);}SubForm[a0_0x11fcbc(0x187)]={'ManaView':ManaView},SubForm['props']={'resModel':String,'context':{'type':Object,'optional':!![]},'mode':{'optional':!![],'validate':_0x4307df=>['edit','readonly'][a0_0x11fcbc(0x17c)](_0x4307df)},'onRecordSaved':{'type':Function,'optional':!![]},'onRecordDiscarded':{'type':Function,'optional':!![]},'removeRecord':{'type':Function,'optional':!![]},'onRecordChanged':{'type':Function,'optional':!![]},'resId':{'type':[Number,Boolean],'optional':!![]},'title':{'type':String,'optional':!![]},'viewId':{'type':[Number,Boolean],'optional':!![]},'preventCreate':{'type':Boolean,'optional':!![]},'preventEdit':{'type':Boolean,'optional':!![]},'isToMany':{'type':Boolean,'optional':!![]}},SubForm[a0_0x11fcbc(0x191)]={'onRecordSaved':()=>{},'onRecordChanged':()=>{},'preventCreate':![],'preventEdit':![],'isToMany':![]},SubForm[a0_0x11fcbc(0x18e)]='mana_dashboard.sub_form';