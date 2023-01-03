(function () {
var cdn = 'https://cdn.admixer.net/analytics/';
var sModules = 'data-from-dom';
var runtimeSrc = cdn + 'tag-manager.runtime.js';
var tagmanSrc = cdn + 'tag-manager.js?m=' + sModules;
function appendScript(src) {
var script = document.createElement('script');
script.src = src;
script.async = true;
document.head.appendChild(script);
}
function appendRuntime() {
var scripts = document.getElementsByTagName('script');
for (var i = 0, ln = scripts.length; i < ln; i++) {
if (scripts[i].src === runtimeSrc) {
return;
}
}
appendScript(runtimeSrc);
}
appendRuntime();
appendScript(tagmanSrc);
(window.admixTMLoad = window.admixTMLoad || []).push({
setPixel: [
'https://inv-nets-eu.admixer.net/dmpapxl.aspx?cntoid=41172022-cf57-4943-af1f-b01e4a4bcdd3&referrer=%%referrer%%&page=%%pageUrl%%',
'https://inv-nets-eu.admixer.net/cntcm.aspx?pvOId=3f0e6568-cee7-4ad2-8e9d-96d79817a902&ssp=2366F914-F0B6-466D-BCD8-FAE722068640&cntoid=41172022-cf57-4943-af1f-b01e4a4bcdd3&pv=1&referrer=%%referrer%%&page=%%pageUrl%%',

],
setData: {"containerOId":"41172022-cf57-4943-af1f-b01e4a4bcdd3"}
,
setDataHandler: 'https://inv-nets-eu.admixer.net/cntdata.aspx?query=',
});
}) ();