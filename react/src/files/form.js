import React,{Component} from 'react';

class Inputs extends React.Component{
	constructor(props){
		super(props);
		this.state={
			stateName:null,
			weightFilePath:null,
			inputs:{
				maxTemperature:0,
				minTemperature:0,
				temperature:0,
				heatIndex:0,
				precipitaion:0,
				windSpeed:0,
				visibility:0,
				cloudCover:0,
				relativeHumidity:0,
				area:0
			},
			predictedProduction:0.0,
		};
	}

	stateNameHandler = (event) => {
		let stateName=event.target.value;
		console.log("select = ",stateName);
		let filePath='weights/';
		filePath+=stateName
		filePath+="_model.h5";
		console.log("path=",filePath)
		this.setState({
			stateName:event.target.value,
			weightFilePath:filePath
		});
		console.log(this.state.stateName);
		console.log(this.state.filePath);
	}

	changeHandler = (event,val) => {
		console.log(val);
		//console.log(event.target.value);
		this.setState({
			inputs:{
			   ...this.state.inputs,[val]:event.target.value
		    }
		});
	}

	submitHandler = (event) => {
		event.preventDefault();
		console.log('submt button clicked');
		console.log("in submitHandler");
		console.log("props");
		console.log(this.props);
		console.log("state");
		console.log(this.state);
		
		let headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('Accept', 'application/json');
        headers.append('Origin','https://crop-yield-prediction-adbc8.firebaseapp.com');//

        console.log("Ready to Send Request");

		fetch('/inputData',{
			method: "POST",
            headers: headers,
            body: JSON.stringify(this.state),
		})
		.then(res=>res.json())
		.then(res=>{
			console.log(res);
			console.log(res.result);
			var output=parseFloat(res.result);
			console.log("output = ",output);
			this.setState({predictedProduction:output});
			console.log(this.state.predictedProduction);
		})
		.catch(function (error){
            console.log('Request failure: ', error);
         });
	};


	render(){

		const states=[
			         "Andaman and Nicobar Islands", "Andhra Pradesh","Arunachal Pradesh", "Assam", 
			         "Bihar", "Chandigarh","Chhattisgarh", "Dadra and Nagar Haveli", "Goa", "Gujarat",
			         "Haryana", "Himachal Pradesh", "Jammu and Kashmir ", "Jharkhand", "Karnataka", 
			         "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalay", "Mizoram", 
			         "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", 
			         "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi"
            ];
		
		return(
			<div className="form">
			  <form onSubmit={this.submitHandler}>
			    <div>
			      <label>Select State</label>
			      <select name="stateName" onChange={this.stateNameHandler}>
			         <option>Select</option>
			        {
			        	states.map((state) => (
			        		<option value={state}>{state}</option>
			            ))
			        }
			      </select>
			    </div>
			    <div>
                	<label>Enter Max Temperature</label>
                	<input type="number" name="maxTemperature" onChange={(event)=>this.changeHandler(event,"maxTemperature")}/>
                
                	<label>Enter Min Temperature</label>
                	<input type="number" name="minTemperature" onChange={(event)=>this.changeHandler(event,"minTemperature")}/>
                </div>
                <div>
                	<label>Enter Temperature</label>
                	<input type="number" name="temperature" onChange={(event)=>this.changeHandler(event,"temperature")}/>
                
                	<label>Enter Heat Index</label>
                	<input type="number" name="heatIndex" onChange={(event)=>this.changeHandler(event,"heatIndex")}/>
                </div>
                <div>
                	<label>Enter Precipitaion</label>
                	<input type="number" name="precipitaion" onChange={(event)=>this.changeHandler(event,"precipitaion")}/>
                </div>
                <div>
               	 	<label>Enter Wind Speed</label>
                	<input type="number" name="windSpeed" onChange={(event)=>this.changeHandler(event,"windSpeed")}/>
                
               		<label>Enter Visibility</label>
                	<input type="number" name="visibility" onChange={(event)=>this.changeHandler(event,"visibility")}/>
                </div>
                <div>
                	<label>Enter Cloud Cover</label>
                	<input type="number" name="cloudCover" onChange={(event)=>this.changeHandler(event,"cloudCover")}/>
                
                	<label>Enter Relative Humidity</label>
                	<input type="number" name="relativeHumidity" onChange={(event)=>this.changeHandler(event,"relativeHumidity")}/>
                </div>
                <div>
                	<label>Enter Area of Production</label>
                	<input type="number" name="area" onChange={(event)=>this.changeHandler(event,"area")}/>
                </div>
                <div>
                   <button class="sbmtbtn">Submit</button>
                </div>
              </form>
              <div>
			    <h2>Predicted Rice Crop Production  is : {this.state.predictedProduction}</h2>
			  </div>
			</div>
		);
	}
}

export default Inputs;