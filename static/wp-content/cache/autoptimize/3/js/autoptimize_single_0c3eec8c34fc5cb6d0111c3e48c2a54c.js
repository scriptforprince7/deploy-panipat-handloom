function dokan_get_i18n_date_format(format=true){if(!format){return dokan_helper.i18n_date_format;}
let formatMap={d:'dd',D:'D',j:'d',l:'DD',F:'MM',m:'mm',M:'M',n:'m',o:'yy',Y:'yy',y:'y'}
let i=0;let char='';let datepickerFormat='';for(i=0;i<dokan_helper.i18n_date_format.length;i++){char=dokan_helper.i18n_date_format[i];if(char in formatMap){datepickerFormat+=formatMap[char];}else{datepickerFormat+=char;}}
return datepickerFormat;}
function dokan_get_i18n_time_format(format=true){if(!format){return dokan_helper.i18n_time_format;}
let replacements={N:'E',S:'o',w:'e',z:'DDD',W:'W',F:'MMMM',m:'MM',M:'MMM',n:'M',o:'YYYY',Y:'YYYY',y:'YY',a:'a',A:'A',g:'h',G:'H',h:'hh',H:'HH',i:'mm',s:'ss',u:'SSS',e:'zz',U:'X',}
let i=0,char='',timeFormat='';for(i=0;i<dokan_helper.i18n_time_format.length;i++){char=dokan_helper.i18n_time_format[i];if(char in replacements){timeFormat+=replacements[char];}else{timeFormat+=char;}}
return timeFormat;}
function dokan_get_formatted_time(time,format){const times=new Date(Date.parse(`Jan 1 ${time}`)),add0=function(t){return t<10?'0'+t:t;},hours=times.getHours(),minutes=times.getMinutes(),seconds=times.getSeconds(),sampm=hours>=12?'pm':'am',campm=hours>=12?'PM':'AM',convertTime=(time)=>{time=time.toString().match(/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/)||[time];if(time.length>1){time=time.slice(1);time[0]=+time[0]%12||12;}
return time[0];},hour12=convertTime(`${add0( hours )}:${add0( minutes )}`),replaceMent={'hh':add0(hour12),'h':hour12,'HH':add0(hours),'H':hours,'g':hour12,'MM':add0(minutes),'M':minutes,'mm':add0(minutes),'m':minutes,'i':add0(minutes),'ss':add0(seconds),'s':seconds,'A':campm,'a':sampm,};for(let key in replaceMent){format=format.replace(key,replaceMent[key]);}
return format;}
function dokan_get_daterange_picker_format(dateTime=dokan_helper.i18n_date_format){let formatMap={d:'D',D:'DD',j:'D',l:'DD',F:'MMMM',m:'MM',M:'MM',n:'M',o:'YYYY',Y:'YYYY',y:'YY',g:'h',G:'H',h:'hh',H:'HH',i:'mm',s:'ss'}
let i=0;let char='';let dateRangePickerFormat='';for(i=0;i<dateTime.length;i++){char=dateTime[i];if(char in formatMap){dateRangePickerFormat+=formatMap[char];}else{dateRangePickerFormat+=char;}}
return dateRangePickerFormat;}
async function dokan_sweetalert(message='',options={}){const defaults={text:message,showCancelButton:true,confirmButtonColor:'#28a745',cancelButtonColor:'#dc3545',};const args={...defaults,...options};const action=args.action;delete args.action;switch(action){case'confirm':case'prompt':return await Swal.fire(args);break;case'alert':default:delete args.showCancelButton;Swal.fire(args);break;}}
function dokan_execute_recaptcha(inputFieldSelector,action){return new Promise(function(resolve){if('undefined'===typeof dokan_google_recaptcha){resolve();}
const recaptchaSiteKey=dokan_google_recaptcha.recaptcha_sitekey;const recaptchaTokenField=document.querySelector(inputFieldSelector);if(''===recaptchaSiteKey){resolve();}
grecaptcha.ready(function(){grecaptcha.execute(recaptchaSiteKey,{action:action}).then(function(token){recaptchaTokenField.value=token;resolve();});});});}