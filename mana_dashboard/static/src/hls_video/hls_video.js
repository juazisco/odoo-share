/** @odoo-module alias=mana_dashboard.hls_video **/
const a0_0x351c85=a0_0x8873;(function(_0x5a1af4,_0x306b90){const _0x27645c=a0_0x8873,_0x4f8a52=_0x5a1af4();while(!![]){try{const _0x4b2b72=-parseInt(_0x27645c(0x93))/0x1*(parseInt(_0x27645c(0x8c))/0x2)+parseInt(_0x27645c(0xad))/0x3*(parseInt(_0x27645c(0x9a))/0x4)+-parseInt(_0x27645c(0xa0))/0x5+-parseInt(_0x27645c(0xab))/0x6+parseInt(_0x27645c(0x99))/0x7+-parseInt(_0x27645c(0x8f))/0x8*(parseInt(_0x27645c(0xaa))/0x9)+parseInt(_0x27645c(0x8b))/0xa;if(_0x4b2b72===_0x306b90)break;else _0x4f8a52['push'](_0x4f8a52['shift']());}catch(_0x47b5cb){_0x4f8a52['push'](_0x4f8a52['shift']());}}}(a0_0x13de,0x66510));
 import {BlockRegistry}  from '@mana_dashboard_base/mana_block_registry';
 import {icons}  from '@mana_dashboard_base/utils/mana_icons';
 import {_t}  from '@web/core/l10n/translation';
 function a0_0x13de(){const _0x57a6da=['hls','BaseView','initialize','pause','isSupported','5493061CBCDWN','9208zGvvAR','destroy','play','addType','DomComponents','Events','1906135woYBtk','prototype','BlockManager','loadSource','extend','add','removed','MANIFEST_PARSED','model','render','18yokbjP','1238034vnMHHU','ensure_libs','327PGEmEq','get','6321350owitCf','8MWUZve','contains','BaseModel','296792wpMYPk','defaults','apply','classList','146731XxGxMH'];a0_0x13de=function(){return _0x57a6da;};return a0_0x13de();}
 import {BlockBase}  from '@mana_dashboard_base/mana_block_base';const BaseView=BlockBase[a0_0x351c85(0x95)],BaseModel=BlockBase[a0_0x351c85(0x8e)];let HLSVideoModel=BaseModel[a0_0x351c85(0xa4)]({'defaults':{...BaseModel['prototype'][a0_0x351c85(0x90)],'tagName':'video','name':_t('HLS Video'),'fetch_model_data':![],'result_type':'standard','classes':['hls_video'],'has_config':![],'template_category':'hls_video','search_sensitive':![],'js_libs':['/mana_dashboard/static/libs/hls/hls.js'],'traits':[{'type':'text','name':'url','label':'URL'}],'attributes':{'url':'https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8'}},'initialize'(){const _0x2fd6fe=a0_0x351c85;BaseModel[_0x2fd6fe(0xa1)][_0x2fd6fe(0x96)]['apply'](this,arguments);}},{'isComponent':_0x3d917d=>{const _0x12c37a=a0_0x351c85;if(_0x3d917d&&_0x3d917d[_0x12c37a(0x92)]&&_0x3d917d['classList'][_0x12c37a(0x8d)]('hls_video'))return{'type':'hls_video'};}}),HLSVideoView=BaseView[a0_0x351c85(0xa4)]({'tagName':'video','events':{...BaseView[a0_0x351c85(0xa1)]['events']},'init'(){const _0x14fa97=a0_0x351c85;BaseView[_0x14fa97(0xa1)]['init'][_0x14fa97(0x91)](this,arguments),this['listenTo'](this[_0x14fa97(0xa8)],'change:url',this[_0x14fa97(0xa9)]);},'render'(){const _0x34100e=a0_0x351c85;return BaseView['prototype']['render'][_0x34100e(0x91)](this,arguments),this[_0x34100e(0xa8)][_0x34100e(0xac)]()['then'](()=>{const _0x33f286=_0x34100e;this[_0x33f286(0x94)]&&(this[_0x33f286(0x94)][_0x33f286(0x9b)](),this[_0x33f286(0x94)]=null);if(Hls[_0x33f286(0x98)]()){this[_0x33f286(0x94)]=new Hls(),this[_0x33f286(0x94)]['attachMedia'](this['el']);let _0x464027=this;this['hls']['on'](Hls[_0x33f286(0x9f)]['MEDIA_ATTACHED'],()=>{const _0x52bc17=_0x33f286;let _0x541b64=this['model'][_0x52bc17(0x8a)]('attributes')['url'];this[_0x52bc17(0x94)][_0x52bc17(0xa3)](_0x541b64),_0x464027[_0x52bc17(0x94)]['on'](Hls[_0x52bc17(0x9f)][_0x52bc17(0xa7)],function(_0x541e86,_0x1abf37){});}),setTimeout(()=>{const _0x5e084b=_0x33f286;this['el'][_0x5e084b(0x9c)]();},0x3e8);}}),this;},'removed'(){const _0x103568=a0_0x351c85;BaseView[_0x103568(0xa1)][_0x103568(0xa6)][_0x103568(0x91)](this,arguments),this[_0x103568(0x94)]&&(this['el'][_0x103568(0x97)](),this[_0x103568(0x94)]['stopLoad'](),this[_0x103568(0x94)][_0x103568(0x9b)](),this[_0x103568(0x94)]=null);}});
 function builder(_0x538c49,_0x2f858c){const _0x4000b5=a0_0x351c85,_0xd1113d=_0x538c49[_0x4000b5(0x9e)];_0x538c49[_0x4000b5(0xa2)]['add']('hls_video',{'label':_t('HLS Video'),'category':'HLS Video','select':!![],'render':()=>{return'<div\x20class=\x22d-flex\x20flex-column\x20align-items-center\x20justify-content-center\x22><div\x20class=\x22chart-icon\x22>'+icons['hls_video_svg']+'</div><div\x20class=\x27anita-block-label\x27>HLS\x20Video</div></div>';},'content':{'type':'hls_video'}}),_0xd1113d[_0x4000b5(0x9d)]('hls_video',{'model':HLSVideoModel,'view':HLSVideoView});}
 function a0_0x8873(_0x227b1f,_0x39ba96){const _0x13dea6=a0_0x13de();return a0_0x8873=function(_0x887367,_0x57c9ee){_0x887367=_0x887367-0x8a;let _0xcfbf7a=_0x13dea6[_0x887367];return _0xcfbf7a;},a0_0x8873(_0x227b1f,_0x39ba96);}BlockRegistry[a0_0x351c85(0xa5)]('hls_video',builder);
export {HLSVideoModel,HLSVideoView};