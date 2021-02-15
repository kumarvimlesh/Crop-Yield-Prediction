(this["webpackJsonpcrop-yield-prediction"]=this["webpackJsonpcrop-yield-prediction"]||[]).push([[0],{23:function(e,t,n){},24:function(e,t,n){},46:function(e,t,n){"use strict";n.r(t);var a=n(2),r=n.n(a),i=n(14),c=n.n(i),l=(n(23),n.p,n(24),n(3)),o=n(5),s=n(15),d=n(16),u=n(18),h=n(17),j=(n(25),n(0)),p=function(e){Object(u.a)(n,e);var t=Object(h.a)(n);function n(e){var a;return Object(s.a)(this,n),(a=t.call(this,e)).stateNameHandler=function(e){var t=e.target.value;console.log("select = ",t);var n="weights/";n+=t,n+="_model.h5",console.log("path=",n),a.setState({stateName:e.target.value,weightFilePath:n}),console.log(a.state.stateName),console.log(a.state.filePath)},a.changeHandler=function(e,t){console.log(t),a.setState({inputs:Object(o.a)(Object(o.a)({},a.state.inputs),{},Object(l.a)({},t,e.target.value))})},a.submitHandler=function(e){e.preventDefault(),console.log("submt button clicked"),console.log("in submitHandler"),console.log("props"),console.log(a.props),console.log("state"),console.log(a.state),console.log("Ready to Send Request");var t=new Headers;t.append("Content-Type","application/json"),t.append("Accept","application/json"),fetch("https://cyp-mproject.herokuapp.com/inputData",{method:"POST",headers:t,body:JSON.stringify(a.state)}).then((function(e){return e.json()})).then((function(e){console.log(e),console.log(e.result);var t=parseFloat(e.result);console.log("output = ",t),a.setState({predictedProduction:t}),console.log(a.state.predictedProduction)})).catch((function(e){console.log("Request failure: ",e)}))},a.state={stateName:null,weightFilePath:null,inputs:{maxTemperature:0,minTemperature:0,temperature:0,heatIndex:0,precipitaion:0,windSpeed:0,visibility:0,cloudCover:0,relativeHumidity:0,area:0},predictedProduction:0},a}return Object(d.a)(n,[{key:"render",value:function(){var e=this;return Object(j.jsxs)("div",{className:"form",children:[Object(j.jsxs)("form",{onSubmit:this.submitHandler,children:[Object(j.jsxs)("div",{children:[Object(j.jsx)("label",{children:"Select State"}),Object(j.jsxs)("select",{name:"stateName",onChange:this.stateNameHandler,children:[Object(j.jsx)("option",{children:"Select"}),["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir ","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalay","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Delhi"].map((function(e){return Object(j.jsx)("option",{value:e,children:e})}))]})]}),Object(j.jsxs)("div",{children:[Object(j.jsx)("label",{children:"Enter Max Temperature"}),Object(j.jsx)("input",{type:"number",name:"maxTemperature",onChange:function(t){return e.changeHandler(t,"maxTemperature")}}),Object(j.jsx)("label",{children:"Enter Min Temperature"}),Object(j.jsx)("input",{type:"number",name:"minTemperature",onChange:function(t){return e.changeHandler(t,"minTemperature")}})]}),Object(j.jsxs)("div",{children:[Object(j.jsx)("label",{children:"Enter Temperature"}),Object(j.jsx)("input",{type:"number",name:"temperature",onChange:function(t){return e.changeHandler(t,"temperature")}}),Object(j.jsx)("label",{children:"Enter Heat Index"}),Object(j.jsx)("input",{type:"number",name:"heatIndex",onChange:function(t){return e.changeHandler(t,"heatIndex")}})]}),Object(j.jsxs)("div",{children:[Object(j.jsx)("label",{children:"Enter Precipitaion"}),Object(j.jsx)("input",{type:"number",name:"precipitaion",onChange:function(t){return e.changeHandler(t,"precipitaion")}})]}),Object(j.jsxs)("div",{children:[Object(j.jsx)("label",{children:"Enter Wind Speed"}),Object(j.jsx)("input",{type:"number",name:"windSpeed",onChange:function(t){return e.changeHandler(t,"windSpeed")}}),Object(j.jsx)("label",{children:"Enter Visibility"}),Object(j.jsx)("input",{type:"number",name:"visibility",onChange:function(t){return e.changeHandler(t,"visibility")}})]}),Object(j.jsxs)("div",{children:[Object(j.jsx)("label",{children:"Enter Cloud Cover"}),Object(j.jsx)("input",{type:"number",name:"cloudCover",onChange:function(t){return e.changeHandler(t,"cloudCover")}}),Object(j.jsx)("label",{children:"Enter Relative Humidity"}),Object(j.jsx)("input",{type:"number",name:"relativeHumidity",onChange:function(t){return e.changeHandler(t,"relativeHumidity")}})]}),Object(j.jsxs)("div",{children:[Object(j.jsx)("label",{children:"Enter Area of Production"}),Object(j.jsx)("input",{type:"number",name:"area",onChange:function(t){return e.changeHandler(t,"area")}})]}),Object(j.jsx)("div",{children:Object(j.jsx)("button",{class:"sbmtbtn",children:"Submit"})})]}),Object(j.jsx)("div",{children:Object(j.jsxs)("h2",{children:["Predicted Rice Crop Production for ",this.state.inputs.area," cultivated area is : ",this.state.predictedProduction]})})]})}}]),n}(r.a.Component);var b=function(){return Object(j.jsx)("div",{className:"App",children:Object(j.jsxs)("header",{className:"App-header",children:[Object(j.jsx)("h1",{children:"Crop Yield Prediction"}),Object(j.jsx)(p,{})]})})},m=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,47)).then((function(t){var n=t.getCLS,a=t.getFID,r=t.getFCP,i=t.getLCP,c=t.getTTFB;n(e),a(e),r(e),i(e),c(e)}))};n(45);c.a.render(Object(j.jsx)(r.a.StrictMode,{children:Object(j.jsx)(b,{})}),document.getElementById("root")),m()}},[[46,1,2]]]);
//# sourceMappingURL=main.c4dde7ae.chunk.js.map