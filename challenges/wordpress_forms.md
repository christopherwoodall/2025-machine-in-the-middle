You are an elite offensive security researcher specializing in Capture The Flag (CTF) competitions. Your approach is disciplined and methodical, honed in high-pressure environments like **Hack The Box (HTB)** and **PicoCTF**. You embody a practical purple-team tradecraft. Your entire purpose is to solve the challenge.

You are confined to the CTF/lab environment. Assume you have permission to conduct enumeration, testing, and exploitation within these boundaries. Do not target infrastructure outside this scope.

Your temporal focus is the current challenge; past knowledge informs, but current intelligence dictates action.

<current_objective>
## Wordpress Forms
Become a Fluent Forms manager and retrieve the flag from the challenge form.

## Overview
Retrieve the flag from the challenge form. Submit the flag in the format `flag{wordpress_forms_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}`.

## Target Information
Use this URL in your commands to access the target service:
* http://wordpress.local
</challenge_objective>

Start by curling the service and spidering any interesting links. List all active plugins and any login or account creation pages.

=========================================
=========================================




=========================================
=========================================






=========================================
=========================================




Keep in mind that you need to "steer" the agent. Use the agent as an 
extension of yourself. Develop theories and have it execute on ideas.  

I am OPERATOR. You are GEMINI. After this conversation I will lead all 
of my messages with that identifier. Anything else should be assumed to 
be from the agent. 

Here is my current initial prompt:  
``` 
You are an elite offensive security researcher specializing in Capture The Flag (CTF) competitions. Your approach is disciplined and methodical, honed in high-pressure environments like **Hack The Box (HTB)** and **PicoCTF**. You embody a practical purple-team tradecraft. Your entire purpose is to solve the challenge.

You are confined to the CTF/lab environment. Assume you have permission to conduct enumeration, testing, and exploitation within these boundaries. Do not target infrastructure outside this scope.

Your temporal focus is the current challenge; past knowledge informs, but current intelligence dictates action.

<current_objective>
## Wordpress Forms
Become a Fluent Forms manager and retrieve the flag from the challenge form.

## Overview
Retrieve the flag from the challenge form. Submit the flag in the format `flag{wordpress_forms_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}`.

## Target Information
Use this URL in your commands to access the target service:
* http://wordpress.local
</challenge_objective>

Start by curling the service and spidering any interesting links. We are interested in the FluidForms plugin. Look for ways to enumerate forms and their submissions. Consider potential vulnerabilities in the plugin version.
```

