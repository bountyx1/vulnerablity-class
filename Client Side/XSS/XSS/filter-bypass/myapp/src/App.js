import React, { Component } from 'react';


class Markdown extends Component{
	 constructor(props) {
    super(props);
    this.myRef = React.createRef();
  }
	render()
	{
		return(

<b>{this.props.text}	</b>
			);



	}
}

class Xss1 extends Component{
 constructor(props) {
    super(props);
    this.state={"xss":"<img src=x>aa"}
  }


	render()
	{
		return(
		<div dangerouslySetInnerHTML={{__html: this.state.xss}} />
		);
	}
}


class Xss2 extends Component{
 constructor(props) {
    super(props);
    this.state={"href":"javascript:alert(1)"}
  }


	render()
	{

		return(
		<a href={this.state.href}>Click Me</a>
		);
	}
}


class Xss3 extends Component{
 constructor(props) {
    super(props);
    this.test=this.test.bind(this);
    this.state={data:"Default"};
  }
test()
{
  const value=this.refs.inputField.value;
  this.setState({data:value})
}

	render()
	{
		return(

		<div>
        <input type="text" ref="inputField" />
        <button type="button" onClick={this.test}> Click Me</button>

        <h1>{this.state.data}</h1>

        </div>
		);
	}
}


class App extends Component{
	render()
	{
		return(
		<div>
		<Xss3 />
		<Xss1 />
		<Xss2 />

		<Markdown />
		</div>
		);
	}
}




export default App;