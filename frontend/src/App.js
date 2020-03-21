import React, {Component} from 'react';
import { render } from "react-dom";
import './App.css';

class App extends Component {
  render () {
    return (
      <div className="App">
        Hello, World!
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);