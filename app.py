<!DOCTYPE html>
<html>
<head>
  <title>Olympus - Great Learning</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="/assets/gl-favicon-v1-2-7b44726a54ca682967d74e59eccfbbe597d4928738c503f1609a9b4e993d1909.svg" />
  <link rel="stylesheet" href="/assets/application-5f1299b394975aad243d90d9cb1a1a1dd8a7f707e36da0ecee93d87271f02f2b.css" media="all" data-turbolinks-track="true" />
  <script type="importmap" data-turbo-track="reload">{
  "imports": {
    "application": "/assets/application-311ebbd75cb2bf7982ad5a1949e189d5a0d8794b56ad6818f9fcbf79a8c2aff9.js",
    "@hotwired/turbo-rails": "/assets/turbo.min-dfd93b3092d1d0ff56557294538d069bdbb28977d3987cb39bc0dd892f32fc57.js",
    "@hotwired/stimulus": "/assets/stimulus.min-d03cf1dff41d6c5698ec2c5d6a501615a7a33754dbeef8d1edd31c928d17c652.js",
    "@hotwired/stimulus-loading": "/assets/stimulus-loading-1fc59770fb1654500044afd3f5f6d7d00800e5be36746d55b94a2963a7a228aa.js",
    "jquery": "/assets/jquery.min-7ee715ee3f73b3fb2f6b3107a4f4aa67bebc05b366aef81d2d164ce30044c7c6.js",
    "controllers/application": "/assets/controllers/application-368d98631bccbf2349e0d4f8269afb3fe9625118341966de054759d96ea86c7e.js",
    "controllers/hello_controller": "/assets/controllers/hello_controller-549135e8e7c683a538c3d6d517339ba470fcfb79d62f738a0a089ba41851a554.js",
    "controllers": "/assets/controllers/index-2db729dddcc5b979110e98de4b6720f83f91a123172e87281d5a58410fc43806.js",
    "controllers/loan_requirement_details": "/assets/controllers/loan_requirement_details-4896f2c373158859ad51d83b7245989fc87fab7d7cf08a6b2f27b2d7f93b9777.js",
    "controllers/payment_transactions": "/assets/controllers/payment_transactions-ba5d0517327f75d1e4ba81b3cdc89f6e1b20bc9503cec06a46982575edd92887.js",
    "controllers/phone_number_validator": "/assets/controllers/phone_number_validator-04024382391bb910584145d8113cf35ef376b55d125bb4516cebeb14ce788597.js"
  }
}</script>
<link rel="modulepreload" href="/assets/application-311ebbd75cb2bf7982ad5a1949e189d5a0d8794b56ad6818f9fcbf79a8c2aff9.js">
<link rel="modulepreload" href="/assets/turbo.min-dfd93b3092d1d0ff56557294538d069bdbb28977d3987cb39bc0dd892f32fc57.js">
<link rel="modulepreload" href="/assets/stimulus.min-d03cf1dff41d6c5698ec2c5d6a501615a7a33754dbeef8d1edd31c928d17c652.js">
<link rel="modulepreload" href="/assets/stimulus-loading-1fc59770fb1654500044afd3f5f6d7d00800e5be36746d55b94a2963a7a228aa.js">
<link rel="modulepreload" href="/assets/jquery.min-7ee715ee3f73b3fb2f6b3107a4f4aa67bebc05b366aef81d2d164ce30044c7c6.js">
<script src="/assets/es-module-shims.min-d89e73202ec09dede55fb74115af9c5f9f2bb965433de1c2446e1faa6dac2470.js" async="async" data-turbo-track="reload"></script>
<script type="module">import "application"</script>
    <link rel="stylesheet" href="/assets/payment_transactions-66ad388ee27c4604e3bda1d1ddb223a8393bbb4b8f3b41f12aca22a663205896.css" media="all" data-turbolinks-track="true" />


  <script src="/assets/application-311ebbd75cb2bf7982ad5a1949e189d5a0d8794b56ad6818f9fcbf79a8c2aff9.js" data-turbolinks-track="true"></script>


    <script src="/assets/controllers/payment_transactions-ba5d0517327f75d1e4ba81b3cdc89f6e1b20bc9503cec06a46982575edd92887.js" data-turbolinks-track="true"></script>



  <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="SPz1xZAfmXIwCbXN86lgVPn0-vr3gZOo_FrUPIxkj2zB-9nnfiXBgKQ0dtApg59UCySrwQQaopbQLPtIB4NAZQ" />

  