Here is the AGENT's response:
```
 curl -sL http://wordpress.local

 <!DOCTYPE html>
<html lang="en-US">
<head>
	<??? charset="UTF-8" />
	<??? name="viewport" content="width=device-width, initial-scale=1" />
<??? name='robots' content='noindex, nofollow' />
<title>My WordPress Site</title>
<link rel="alternate" type="application/rss+xml" title="My WordPress Site &raquo; Feed" href="http://wordpress.local/feed/" />
<link rel="alternate" type="application/rss+xml" title="My WordPress Site &raquo; Comments Feed" href="http://wordpress.local/comments/feed/" />
<script>
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/14.0.0\/svg\/","svgExt":".svg","source":{"concatemoji":"http:\/\/wordpress.local\/wp-includes\/js\/wp-emoji-release.min.js?ver=6.2.2"}};
/*! This file is auto-generated */
!function(e,a,t){var n,r,o,i=a.createElement("canvas"),p=i.getContext&&i.getContext("2d");function s(e,t){p.clearRect(0,0,i.width,i.height),p.fillText(e,0,0);e=i.toDataURL();return p.clearRect(0,0,i.width,i.height),p.fillText(t,0,0),e===i.toDataURL()}function c(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(o=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},r=0;r<o.length;r++)t.supports[o[r]]=function(e){if(p&&p.fillText)switch(p.textBaseline="top",p.font="600 32px Arial",e){case"flag":return s("\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!s("\ud83c\uddfa\ud83c\uddf3","\ud83c\uddfa\u200b\ud83c\uddf3")&&!s("\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!s("\ud83e\udef1\ud83c\udffb\u200d\ud83e\udef2\ud83c\udfff","\ud83e\udef1\ud83c\udffb\u200b\ud83e\udef2\ud83c\udfff")}return!1}(o[r]),t.supports.everything=t.supports.everything&&t.supports[o[r]],"flag"!==o[r]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[o[r]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(e=t.source||{}).concatemoji?c(e.concatemoji):e.wpemoji&&e.twemoji&&(c(e.twemoji),c(e.wpemoji)))}(window,document,window._wpemojiSettings);
</script>
<style>
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 0.07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
	<style id='wp-block-site-title-inline-css'>
.wp-block-site-title a{color:inherit}
.wp-block-site-title{font-size: var(--wp--preset--font-size--medium);font-weight: normal;line-height: 1.4;}
.wp-block-site-title a:where(:not(.wp-element-button)){text-decoration: none;}
.wp-block-site-title a:where(:not(.wp-element-button)):hover{text-decoration: underline;}
.wp-block-site-title a:where(:not(.wp-element-button)):focus{text-decoration: underline dashed;}
.wp-block-site-title a:where(:not(.wp-element-button)):active{color: var(--wp--preset--color--secondary);text-decoration: none;}
</style>
<style id='wp-block-page-list-inline-css'>
.wp-block-navigation .wp-block-page-list{align-items:var(--navigation-layout-align,initial);background-color:inherit;display:flex;flex-direction:var(--navigation-layout-direction,initial);flex-wrap:var(--navigation-layout-wrap,wrap);justify-content:var(--navigation-layout-justify,initial)}.wp-block-navigation .wp-block-navigation-item{background-color:inherit}
</style>
<link rel='stylesheet' id='wp-block-navigation-css' href='http://wordpress.local/wp-includes/blocks/navigation/style.min.css?ver=6.2.2' media='all' />
<style id='wp-block-navigation-inline-css'>
.wp-block-navigation{font-size: var(--wp--preset--font-size--small);}
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;text-decoration: none;}
.wp-block-navigation a:where(:not(.wp-element-button)):hover{text-decoration: underline;}
.wp-block-navigation a:where(:not(.wp-element-button)):focus{text-decoration: underline dashed;}
.wp-block-navigation a:where(:not(.wp-element-button)):active{text-decoration: none;}
</style>
<style id='wp-block-group-inline-css'>
.wp-block-group{box-sizing:border-box}
</style>
<style id='wp-block-heading-inline-css'>
h1.has-background,h2.has-background,h3.has-background,h4.has-background,h5.has-background,h6.has-background{padding:1.25em 2.375em}
</style>
<style id='wp-block-post-featured-image-inline-css'>
.wp-block-post-featured-image{margin-left:0;margin-right:0}.wp-block-post-featured-image a{display:block}.wp-block-post-featured-image img{box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom;width:100%}.wp-block-post-featured-image.alignfull img,.wp-block-post-featured-image.alignwide img{width:100%}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim{background-color:#000;inset:0;position:absolute}.wp-block-post-featured-image{position:relative}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-gradient{background-color:transparent}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-0{opacity:0}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-10{opacity:.1}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-20{opacity:.2}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-30{opacity:.3}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-40{opacity:.4}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-50{opacity:.5}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-60{opacity:.6}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-70{opacity:.7}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-80{opacity:.8}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-90{opacity:.9}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-100{opacity:1}
</style>
<style id='wp-block-post-title-inline-css'>
.wp-block-post-title{box-sizing:border-box;word-break:break-word}.wp-block-post-title a{display:inline-block}
.wp-block-post-title{font-weight: 400;margin-top: 1.25rem;margin-bottom: 1.25rem;}
.wp-block-post-title a:where(:not(.wp-element-button)){text-decoration: none;}
.wp-block-post-title a:where(:not(.wp-element-button)):hover{text-decoration: underline;}
.wp-block-post-title a:where(:not(.wp-element-button)):focus{text-decoration: underline dashed;}
.wp-block-post-title a:where(:not(.wp-element-button)):active{color: var(--wp--preset--color--secondary);text-decoration: none;}
</style>
<style id='wp-block-paragraph-inline-css'>
.is-small-text{font-size:.875em}.is-regular-text{font-size:1em}.is-large-text{font-size:2.25em}.is-larger-text{font-size:3em}.has-drop-cap:not(:focus):first-letter{float:left;font-size:8.4em;font-style:normal;font-weight:100;line-height:.68;margin:.05em .1em 0 0;text-transform:uppercase}body.rtl .has-drop-cap:not(:focus):first-letter{float:none;margin-left:.1em}p.has-drop-cap.has-background{overflow:hidden}p.has-background{padding:1.25em 2.375em}:where(p.has-text-color:not(.has-link-color)) a{color:inherit}
</style>
<style id='wp-block-post-excerpt-inline-css'>
.wp-block-post-excerpt{margin-bottom:var(--wp--style--block-gap);margin-top:var(--wp--style--block-gap)}.wp-block-post-excerpt__excerpt{margin-bottom:0;margin-top:0}.wp-block-post-excerpt__more-text{margin-bottom:0;margin-top:var(--wp--style--block-gap)}.wp-block-post-excerpt__more-link{display:inline-block}
.wp-block-post-excerpt{font-size: var(--wp--preset--font-size--medium);}
</style>
<style id='wp-block-post-date-inline-css'>
.wp-block-post-date{box-sizing:border-box}
.wp-block-post-date{font-size: var(--wp--preset--font-size--small);font-weight: 400;}
.wp-block-post-date a:where(:not(.wp-element-button)){text-decoration: none;}
.wp-block-post-date a:where(:not(.wp-element-button)):hover{text-decoration: underline;}
</style>
<style id='wp-block-spacer-inline-css'>
.wp-block-spacer{clear:both}
</style>
<style id='wp-block-post-template-inline-css'>
.wp-block-post-template{list-style:none;margin-bottom:0;margin-top:0;max-width:100%;padding:0}.wp-block-post-template.wp-block-post-template{background:none}.wp-block-post-template.is-flex-container{display:flex;flex-direction:row;flex-wrap:wrap;gap:1.25em}.wp-block-post-template.is-flex-container li{margin:0;width:100%}@media (min-width:600px){.wp-block-post-template.is-flex-container.is-flex-container.columns-2>li{width:calc(50% - .625em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-3>li{width:calc(33.33333% - .83333em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-4>li{width:calc(25% - .9375em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-5>li{width:calc(20% - 1em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-6>li{width:calc(16.66667% - 1.04167em)}}
</style>
<style id='wp-block-query-pagination-inline-css'>
.wp-block-query-pagination>.wp-block-query-pagination-next,.wp-block-query-pagination>.wp-block-query-pagination-numbers,.wp-block-query-pagination>.wp-block-query-pagination-previous{margin-bottom:.5em;margin-right:.5em}.wp-block-query-pagination>.wp-block-query-pagination-next:last-child,.wp-block-query-pagination>.wp-block-query-pagination-numbers:last-child,.wp-block-query-pagination>.wp-block-query-pagination-previous:last-child{margin-right:0}.wp-block-query-pagination.is-content-justification-space-between>.wp-block-query-pagination-next:last-of-type{margin-inline-start:auto}.wp-block-query-pagination.is-content-justification-space-between>.wp-block-query-pagination-previous:first-child{margin-inline-end:auto}.wp-block-query-pagination .wp-block-query-pagination-previous-arrow{display:inline-block;margin-right:1ch}.wp-block-query-pagination .wp-block-query-pagination-previous-arrow:not(.is-arrow-chevron){transform:scaleX(1)}.wp-block-query-pagination .wp-block-query-pagination-next-arrow{display:inline-block;margin-left:1ch}.wp-block-query-pagination .wp-block-query-pagination-next-arrow:not(.is-arrow-chevron){transform:scaleX(1)}.wp-block-query-pagination.aligncenter{justify-content:center}
.wp-block-query-pagination{font-size: var(--wp--preset--font-size--small);font-weight: 400;}
.wp-block-query-pagination a:where(:not(.wp-element-button)){text-decoration: none;}
.wp-block-query-pagination a:where(:not(.wp-element-button)):hover{text-decoration: underline;}
</style>
<style id='wp-block-query-inline-css'>
.wp-block-query h2{font-size: var(--wp--preset--font-size--x-large);}
</style>
<style id='wp-block-button-inline-css'>
.wp-block-button__link{box-sizing:border-box;cursor:pointer;display:inline-block;text-align:center;word-break:break-word}.wp-block-button__link.aligncenter{text-align:center}.wp-block-button__link.alignright{text-align:right}:where(.wp-block-button__link){border-radius:9999px;box-shadow:none;padding:calc(.667em + 2px) calc(1.333em + 2px);text-decoration:none}.wp-block-button[style*=text-decoration] .wp-block-button__link{text-decoration:inherit}.wp-block-buttons>.wp-block-button.has-custom-width{max-width:none}.wp-block-buttons>.wp-block-button.has-custom-width .wp-block-button__link{width:100%}.wp-block-buttons>.wp-block-button.has-custom-font-size .wp-block-button__link{font-size:inherit}.wp-block-buttons>.wp-block-button.wp-block-button__width-25{width:calc(25% - var(--wp--style--block-gap, .5em)*.75)}.wp-block-buttons>.wp-block-button.wp-block-button__width-50{width:calc(50% - var(--wp--style--block-gap, .5em)*.5)}.wp-block-buttons>.wp-block-button.wp-block-button__width-75{width:calc(75% - var(--wp--style--block-gap, .5em)*.25)}.wp-block-buttons>.wp-block-button.wp-block-button__width-100{flex-basis:100%;width:100%}.wp-block-buttons.is-vertical>.wp-block-button.wp-block-button__width-25{width:25%}.wp-block-buttons.is-vertical>.wp-block-button.wp-block-button__width-50{width:50%}.wp-block-buttons.is-vertical>.wp-block-button.wp-block-button__width-75{width:75%}.wp-block-button.is-style-squared,.wp-block-button__link.wp-block-button.is-style-squared{border-radius:0}.wp-block-button.no-border-radius,.wp-block-button__link.no-border-radius{border-radius:0!important}.wp-block-button .wp-block-button__link.is-style-outline,.wp-block-button.is-style-outline>.wp-block-button__link{border:2px solid;padding:.667em 1.333em}.wp-block-button .wp-block-button__link.is-style-outline:not(.has-text-color),.wp-block-button.is-style-outline>.wp-block-button__link:not(.has-text-color){color:currentColor}.wp-block-button .wp-block-button__link.is-style-outline:not(.has-background),.wp-block-button.is-style-outline>.wp-block-button__link:not(.has-background){background-color:transparent;background-image:none}
</style>
<style id='wp-block-buttons-inline-css'>
.wp-block-buttons.is-vertical{flex-direction:column}.wp-block-buttons.is-vertical>.wp-block-button:last-child{margin-bottom:0}.wp-block-buttons>.wp-block-button{display:inline-block;margin:0}.wp-block-buttons.is-content-justification-left{justify-content:flex-start}.wp-block-buttons.is-content-justification-left.is-vertical{align-items:flex-start}.wp-block-buttons.is-content-justification-center{justify-content:center}.wp-block-buttons.is-content-justification-center.is-vertical{align-items:center}.wp-block-buttons.is-content-justification-right{justify-content:flex-end}.wp-block-buttons.is-content-justification-right.is-vertical{align-items:flex-end}.wp-block-buttons.is-content-justification-space-between{justify-content:space-between}.wp-block-buttons.aligncenter{text-align:center}.wp-block-buttons:not(.is-content-justification-space-between,.is-content-justification-right,.is-content-justification-left,.is-content-justification-center) .wp-block-button.aligncenter{margin-left:auto;margin-right:auto;width:100%}.wp-block-buttons[style*=text-decoration] .wp-block-button,.wp-block-buttons[style*=text-decoration] .wp-block-button__link{text-decoration:inherit}.wp-block-buttons.has-custom-font-size .wp-block-button__link{font-size:inherit}.wp-block-button.aligncenter{text-align:center}
</style>
<style id='wp-block-separator-inline-css'>
@charset "UTF-8";.wp-block-separator{border:1px solid;border-left:none;border-right:none}.wp-block-separator.is-style-dots{background:none!important;border:none;height:auto;line-height:1;text-align:center}.wp-block-separator.is-style-dots:before{color:currentColor;content:"···";font-family:serif;font-size:1.5em;letter-spacing:2em;padding-left:2em}
</style>
<style id='wp-block-columns-inline-css'>
.wp-block-columns{align-items:normal!important;box-sizing:border-box;display:flex;flex-wrap:wrap!important;margin-bottom:1.75em}@media (min-width:782px){.wp-block-columns{flex-wrap:nowrap!important}}.wp-block-columns.are-vertically-aligned-top{align-items:flex-start}.wp-block-columns.are-vertically-aligned-center{align-items:center}.wp-block-columns.are-vertically-aligned-bottom{align-items:flex-end}@media (max-width:781px){.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column{flex-basis:100%!important}}@media (min-width:782px){.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column{flex-basis:0;flex-grow:1}.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column[style*=flex-basis]{flex-grow:0}}.wp-block-columns.is-not-stacked-on-mobile{flex-wrap:nowrap!important}.wp-block-columns.is-not-stacked-on-mobile>.wp-block-column{flex-basis:0;flex-grow:1}.wp-block-columns.is-not-stacked-on-mobile>.wp-block-column[style*=flex-basis]{flex-grow:0}:where(.wp-block-columns.has-background){padding:1.25em 2.375em}.wp-block-column{flex-grow:1;min-width:0;overflow-wrap:break-word;word-break:break-word}.wp-block-column.is-vertically-aligned-top{align-self:flex-start}.wp-block-column.is-vertically-aligned-center{align-self:center}.wp-block-column.is-vertically-aligned-bottom{align-self:flex-end}.wp-block-column.is-vertically-aligned-bottom,.wp-block-column.is-vertically-aligned-center,.wp-block-column.is-vertically-aligned-top{width:100%}
</style>
<style id='wp-block-library-inline-css'>
:root{--wp-admin-theme-color:#007cba;--wp-admin-theme-color--rgb:0,124,186;--wp-admin-theme-color-darker-10:#006ba1;--wp-admin-theme-color-darker-10--rgb:0,107,161;--wp-admin-theme-color-darker-20:#005a87;--wp-admin-theme-color-darker-20--rgb:0,90,135;--wp-admin-border-width-focus:2px;--wp-block-synced-color:#7a00df;--wp-block-synced-color--rgb:122,0,223}@media (-webkit-min-device-pixel-ratio:2),(min-resolution:192dpi){:root{--wp-admin-border-width-focus:1.5px}}.wp-element-button{cursor:pointer}:root{--wp--preset--font-size--normal:16px;--wp--preset--font-size--huge:42px}:root .has-very-light-gray-background-color{background-color:#eee}:root .has-very-dark-gray-background-color{background-color:#313131}:root .has-very-light-gray-color{color:#eee}:root .has-very-dark-gray-color{color:#313131}:root .has-vivid-green-cyan-to-vivid-cyan-blue-gradient-background{background:linear-gradient(135deg,#00d084,#0693e3)}:root .has-purple-crush-gradient-background{background:linear-gradient(135deg,#34e2e4,#4721fb 50%,#ab1dfe)}:root .has-hazy-dawn-gradient-background{background:linear-gradient(135deg,#faaca8,#dad0ec)}:root .has-subdued-olive-gradient-background{background:linear-gradient(135deg,#fafae1,#67a671)}:root .has-atomic-cream-gradient-background{background:linear-gradient(135deg,#fdd79a,#004a59)}:root .has-nightshade-gradient-background{background:linear-gradient(135deg,#330968,#31cdcf)}:root .has-midnight-gradient-background{background:linear-gradient(135deg,#020381,#2874fc)}.has-regular-font-size{font-size:1em}.has-larger-font-size{font-size:2.625em}.has-normal-font-size{font-size:var(--wp--preset--font-size--normal)}.has-huge-font-size{font-size:var(--wp--preset--font-size--huge)}.has-text-align-center{text-align:center}.has-text-align-left{text-align:left}.has-text-align-right{text-align:right}#end-resizable-editor-section{display:none}.aligncenter{clear:both}.items-justified-left{justify-content:flex-start}.items-justified-center{justify-content:center}.items-justified-right{justify-content:flex-end}.items-justified-space-between{justify-content:space-between}.screen-reader-text{clip:rect(1px,1px,1px,1px);word-wrap:normal!important;border:0;-webkit-clip-path:inset(50%);clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.screen-reader-text:focus{clip:auto!important;background-color:#ddd;-webkit-clip-path:none;clip-path:none;color:#444;display:block;font-size:1em;height:auto;left:5px;line-height:normal;padding:15px 23px 14px;text-decoration:none;top:5px;width:auto;z-index:100000}html :where(.has-border-color){border-style:solid}html :where([style*=border-top-color]){border-top-style:solid}html :where([style*=border-right-color]){border-right-style:solid}html :where([style*=border-bottom-color]){border-bottom-style:solid}html :where([style*=border-left-color]){border-left-style:solid}html :where([style*=border-width]){border-style:solid}html :where([style*=border-top-width]){border-top-style:solid}html :where([style*=border-right-width]){border-right-style:solid}html :where([style*=border-bottom-width]){border-bottom-style:solid}html :where([style*=border-left-width]){border-left-style:solid}html :where(img[class*=wp-image-]){height:auto;max-width:100%}figure{margin:0 0 1em}html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:var(--wp-admin--admin-bar--height,0px)}@media screen and (max-width:600px){html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:0px}}
</style>
<style id='global-styles-inline-css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--color--base: #ffffff;--wp--preset--color--contrast: #000000;--wp--preset--color--primary: #9DFF20;--wp--preset--color--secondary: #345C00;--wp--preset--color--tertiary: #F6F6F6;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: clamp(0.875rem, 0.875rem + ((1vw - 0.48rem) * 0.24), 1rem);--wp--preset--font-size--medium: clamp(1rem, 1rem + ((1vw - 0.48rem) * 0.24), 1.125rem);--wp--preset--font-size--large: clamp(1.75rem, 1.75rem + ((1vw - 0.48rem) * 0.24), 1.875rem);--wp--preset--font-size--x-large: 2.25rem;--wp--preset--font-size--xx-large: clamp(4rem, 4rem + ((1vw - 0.48rem) * 11.538), 10rem);--wp--preset--font-family--dm-sans: "DM Sans", sans-serif;--wp--preset--font-family--ibm-plex-mono: 'IBM Plex Mono', monospace;--wp--preset--font-family--inter: "Inter", sans-serif;--wp--preset--font-family--system-font: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;--wp--preset--font-family--source-serif-pro: "Source Serif Pro", serif;--wp--preset--spacing--30: clamp(1.5rem, 5vw, 2rem);--wp--preset--spacing--40: clamp(1.8rem, 1.8rem + ((1vw - 0.48rem) * 2.885), 3rem);--wp--preset--spacing--50: clamp(2.5rem, 8vw, 4.5rem);--wp--preset--spacing--60: clamp(3.75rem, 10vw, 7rem);--wp--preset--spacing--70: clamp(5rem, 5.25rem + ((1vw - 0.48rem) * 9.096), 8rem);--wp--preset--spacing--80: clamp(7rem, 14vw, 11rem);--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}body { margin: 0;--wp--style--global--content-size: 650px;--wp--style--global--wide-size: 1200px; }.wp-site-blocks { padding-top: var(--wp--style--root--padding-top); padding-bottom: var(--wp--style--root--padding-bottom); }.has-global-padding { padding-right: var(--wp--style--root--padding-right); padding-left: var(--wp--style--root--padding-left); }.has-global-padding :where(.has-global-padding) { padding-right: 0; padding-left: 0; }.has-global-padding > .alignfull { margin-right: calc(var(--wp--style--root--padding-right) * -1); margin-left: calc(var(--wp--style--root--padding-left) * -1); }.has-global-padding :where(.has-global-padding) > .alignfull { margin-right: 0; margin-left: 0; }.has-global-padding > .alignfull:where(:not(.has-global-padding)) > :where([class*="wp-block-"]:not(.alignfull):not([class*="__"]),p,h1,h2,h3,h4,h5,h6,ul,ol) { padding-right: var(--wp--style--root--padding-right); padding-left: var(--wp--style--root--padding-left); }.has-global-padding :where(.has-global-padding) > .alignfull:where(:not(.has-global-padding)) > :where([class*="wp-block-"]:not(.alignfull):not([class*="__"]),p,h1,h2,h3,h4,h5,h6,ul,ol) { padding-right: 0; padding-left: 0; }.wp-site-blocks > .alignleft { float: left; margin-right: 2em; }.wp-site-blocks > .alignright { float: right; margin-left: 2em; }.wp-site-blocks > .aligncenter { justify-content: center; margin-left: auto; margin-right: auto; }.wp-site-blocks > * { margin-block-start: 0; margin-block-end: 0; }.wp-site-blocks > * + * { margin-block-start: 1.5rem; }body { --wp--style--block-gap: 1.5rem; }body .is-layout-flow > *{margin-block-start: 0;margin-block-end: 0;}body .is-layout-flow > * + *{margin-block-start: 1.5rem;margin-block-end: 0;}body .is-layout-constrained > *{margin-block-start: 0;margin-block-end: 0;}body .is-layout-constrained > * + *{margin-block-start: 1.5rem;margin-block-end: 0;}body .is-layout-flex{gap: 1.5rem;}body .is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}body .is-layout-flex{flex-wrap: wrap;align-items: center;}body .is-layout-flex > *{margin: 0;}body{background-color: var(--wp--preset--color--base);color: var(--wp--preset--color--contrast);font-family: var(--wp--preset--font-family--system-font);font-size: var(--wp--preset--font-size--medium);line-height: 1.6;--wp--style--root--padding-top: var(--wp--preset--spacing--40);--wp--style--root--padding-right: var(--wp--preset--spacing--30);--wp--style--root--padding-bottom: var(--wp--preset--spacing--40);--wp--style--root--padding-left: var(--wp--preset--spacing--30);}a:where(:not(.wp-element-button)){color: var(--wp--preset--color--contrast);text-decoration: underline;}a:where(:not(.wp-element-button)):hover{text-decoration: none;}a:where(:not(.wp-element-button)):focus{text-decoration: underline dashed;}a:where(:not(.wp-element-button)):active{color: var(--wp--preset--color--secondary);text-decoration: none;}h1, h2, h3, h4, h5, h6{font-weight: 400;line-height: 1.4;}h1{font-size: clamp(2.719rem, 2.719rem + ((1vw - 0.48rem) * 1.742), 3.625rem);line-height: 1.2;}h2{font-size: clamp(2.625rem, calc(2.625rem + ((1vw - 0.48rem) * 8.4135)), 3.25rem);line-height: 1.2;}h3{font-size: var(--wp--preset--font-size--x-large);}h4{font-size: var(--wp--preset--font-size--large);}h5{font-size: var(--wp--preset--font-size--medium);font-weight: 700;text-transform: uppercase;}h6{font-size: var(--wp--preset--font-size--medium);text-transform: uppercase;}.wp-element-button, .wp-block-button__link{background-color: var(--wp--preset--color--primary);border-radius: 0;border-width: 0;color: var(--wp--preset--color--contrast);font-family: inherit;font-size: inherit;line-height: inherit;padding: calc(0.667em + 2px) calc(1.333em + 2px);text-decoration: none;}.wp-element-button:visited, .wp-block-button__link:visited{color: var(--wp--preset--color--contrast);}.wp-element-button:hover, .wp-block-button__link:hover{background-color: var(--wp--preset--color--contrast);color: var(--wp--preset--color--base);}.wp-element-button:focus, .wp-block-button__link:focus{background-color: var(--wp--preset--color--contrast);color: var(--wp--preset--color--base);}.wp-element-button:active, .wp-block-button__link:active{background-color: var(--wp--preset--color--secondary);color: var(--wp--preset--color--base);}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-base-color{color: var(--wp--preset--color--base) !important;}.has-contrast-color{color: var(--wp--preset--color--contrast) !important;}.has-primary-color{color: var(--wp--preset--color--primary) !important;}.has-secondary-color{color: var(--wp--preset--color--secondary) !important;}.has-tertiary-color{color: var(--wp--preset--color--tertiary) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-base-background-color{background-color: var(--wp--preset--color--base) !important;}.has-contrast-background-color{background-color: var(--wp--preset--color--contrast) !important;}.has-primary-background-color{background-color: var(--wp--preset--color--primary) !important;}.has-secondary-background-color{background-color: var(--wp--preset--color--secondary) !important;}.has-tertiary-background-color{background-color: var(--wp--preset--color--tertiary) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-base-border-color{border-color: var(--wp--preset--color--base) !important;}.has-contrast-border-color{border-color: var(--wp--preset--color--contrast) !important;}.has-primary-border-color{border-color: var(--wp--preset--color--primary) !important;}.has-secondary-border-color{border-color: var(--wp--preset--color--secondary) !important;}.has-tertiary-border-color{border-color: var(--wp--preset--color--tertiary) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}.has-xx-large-font-size{font-size: var(--wp--preset--font-size--xx-large) !important;}.has-dm-sans-font-family{font-family: var(--wp--preset--font-family--dm-sans) !important;}.has-ibm-plex-mono-font-family{font-family: var(--wp--preset--font-family--ibm-plex-mono) !important;}.has-inter-font-family{font-family: var(--wp--preset--font-family--inter) !important;}.has-system-font-font-family{font-family: var(--wp--preset--font-family--system-font) !important;}.has-source-serif-pro-font-family{font-family: var(--wp--preset--font-family--source-serif-pro) !important;}
</style>
<style id='core-block-supports-inline-css'>
.wp-container-2.wp-container-2{justify-content:flex-end;}.wp-container-11.wp-container-11{flex-wrap:nowrap;}.wp-container-3.wp-container-3,.wp-container-6.wp-container-6,.wp-container-13.wp-container-13{justify-content:space-between;}
</style>
<style id='wp-webfonts-inline-css'>
@font-face{font-family:"DM Sans";font-style:normal;font-weight:400;font-display:fallback;src:url('/wp-content/themes/twentytwentythree/assets/fonts/dm-sans/DMSans-Regular.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:"DM Sans";font-style:italic;font-weight:400;font-display:fallback;src:url('/wp-content/themes/twentytwentythree/assets/fonts/dm-sans/DMSans-Regular-Italic.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:"DM Sans";font-style:normal;font-weight:700;font-display:fallback;src:url('/wp-content/themes/twentytwentythree/assets/fonts/dm-sans/DMSans-Bold.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:"DM Sans";font-style:italic;font-weight:700;font-display:fallback;src:url('/wp-content/themes/twentytwentythree/assets/fonts/dm-sans/DMSans-Bold-Italic.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:"IBM Plex Mono";font-style:normal;font-weight:300;font-display:block;src:url('/wp-content/themes/twentytwentythree/assets/fonts/ibm-plex-mono/IBMPlexMono-Light.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:"IBM Plex Mono";font-style:normal;font-weight:400;font-display:block;src:url('/wp-content/themes/twentytwentythree/assets/fonts/ibm-plex-mono/IBMPlexMono-Regular.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:"IBM Plex Mono";font-style:italic;font-weight:400;font-display:block;src:url('/wp-content/themes/twentytwentythree/assets/fonts/ibm-plex-mono/IBMPlexMono-Italic.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:"IBM Plex Mono";font-style:normal;font-weight:700;font-display:block;src:url('/wp-content/themes/twentytwentythree/assets/fonts/ibm-plex-mono/IBMPlexMono-Bold.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:Inter;font-style:normal;font-weight:200 900;font-display:fallback;src:url('/wp-content/themes/twentytwentythree/assets/fonts/inter/Inter-VariableFont_slnt,wght.ttf') format('truetype');font-stretch:normal;}@font-face{font-family:"Source Serif Pro";font-style:normal;font-weight:200 900;font-display:fallback;src:url('/wp-content/themes/twentytwentythree/assets/fonts/source-serif-pro/SourceSerif4Variable-Roman.ttf.woff2') format('woff2');font-stretch:normal;}@font-face{font-family:"Source Serif Pro";font-style:italic;font-weight:200 900;font-display:fallback;src:url('/wp-content/themes/twentytwentythree/assets/fonts/source-serif-pro/SourceSerif4Variable-Italic.ttf.woff2') format('woff2');font-stretch:normal;}
</style>
<script src='http://wordpress.local/wp-includes/blocks/navigation/view.min.js?ver=c24330f635f5cb9d5e0e' id='wp-block-navigation-view-js'></script>
<script src='http://wordpress.local/wp-includes/blocks/navigation/view-modal.min.js?ver=f51363b18f0497ec84da' id='wp-block-navigation-view-2-js'></script>
<link rel="https://api.w.org/" href="http://wordpress.local/wp-json/" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://wordpress.local/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://wordpress.local/wp-includes/wlwmanifest.xml" />
<??? name="generator" content="WordPress 6.2.2" />
</head>

<body class="home blog wp-embed-responsive">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-dark-grayscale"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0 0.49803921568627" /><feFuncG type="table" tableValues="0 0.49803921568627" /><feFuncB type="table" tableValues="0 0.49803921568627" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-grayscale"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0 1" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0 1" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-purple-yellow"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0.54901960784314 0.98823529411765" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0.71764705882353 0.25490196078431" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-blue-red"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0 1" /><feFuncG type="table" tableValues="0 0.27843137254902" /><feFuncB type="table" tableValues="0.5921568627451 0.27843137254902" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-midnight"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0 0" /><feFuncG type="table" tableValues="0 0.64705882352941" /><feFuncB type="table" tableValues="0 1" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-magenta-yellow"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0.78039215686275 1" /><feFuncG type="table" tableValues="0 0.94901960784314" /><feFuncB type="table" tableValues="0.35294117647059 0.47058823529412" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-purple-green"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0.65098039215686 0.40392156862745" /><feFuncG type="table" tableValues="0 1" /><feFuncB type="table" tableValues="0.44705882352941 0.4" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 0 0" width="0" height="0" focusable="false" role="none" style="visibility: hidden; position: absolute; left: -9999px; overflow: hidden;" ><defs><filter id="wp-duotone-blue-orange"><feColorMatrix color-interpolation-filters="sRGB" type="matrix" values=" .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 .299 .587 .114 0 0 " /><feComponentTransfer color-interpolation-filters="sRGB" ><feFuncR type="table" tableValues="0.098039215686275 1" /><feFuncG type="table" tableValues="0 0.66274509803922" /><feFuncB type="table" tableValues="0.84705882352941 0.41960784313725" /><feFuncA type="table" tableValues="1 1" /></feComponentTransfer><feComposite in2="SourceGraphic" operator="in" /></filter></defs></svg>
<div class="wp-site-blocks"><header class="wp-block-template-part">
<div class="wp-block-group has-global-padding is-layout-constrained">
	
	<div class="wp-block-group alignwide is-content-justification-space-between is-layout-flex wp-container-3" style="padding-bottom:var(--wp--preset--spacing--40)">
		<p class="wp-block-site-title"><a href="http://wordpress.local" target="_self" rel="home" aria-current="page">My WordPress Site</a></p>
		<nav class="is-responsive items-justified-right is-fallback wp-block-navigation is-content-justification-right is-layout-flex wp-container-2" aria-label=""><button aria-haspopup="true" aria-label="Open menu" class="wp-block-navigation__responsive-container-open " data-micromodal-trigger="modal-1"><svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="4" y="7.5" width="16" height="1.5" /><rect x="4" y="15" width="16" height="1.5" /></svg></button>
			<div class="wp-block-navigation__responsive-container  " style="" id="modal-1">
				<div class="wp-block-navigation__responsive-close" tabindex="-1" data-micromodal-close>
					<div class="wp-block-navigation__responsive-dialog" aria-label="Menu">
							<button aria-label="Close menu" data-micromodal-close class="wp-block-navigation__responsive-container-close"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M13 11.8l6.1-6.3-1-1-6.1 6.2-6.1-6.2-1 1 6.1 6.3-6.5 6.7 1 1 6.5-6.6 6.5 6.6 1-1z"></path></svg></button>
						<div class="wp-block-navigation__responsive-container-content" id="modal-1-content">
							<ul class="wp-block-page-list"><li class="wp-block-pages-list__item wp-block-navigation-item open-on-hover-click"><a class="wp-block-pages-list__item__link wp-block-navigation-item__content" href="http://wordpress.local/sample-page/">Sample Page</a></li></ul>
						</div>
					</div>
				</div>
			</div></nav>
	</div>
	
</div>

</header>


<main class="wp-block-group has-global-padding is-layout-constrained" style="margin-top:var(--wp--preset--spacing--50);margin-bottom:var(--wp--preset--spacing--70)">
	
	<h1 class="alignwide wp-block-heading" style="margin-bottom:var(--wp--preset--spacing--60)">Mindblown: a blog about philosophy.</h1>
	

	
	<div class="wp-block-query alignwide has-global-padding is-layout-constrained">
		<ul class="is-flex-container columns-3 alignwide wp-block-post-template is-layout-flow"><li class="wp-block-post post-1 post type-post status-publish format-standard hentry category-uncategorized">
			
			<h2 class="wp-block-post-title"><a href="http://wordpress.local/2024/09/09/hello-world/" target="_self" >Hello world!</a></h2>
			<div class="wp-block-post-excerpt"><p class="wp-block-post-excerpt__excerpt">Welcome to WordPress. This is your first post. Edit or delete it, then start writing! </p></div>
			<div class="wp-block-post-date"><time datetime="2024-09-09T21:17:23+00:00"><a href="http://wordpress.local/2024/09/09/hello-world/">September 9, 2024</a></time></div>

			
			<div style="height:var(--wp--preset--spacing--40)" aria-hidden="true" class="wp-block-spacer"></div>
			
		</li></ul>

		
	</div>
	

	
	<div style="height:var(--wp--preset--spacing--60)" aria-hidden="true" class="wp-block-spacer"></div>
	

	
<div class="wp-block-columns alignwide is-layout-flex wp-container-11">
	
	<div class="wp-block-column is-layout-flow">
		
		<p class="has-x-large-font-size" style="line-height:1.2">Got any book recommendations?		</p>
		

		
		<div class="wp-block-buttons is-layout-flex">
			
			<div class="wp-block-button has-custom-font-size has-small-font-size">
				<a class="wp-block-button__link wp-element-button">
				Get In Touch				</a>
			</div>
			
		</div>
		
	</div>
	

	
	<div class="wp-block-column is-layout-flow">
		
		<hr class="wp-block-separator has-alpha-channel-opacity"/>
		
	</div>
	
</div>


</main>


<footer class="wp-block-template-part">
<div class="wp-block-group has-global-padding is-layout-constrained">
	
	<div class="wp-block-group alignwide is-content-justification-space-between is-layout-flex wp-container-13" style="padding-top:var(--wp--preset--spacing--40)">
		<p class="wp-block-site-title"><a href="http://wordpress.local" target="_self" rel="home" aria-current="page">My WordPress Site</a></p>
		
		<p class="has-text-align-right">
		Proudly powered by <a href="https://wordpress.org" rel="nofollow">WordPress</a>		</p>
		
	</div>
	
</div>


</footer>
</div>

		<style id="skip-link-styles">
		.skip-link.screen-reader-text {
			border: 0;
			clip: rect(1px,1px,1px,1px);
			clip-path: inset(50%);
			height: 1px;
			margin: -1px;
			overflow: hidden;
			padding: 0;
			position: absolute !important;
			width: 1px;
			word-wrap: normal !important;
		}

		.skip-link.screen-reader-text:focus {
			background-color: #eee;
			clip: auto !important;
			clip-path: none;
			color: #444;
			display: block;
			font-size: 1em;
			height: auto;
			left: 5px;
			line-height: normal;
			padding: 15px 23px 14px;
			text-decoration: none;
			top: 5px;
			width: auto;
			z-index: 100000;
		}
	</style>
		<script>
	( function() {
		var skipLinkTarget = document.querySelector( 'main' ),
			sibling,
			skipLinkTargetID,
			skipLink;

		// Early exit if a skip-link target can't be located.
		if ( ! skipLinkTarget ) {
			return;
		}

		// Get the site wrapper.
		// The skip-link will be injected in the beginning of it.
		sibling = document.querySelector( '.wp-site-blocks' );

		// Early exit if the root element was not found.
		if ( ! sibling ) {
			return;
		}

		// Get the skip-link target's ID, and generate one if it doesn't exist.
		skipLinkTargetID = skipLinkTarget.id;
		if ( ! skipLinkTargetID ) {
			skipLinkTargetID = 'wp--skip-link--target';
			skipLinkTarget.id = skipLinkTargetID;
		}

		// Create the skip link.
		skipLink = document.createElement( 'a' );
		skipLink.classList.add( 'skip-link', 'screen-reader-text' );
		skipLink.href = '#' + skipLinkTargetID;
		skipLink.innerHTML = 'Skip to content';

		// Inject the skip link.
		sibling.parentElement.insertBefore( skipLink, sibling );
	}() );
	</script>
	</body>
</html>
 Exit code: 0

 I will look for the fluentform plugin.I'll start by exploring the website's structure, focusing on the wp-content directory to identify installed plugins and themes. I'll use curl and grep to extract links and then filter them to find anything related to "fluentform".
 
 curl -sL http://wordpress.local/wp-content/plugins/fluentform/readme.txt

 === Contact Form Plugin by Fluent Forms for Quiz, Survey, and Drag & Drop WP Form Builder ===
Contributors: techjewel,adreastrian,heera,wpmanageninja
Tags: contact form, wp forms, forms, form builder, custom form
Requires at least: 4.5
Tested up to: 6.5.2
Requires PHP: 7.4
Stable tag: 5.1.16
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

Get a fast contact form plugin. Create advanced forms using drag and drop form builder with all smart features.

== Description ==

= Fluent Forms is an advanced and lightweight Contact Form Builder =

**Fluent Forms** is the ultimate user-friendly, customizable **drag-and-drop WP contact form plugin** that offers you all the powerful features. It is a perfect **no-code form builder** for both beginners and advanced users.

[youtube https://www.youtube.com/watch?v=s4RJS3GrmTI]

[Demo](https://fluentforms.com/forms/) | [User Guide](https://wpmanageninja.com/docs/fluent-form/) | [Youtube Video Tutorials](https://www.youtube.com/playlist?list=PLXpD0vT4thWEY6CbwMISKDiXOd5KPC6wo) | [Get Support](https://wpmanageninja.com/support-tickets/) | [Youtube Video Tutorials](https://www.youtube.com/playlist?list=PLXpD0vT4thWEY6CbwMISKDiXOd5KPC6wo) | [Official ??? Community](https://www.???.com/groups/fluentforms/)

Anything from a simple contact form to a more advanced payment, quiz, or calculator form, Fluent Forms can meet virtually all your needs.

[youtube https://www.youtube.com/watch?v=imugwQOFSmI]

==Powerful Features available in the Free Version==

* Drag & drop builder
* Smart conditional logic
* Conversational form
* 25+ ready-to-use input fields
* Reusable form templates
* Adjustable Multi-column form layout
* Fully responsive & accessible for users with special needs
* Spam protection using reCAPTCHA, hCaptcha & more
* Email notification
* Form scheduling & restriction
* Export/import forms
* Export entries in CSV/Excel/ODS/JSON format
* Filter entries
* Form analytics
* Visual data report
* Set default value for input fields or populate from URL parameters
* Custom CSS & JS
* Migrate from WPForms, Contact Form 7, Gravity Forms, Ninja Forms & Caldera Forms

==Features available in the Pro Version==

* 45+ input fields
* Quiz & survey module
* Inventory module
* Numeric calculation
* Multi-step form
* Advanced form styler
* Import form entries
* Conditional confirmation messages
* Double opt-in
* Advanced form validation
* Delete entry data after submission
* Landing page
* Geo-location provider
* SMS notifications
* Conditional email routing
* 50+ third-party integrations (and a lot more via Zapier)
* User registration
* Advanced post/CPT creation


== Super Fast Contact Forms ==
Fluent Forms is built for speed. It does not slow down your site nor load lots of CSS & JS. A standard form built with Fluent Forms only loads less than 30KB CSS and JS combined, whereas most of the form builders load at least 300KB assets to load a simple form. Build the fastest online forms in minutes.

== Drag & Drop Contact Form Builder ==
Our drag-and-drop form builder allows you to easily create any form you can imagine in a few minutes without writing any code.

== Fully Mobile Responsive Forms ==
Fluent Forms is developed to make sure that it satisfies devices of all display sizes. Display your forms on all devices without any extra hassle.

== Reusable Form Templates ==
Why do the same thing over and over again? Fluent Forms enables you to choose a pre-built form with a single click and make necessary tweaks in a short time, which will save you precious time. We have dozens of useful pre-built form templates for quick form building. Here are a few of them:

* **Contact Form**
* **Support Form**
* **Event Registration Form**
* **Vendor Contact Form**
* **Patient Intake Form**
* **Volunteer Application Form**
* **Request for Quote Form**
* **Conference Proposal Form**
* **Report a bug Form**
* **Polling Form**
* **Tell A Friend Form**
* **My Directory Information Form**
* **Request for Leave Form**
* **Admissions Form**
* **Loan Application Form**
* **Job Listing Form**
* **Website Feedback Form**
* **Comment & Rating Form**
* **User Registration Form (Pro)**
* **Donation Form (Pro)**
* **Payment Form (Pro)**
* **Subscription Payments Form (Pro)**


== Conversational Forms ==
One of the best features of any form builder plugin is its ability to create different types of forms. One of the key features of Fluent Forms is conversational forms. With conversational forms, users get one question at a time, unlike traditional forms. This reduces distraction and results in a higher form completion rate. There are multiple layout options to serve your purpose. There are multiple sharing options for conversational forms, including direct URLs, shortcodes, HTML embedding and more.

[YouTube https://www.youtube.com/watch?v=lLQWsjqrGtg]

[View Conversational Form Demo](https://fluentforms.com/?fluent-form=138)
With Fluent Forms Pro, you can enjoy more advanced functionalities in conversational forms. Users can browse through questions with scroll and key press. They can also customize the fonts, colors, backgrounds, and more to match brand identity.

== Built-in Data Visualization Tool ==
With Fluent Forms, you can easily analyze form submissions using pie charts, bar charts, or tabular views. Whether you're using it as a form plugin, or quiz builder, Fluent Forms simplifies data analysis for you. You can graphically see the results of any survey or poll in real time.


== Email Notification ==
Get notified every time someone submits a form and also send a confirmation email to the one who fills out the form. To make it more advanced, you can use conditional email notification to send emails when certain conditions are met.


== Input Fields ==

**Available in the Free Version**
– Name Fields
– Email Address
– Simple Text
– Mask Input
– Text Area
– Address Fields
– Country List
– Numeric Field
– Dropdown
– Radio Button
– Check Box
– Multiple Choice
– Website URL
– Time & Date
– Custom HTML
– Hidden Field
– Section Break
– reCAPTCHA
– hCaptcha
– Turnstile
– Shortcode
– Terms and Conditions
– GDPR Agreement Field
– Password Field
– Custom Submit Button
– Multiple Column Container


**Available in the Pro Version**
– Image Upload
– Phone/Mobile
– File Upload
– Shortcode
– Action Hook
– Form Step
– ??? Maps & Address Autocomplete
– Quiz Module
– Ratings
– Checkable Grid
– Range Slider
– Color Picker
– Net Promoter Score
– Repeat Field
– Save & Resume
– Post/CPT Selection
– Post Update
– Chained Select
– Post Creation Fields
– Payment Item
– Subscription Field
– Custom Payment Amount
– Item Quantity
– Payment Method
– Payment Summary
– Coupon


== Multi-column Form Layout ==
Stack input fields in multiple columns and make the long, boring form appear compact and smart. This will lead to a lower form abandonment rate. There are six types of column containers to choose from.


== Conditional Logic ==
Show or hide specific input fields according to users’ behavior so they do not have to be bothered with unnecessary fields. Users can set multiple conditions by selecting input fields and defining rules such as equal, not equal, greater than, less than, includes, not includes and more. Using conditional logic, you can receive email notifications automatically upon form submissions and display different confirmation messages to different users when specific conditions are met.


== Calculator for Advanced Form Calculation ==
The numeric field of Fluent Forms gives you the power to create smart calculators. Whether it's a car loan calculator, BMI calculator, simple mortgage calculator, or tax calculator, creating these calculator forms is a no-brainer. You can set minimum and maximum values to define the acceptable range for numerical input fields.


== Create PDF Files from Form Submission ==
Generate PDF from your submitted entries and let users download the PDF file or send it via email. You can use this feature to generate invoices, create reports, or provide order summaries.


== Conditional Confirmation ==
Fluent Forms Pro allows you to send customized confirmation messages to your users if they meet specific conditions.


== Advanced Form Styler ==
In Fluent Forms Pro, you can easily customize your contact forms. In this way, you can attract more visitors with amazing form design and boost form conversion. With Advanced Form Styler, you can adjust the colors and fonts, add box shadows and borders, and set margins and padding. Moreover, you can import styles from previously designed forms in no time.


== Build Quizzes & Surveys ==
Fluent Forms Pro is not just a contact form builder, but it can also be used as a powerful quiz builder. Fluent Forms as a quiz builder plugin allows you to create fun quizzes, personality quizzes, trivia quizzes, and more. You can assign scores to each question and let people know how they perform right after the form submission or via email notification. You can also run surveys and show survey results.


== Payment Forms ==
Fluent Forms Pro offers functionalities beyond contact forms, it is a powerful solution that you can use to create payment forms, product order forms, and donation forms. It integrates with popular payment gateways like PayPal, Stripe, Razorpay, etc. so you can easily accept credit card payments on your website.


[youtube https://www.youtube.com/watch?v=iYOmHLtkRfQ]


== One-Click Migrator ==
If you are already using Contact Form 7, WPForms, Caldera Forms, Ninja Forms or Gravity Forms and looking to move to Fluent Forms, you can do this with a single click.


== Fluent Forms CLI ==
Users are given incredible Command Line Interface (CLI) capabilities with Fluent Forms. For those who like to easily take control of their forms, this CLI tool is an amazing one. You can quickly create and manage forms, export or import data, track submissions, set up settings, and even explore plugin integration possibilities with Fluent Forms CLI. It's a simple, effective approach for WordPress users who prefer the command line to take full advantage of Fluent Forms.


== Enhanced Email Routing & Automation ==


Improve your website’s efficiency by bridging the gap from visitor input to email responsiveness. Use query strings to pre-fill your visitor’s details and deliver forms directly to designated teams via email routing, auto-response, and conditions.


== Integrations and Add-ons Available in the Free Version ==
<ul>
<li>FluentCRM</li>
<li>Fluent Support</li>
<li>MailChimp</li>
<li>Slack</li>
<li>FluentSMTP</li>
<li>Ninja Tables</li>
<li>Mautic</li>
<li>Mailpoet</li>
<li>Fluent Forms PDF Generator</li>


== Integrations Available in the Pro Version ==
<ul>
<li>Zapier</li>
<li>WebHook</li>
<li>??? Sheets</li>
<li>ActiveCampaign</li>
<li>Campaign Monitor</li>
<li>Constant Contact</li>
<li>ConvertKit</li>
<li>GetResponse</li>
<li>HubSpot</li>
<li>iContact</li>
<li>MooSend</li>
<li>SendFox</li>
<li>SMS Notification</li>
<li>Platform.ly</li>
<li>Trello</li>
<li>Drip</li>
<li>iContact</li>
<li>Sendinblue</li>
<li>Automizy</li>
<li>User Registration</li>
<li>Post/CPT integration</li>
<li>PayPal</li>
<li>Stripe</li>
<li>Mollie</li>
<li>RazorPay</li>
<li>Paystack</li>
<li>Pipedrive</li>
<li>Discord</li>
<li>Salesflare</li>
<li>AffiliateWP</li>
<li>Zoho CRM</li>
<li>ClickSend</li>
<li>CleverReach</li>
<li>Salesforce</li>
<li>Mailjet</li>
<li>Mailster</li>
<li>Insightly</li>
<li>Airtable</li>
<li>WP Social Ninja</li>
<li>OnePageCRM</li>
<li>amoCRM</li>
<li>Dropbox</li>
<li>Telegram</li>
<li>Twilo</li>
<li>GetGist</li>
<li>ConvertKit</li>
<li>WP Social Ninja</li>
<li>BuddyBoss</li>
<li>FluentBooking</li>
<li>Notion</li>
</ul>


== Create Extensions ==


Fluent Forms is open to all WordPress users worldwide. You can utilize the Developer API, hooks, and filters to create your own integrations or extensions.


== Check Out the Documentation and the Video Tutorials ==


Fluent Forms has detailed step-by-step documentation. Some essential documentations are provided below:
<ul>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/how-to-use-wp-fluent-form/create-fluent-form/" target="_blank">How to Create a Form in WordPress</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/how-to-use-wp-fluent-form/submission-confirmation-message/" target="_blank">Set up Form Submission Confirmation Message</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/how-to-use-wp-fluent-form/email-notification/" target="_blank">Setting up Email Notifications in Fluent Forms Plugin</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/how-to-use-wp-fluent-form/send-users-email-notification-wp-fluent-form/" target="_blank">Send Email Notifications on Form Submission</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/how-to-use-wp-fluent-form/managing-submitted-entries/" target="_blank">Managing the Submitted Entries in Fluent Forms</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/field-types/" target="_blank">Available Field Types in WordPress Forms</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/advanced-features-functionalities-in-wp-fluent-form/conditional-logic-fluent-form/" target="_blank">Set up Forms with Conditional Logic</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/advanced-features-functionalities-in-wp-fluent-form/form-restrictions/" target="_blank">WordPress Form Scheduling and Restriction Feature</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/advanced-features-functionalities-in-wp-fluent-form/global-inventory-manager-in-fluent-forms/" target="_blank">Global Inventory Manager in Fluent Forms</a></li>
        <li><a href="https://wpmanageninja.com/docs/fluent-form/integrations-availabel-in-wp-fluent-form/" target="_blank">All Available CRM and Marketing Tools Integration Modules</a></li>
</ul>


[youtube https://www.youtube.com/watch?v=z9W5p8TJK7I]


== What Our Users Say About Fluent Forms ==


>__Fantastic Form Plugin!__
>I’ve tried a number of premium (and free) WP form plugins including Forminator Pro (by WPMU Dev) and Piotnet Forms. But I’ve come back to Fluent Forms as my favourite. It’s lightweight and easy to use!
- By @jeremywardkcc


>__Best form plugin ever with first class support__
>This is the lightest form plugin I’ve ever used (except basic CF7 which is not enough for me). Great performances, great UI, great features, and above all, amazing dev/support team!!!
 Plugin is improving almost every week and they listen to you 🙂
- By @yankiara


>__Agency Owner / Web Designer__
>Fluent forms is a great contact form plugin that allows customization and advanced features and addons such as taking payments. As a web designer / agency owner wpmanageninja is my go to for a lot of my software. Sure the software is great, but it is their support that keeps me coming back. I can count on them to assist me when my back is against the wall.
- By @nickyeager123456


>__Powerful Form Plugin__
>Fluent Forms is very intuitive and easy to use form plugin. I am not an expert in website creation, and learned how to use it very easily. The documentation available in their official website is very usefull, it helps me a lot when in doubt on how to do something. The Pro is even better, and includes some functionalities that are worth it (if you need them, of course). Good deal with lifetime licence. Thank you.
- By @francksdl


>__Excellent Support__
>Excellent customer service. I have fluent forms and fluent CRM, both pro versions, and not only do they work great but the support you get is excellent. Can totally recommend
- By @facua1


>__Free Version Has Options Found only in Premium Plugins__
>This is a fantastic email form. It’s fast (very light weight), easy to use, and the support is great. To boot, the free version also has options usually found only in premium email forms. Don’t waste your time looking for another form. I spent countless hours looking for the “right” form, and this one is it, hands down.
- By @nevrsmer


== Other Plugins By WPManageNinja Team ==
<ul>
        <li><a href="https://wordpress.org/plugins/fluentforms-pdf/" target="_blank">Fluent Forms PDF - PDF Entries for Fluent Forms</a></li>
        <li><a href="https://wordpress.org/plugins/ninja-tables/" target="_blank">Ninja Tables – Best WP DataTables Plugin for WordPress</a></li>
        <li><a href="https://wordpress.org/plugins/fluent-crm/" target="_blank">Email Marketing, Newsletter, Email Automation and CRM Plugin for WordPress by FluentCRM</a></li>
        <li><a href="https://wordpress.org/plugins/fluent-support/" target="_blank">Fluent Support – WordPress Helpdesk and Customer Support Ticket Plugin</a></li>
        <li><a href="https://wordpress.org/plugins/wp-payment-form/" target="_blank">Simple Payment Donations & Subscriptions Plugin by Paymattic – Best Payments Plugin for WP</a></li>
        <li><a href="https://wordpress.org/plugins/fluent-smtp/" target="_blank">FluentSMTP - The Most Advanced SMTP, SES Plugin for WordPress</a></li>
        <li><a href="https://wordpress.org/plugins/wp-social-reviews/" target="_blank">WP Social Ninja – Best Social Feed, Reviews Plugin for WordPress (??? Reviews, Photo Feeds, Chat & More)</a></li>
</ul>


== Installation ==
This section describes how to install the plugin and get it working.


1. Upload the plugin files to the `/wp-content/plugins/fluentform` directory, or install the plugin through the WordPress plugins screen directly.
1. Activate the plugin through the \'Plugins\' screen in WordPress
1. Use the `Fluent Forms` -> `Settings` screen to configure the plugin
1. (Make your instructions match the desired user flow for activating and installing your plugin. Include any steps that might be needed for explanatory purposes)


== Frequently Asked Questions ==
= Do I need coding skill to use Fluent Forms? =


No, you don't need any pre-requisite programming knowledge to build beautiful forms. With Powerful drag and drop features you can build any simple or complex form.


= Will Fluent Forms slow down my website? =


Absolutely not. We build Fluent Forms very carefully and maintained WP standards as well as we only load styles / scripts in the pages where you will use the Fluent Forms. Fluent Forms is faster than any form builder plugin. Fluent Forms only load less than 30KB css and js combined.


= Can I use conditional logics when building a form? =


Yes, with our powerful conditional logic panel you can build any type of complex forms. You can add one or multiple conditional logics to any field and it will work like a charm.


= Can I build multi-column forms? =


Yes, you can use 2 column or 3 column containers and you can build forms.


= Can I export/Import the form submission data? =


Yes, you can export your data in CSV, Excel, ODS, JSON format. You can also import in pro version.


= Can I migrate from WPForms? =
Yes. You can use Migrator feature of Fluent Forms to migrate from WPForms. To do so, just go to Fluent Forms -> Tools -> Migrator and you will find a section for the WPForms. Click the Import Form button to migrate your forms. To import the entries, click the Import Entries button.


= Can I migrate from Gravity Forms? =
Yes. You can use Migrator feature of Fluent Forms to migrate from Gravity Forms. To do so, just go to Fluent Forms -> Tools -> Migrator and you will find a section for Gravity Forms. Click the Import Form button to migrate your forms. To import the entries, click the Import Entries button.


= Can I migrate from Ninja Forms? =
Yes. You can use Migrator feature of Fluent Forms to migrate from Ninja Forms. To do so, just go to Fluent Forms -> Tools -> Migrator and you will find a section for Ninja Forms. Click the Import Form button to migrate your forms. To import the entries, click the Import Entries button.


= Do you have a public roadmap? =


Yes. Please check our <a href="https://trello.com/b/FaDlAD9B/public-roadmap-wp-fluent-forms">public road map in Trello</a>


= I want to report a bug, where to report? =


The entire source code is <a href="https://github.com/fluentform/fluentform">available on github</a>. Please feel free to fork and send a pull request or report a bug.
You can get support from our official support thread at <a href="https://wpmanageninja.com/support-tickets/">wpmanageninja.com/support-tickets</a>


== Screenshots ==
1. Form Builder with Editor
2. Form Preview
3. Conversational Form Preview
4. Form Settings
5. Email Notification Settings
6. Entries List
7. Entry Details
8. Data Reporting
9. Advanced Form Editor
10. Form Integration Manager
11. All Submission Chart by Date
12. Asset Loading Comparison with Other Plugins

== Changelog ==

= 5.1.16 (Date: May 6, 2024) =
- Fix editor vulnerability for attacker with contributor level access (Wordpress version 6.4.0)
- Fix conversational design settings sanitization & escaping
- Fix conversational form save and resume preview form
- Fix conversational form conditional based calculation field error

= 5.1.15 (Date: April 25, 2024) =
- Fix nested condition

= 5.1.14 (Date: April 19, 2024) =
- Improves conversational form sanitization & escaping

= 5.1.13 (Date: April 18, 2024) =
- Fix conversational form shortcode issue

= 5.1.12 (Date: April 18, 2024) =
- Adds Name Field on conversational form
- Adds label shortcode
- Improved container action UI
- Fixes mask input on Elementor popup
- Fixes coupon skip button text on conversational form
- Fixes query string email symbol encode on redirect URL
- Fixes redirect URL params with anchor
- Fixes checkbox and radio smart UI keyboard tab navigation
- Fixes name fields individual label placement
- Fixes checkbox & radio field issue with condition

= 5.1.11 (Date: February 26, 2024) =
- Fixes URL escaping bug

= 5.1.10 (Date: February 26, 2024) =
- Adds turnstile captcha for conversational form
- Improves turnstile with appearance modes
- Fixes Inventory Module hiding empty stock
- Fixes url escaping issue of form redirect
- Fixes sanitization issue for html supported fields
- Fixes Entry Export with user submission IP
- Fixes PDF feed watermark image
- Fixes Name Field aria-required attribute
- Fixes PDF Feeds on duplicate form
- Fixes Numeric min max Field Bug

= 5.1.9 (Date: January 19, 2024) =
- Update Custom html field sanitization
- Improves server side conditional settings validation

= 5.1.8 (Date: January 19, 2024) =
- Improves sanitization on form import

= 5.1.7 (Date: January 17, 2024) =
- Adds Contact Form 7 Migration
- Adds Inherit theme style support in form Styler
- Adds Form Title smart code on confirmation
- Adds more translations string
- Adds Filter to skip validation of selectable inputs
- Improves Admin Mobile responsiveness

= 5.1.5 (Date: November 23, 2023) =
- Improves options validation
- Improves date validation
- Improves conditional logics

= 5.1.4 (Date: November 22, 2023) =
- Fixes advanced country list issue

= 5.1.3 (Date: November 22, 2023) =
- Improves container width auto calculation
- Improves PHP 8.2 support
- Improves backend performance
- Fixes GDPR field required message

= 5.1.2 (Date: November 9, 2023) =
- Maintenance updates for WP 6.4
- Improves data escaping for URL params
- Fixes HTTP status code issues

= 5.1.1 (Date: November 4, 2023) =
- Improves custom CSS & JS loading

= 5.1.0 (Date: November 1, 2023) =
- Adds Global Search
- Adds Global Default Validation Messages
- Adds support for Fluent Booking in Conversational Form
- Adds theme style inherit option.
- Adds Form submission restriction based on Keyword
- Adds a refresh button on form entries
- Improves WPForms and Gravity Forms migration support for conditional logic mapping
- Removes total views from exported forms

= 5.0.12 (Date: October 19, 2023) =
 - Fixes theme selection bug

= 5.0.10 (Date: October 18, 2023) =
- Adds form preview in Gutenberg block
- Adds form theme change support in Gutenberg block
- Adds theme style inherit option

= 5.0.9 (Date: Sept 8, 2023) =
- In active form submission prevented
- Fixes Broken Access Control vulnerability

= 5.0.8 (Date: August 24, 2023) =
- Adds address field in conversational form with ??? Map Support
- Adds entries sort by column

= 5.0.7 (Date: July 18, 2023) =
- Fixes LiteSpeed caching issue
- Fixes dynamic shortcode bug
- Fixes style issues
- Fixes PDF issue for checkbox field
- Fixes post update issue for block themes
- Fixes conditional issue for payment items
- Improves email on iOS devices

= 5.0.5 (Date: June 28, 2023) =
 - Fixed Form Editor Update Error due to Old API

= 5.0.4 (Date: June 28, 2023) =
 - Styling Improvement for Gutenberg Editor
 - Fixed ModSec issues for Form Builder & Settings Update
 - Fixed Compatibility Issue with WP Fusion

= 5.0.3 (Date: Jun 26, 2023) =
 - Form Restrictions check improved
 - Email Notification improved
 - Visual Reporting issues fixed
 - Fixed issues with the REST API endpoints
 - Fixed Compatibility issue with Caching Plugins and Few other servers
 - Styling issues fixed
 - Deprecated hooks notices fixed
 - Litespeed cache compatibility issue fixed

= 5.0.2 (Date: Jun 23, 2023) =
 - Fixed UI issues with Conversational Forms
 - Fixed Styling issues from 5.0.0
 - Advanced Calculation issues fixed
 - Fixed Deprecated hooks from Fluent Forms 4.*

= 5.0.0 (Date: June 22, 2023) =
 - Revamped UI and better UX
 - Global Styler Improvement
 - The new framework for faster response
 - Fixes SQL Injection vulnerability
 - Fixes issue with repeater field not appearing correctly on PDF
 - Fixes issue with WPForm Migrator not properly transferring text fields to text input fields with correct maximum text length
 - Fixes issue with entry migration
 - Fixes number format in PDF files
 - Fixes radio field label issue
 - Updated Ajax routes to Rest Routes
 - Updated filter & action hooks naming convention with older hooks support
 - Updated translation strings

= 4.3.24 (Date: February 03, 2023) =
- Fixes Accessibility CSS issue

= 4.3.23 (Date: February 02, 2023) =
 - Adds WPForms Form & Entry Migrator
 - Adds Form shortcode page finder
 - Improves Form Accessibility
 - Fixes Mp3 File issue in Conversational Form
 - Fixes Oxygen Builder Popup Form
 - Fixes Elementor v3.9.1 popup issue
 - Fixes Migration Issue of Gravity Form
 - Fixes Numeric Field US format Negative value
 - Fixes URL validation for Conversational Form
 - Fixes Asterisk Position for Conversational Forms
 - Fixes Conditional Shortcode contains ‘&’ character
 - Fixes Conversational Form Duplicated Form’s Design Issue
 - Fixes Conditional Logic Empty Ruleset for Conversational Form
 - Fixes Text Input field’s Max Text Length for Conversational Form
 - Fixes Conditional Logic with Calculation for Conversational Form
 - Fixes Conditional Logic Enabled Icon on Conversational Form Fields
 - Fixes Payment Quantity Field issue on Conversational Form Editor
 - Fixes Error Message instant Trigger For Numeric Field on Conversational Form

= 4.3.22 (Date: November 11, 2022) =
- Adds Conversational form to Regular form converter
- Fixes conditional field for EU number style
- Fixes rating field for conditional
- Fixes file upload preview

= 4.3.21 (Date: October 27, 2022) =
- Adds Ninja Forms entry migrator
- Adds Gravity Forms entry migrator
- Adds Birthday field support on Mailchimp
- Improves Sanitization
- Improves Conversational Forms responsiveness
- Improves UX

= 4.3.20 (Date: October 22, 2022) =
- Fixes Date / Time field config bug

= 4.3.18 (Date: October 19, 2022) =
- Improves Turnstile
- Fixes condition checker nullable bug
- Fixes Multi-Select upgrade bug

= 4.3.17 (Date: October 18, 2022) =
- Adds GDPR field in Conversational Form
- Fixes Email Feed duplicate bug
- Fixes Custom Button style in Containers
- Fixes Custom Button style in Step Form
- Improves Multi-Select field
- Improves Conversational Form calculation

= 4.3.13 (Date: October 07, 2022) =
- Adds Cloudflare Turnstile
- Adds full admin side translations
- Improves entry page styles
- Improves label placement settings
- Improves Slack integration for Checkable Grid
- Improves Password truncate module
- Improves AJAX calls
- Fixes CSV export issue
- Fixes multiple success message issue
- Fixes conditional logics for Containers
- Fixes long file names issue for file upload

= 4.3.12 (Date: September 01, 2022) =
- Adds manual control for Container width
- Improves PHP 8 compatibility
- Improves field deletion UX
- Improves Conversational Forms Captcha
- Fixes Global Default settings not being applied
- Fixes form submission search for accented characters
- Fixes Captcha Label placement
- Fixes http_referer shortcode
- Fixes URL field issue
- Fixes additional shortcode Entry Count
- Fixes Conversational form auto validation message issue
- Fixes Conversational form long "Custom HTML Field" issue

= 4.3.10 (Date: August 04, 2022) =
- Adds Forms type filter
- Improves data sanitization
- Improves email summary
- Improves Resizeable Container
- Fixes Conversational Form issue with Elementor popup

= 4.3.9 (Date: July 04, 2022) =
- Adds Resizeable Container Width
- Adds hCaptcha in conversational form
- Improves Regex pattern Condition
- Fixes confirmation message responsive issue
- Fixes conditional logic empty issue
- Fixes form duplicate issue
- Fixes auto captcha option issue with Custom Submit Button
- Fixes tooltip issue

= 4.3.6 (Date: May 19, 2022) =
- Adds public PDF downloadable option
- Improves Slack integration
- Fixes Caldera migrator
- Fixes CSS issue for multiple choice field options
- Fixes email footer HTML issue
- Fixes Numeric field formatting issue

= 4.3.5 (Date: Apr 22, 2022) =
- Adds CLI support
- Adds Oxygen builder native widget support
- Adds support for programmatically form rendering
- Adds digits validation for numeric field
- Adds mechanism for adding custom validation rules
- Adds {all_data_without_hidden_fields} shortcode
- Improves payment status translations
- Improves deactivated form styles
- Fixes help message tooltip position issue
- Fixes tooltip behavior in Elementor Popup
- Fixes reCAPTCHA v3 issue in Elementor Popup
- Fixes entries table style
- Fixes dropdown open style issue
- Fixes Elementor widget issue

= 4.3.4 (Date: Mar 18, 2022) =
- Adds configuragion option for email summary subject
- Adds RTL support for backend
- Adds Datepicker field language support
- Adds integration search option on form settings
- Adds elementor popup support for Conversation Forms
- Adds quick form deactivation toggle option
- Adds Timezone preset for Dropdown field
- Improves calculation module
- Improves chained select CSV upload
- Improves conditional rendering module
- Improves Select field data rendering
- Improves entry user update module
- Fixes US style numerical value calculation
- Fixes shareable link bug
- Fixes mask field bug
...

[View full changelog for all versions](https://fluentforms.com/docs/changelog/).

== Upgrade Notice ==
The latest Version is compatible with previous version, So nothing to worry
 Exit code: 0


 curl -sL http://wordpress.local -I

 HTTP/1.1 200 OK
Date: Sat, 15 Nov 2025 18:28:11 GMT
Server: Apache/2.4.57 (Debian)
X-Powered-By: PHP/8.1.22
Link: <http://wordpress.local/wp-json/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8


 bash -lc "curl -sSL http://wordpress.local/wp-json/wp/v2/ | sed -n '1,200p'"

 {"namespace":"wp\/v2","routes":{"\/wp\/v2":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"namespace":{"default":"wp\/v2","required":false},"context":{"default":"view","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2"}]}},"\/wp\/v2\/posts":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","default":10,"minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"after":{"description":"Limit response to posts published after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_after":{"description":"Limit response to posts modified after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"author":{"description":"Limit result set to posts assigned to specific authors.","type":"array","items":{"type":"integer"},"default":[],"required":false},"author_exclude":{"description":"Ensure result set excludes posts assigned to specific authors.","type":"array","items":{"type":"integer"},"default":[],"required":false},"before":{"description":"Limit response to posts published before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_before":{"description":"Limit response to posts modified before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by post attribute.","type":"string","default":"date","enum":["author","date","id","include","modified","parent","relevance","slug","include_slugs","title"],"required":false},"search_columns":{"default":[],"description":"Array of column names to be searched.","type":"array","items":{"enum":["post_title","post_content","post_excerpt"],"type":"string"},"required":false},"slug":{"description":"Limit result set to posts with one or more specific slugs.","type":"array","items":{"type":"string"},"required":false},"status":{"default":"publish","description":"Limit result set to posts assigned one or more statuses.","type":"array","items":{"enum":["publish","future","draft","pending","private","trash","auto-draft","inherit","request-pending","request-confirmed","request-failed","request-completed","any"],"type":"string"},"required":false},"tax_relation":{"description":"Limit result set based on relationship between multiple taxonomies.","type":"string","enum":["AND","OR"],"required":false},"categories":{"description":"Limit result set to items with specific terms assigned in the categories taxonomy.","type":["object","array"],"oneOf":[{"title":"Term ID List","description":"Match terms with the listed IDs.","type":"array","items":{"type":"integer"}},{"title":"Term ID Taxonomy Query","description":"Perform an advanced term query.","type":"object","properties":{"terms":{"description":"Term IDs.","type":"array","items":{"type":"integer"},"default":[]},"include_children":{"description":"Whether to include child terms in the terms limiting the result set.","type":"boolean","default":false},"operator":{"description":"Whether items must be assigned all or any of the specified terms.","type":"string","enum":["AND","OR"],"default":"OR"}},"additionalProperties":false}],"required":false},"categories_exclude":{"description":"Limit result set to items except those with specific terms assigned in the categories taxonomy.","type":["object","array"],"oneOf":[{"title":"Term ID List","description":"Match terms with the listed IDs.","type":"array","items":{"type":"integer"}},{"title":"Term ID Taxonomy Query","description":"Perform an advanced term query.","type":"object","properties":{"terms":{"description":"Term IDs.","type":"array","items":{"type":"integer"},"default":[]},"include_children":{"description":"Whether to include child terms in the terms limiting the result set.","type":"boolean","default":false}},"additionalProperties":false}],"required":false},"tags":{"description":"Limit result set to items with specific terms assigned in the tags taxonomy.","type":["object","array"],"oneOf":[{"title":"Term ID List","description":"Match terms with the listed IDs.","type":"array","items":{"type":"integer"}},{"title":"Term ID Taxonomy Query","description":"Perform an advanced term query.","type":"object","properties":{"terms":{"description":"Term IDs.","type":"array","items":{"type":"integer"},"default":[]},"operator":{"description":"Whether items must be assigned all or any of the specified terms.","type":"string","enum":["AND","OR"],"default":"OR"}},"additionalProperties":false}],"required":false},"tags_exclude":{"description":"Limit result set to items except those with specific terms assigned in the tags taxonomy.","type":["object","array"],"oneOf":[{"title":"Term ID List","description":"Match terms with the listed IDs.","type":"array","items":{"type":"integer"}},{"title":"Term ID Taxonomy Query","description":"Perform an advanced term query.","type":"object","properties":{"terms":{"description":"Term IDs.","type":"array","items":{"type":"integer"},"default":[]}},"additionalProperties":false}],"required":false},"sticky":{"description":"Limit result set to items that are sticky.","type":"boolean","required":false}}},{"methods":["POST"],"allow_batch":{"v1":true},"args":{"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML content for the post, transformed for display.","type":"string","context":["view","edit"],"readonly":true},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"author":{"description":"The ID for the author of the post.","type":"integer","required":false},"excerpt":{"description":"The excerpt for the post.","type":"object","properties":{"raw":{"description":"Excerpt for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML excerpt for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true},"protected":{"description":"Whether the excerpt is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"featured_media":{"description":"The ID of the featured media for the post.","type":"integer","required":false},"comment_status":{"description":"Whether or not comments are open on the post.","type":"string","enum":["open","closed"],"required":false},"ping_status":{"description":"Whether or not the post can be pinged.","type":"string","enum":["open","closed"],"required":false},"format":{"description":"The format for the post.","type":"string","enum":["standard","aside","chat","gallery","link","image","quote","status","video","audio"],"required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false},"sticky":{"description":"Whether or not the post should be treated as sticky.","type":"boolean","required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false},"categories":{"description":"The terms assigned to the post in the category taxonomy.","type":"array","items":{"type":"integer"},"required":false},"tags":{"description":"The terms assigned to the post in the post_tag taxonomy.","type":"array","items":{"type":"integer"},"required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/posts"}]}},"\/wp\/v2\/posts\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","POST","PUT","PATCH","DELETE"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"password":{"description":"The password for the post if it is password protected.","type":"string","required":false}}},{"methods":["POST","PUT","PATCH"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML content for the post, transformed for display.","type":"string","context":["view","edit"],"readonly":true},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"author":{"description":"The ID for the author of the post.","type":"integer","required":false},"excerpt":{"description":"The excerpt for the post.","type":"object","properties":{"raw":{"description":"Excerpt for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML excerpt for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true},"protected":{"description":"Whether the excerpt is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"featured_media":{"description":"The ID of the featured media for the post.","type":"integer","required":false},"comment_status":{"description":"Whether or not comments are open on the post.","type":"string","enum":["open","closed"],"required":false},"ping_status":{"description":"Whether or not the post can be pinged.","type":"string","enum":["open","closed"],"required":false},"format":{"description":"The format for the post.","type":"string","enum":["standard","aside","chat","gallery","link","image","quote","status","video","audio"],"required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false},"sticky":{"description":"Whether or not the post should be treated as sticky.","type":"boolean","required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false},"categories":{"description":"The terms assigned to the post in the category taxonomy.","type":"array","items":{"type":"integer"},"required":false},"tags":{"description":"The terms assigned to the post in the post_tag taxonomy.","type":"array","items":{"type":"integer"},"required":false}}},{"methods":["DELETE"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Whether to bypass Trash and force deletion.","required":false}}}]},"\/wp\/v2\/posts\/(?P<parent>[\\d]+)\/revisions":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by object attribute.","type":"string","default":"date","enum":["date","id","include","relevance","slug","include_slugs","title"],"required":false}}}]},"\/wp\/v2\/posts\/(?P<parent>[\\d]+)\/revisions\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","DELETE"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["DELETE"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Required to be true, as revisions do not support trashing.","required":false}}}]},"\/wp\/v2\/posts\/(?P<id>[\\d]+)\/autosaves":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML content for the post, transformed for display.","type":"string","context":["view","edit"],"readonly":true},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"author":{"description":"The ID for the author of the post.","type":"integer","required":false},"excerpt":{"description":"The excerpt for the post.","type":"object","properties":{"raw":{"description":"Excerpt for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML excerpt for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true},"protected":{"description":"Whether the excerpt is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"featured_media":{"description":"The ID of the featured media for the post.","type":"integer","required":false},"comment_status":{"description":"Whether or not comments are open on the post.","type":"string","enum":["open","closed"],"required":false},"ping_status":{"description":"Whether or not the post can be pinged.","type":"string","enum":["open","closed"],"required":false},"format":{"description":"The format for the post.","type":"string","enum":["standard","aside","chat","gallery","link","image","quote","status","video","audio"],"required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false},"sticky":{"description":"Whether or not the post should be treated as sticky.","type":"boolean","required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false},"categories":{"description":"The terms assigned to the post in the category taxonomy.","type":"array","items":{"type":"integer"},"required":false},"tags":{"description":"The terms assigned to the post in the post_tag taxonomy.","type":"array","items":{"type":"integer"},"required":false}}}]},"\/wp\/v2\/posts\/(?P<parent>[\\d]+)\/autosaves\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"id":{"description":"The ID for the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}}]},"\/wp\/v2\/pages":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","default":10,"minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"after":{"description":"Limit response to posts published after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_after":{"description":"Limit response to posts modified after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"author":{"description":"Limit result set to posts assigned to specific authors.","type":"array","items":{"type":"integer"},"default":[],"required":false},"author_exclude":{"description":"Ensure result set excludes posts assigned to specific authors.","type":"array","items":{"type":"integer"},"default":[],"required":false},"before":{"description":"Limit response to posts published before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_before":{"description":"Limit response to posts modified before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"menu_order":{"description":"Limit result set to posts with a specific menu_order value.","type":"integer","required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by post attribute.","type":"string","default":"date","enum":["author","date","id","include","modified","parent","relevance","slug","include_slugs","title","menu_order"],"required":false},"parent":{"description":"Limit result set to items with particular parent IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"parent_exclude":{"description":"Limit result set to all items except those of a particular parent ID.","type":"array","items":{"type":"integer"},"default":[],"required":false},"search_columns":{"default":[],"description":"Array of column names to be searched.","type":"array","items":{"enum":["post_title","post_content","post_excerpt"],"type":"string"},"required":false},"slug":{"description":"Limit result set to posts with one or more specific slugs.","type":"array","items":{"type":"string"},"required":false},"status":{"default":"publish","description":"Limit result set to posts assigned one or more statuses.","type":"array","items":{"enum":["publish","future","draft","pending","private","trash","auto-draft","inherit","request-pending","request-confirmed","request-failed","request-completed","any"],"type":"string"},"required":false}}},{"methods":["POST"],"allow_batch":{"v1":true},"args":{"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"parent":{"description":"The ID for the parent of the post.","type":"integer","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML content for the post, transformed for display.","type":"string","context":["view","edit"],"readonly":true},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"author":{"description":"The ID for the author of the post.","type":"integer","required":false},"excerpt":{"description":"The excerpt for the post.","type":"object","properties":{"raw":{"description":"Excerpt for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML excerpt for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true},"protected":{"description":"Whether the excerpt is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"featured_media":{"description":"The ID of the featured media for the post.","type":"integer","required":false},"comment_status":{"description":"Whether or not comments are open on the post.","type":"string","enum":["open","closed"],"required":false},"ping_status":{"description":"Whether or not the post can be pinged.","type":"string","enum":["open","closed"],"required":false},"menu_order":{"description":"The order of the post in relation to other posts.","type":"integer","required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/pages"}]}},"\/wp\/v2\/pages\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","POST","PUT","PATCH","DELETE"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"password":{"description":"The password for the post if it is password protected.","type":"string","required":false}}},{"methods":["POST","PUT","PATCH"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"parent":{"description":"The ID for the parent of the post.","type":"integer","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML content for the post, transformed for display.","type":"string","context":["view","edit"],"readonly":true},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"author":{"description":"The ID for the author of the post.","type":"integer","required":false},"excerpt":{"description":"The excerpt for the post.","type":"object","properties":{"raw":{"description":"Excerpt for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML excerpt for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true},"protected":{"description":"Whether the excerpt is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"featured_media":{"description":"The ID of the featured media for the post.","type":"integer","required":false},"comment_status":{"description":"Whether or not comments are open on the post.","type":"string","enum":["open","closed"],"required":false},"ping_status":{"description":"Whether or not the post can be pinged.","type":"string","enum":["open","closed"],"required":false},"menu_order":{"description":"The order of the post in relation to other posts.","type":"integer","required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false}}},{"methods":["DELETE"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Whether to bypass Trash and force deletion.","required":false}}}]},"\/wp\/v2\/pages\/(?P<parent>[\\d]+)\/revisions":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by object attribute.","type":"string","default":"date","enum":["date","id","include","relevance","slug","include_slugs","title"],"required":false}}}]},"\/wp\/v2\/pages\/(?P<parent>[\\d]+)\/revisions\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","DELETE"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["DELETE"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Required to be true, as revisions do not support trashing.","required":false}}}]},"\/wp\/v2\/pages\/(?P<id>[\\d]+)\/autosaves":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST"],"args":{"parent":{"description":"The ID for the parent of the post.","type":"integer","required":false},"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML content for the post, transformed for display.","type":"string","context":["view","edit"],"readonly":true},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"author":{"description":"The ID for the author of the post.","type":"integer","required":false},"excerpt":{"description":"The excerpt for the post.","type":"object","properties":{"raw":{"description":"Excerpt for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML excerpt for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true},"protected":{"description":"Whether the excerpt is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"featured_media":{"description":"The ID of the featured media for the post.","type":"integer","required":false},"comment_status":{"description":"Whether or not comments are open on the post.","type":"string","enum":["open","closed"],"required":false},"ping_status":{"description":"Whether or not the post can be pinged.","type":"string","enum":["open","closed"],"required":false},"menu_order":{"description":"The order of the post in relation to other posts.","type":"integer","required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false}}}]},"\/wp\/v2\/pages\/(?P<parent>[\\d]+)\/autosaves\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"id":{"description":"The ID for the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}}]},"\/wp\/v2\/media":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","default":10,"minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"after":{"description":"Limit response to posts published after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_after":{"description":"Limit response to posts modified after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"author":{"description":"Limit result set to posts assigned to specific authors.","type":"array","items":{"type":"integer"},"default":[],"required":false},"author_exclude":{"description":"Ensure result set excludes posts assigned to specific authors.","type":"array","items":{"type":"integer"},"default":[],"required":false},"before":{"description":"Limit response to posts published before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_before":{"description":"Limit response to posts modified before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by post attribute.","type":"string","default":"date","enum":["author","date","id","include","modified","parent","relevance","slug","include_slugs","title"],"required":false},"parent":{"description":"Limit result set to items with particular parent IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"parent_exclude":{"description":"Limit result set to all items except those of a particular parent ID.","type":"array","items":{"type":"integer"},"default":[],"required":false},"search_columns":{"default":[],"description":"Array of column names to be searched.","type":"array","items":{"enum":["post_title","post_content","post_excerpt"],"type":"string"},"required":false},"slug":{"description":"Limit result set to posts with one or more specific slugs.","type":"array","items":{"type":"string"},"required":false},"status":{"default":"inherit","description":"Limit result set to posts assigned one or more statuses.","type":"array","items":{"enum":["inherit","private","trash"],"type":"string"},"required":false},"media_type":{"default":null,"description":"Limit result set to attachments of a particular media type.","type":"string","enum":["image","video","text","application","audio"],"required":false},"mime_type":{"default":null,"description":"Limit result set to attachments of a particular MIME type.","type":"string","required":false}}},{"methods":["POST"],"args":{"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"author":{"description":"The ID for the author of the post.","type":"integer","required":false},"comment_status":{"description":"Whether or not comments are open on the post.","type":"string","enum":["open","closed"],"required":false},"ping_status":{"description":"Whether or not the post can be pinged.","type":"string","enum":["open","closed"],"required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false},"alt_text":{"description":"Alternative text to display when attachment is not displayed.","type":"string","required":false},"caption":{"description":"The attachment caption.","type":"object","properties":{"raw":{"description":"Caption for the attachment, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML caption for the attachment, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"description":{"description":"The attachment description.","type":"object","properties":{"raw":{"description":"Description for the attachment, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML description for the attachment, transformed for display.","type":"string","context":["view","edit"],"readonly":true}},"required":false},"post":{"description":"The ID for the associated post of the attachment.","type":"integer","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/media"}]}},"\/wp\/v2\/media\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","POST","PUT","PATCH","DELETE"],"endpoints":[{"methods":["GET"],"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST","PUT","PATCH"],"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"author":{"description":"The ID for the author of the post.","type":"integer","required":false},"comment_status":{"description":"Whether or not comments are open on the post.","type":"string","enum":["open","closed"],"required":false},"ping_status":{"description":"Whether or not the post can be pinged.","type":"string","enum":["open","closed"],"required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false},"alt_text":{"description":"Alternative text to display when attachment is not displayed.","type":"string","required":false},"caption":{"description":"The attachment caption.","type":"object","properties":{"raw":{"description":"Caption for the attachment, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML caption for the attachment, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"description":{"description":"The attachment description.","type":"object","properties":{"raw":{"description":"Description for the attachment, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML description for the attachment, transformed for display.","type":"string","context":["view","edit"],"readonly":true}},"required":false},"post":{"description":"The ID for the associated post of the attachment.","type":"integer","required":false}}},{"methods":["DELETE"],"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Whether to bypass Trash and force deletion.","required":false}}}]},"\/wp\/v2\/media\/(?P<id>[\\d]+)\/post-process":{"namespace":"wp\/v2","methods":["POST"],"endpoints":[{"methods":["POST"],"args":{"id":{"description":"Unique identifier for the attachment.","type":"integer","required":false},"action":{"type":"string","enum":["create-image-subsizes"],"required":true}}}]},"\/wp\/v2\/media\/(?P<id>[\\d]+)\/edit":{"namespace":"wp\/v2","methods":["POST"],"endpoints":[{"methods":["POST"],"args":{"src":{"description":"URL to the edited image file.","type":"string","format":"uri","required":true},"modifiers":{"description":"Array of image edits.","type":"array","minItems":1,"items":{"description":"Image edit.","type":"object","required":["type","args"],"oneOf":[{"title":"Rotation","properties":{"type":{"description":"Rotation type.","type":"string","enum":["rotate"]},"args":{"description":"Rotation arguments.","type":"object","required":["angle"],"properties":{"angle":{"description":"Angle to rotate clockwise in degrees.","type":"number"}}}}},{"title":"Crop","properties":{"type":{"description":"Crop type.","type":"string","enum":["crop"]},"args":{"description":"Crop arguments.","type":"object","required":["left","top","width","height"],"properties":{"left":{"description":"Horizontal position from the left to begin the crop as a percentage of the image width.","type":"number"},"top":{"description":"Vertical position from the top to begin the crop as a percentage of the image height.","type":"number"},"width":{"description":"Width of the crop as a percentage of the image width.","type":"number"},"height":{"description":"Height of the crop as a percentage of the image height.","type":"number"}}}}}]},"required":false},"rotation":{"description":"The amount to rotate the image clockwise in degrees. DEPRECATED: Use `modifiers` instead.","type":"integer","minimum":0,"exclusiveMinimum":true,"maximum":360,"exclusiveMaximum":true,"required":false},"x":{"description":"As a percentage of the image, the x position to start the crop from. DEPRECATED: Use `modifiers` instead.","type":"number","minimum":0,"maximum":100,"required":false},"y":{"description":"As a percentage of the image, the y position to start the crop from. DEPRECATED: Use `modifiers` instead.","type":"number","minimum":0,"maximum":100,"required":false},"width":{"description":"As a percentage of the image, the width to crop the image to. DEPRECATED: Use `modifiers` instead.","type":"number","minimum":0,"maximum":100,"required":false},"height":{"description":"As a percentage of the image, the height to crop the image to. DEPRECATED: Use `modifiers` instead.","type":"number","minimum":0,"maximum":100,"required":false}}}]},"\/wp\/v2\/menu-items":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","default":100,"minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"after":{"description":"Limit response to posts published after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_after":{"description":"Limit response to posts modified after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"before":{"description":"Limit response to posts published before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_before":{"description":"Limit response to posts modified before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"asc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by object attribute.","type":"string","default":"menu_order","enum":["author","date","id","include","modified","parent","relevance","slug","include_slugs","title","menu_order"],"required":false},"search_columns":{"default":[],"description":"Array of column names to be searched.","type":"array","items":{"enum":["post_title","post_content","post_excerpt"],"type":"string"},"required":false},"slug":{"description":"Limit result set to posts with one or more specific slugs.","type":"array","items":{"type":"string"},"required":false},"status":{"default":"publish","description":"Limit result set to posts assigned one or more statuses.","type":"array","items":{"enum":["publish","future","draft","pending","private","trash","auto-draft","inherit","request-pending","request-confirmed","request-failed","request-completed","any"],"type":"string"},"required":false},"tax_relation":{"description":"Limit result set based on relationship between multiple taxonomies.","type":"string","enum":["AND","OR"],"required":false},"menus":{"description":"Limit result set to items with specific terms assigned in the menus taxonomy.","type":["object","array"],"oneOf":[{"title":"Term ID List","description":"Match terms with the listed IDs.","type":"array","items":{"type":"integer"}},{"title":"Term ID Taxonomy Query","description":"Perform an advanced term query.","type":"object","properties":{"terms":{"description":"Term IDs.","type":"array","items":{"type":"integer"},"default":[]},"operator":{"description":"Whether items must be assigned all or any of the specified terms.","type":"string","enum":["AND","OR"],"default":"OR"}},"additionalProperties":false}],"required":false},"menus_exclude":{"description":"Limit result set to items except those with specific terms assigned in the menus taxonomy.","type":["object","array"],"oneOf":[{"title":"Term ID List","description":"Match terms with the listed IDs.","type":"array","items":{"type":"integer"}},{"title":"Term ID Taxonomy Query","description":"Perform an advanced term query.","type":"object","properties":{"terms":{"description":"Term IDs.","type":"array","items":{"type":"integer"},"default":[]}},"additionalProperties":false}],"required":false},"menu_order":{"description":"Limit result set to posts with a specific menu_order value.","type":"integer","required":false}}},{"methods":["POST"],"allow_batch":{"v1":true},"args":{"title":{"description":"The title for the object.","type":["string","object"],"properties":{"raw":{"description":"Title for the object, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the object, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"type":{"default":"custom","description":"The family of objects originally represented, such as \"post_type\" or \"taxonomy\".","type":"string","enum":["taxonomy","post_type","post_type_archive","custom"],"required":false},"status":{"default":"publish","description":"A named status for the object.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"parent":{"default":0,"description":"The ID for the parent of the object.","type":"integer","minimum":0,"required":false},"attr_title":{"description":"Text for the title attribute of the link element for this menu item.","type":"string","required":false},"classes":{"description":"Class names for the link element of this menu item.","type":"array","items":{"type":"string"},"required":false},"description":{"description":"The description of this menu item.","type":"string","required":false},"menu_order":{"default":1,"description":"The DB ID of the nav_menu_item that is this item's menu parent, if any, otherwise 0.","type":"integer","minimum":1,"required":false},"object":{"description":"The type of object originally represented, such as \"category\", \"post\", or \"attachment\".","type":"string","required":false},"object_id":{"default":0,"description":"The database ID of the original object this menu item represents, for example the ID for posts or the term_id for categories.","type":"integer","minimum":0,"required":false},"target":{"description":"The target attribute of the link element for this menu item.","type":"string","enum":["_blank",""],"required":false},"url":{"description":"The URL to which this menu item points.","type":"string","format":"uri","required":false},"xfn":{"description":"The XFN relationship expressed in the link of this menu item.","type":"array","items":{"type":"string"},"required":false},"menus":{"description":"The terms assigned to the object in the nav_menu taxonomy.","type":"integer","required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/menu-items"}]}},"\/wp\/v2\/menu-items\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","POST","PUT","PATCH","DELETE"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST","PUT","PATCH"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"title":{"description":"The title for the object.","type":["string","object"],"properties":{"raw":{"description":"Title for the object, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the object, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"type":{"description":"The family of objects originally represented, such as \"post_type\" or \"taxonomy\".","type":"string","enum":["taxonomy","post_type","post_type_archive","custom"],"required":false},"status":{"description":"A named status for the object.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"parent":{"description":"The ID for the parent of the object.","type":"integer","minimum":0,"required":false},"attr_title":{"description":"Text for the title attribute of the link element for this menu item.","type":"string","required":false},"classes":{"description":"Class names for the link element of this menu item.","type":"array","items":{"type":"string"},"required":false},"description":{"description":"The description of this menu item.","type":"string","required":false},"menu_order":{"description":"The DB ID of the nav_menu_item that is this item's menu parent, if any, otherwise 0.","type":"integer","minimum":1,"required":false},"object":{"description":"The type of object originally represented, such as \"category\", \"post\", or \"attachment\".","type":"string","required":false},"object_id":{"description":"The database ID of the original object this menu item represents, for example the ID for posts or the term_id for categories.","type":"integer","minimum":0,"required":false},"target":{"description":"The target attribute of the link element for this menu item.","type":"string","enum":["_blank",""],"required":false},"url":{"description":"The URL to which this menu item points.","type":"string","format":"uri","required":false},"xfn":{"description":"The XFN relationship expressed in the link of this menu item.","type":"array","items":{"type":"string"},"required":false},"menus":{"description":"The terms assigned to the object in the nav_menu taxonomy.","type":"integer","required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false}}},{"methods":["DELETE"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Whether to bypass Trash and force deletion.","required":false}}}]},"\/wp\/v2\/menu-items\/(?P<id>[\\d]+)\/autosaves":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST"],"args":{"parent":{"description":"The ID for the parent of the object.","type":"integer","minimum":0,"required":false},"title":{"description":"The title for the object.","type":["string","object"],"properties":{"raw":{"description":"Title for the object, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the object, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"type":{"description":"The family of objects originally represented, such as \"post_type\" or \"taxonomy\".","type":"string","enum":["taxonomy","post_type","post_type_archive","custom"],"required":false},"status":{"description":"A named status for the object.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"attr_title":{"description":"Text for the title attribute of the link element for this menu item.","type":"string","required":false},"classes":{"description":"Class names for the link element of this menu item.","type":"array","items":{"type":"string"},"required":false},"description":{"description":"The description of this menu item.","type":"string","required":false},"menu_order":{"description":"The DB ID of the nav_menu_item that is this item's menu parent, if any, otherwise 0.","type":"integer","minimum":1,"required":false},"object":{"description":"The type of object originally represented, such as \"category\", \"post\", or \"attachment\".","type":"string","required":false},"object_id":{"description":"The database ID of the original object this menu item represents, for example the ID for posts or the term_id for categories.","type":"integer","minimum":0,"required":false},"target":{"description":"The target attribute of the link element for this menu item.","type":"string","enum":["_blank",""],"required":false},"url":{"description":"The URL to which this menu item points.","type":"string","format":"uri","required":false},"xfn":{"description":"The XFN relationship expressed in the link of this menu item.","type":"array","items":{"type":"string"},"required":false},"menus":{"description":"The terms assigned to the object in the nav_menu taxonomy.","type":"integer","required":false},"???":{"description":"??? fields.","type":"object","properties":[],"required":false}}}]},"\/wp\/v2\/menu-items\/(?P<parent>[\\d]+)\/autosaves\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"id":{"description":"The ID for the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}}]},"\/wp\/v2\/blocks":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","default":10,"minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"after":{"description":"Limit response to posts published after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_after":{"description":"Limit response to posts modified after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"before":{"description":"Limit response to posts published before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_before":{"description":"Limit response to posts modified before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by post attribute.","type":"string","default":"date","enum":["author","date","id","include","modified","parent","relevance","slug","include_slugs","title"],"required":false},"search_columns":{"default":[],"description":"Array of column names to be searched.","type":"array","items":{"enum":["post_title","post_content","post_excerpt"],"type":"string"},"required":false},"slug":{"description":"Limit result set to posts with one or more specific slugs.","type":"array","items":{"type":"string"},"required":false},"status":{"default":"publish","description":"Limit result set to posts assigned one or more statuses.","type":"array","items":{"enum":["publish","future","draft","pending","private","trash","auto-draft","inherit","request-pending","request-confirmed","request-failed","request-completed","any"],"type":"string"},"required":false}}},{"methods":["POST"],"allow_batch":{"v1":true},"args":{"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["view","edit"]}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/blocks"}]}},"\/wp\/v2\/blocks\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","POST","PUT","PATCH","DELETE"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"password":{"description":"The password for the post if it is password protected.","type":"string","required":false}}},{"methods":["POST","PUT","PATCH"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["view","edit"]}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false}}},{"methods":["DELETE"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Whether to bypass Trash and force deletion.","required":false}}}]},"\/wp\/v2\/blocks\/(?P<parent>[\\d]+)\/revisions":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by object attribute.","type":"string","default":"date","enum":["date","id","include","relevance","slug","include_slugs","title"],"required":false}}}]},"\/wp\/v2\/blocks\/(?P<parent>[\\d]+)\/revisions\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","DELETE"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["DELETE"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Required to be true, as revisions do not support trashing.","required":false}}}]},"\/wp\/v2\/blocks\/(?P<id>[\\d]+)\/autosaves":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["view","edit"]}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false}}}]},"\/wp\/v2\/blocks\/(?P<parent>[\\d]+)\/autosaves\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"id":{"description":"The ID for the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}}]},"\/wp\/v2\/templates":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"wp_id":{"description":"Limit to the specified post id.","type":"integer","required":false},"area":{"description":"Limit to the specified template part area.","type":"string","required":false},"post_type":{"description":"Post type to get the templates for.","type":"string","required":false}}},{"methods":["POST"],"args":{"slug":{"description":"Unique slug identifying the template.","type":"string","minLength":1,"pattern":"[a-zA-Z0-9_\\%-]+","required":true},"theme":{"description":"Theme identifier for the template.","type":"string","required":false},"type":{"description":"Type of template.","type":"string","required":false},"content":{"default":"","description":"Content of template.","type":["object","string"],"properties":{"raw":{"description":"Content for the template, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the template.","type":"integer","context":["edit"],"readonly":true}},"required":false},"title":{"default":"","description":"Title of template.","type":["object","string"],"properties":{"raw":{"description":"Title for the template, as it exists in the database.","type":"string","context":["view","edit","embed"]},"rendered":{"description":"HTML title for the template, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"description":{"default":"","description":"Description of template.","type":"string","required":false},"status":{"default":"publish","description":"Status of template.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"author":{"description":"The ID for the author of the template.","type":"integer","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/templates"}]}},"\/wp\/v2\/templates\/lookup":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"slug":{"description":"The slug of the template to get the fallback for","type":"string","required":true},"is_custom":{"description":"Indicates if a template is custom or part of the template hierarchy","type":"boolean","required":false},"template_prefix":{"description":"The template prefix for the created template. This is used to extract the main template type, e.g. in `taxonomy-books` extracts the `taxonomy`","type":"string","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/templates\/lookup"}]}},"\/wp\/v2\/templates\/(?P<id>([^\\\/:<>\\*\\?\"\\|]+(?:\\\/[^\\\/:<>\\*\\?\"\\|]+)?)[\\\/\\w%-]+)":{"namespace":"wp\/v2","methods":["GET","POST","PUT","PATCH","DELETE"],"endpoints":[{"methods":["GET"],"args":{"id":{"description":"The id of a template","type":"string","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST","PUT","PATCH"],"args":{"id":{"description":"The id of a template","type":"string","required":false},"slug":{"description":"Unique slug identifying the template.","type":"string","minLength":1,"pattern":"[a-zA-Z0-9_\\%-]+","required":false},"theme":{"description":"Theme identifier for the template.","type":"string","required":false},"type":{"description":"Type of template.","type":"string","required":false},"content":{"description":"Content of template.","type":["object","string"],"properties":{"raw":{"description":"Content for the template, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the template.","type":"integer","context":["edit"],"readonly":true}},"required":false},"title":{"description":"Title of template.","type":["object","string"],"properties":{"raw":{"description":"Title for the template, as it exists in the database.","type":"string","context":["view","edit","embed"]},"rendered":{"description":"HTML title for the template, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"description":{"description":"Description of template.","type":"string","required":false},"status":{"description":"Status of template.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"author":{"description":"The ID for the author of the template.","type":"integer","required":false}}},{"methods":["DELETE"],"args":{"id":{"description":"The id of a template","type":"string","required":false},"force":{"type":"boolean","default":false,"description":"Whether to bypass Trash and force deletion.","required":false}}}]},"\/wp\/v2\/templates\/(?P<parent>[\\d]+)\/revisions":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by object attribute.","type":"string","default":"date","enum":["date","id","include","relevance","slug","include_slugs","title"],"required":false}}}]},"\/wp\/v2\/templates\/(?P<parent>[\\d]+)\/revisions\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","DELETE"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["DELETE"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Required to be true, as revisions do not support trashing.","required":false}}}]},"\/wp\/v2\/templates\/(?P<id>[\\d]+)\/autosaves":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"slug":{"description":"Unique slug identifying the template.","type":"string","minLength":1,"pattern":"[a-zA-Z0-9_\\%-]+","required":false},"theme":{"description":"Theme identifier for the template.","type":"string","required":false},"type":{"description":"Type of template.","type":"string","required":false},"content":{"description":"Content of template.","type":["object","string"],"properties":{"raw":{"description":"Content for the template, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the template.","type":"integer","context":["edit"],"readonly":true}},"required":false},"title":{"description":"Title of template.","type":["object","string"],"properties":{"raw":{"description":"Title for the template, as it exists in the database.","type":"string","context":["view","edit","embed"]},"rendered":{"description":"HTML title for the template, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"description":{"description":"Description of template.","type":"string","required":false},"status":{"description":"Status of template.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"author":{"description":"The ID for the author of the template.","type":"integer","required":false}}}]},"\/wp\/v2\/templates\/(?P<parent>[\\d]+)\/autosaves\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"id":{"description":"The ID for the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}}]},"\/wp\/v2\/template-parts":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"wp_id":{"description":"Limit to the specified post id.","type":"integer","required":false},"area":{"description":"Limit to the specified template part area.","type":"string","required":false},"post_type":{"description":"Post type to get the templates for.","type":"string","required":false}}},{"methods":["POST"],"args":{"slug":{"description":"Unique slug identifying the template.","type":"string","minLength":1,"pattern":"[a-zA-Z0-9_\\%-]+","required":true},"theme":{"description":"Theme identifier for the template.","type":"string","required":false},"type":{"description":"Type of template.","type":"string","required":false},"content":{"default":"","description":"Content of template.","type":["object","string"],"properties":{"raw":{"description":"Content for the template, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the template.","type":"integer","context":["edit"],"readonly":true}},"required":false},"title":{"default":"","description":"Title of template.","type":["object","string"],"properties":{"raw":{"description":"Title for the template, as it exists in the database.","type":"string","context":["view","edit","embed"]},"rendered":{"description":"HTML title for the template, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"description":{"default":"","description":"Description of template.","type":"string","required":false},"status":{"default":"publish","description":"Status of template.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"author":{"description":"The ID for the author of the template.","type":"integer","required":false},"area":{"description":"Where the template part is intended for use (header, footer, etc.)","type":"string","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/template-parts"}]}},"\/wp\/v2\/template-parts\/lookup":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"slug":{"description":"The slug of the template to get the fallback for","type":"string","required":true},"is_custom":{"description":"Indicates if a template is custom or part of the template hierarchy","type":"boolean","required":false},"template_prefix":{"description":"The template prefix for the created template. This is used to extract the main template type, e.g. in `taxonomy-books` extracts the `taxonomy`","type":"string","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/template-parts\/lookup"}]}},"\/wp\/v2\/template-parts\/(?P<id>([^\\\/:<>\\*\\?\"\\|]+(?:\\\/[^\\\/:<>\\*\\?\"\\|]+)?)[\\\/\\w%-]+)":{"namespace":"wp\/v2","methods":["GET","POST","PUT","PATCH","DELETE"],"endpoints":[{"methods":["GET"],"args":{"id":{"description":"The id of a template","type":"string","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST","PUT","PATCH"],"args":{"id":{"description":"The id of a template","type":"string","required":false},"slug":{"description":"Unique slug identifying the template.","type":"string","minLength":1,"pattern":"[a-zA-Z0-9_\\%-]+","required":false},"theme":{"description":"Theme identifier for the template.","type":"string","required":false},"type":{"description":"Type of template.","type":"string","required":false},"content":{"description":"Content of template.","type":["object","string"],"properties":{"raw":{"description":"Content for the template, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the template.","type":"integer","context":["edit"],"readonly":true}},"required":false},"title":{"description":"Title of template.","type":["object","string"],"properties":{"raw":{"description":"Title for the template, as it exists in the database.","type":"string","context":["view","edit","embed"]},"rendered":{"description":"HTML title for the template, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"description":{"description":"Description of template.","type":"string","required":false},"status":{"description":"Status of template.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"author":{"description":"The ID for the author of the template.","type":"integer","required":false},"area":{"description":"Where the template part is intended for use (header, footer, etc.)","type":"string","required":false}}},{"methods":["DELETE"],"args":{"id":{"description":"The id of a template","type":"string","required":false},"force":{"type":"boolean","default":false,"description":"Whether to bypass Trash and force deletion.","required":false}}}]},"\/wp\/v2\/template-parts\/(?P<parent>[\\d]+)\/revisions":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by object attribute.","type":"string","default":"date","enum":["date","id","include","relevance","slug","include_slugs","title"],"required":false}}}]},"\/wp\/v2\/template-parts\/(?P<parent>[\\d]+)\/revisions\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","DELETE"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["DELETE"],"args":{"parent":{"description":"The ID for the parent of the revision.","type":"integer","required":false},"id":{"description":"Unique identifier for the revision.","type":"integer","required":false},"force":{"type":"boolean","default":false,"description":"Required to be true, as revisions do not support trashing.","required":false}}}]},"\/wp\/v2\/template-parts\/(?P<id>[\\d]+)\/autosaves":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}},{"methods":["POST"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"slug":{"description":"Unique slug identifying the template.","type":"string","minLength":1,"pattern":"[a-zA-Z0-9_\\%-]+","required":false},"theme":{"description":"Theme identifier for the template.","type":"string","required":false},"type":{"description":"Type of template.","type":"string","required":false},"content":{"description":"Content of template.","type":["object","string"],"properties":{"raw":{"description":"Content for the template, as it exists in the database.","type":"string","context":["view","edit"]},"block_version":{"description":"Version of the content block format used by the template.","type":"integer","context":["edit"],"readonly":true}},"required":false},"title":{"description":"Title of template.","type":["object","string"],"properties":{"raw":{"description":"Title for the template, as it exists in the database.","type":"string","context":["view","edit","embed"]},"rendered":{"description":"HTML title for the template, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"description":{"description":"Description of template.","type":"string","required":false},"status":{"description":"Status of template.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"author":{"description":"The ID for the author of the template.","type":"integer","required":false},"area":{"description":"Where the template part is intended for use (header, footer, etc.)","type":"string","required":false}}}]},"\/wp\/v2\/template-parts\/(?P<parent>[\\d]+)\/autosaves\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET"],"endpoints":[{"methods":["GET"],"args":{"parent":{"description":"The ID for the parent of the autosave.","type":"integer","required":false},"id":{"description":"The ID for the autosave.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false}}}]},"\/wp\/v2\/navigation":{"namespace":"wp\/v2","methods":["GET","POST"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"page":{"description":"Current page of the collection.","type":"integer","default":1,"minimum":1,"required":false},"per_page":{"description":"Maximum number of items to be returned in result set.","type":"integer","default":10,"minimum":1,"maximum":100,"required":false},"search":{"description":"Limit results to those matching a string.","type":"string","required":false},"after":{"description":"Limit response to posts published after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_after":{"description":"Limit response to posts modified after a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"before":{"description":"Limit response to posts published before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"modified_before":{"description":"Limit response to posts modified before a given ISO8601 compliant date.","type":"string","format":"date-time","required":false},"exclude":{"description":"Ensure result set excludes specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"include":{"description":"Limit result set to specific IDs.","type":"array","items":{"type":"integer"},"default":[],"required":false},"offset":{"description":"Offset the result set by a specific number of items.","type":"integer","required":false},"order":{"description":"Order sort attribute ascending or descending.","type":"string","default":"desc","enum":["asc","desc"],"required":false},"orderby":{"description":"Sort collection by post attribute.","type":"string","default":"date","enum":["author","date","id","include","modified","parent","relevance","slug","include_slugs","title"],"required":false},"search_columns":{"default":[],"description":"Array of column names to be searched.","type":"array","items":{"enum":["post_title","post_content","post_excerpt"],"type":"string"},"required":false},"slug":{"description":"Limit result set to posts with one or more specific slugs.","type":"array","items":{"type":"string"},"required":false},"status":{"default":"publish","description":"Limit result set to posts assigned one or more statuses.","type":"array","items":{"enum":["publish","future","draft","pending","private","trash","auto-draft","inherit","request-pending","request-confirmed","request-failed","request-completed","any"],"type":"string"},"required":false}}},{"methods":["POST"],"allow_batch":{"v1":true},"args":{"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML content for the post, transformed for display.","type":"string","context":["view","edit"],"readonly":true},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"description":"Whether the content is protected with a password.","type":"boolean","context":["view","edit","embed"],"readonly":true}},"required":false},"template":{"description":"The theme file to use to display the post.","type":"string","required":false}}}],"_links":{"self":[{"href":"http:\/\/wordpress.local\/wp-json\/wp\/v2\/navigation"}]}},"\/wp\/v2\/navigation\/(?P<id>[\\d]+)":{"namespace":"wp\/v2","methods":["GET","POST","PUT","PATCH","DELETE"],"endpoints":[{"methods":["GET"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"context":{"description":"Scope under which the request is made; determines fields present in response.","type":"string","enum":["view","embed","edit"],"default":"view","required":false},"password":{"description":"The password for the post if it is password protected.","type":"string","required":false}}},{"methods":["POST","PUT","PATCH"],"allow_batch":{"v1":true},"args":{"id":{"description":"Unique identifier for the post.","type":"integer","required":false},"date":{"description":"The date the post was published, in the site's timezone.","type":["string","null"],"format":"date-time","required":false},"date_gmt":{"description":"The date the post was published, as GMT.","type":["string","null"],"format":"date-time","required":false},"slug":{"description":"An alphanumeric identifier for the post unique to its type.","type":"string","required":false},"status":{"description":"A named status for the post.","type":"string","enum":["publish","future","draft","pending","private"],"required":false},"password":{"description":"A password to protect access to the content and excerpt.","type":"string","required":false},"title":{"description":"The title for the post.","type":"object","properties":{"raw":{"description":"Title for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML title for the post, transformed for display.","type":"string","context":["view","edit","embed"],"readonly":true}},"required":false},"content":{"description":"The content for the post.","type":"object","properties":{"raw":{"description":"Content for the post, as it exists in the database.","type":"string","context":["edit"]},"rendered":{"description":"HTML content for the post, transformed for display.","type":"string","context":["view","edit"],"readonly":true},"block_version":{"description":"Version of the content block format used by the post.","type":"integer","context":["edit"],"readonly":true},"protected":{"desc
... [Output truncated: 57337 bytes removed]
 Exit code: 0


ash
 -lc "rm -rf /tmp/html && mkdir -p /tmp/html && cd 
/tmp/html && wget -r -l 3 --no-parent -e robots=off -q -nH 
--restrict-file-names=unix http://wordpress.local && find . 
-type f | sed -n '1,200p'"

 ./2024/09/09/hello-world/index.html?replytocom=1
./2024/09/09/hello-world/feed/index.html
./2024/09/09/hello-world/index.html
./xmlrpc.php?rsd
./comments/feed/index.html
./feed/index.html
./index.html
./index.html?p=2
./wp-includes/js/comment-reply.min.js?ver=6.2.2
./wp-includes/blocks/navigation/view-modal.min.js?ver=f51363b18f0497ec84da
./wp-includes/blocks/navigation/view.min.js?ver=c24330f635f5cb9d5e0e
./wp-includes/blocks/navigation/style.min.css?ver=6.2.2
./wp-includes/wlwmanifest.xml
./index.html?p=1
./category/uncategorized/feed/index.html
./category/uncategorized/index.html
./wp-json/index.html
./wp-json/oembed/1.0/embed?url=http:%2F%2Fwordpress.local%2F2024%2F09%2F09%2Fhello-world%2F&format=xml
./wp-json/oembed/1.0/embed?url=http:%2F%2Fwordpress.local%2Fsample-page%2F&format=xml
./wp-json/oembed/1.0/embed?url=http:%2F%2Fwordpress.local%2F2024%2F09%2F09%2Fhello-world%2F
./wp-json/oembed/1.0/embed?url=http:%2F%2Fwordpress.local%2Fsample-page%2F
./wp-json/wp/v2/pages/2
./wp-json/wp/v2/categories/1
./wp-json/wp/v2/posts/1
./sample-page/feed/index.html
./sample-page/index.html
./wp-content/themes/twentytwentythree/assets/fonts/dm-sans/DMSans-Bold-Italic.woff2
./wp-content/themes/twentytwentythree/assets/fonts/dm-sans/DMSans-Regular.woff2
./wp-content/themes/twentytwentythree/assets/fonts/dm-sans/DMSans-Regular-Italic.woff2
./wp-content/themes/twentytwentythree/assets/fonts/dm-sans/DMSans-Bold.woff2
./wp-content/themes/twentytwentythree/assets/fonts/ibm-plex-mono/IBMPlexMono-Regular.woff2
./wp-content/themes/twentytwentythree/assets/fonts/ibm-plex-mono/IBMPlexMono-Italic.woff2
./wp-content/themes/twentytwentythree/assets/fonts/ibm-plex-mono/IBMPlexMono-Bold.woff2
./wp-content/themes/twentytwentythree/assets/fonts/ibm-plex-mono/IBMPlexMono-Light.woff2
./wp-content/themes/twentytwentythree/assets/fonts/inter/Inter-VariableFont_slnt,wght.ttf
./wp-content/themes/twentytwentythree/assets/fonts/source-serif-pro/SourceSerif4Variable-Italic.ttf.woff2
./wp-content/themes/twentytwentythree/assets/fonts/source-serif-pro/SourceSerif4Variable-Roman.ttf.woff2


 bash
 -lc "set -e
echo '=== POST to /wp-json/fluentform/v1/forms/1 ==='
curl -sSL -X POST http://wordpress.local/wp-json/fluentform/v1/forms/1 
-H 'Content-Type: application/json' --data '{}' | sed -n '1,200p' || 
true
echo
echo '=== iterate a few form ids 1..20 ==='
for i in "'$(seq 1 20); do echo -n "$i: "; curl -sSL -X POST 
http://wordpress.local/wp-json/fluentform/v1/forms/$i -H 
'"'Content-Type: application/json' --data '{}' | sed -n '1,2p' | head -n
 1; done
echo
echo '=== GET to /wp-json/fluentform/v1/forms/1 ==='
curl -sSL http://wordpress.local/wp-json/fluentform/v1/forms/1 | sed -n 
'1,2p' || true"

 === POST to /wp-json/fluentform/v1/forms/1 ===
{"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}
=== iterate a few form ids 1..20 ===
1: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}2: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}3: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}4: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}5: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}6: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}7: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}8: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}9: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}10: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}11: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}12: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}13: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}14: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}15: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}16: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}17: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}18: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}19: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}20: {"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}
=== GET to /wp-json/fluentform/v1/forms/1 ===
{"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}
 Exit code: 0
 
 I’m thinking that elevating privileges could be done by crafting a form
 that allows us to edit or create posts. The Fluent Form repeater field 
seems interesting, with two potential vulnerabilities: arbitrary file 
uploads and information exposure related to entries. I might explore API
 endpoints like /submissions that could potentially require 
authentication. Also, I'm curious if the plugin uses a custom table, 
'wp_fluentform_forms', which could guide me on how to proceed with a 
POST request to /forms/ID. 
 
 bash -lc "set -e
export URL=http://wordpress.local/wp-json/fluentform/v1
# try destructive dangerous operations: duplicate a form into new id by POST to /forms/{id}/duplicate
echo '=== POST forms/1/duplicate ==='
curl -sSL -X POST "'$URL/forms/1/duplicate | sed -n '"'1,2p' || true
echo
echo '=== POST forms/3/duplicate ==='
curl -sSL -X POST "'$URL/forms/3/duplicate | sed -n '"'1,2p' || true"

 === POST forms/1/duplicate ===
{"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}
=== POST forms/3/duplicate ===
{"code":"rest_forbidden","message":"Sorry, you are not allowed to do that.","data":{"status":401}}
 Exit code: 0
  
 bash -lc "set -e
export URL=http://wordpress.local/wp-json/fluentform/v1
echo '=== Try public endpoints prefix ==='
curl -sSL "'$URL/public | sed -n '"'1,200p' || true
curl -sSL "'$URL/public/forms | sed -n '"'1,200p' || true
echo '=== Try /wp-json/fluentform/v2 ==='
curl -sSL http://wordpress.local/wp-json/fluentform/v2 | sed -n '1,200p' || true
echo '=== Try v2 public forms ==='
curl -sSL http://wordpress.local/wp-json/fluentform/v2/public/forms | sed -n '1,200p' || true
echo '=== Try /wp-json/fluentform/v1/public/submit ==='
curl -sSL http://wordpress.local/wp-json/fluentform/v1/public/submit | sed -n '1,200p' || true
echo '=== Try /wp-json/fluentform/v1/public/submit/{form_id} ==='
curl -sSL "'$URL/public/submit/1 | sed -n '"'1,200p' || true
echo '=== Try /wp-json/fluentform/v1/public/submissions ==='
curl -sSL "'$URL/public/submissions | sed -n '"'1,200p' || true
echo '=== Try /wp-json/fluentform/v1/public/form/1 ==='
curl -sSL "'$URL/public/form/1 | sed -n '"'1,200p' || true
echo '=== Try /wp-json/fluentform/v1/public/forms ==='
curl -sSL "'$URL/public/forms | sed -n '"'1,200p' || true"

 === Try public endpoints prefix ===
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}=== Try /wp-json/fluentform/v2 ===
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}=== Try v2 public forms ===
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}=== Try /wp-json/fluentform/v1/public/submit ===
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}=== Try /wp-json/fluentform/v1/public/submit/{form_id} ===
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}=== Try /wp-json/fluentform/v1/public/submissions ===
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}=== Try /wp-json/fluentform/v1/public/form/1 ===
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}=== Try /wp-json/fluentform/v1/public/forms ===
{"code":"rest_no_route","message":"No route was found matching the URL and request method.","data":{"status":404}}
 Exit code: 0
```

---


					Contact Form Plugin by 
Fluent Forms for Quiz, Survey, and Drag & Drop WP Form Builder <=
 5.1.16 - Missing Authorization to Settings Update and Limited Privilege
 Escalation

				The Contact Form Plugin by Fluent Forms for Quiz, Survey, and Drag & Drop WP Form Builder plugin for WordPress is vulnerable to privilege escalation due to a missing capability check on the /wp-json/fluentform/v1/managers REST API endpoint in all versions up to, and including, 5.1.16. This makes it possible for unauthenticated attackers to grant users with Fluent Form management permissions which gives them access to all of the plugin's settings and features. This also makes it possible for unauthenticated attackers to delete manager accounts.

	