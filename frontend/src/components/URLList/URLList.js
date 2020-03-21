import React, { Component } from "react";
import './URLList.css';

function URLItem(props) {
  return (
    <tr className="URLItem">
      <td>{props.title}</td>
      <td>{props.original_url}</td>
      <td><a href={props.short_url}>{props.short_url}</a></td>
      <td>{props.visit_count}</td>
    </tr>
  )
}

class URLList extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    if (this.props.receivedData) {
      let rows = [];
      for (let i=0; i < this.props.data.length; i++) {
        rows.push(<URLItem key={this.props.data[i].id} 
                           title={this.props.data[i].title}
                           original_url={this.props.data[i].original_url}
                           short_url={this.props.data[i].short_url}
                           visit_count={this.props.data[i].visit_count} />);
      }
      return (
        <div className="URLList"> 
          <table>
            <thead>
              <tr>
                <th>Title</th>
                <th>Original URL</th>
                <th>Short URL</th>
                <th>Visit Count</th>
              </tr>
            </thead>
            <tbody>
              {rows}
            </tbody>
          </table>
          <button className="ListButton" onClick={this.props.handlePreviousPage}>
            Previous
          </button>
          <button className="ListButton" onClick={this.props.handleNextPage}>
            Next
          </button>
        </div>
      )
    }
    return <></>;
  }
}

export default URLList;