<!-- start Rollbar -->
<script>
    console.log('Rollbar!!!');

    var _rollbarConfig = {
        accessToken: "7f92909729704dc991b20b1fd082e078",
        captureUncaught: true,
        captureUnhandledRejections: true,
        payload: {
            environment: "production"
        }
    };
// Rollbar Snippet
!function(r){var e={};function o(n){if(e[n])return e[n].exports;var t=e[n]={i:n,l:!1,exports:{}};return r[n].call(t.exports,t,t.exports,o),t.l=!0,t.exports}o.m=r,o.c=e,o.d=function(r,e,n){o.o(r,e)||Object.defineProperty(r,e,{enumerable:!0,get:n})},o.r=function(r){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(r,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(r,"__esModule",{value:!0})},o.t=function(r,e){if(1&e&&(r=o(r)),8&e)return r;if(4&e&&"object"==typeof r&&r&&r.__esModule)return r;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:r}),2&e&&"string"!=typeof r)for(var t in r)o.d(n,t,function(e){return r[e]}.bind(null,t));return n},o.n=function(r){var e=r&&r.__esModule?function(){return r.default}:function(){return r};return o.d(e,"a",e),e},o.o=function(r,e){return Object.prototype.hasOwnProperty.call(r,e)},o.p="",o(o.s=0)}([function(r,e,o){"use strict";var n=o(1),t=o(5);_rollbarConfig=_rollbarConfig||{},_rollbarConfig.rollbarJsUrl=_rollbarConfig.rollbarJsUrl||"https://cdn.rollbar.com/rollbarjs/refs/tags/v2.23.0/rollbar.min.js",_rollbarConfig.async=void 0===_rollbarConfig.async||_rollbarConfig.async;var a=n.setupShim(window,_rollbarConfig),l=t(_rollbarConfig);window.rollbar=n.Rollbar,a.loadFull(window,document,!_rollbarConfig.async,_rollbarConfig,l)},function(r,e,o){"use strict";var n=o(2),t=o(3);function a(r){return function(){try{return r.apply(this,arguments)}catch(r){try{console.error("[Rollbar]: Internal error",r)}catch(r){}}}}var l=0;function i(r,e){this.options=r,this._rollbarOldOnError=null;var o=l++;this.shimId=function(){return o},"undefined"!=typeof window&&window._rollbarShims&&(window._rollbarShims[o]={handler:e,messages:[]})}var s=o(4),d=function(r,e){return new i(r,e)},c=function(r){return new s(d,r)};function u(r){return a((function(){var e=this,o=Array.prototype.slice.call(arguments,0),n={shim:e,method:r,args:o,ts:new Date};window._rollbarShims[this.shimId()].messages.push(n)}))}i.prototype.loadFull=function(r,e,o,n,t){var l=!1,i=e.createElement("script"),s=e.getElementsByTagName("script")[0],d=s.parentNode;i.crossOrigin="",i.src=n.rollbarJsUrl,o||(i.async=!0),i.onload=i.onreadystatechange=a((function(){if(!(l||this.readyState&&"loaded"!==this.readyState&&"complete"!==this.readyState)){i.onload=i.onreadystatechange=null;try{d.removeChild(i)}catch(r){}l=!0,function(){var e;if(void 0===r._rollbarDidLoad){e=new Error("rollbar.js did not load");for(var o,n,a,l,i=0;o=r._rollbarShims[i++];)for(o=o.messages||[];n=o.shift();)for(a=n.args||[],i=0;i<a.length;++i)if("function"==typeof(l=a[i])){l(e);break}}"function"==typeof t&&t(e)}()}})),d.insertBefore(i,s)},i.prototype.wrap=function(r,e,o){try{var n;if(n="function"==typeof e?e:function(){return e||{}},"function"!=typeof r)return r;if(r._isWrap)return r;if(!r._rollbar_wrapped&&(r._rollbar_wrapped=function(){o&&"function"==typeof o&&o.apply(this,arguments);try{return r.apply(this,arguments)}catch(o){var e=o;throw e&&("string"==typeof e&&(e=new String(e)),e._rollbarContext=n()||{},e._rollbarContext._wrappedSource=r.toString(),window._rollbarWrappedError=e),e}},r._rollbar_wrapped._isWrap=!0,r.hasOwnProperty))for(var t in r)r.hasOwnProperty(t)&&(r._rollbar_wrapped[t]=r[t]);return r._rollbar_wrapped}catch(e){return r}};for(var p="log,debug,info,warn,warning,error,critical,global,configure,handleUncaughtException,handleAnonymousErrors,handleUnhandledRejection,captureEvent,captureDomContentLoaded,captureLoad".split(","),f=0;f<p.length;++f)i.prototype[p[f]]=u(p[f]);r.exports={setupShim:function(r,e){if(r){var o=e.globalAlias||"Rollbar";if("object"==typeof r[o])return r[o];r._rollbarShims={},r._rollbarWrappedError=null;var l=new c(e);return a((function(){e.captureUncaught&&(l._rollbarOldOnError=r.onerror,n.captureUncaughtExceptions(r,l,!0),e.wrapGlobalEventHandlers&&t(r,l,!0)),e.captureUnhandledRejections&&n.captureUnhandledRejections(r,l,!0);var a=e.autoInstrument;return!1!==e.enabled&&(void 0===a||!0===a||"object"==typeof a&&a.network)&&r.addEventListener&&(r.addEventListener("load",l.captureLoad.bind(l)),r.addEventListener("DOMContentLoaded",l.captureDomContentLoaded.bind(l))),r[o]=l,l}))()}},Rollbar:c}},function(r,e,o){"use strict";function n(r,e,o,n){r._rollbarWrappedError&&(n[4]||(n[4]=r._rollbarWrappedError),n[5]||(n[5]=r._rollbarWrappedError._rollbarContext),r._rollbarWrappedError=null);var t=e.handleUncaughtException.apply(e,n);o&&o.apply(r,n),"anonymous"===t&&(e.anonymousErrorsPending+=1)}r.exports={captureUncaughtExceptions:function(r,e,o){if(r){var t;if("function"==typeof e._rollbarOldOnError)t=e._rollbarOldOnError;else if(r.onerror){for(t=r.onerror;t._rollbarOldOnError;)t=t._rollbarOldOnError;e._rollbarOldOnError=t}e.handleAnonymousErrors();var a=function(){var o=Array.prototype.slice.call(arguments,0);n(r,e,t,o)};o&&(a._rollbarOldOnError=t),r.onerror=a}},captureUnhandledRejections:function(r,e,o){if(r){"function"==typeof r._rollbarURH&&r._rollbarURH.belongsToShim&&r.removeEventListener("unhandledrejection",r._rollbarURH);var n=function(r){var o,n,t;try{o=r.reason}catch(r){o=void 0}try{n=r.promise}catch(r){n="[unhandledrejection] error getting `promise` from event"}try{t=r.detail,!o&&t&&(o=t.reason,n=t.promise)}catch(r){}o||(o="[unhandledrejection] error getting `reason` from event"),e&&e.handleUnhandledRejection&&e.handleUnhandledRejection(o,n)};n.belongsToShim=o,r._rollbarURH=n,r.addEventListener("unhandledrejection",n)}}}},function(r,e,o){"use strict";function n(r,e,o){if(e.hasOwnProperty&&e.hasOwnProperty("addEventListener")){for(var n=e.addEventListener;n._rollbarOldAdd&&n.belongsToShim;)n=n._rollbarOldAdd;var t=function(e,o,t){n.call(this,e,r.wrap(o),t)};t._rollbarOldAdd=n,t.belongsToShim=o,e.addEventListener=t;for(var a=e.removeEventListener;a._rollbarOldRemove&&a.belongsToShim;)a=a._rollbarOldRemove;var l=function(r,e,o){a.call(this,r,e&&e._rollbar_wrapped||e,o)};l._rollbarOldRemove=a,l.belongsToShim=o,e.removeEventListener=l}}r.exports=function(r,e,o){if(r){var t,a,l="EventTarget,Window,Node,ApplicationCache,AudioTrackList,ChannelMergerNode,CryptoOperation,EventSource,FileReader,HTMLUnknownElement,IDBDatabase,IDBRequest,IDBTransaction,KeyOperation,MediaController,MessagePort,ModalWindow,Notification,SVGElementInstance,Screen,TextTrack,TextTrackCue,TextTrackList,WebSocket,WebSocketWorker,Worker,XMLHttpRequest,XMLHttpRequestEventTarget,XMLHttpRequestUpload".split(",");for(t=0;t<l.length;++t)r[a=l[t]]&&r[a].prototype&&n(e,r[a].prototype,o)}}},function(r,e,o){"use strict";function n(r,e){this.impl=r(e,this),this.options=e,function(r){for(var e=function(r){return function(){var e=Array.prototype.slice.call(arguments,0);if(this.impl[r])return this.impl[r].apply(this.impl,e)}},o="log,debug,info,warn,warning,error,critical,global,configure,handleUncaughtException,handleAnonymousErrors,handleUnhandledRejection,_createItem,wrap,loadFull,shimId,captureEvent,captureDomContentLoaded,captureLoad".split(","),n=0;n<o.length;n++)r[o[n]]=e(o[n])}(n.prototype)}n.prototype._swapAndProcessMessages=function(r,e){var o,n,t;for(this.impl=r(this.options);o=e.shift();)n=o.method,t=o.args,this[n]&&"function"==typeof this[n]&&("captureDomContentLoaded"===n||"captureLoad"===n?this[n].apply(this,[t[0],o.ts]):this[n].apply(this,t));return this},r.exports=n},function(r,e,o){"use strict";r.exports=function(r){return function(e){if(!e&&!window._rollbarInitialized){for(var o,n,t=(r=r||{}).globalAlias||"Rollbar",a=window.rollbar,l=function(r){return new a(r)},i=0;o=window._rollbarShims[i++];)n||(n=o.handler),o.handler._swapAndProcessMessages(l,o.messages);window[t]=n,window._rollbarInitialized=!0}}}}]);
// End Rollbar Snippet

