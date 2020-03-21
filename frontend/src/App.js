import React, {Component} from 'react';
import { render } from "react-dom";

import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';
import URLInput from './components/URLInput/URLInput';
import TopHundred from './components/TopHundred/TopHundred';
import './App.css';

class App extends Component {
  render () {
    return (
      <div className="App">
        <Header className="Header" />
        <URLInput className="Main" />
        <TopHundred className="Top-Hundred" />
        <Footer className="Footer" />
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);