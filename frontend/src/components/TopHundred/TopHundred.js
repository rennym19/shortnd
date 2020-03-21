import React, { Component } from "react";
import cogoToast from 'cogo-toast';
import URLList from '../URLList/URLList';
import './TopHundred.css';

class TopHundred extends Component {
  constructor(props) {
    super(props);
    this.state = {
      topUrl: 'top_hundred/', 
      receivedData: false,
      data: null,
      next: null,
      previous: null
    };

    this.requestTopHundred = this.requestTopHundred.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.handleNextPage = this.handleNextPage.bind(this);
    this.handlePreviousPage = this.handlePreviousPage.bind(this);
  }

  handleClick(event) {
    event.preventDefault();
    this.setState({
      topUrl: 'top_hundred/'
    });
    this.requestTopHundred();
  }

  handleNextPage(event) {
    event.preventDefault();
    if (this.state.next !== null) {
      this.setState({
        topUrl: this.state.next
      });
      this.requestTopHundred();
    }
  }

  handlePreviousPage(event) {
    event.preventDefault();
    if (this.state.previous !== null) {
      this.setState({
        topUrl: this.state.previous
      });
      this.requestTopHundred();
    }
  }

  requestTopHundred() {
    fetch(this.state.topUrl, {
      method: 'GET'
    })
    .then((response) => response.json())
    .then((data) => {
      this.setState({
        receivedData: true,
        data: data.results,
        next: data.next,
        previous: data.previous
      });
    })
    .catch((error) => {
      cogoToast.error(error);
      this.setState({
        receivedData: false
      });
    });
  }

  render() {
    return (
      <div className="TopHundredSection">
        <button className="TopHundredButton" 
                onClick={this.handleClick}>
                  Top 100
        </button>
        <URLList receivedData={this.state.receivedData}
                 data={this.state.data}
                 next={this.state.next}
                 previous={this.state.previous}
                 handleNextPage={this.handleNextPage}
                 handlePreviousPage={this.handlePreviousPage}/>
      </div>
    );
  }
}

export default TopHundred;