// window.onerror("TestError: Hello Ninja Dashboard", window.location.href);

</script>
<!-- end Rollbar -->

  <!-- start Mixpanel -->
<script type="text/javascript">(function(e,a){if(!a.__SV){var b=window;try{var c,l,i,j=b.location,g=j.hash;c=function(a,b){return(l=a.match(RegExp(b+"=([^&]*)")))?l[1]:null};g&&c(g,"state")&&(i=JSON.parse(decodeURIComponent(c(g,"state"))),"mpeditor"===i.action&&(b.sessionStorage.setItem("_mpcehash",g),history.replaceState(i.desiredHash||"",e.title,j.pathname+j.search)))}catch(m){}var k,h;window.mixpanel=a;a._i=[];a.init=function(b,c,f){function e(b,a){var c=a.split(".");2==c.length&&(b=b[c[0]],a=c[1]);b[a]=function(){b.push([a].concat(Array.prototype.slice.call(arguments,
  0)))}}var d=a;"undefined"!==typeof f?d=a[f]=[]:f="mixpanel";d.people=d.people||[];d.toString=function(b){var a="mixpanel";"mixpanel"!==f&&(a+="."+f);b||(a+=" (stub)");return a};d.people.toString=function(){return d.toString(1)+".people (stub)"};k="disable time_event track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config reset people.set people.set_once people.increment people.append people.union people.track_charge people.clear_charges people.delete_user".split(" ");
  for(h=0;h<k.length;h++)e(d,k[h]);a._i.push([b,c,f])};a.__SV=1.2;b=e.createElement("script");b.type="text/javascript";b.async=!0;b.src="undefined"!==typeof MIXPANEL_CUSTOM_LIB_URL?MIXPANEL_CUSTOM_LIB_URL:"file:"===e.location.protocol&&"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//)?"https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js":"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";c=e.getElementsByTagName("script")[0];c.parentNode.insertBefore(b,c)}})(document,window.mixpanel||[]);

mixpanel.init('be636828dad51bd56fbfb1e20bbddc37');</script>
<!-- end Mixpanel -->

</head>
<body>

  <div class="container-fluid">
    <input type="hidden" id="current_env" value="production">

                                                                  
        <nav class="navbar navbar-default navbar-fixed-top hide-nav-mobile">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <a class="navbar-brand" href="#">
                    <img src="https://d9jmtjs5r4cgq.cloudfront.net/images/branding/greatlearning-brand-v1-2.svg" alt='Greatlearning'>
                </a>
            </div>
            
            <div class="page-title hidden-xs">
                <h4 class="m-0 p-0"> Payments</h4>
            </div>
            
            <div class="collapse navbar-collapse" id="career-support-navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li id="jobs_tab" class="active"></li>
                </ul>
            </div>
        </div>
    </nav>


<input type="hidden" name="program_fee_code" id="program_fee_code" value="">
<input type="hidden" name="invalid-fee-payment-link" id="invalid-fee-payment-link" value="true">
<div class="wraper">
  <div class="card-container">
    <div class="card-content">
      <svg width="150px" height="150px" viewBox="0 0 150 150" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <g id="Attendance" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
          <g id="Board" transform="translate(-942.000000, -228.000000)">
            <g id="Group-2" transform="translate(941.143750, 227.300000)">
              <circle id="Oval" fill="#E5E7FA" cx="75.85625" cy="75.7" r="75"></circle>
              <path d="M44.45625,106.4 C39.55625,106.4 34.95625,103.4 33.15625,98.5 L31.75625,94.7 C30.65625,91.7 30.75625,88.4 32.05625,85.5 C33.35625,82.6 35.75625,80.3 38.85625,79.2 L57.75625,72.2 C60.95625,71 64.55625,71.2 67.55625,72.8 C69.55625,73.8 70.25625,76.2 69.25625,78.2 C68.25625,80.2 65.85625,80.9 63.85625,79.9 C62.85625,79.4 61.65625,79.3 60.55625,79.7 L41.65625,86.7 C40.65625,87.1 39.85625,87.8 39.35625,88.8 C38.85625,89.8 38.85625,90.9 39.25625,91.9 L40.65625,95.7 C41.45625,97.8 43.75625,98.9 45.85625,98.1 L64.75625,91.1 C65.85625,90.7 66.55625,89.9 66.85625,89.3 C67.95625,87.4 70.45625,86.7 72.35625,87.8 C74.25625,88.9 74.95625,91.4 73.85625,93.3 C72.45625,95.7 70.25625,97.6 67.65625,98.6 L48.75625,105.6 C47.25625,106.2 45.85625,106.4 44.45625,106.4 Z M108.25625,102.9 C107.75625,102.9 107.35625,102.9 106.85625,102.8 L86.75625,100.5 C83.75625,100.2 80.95625,98.7 78.95625,96.4 C77.55625,94.7 77.65625,92.2 79.35625,90.8 C81.05625,89.4 83.55625,89.5 84.95625,91.2 C85.65625,92 86.55625,92.5 87.55625,92.6 L107.65625,94.9 C108.75625,95 109.85625,94.7 110.65625,94 C111.55625,93.3 112.05625,92.3 112.15625,91.2 L112.65625,87.2 C112.95625,85 111.25625,82.9 109.05625,82.7 L88.95625,80.4 C87.75625,80.3 86.65625,80.6 85.75625,81.4 C84.15625,82.9 81.55625,82.8 80.05625,81.1 C78.55625,79.5 78.65625,76.9 80.35625,75.4 C82.95625,73.1 86.35625,71.9 89.85625,72.3 L110.05625,74.7 C116.65625,75.5 121.45625,81.5 120.65625,88.1 L120.15625,92.1 C119.75625,95.3 118.15625,98.2 115.65625,100.2 C113.55625,101.9 110.95625,102.9 108.25625,102.9 Z M75.75625,70 C73.55625,70 71.75625,68.2 71.75625,66 L71.85625,49 C71.85625,46.8 73.65625,45 75.85625,45 C78.05625,45 79.85625,46.8 79.85625,49 L79.75625,66 C79.75625,68.2 77.95625,70 75.75625,70 Z M64.95625,69.9 C63.75625,69.9 62.55625,69.3 61.75625,68.3 L55.65625,60.1 C54.35625,58.3 54.65625,55.8 56.45625,54.5 C58.25625,53.2 60.75625,53.5 62.05625,55.3 L68.15625,63.5 C69.45625,65.3 69.15625,67.8 67.35625,69.1 C66.55625,69.6 65.75625,69.9 64.95625,69.9 Z M86.75625,69.9 C85.95625,69.9 85.05625,69.6 84.35625,69.1 C82.55625,67.8 82.25625,65.3 83.55625,63.5 L89.65625,55.3 C90.95625,53.5 93.45625,53.2 95.25625,54.5 C97.05625,55.8 97.35625,58.3 96.05625,60.1 L89.95625,68.3 C89.25625,69.3 88.05625,69.9 86.75625,69.9 Z" id="Combined-Shape" fill="#6979F8" fill-rule="nonzero"></path>
            </g>
          </g>
        </g>
      </svg>
      <h3>Invalid link</h3>
      <p>The payment link for this program has changed/expired. Please connect with your learning consultant for the new payment link.</p>
    </div>
  </div>
</div>
<input type="hidden" id='invalid_link_error' value=Invalid link due to other reasons>
<footer class="footer flex align-items-center">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <p class="text-center m-0">
            <small>&copy; 2024 All rights reserved.</small>
          </p>
        </div>
      </div>
    </div>
</footer>

  </div>

</body>
</html>

